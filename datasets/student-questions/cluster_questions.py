#!/usr/bin/env python3
"""
Cluster student questions.

Pipeline:
  1. Collect all words across all questions (lowercased, punctuation stripped).
  2. Remove stop words (scikit-learn's English stop-word list + a few extras).
  3. Vectorize the questions in the resulting vocabulary (TF-IDF).
  4. Agglomeratively cluster questions by pairwise distance in that vector space.
  5. Name each cluster with a local LLM (ollama).
  6. Write:
       - cluster-names.md          : LLM-generated names for the k clusters
       - clustered-questions.json  : each cluster -> {name, questions[]}

Usage:
  python3 cluster_questions.py [--n-clusters 20] [--model gemma4:26b]
"""

import argparse
import json
import re
import sys
import time
import urllib.request

import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS, TfidfVectorizer

SCRIPT_DIR = __import__("pathlib").Path(__file__).resolve().parent
CSV_PATH = SCRIPT_DIR / "questions.csv"
NAMES_PATH = SCRIPT_DIR / "cluster-names.md"
JSON_PATH = SCRIPT_DIR / "clustered-questions.json"

OLLAMA_URL = "http://127.0.0.1:11434/api/generate"

# Extra tokens that are common in student questions but not real content words.
EXTRA_STOP = {
    "does", "do", "how", "what", "why", "which", "who", "where", "when",
    "affect", "affects", "affected", "related", "relate", "relates",
    "etc", "tbd", "per", "vs", "e", "g", "w", "r", "u", "im", "dont",
    "people", "someone", "person", "students", "people", "use", "using",
    "one", "many", "much", "lot", "any", "such", "also", "well", "actual",
    "actually", "really", "change", "changes", "happen", "happens", "look",
    "come", "going", "make",
}
STOP_WORDS = set(ENGLISH_STOP_WORDS) | EXTRA_STOP


def read_questions():
    df = pd.read_csv(CSV_PATH)
    qcol = df["question"] if "question" in df.columns else df.iloc[:, 1]
    return [str(q).strip() for q in qcol if str(q).strip()]


def normalize(text):
    # Lowercase and strip everything that isn't a letter (keep word shapes).
    text = text.lower()
    text = re.sub(r"[^\w\s]", " ", text, flags=re.UNICODE)
    return text


def collect_words(questions):
    """All words across all questions, stop words removed, deduped."""
    words = set()
    for q in questions:
        for w in normalize(q).split():
            if w.isalpha() and w not in STOP_WORDS:
                words.add(w)
    return sorted(words)


def vectorize(questions, vocabulary):
    vec = TfidfVectorizer(vocabulary=vocabulary)
    return vec.fit_transform(questions)


def cluster_matrix(X, n_clusters):
    """Agglomerative clustering on pairwise (cosine) distance in the space."""
    model = AgglomerativeClustering(
        n_clusters=n_clusters, metric="cosine", linkage="average"
    )
    return model.fit_predict(X.toarray())


def name_cluster(model, questions):
    """Ask a local LLM for a short, meaningful name for a cluster of questions."""
    listing = "\n".join(f"- {q}" for q in questions)
    prompt = (
        "You are naming clusters of student research questions for a data "
        "science class. Given the questions below that were grouped together, "
        "produce ONE short cluster name (3 to 6 words) that captures the shared "
        "topic.\n\n"
        "Questions:\n"
        f"{listing}\n\n"
        'Respond with only the cluster name, e.g. "Traffic safety cameras".'
    )
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {"temperature": 0.2},
    }
    req = urllib.request.Request(
        OLLAMA_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    # Big local models can blow the default timeout; retry with backoff.
    last_err = None
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=300) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            break
        except Exception as e:  # noqa: BLE001 - retry transient LLM failures
            last_err = e
            time.sleep(5 * (attempt + 1))
    else:
        raise RuntimeError(f"LLM request failed 5 times: {last_err}")
    name = data.get("response", "").strip()
    # Collapse the name to a single line.
    name = re.sub(r"\s+", " ", name).strip(" \n\t-*#\"'.")
    if not name:
        raise RuntimeError(f"LLM returned empty name for cluster with {len(questions)} questions")
    return name


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n-clusters", type=int, default=20)
    ap.add_argument("--model", default="qwen3:8b",
                    help="Local ollama model used to name the clusters.")
    args = ap.parse_args()

    questions = read_questions()
    print(f"Read {len(questions)} questions from {CSV_PATH.name}")

    vocabulary = collect_words(questions)
    print(f"Vocabulary after stop-word removal: {len(vocabulary)} unique words")

    X = vectorize(questions, vocabulary)
    labels = cluster_matrix(X, args.n_clusters)
    print(f"Performed agglomerative clustering -> {args.n_clusters} clusters")

    # Group question indices by cluster label (stable order).
    groups = {}
    for i, lab in enumerate(labels):
        groups.setdefault(int(lab), []).append(i)

    # Name each cluster with the local LLM.
    cluster_names = {}
    cluster_questions = {}
    for lab in sorted(groups):
        idxs = groups[lab]
        cluster_qs = [questions[i] for i in idxs]
        name = name_cluster(args.model, cluster_qs)
        cluster_names[lab] = name
        cluster_questions[lab] = {"name": name, "questions": cluster_qs}
        print(f"  cluster {lab}: {name} ({len(cluster_qs)} questions)")
        sys.stdout.flush()

    # ---- Write outputs ----
    with open(NAMES_PATH, "w", encoding="utf-8") as f:
        f.write(f"# Cluster names ({args.n_clusters} clusters)\n\n")
        f.write(f"Named with local model `{args.model}`.\n\n")
        for lab in sorted(cluster_names):
            f.write(f"{lab + 1}. **{cluster_names[lab]}**\n")
            f.write("   " + " | ".join(questions[i] for i in groups[lab]) + "\n\n")

    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(list(cluster_questions.values()), f, indent=2, ensure_ascii=False)

    print(f"\nWrote:\n  {NAMES_PATH}\n  {JSON_PATH}")


if __name__ == "__main__":
    main()
