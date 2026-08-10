# Ethics in Data Science — TODO toward a complete text


- Comparison points
- [*Fairness and Machine Learning*](https://fairmlbook.org) — Barocas, Hardt, Narayanan
- [*Practical Data Ethics*](https://ethics.fast.ai) — Rachel Thomas
- [*Calling Bullshit*](https://www.callingbullshit.org/syllabus.html) — Bergstrom & West
- [*Data Science Ethics*](https://global.oup.com/academic/product/data-science-ethics-9780192847270) — David Martens (OUP)
- *Data Feminism* — D'Ignazio & Klein

---


## To add

### Fairness and discrimination

Not a full chapter. 

- [ ] Group vs. individual notions of fairness
- [ ] The impossibility results (can't satisfy all the criteria at once)
- [ ] Disparate impact and the legal frame
- [ ] Proxies and redundant encoding — promote and expand the existing 4.3.1.1 "Proxies"
- [ ] Auditing methods; testing for discrimination in practice
- [ ] Placement: after *Ethics in Understanding*, before reporting

### Deployment and maintenance

("Tech debt and documentation debt," Goodhart's Law, Campbell's Law).

- [ ] Monitoring and drift
- [ ] Feedback loops and performativity
- [ ] Human oversight and contestability
- [ ] Incident response
- [ ] Deprecation and sunsetting

### LLMs

- [ ] (ir)responsible use as data scientist
- [ ] Training-data provenance and copyright
- [ ] annotation labor behind models
- [ ] Synthetic data — expand the existing 3.4 subsection
- [ ] Hallucination and evaluation
- [ ] Agentic systems

### Privacy, law, and regulation

- [ ] GDPR, HIPAA, FERPA, CCPA
- [ ] The Common Rule and IRB review
- [ ] Illinois BIPA 
- [ ] Technical siblings: re-identification, k-anonymity, differential privacy generalized out of the Census example

### Disinformation and the information ecosystem

- [ ] Publication bias
- [ ] p-hacking and data dredging
- [ ] How bad claims spread — ecology
- [ ] Refutation strategies for different audiences

### Power, labor, and political economy

*Data Feminism*'s core principles (examine power, challenge power, elevate emotion and
embodiment) and fast.ai's Lessons 5–6 (metrics, venture capital, hypergrowth,
algorithmic colonialism).

### Professional practice and governance

Pairs directly with the ACM competency mapping already in the preface.

- [ ] Codes of ethics (ACM)
- [ ] Documentation artifacts: datasheets, model cards
- [ ] Impact assessments and auditing
- [ ] Whistleblowing and organized refusal
- [ ] Career-stage advice

---

## Restructuring

- [ ] **Distribute Appendix C's case studies into the chapters they illustrate,** and keep a case index in the back matter.

---

## Per-chapter


- [ ] **Learning objectives** opening each chapter, mapped to the ACM competencies already tracked in the preface.
- [ ] **End-of-chapter exercises and discussion questions,** with solutions.
- [ ] **Hands-on labs / notebooks.** The "by hand" pedagogy is the most distinctive thing about the course and is currently invisible in the book.
- [ ] **Key terms per chapter,** cross-linked to the glossary in Appendix A.
- [ ] **Further reading per chapter.**
- [ ] **"How to use this book"** front matter, with 10-week and 15-week paths.
- [ ] **Index**, alongside the existing consolidated bibliography (`references.bib`).
