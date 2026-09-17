import worker from "./worker.js";

function makeKV() {
  const m = new Map();
  return {
    m,
    writes: 0,
    async get(k) { return m.has(k) ? m.get(k) : null; },
    async put(k, v) { this.writes++; m.set(k, v); },
    async list({ cursor }) { return { keys: [...m.keys()].map((name) => ({ name })), list_complete: true }; },
  };
}
const post = (body, headers = {}) =>
  new Request("https://x/", { method: "POST", headers: { "Content-Type": "application/json", ...headers }, body: typeof body === "string" ? body : JSON.stringify(body) });

let failed = 0;
const check = (name, cond, extra = "") => { console.log((cond ? "PASS  " : "FAIL  ") + name + (cond ? "" : "  <- " + extra)); if (!cond) failed++; };

// 1. the fix: an unknown assignment must not mint a key
{
  const kv = makeKV();
  const r = await worker.fetch(post({ assignment: "zzattacker", tool: "claude-code", event: "session-start", install: "abcd1234" }), { COUNTS: kv });
  check("unknown assignment rejected", r.status === 400, "status " + r.status);
  check("unknown assignment writes nothing", kv.m.size === 0 && kv.writes === 0, "keys=" + [...kv.m.keys()]);
}

// 2. unknown tool likewise
{
  const kv = makeKV();
  const r = await worker.fetch(post({ assignment: "hw1", tool: "evil-tool", event: "session-start", install: "abcd1234" }), { COUNTS: kv });
  check("unknown tool rejected", r.status === 400, "status " + r.status);
  check("unknown tool writes nothing", kv.m.size === 0, "keys=" + [...kv.m.keys()]);
}

// 3. no regression: a legitimate session still counts
{
  const kv = makeKV();
  const r = await worker.fetch(post({ assignment: "hw1", tool: "claude-code", event: "session-start", install: "3f9a1c22b0d74e88" }), { COUNTS: kv });
  check("legit session accepted", r.status === 204, "status " + r.status);
  check("total incremented", kv.m.get("total") === "1");
  check("assignment counted", kv.m.get("assignment:hw1") === "1");
  check("tool counted", kv.m.get("tool:claude-code") === "1");
  check("installs counted", kv.m.get("installs") === "1");
  check("per-tool installs counted", kv.m.get("installs:tool:claude-code") === "1");

  // same folder again -> sessions rise, installs do not
  await worker.fetch(post({ assignment: "hw1", tool: "claude-code", event: "session-start", install: "3f9a1c22b0d74e88" }), { COUNTS: kv });
  check("repeat session counts again", kv.m.get("total") === "2");
  check("repeat folder does not re-count install", kv.m.get("installs") === "1");
}

// 4. oversized body rejected before parsing
{
  const kv = makeKV();
  const big = JSON.stringify({ assignment: "hw1", tool: "claude-code", event: "session-start", install: "a".repeat(5000) });
  const r = await worker.fetch(post(big), { COUNTS: kv });
  check("oversized body rejected", r.status === 413, "status " + r.status);
  check("oversized body writes nothing", kv.m.size === 0);
}

// 5. stats still renders and hides internal keys
{
  const kv = makeKV();
  await worker.fetch(post({ assignment: "hw1", tool: "claude-code", event: "session-start", install: "3f9a1c22b0d74e88" }), { COUNTS: kv });
  const out = await (await worker.fetch(new Request("https://x/stats.json"), { COUNTS: kv })).json();
  check("stats total", out.total === 1, JSON.stringify(out));
  check("stats assignments", out.assignments.hw1 === 1);
  check("stats hides seen:/meta:", !JSON.stringify(out).includes("seen:") && !JSON.stringify(out).includes("meta:"));
}

console.log(failed === 0 ? "\nALL PASS" : `\n${failed} FAILED`);
process.exit(failed ? 1 : 0);
