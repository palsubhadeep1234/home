---
permalink: /projects/ai-discovery/
title: "AI & Data-Driven Scientific Discovery"
layout: single
author_profile: true
---

<a href="/home/projects/" class="back-link">← Back to Research Projects</a>

My current work at MIT sits at the intersection of **large language models**, **reinforcement learning**, and **autonomous multi-agent systems** — applied to open-ended materials discovery. The central goal is to build AI systems that can reason about scientific hypotheses, chain domain-specific skills, and validate design candidates computationally without human-in-the-loop intervention.

---

### 1. Structured Scientific Reasoning in Open-Weight LLMs via Reinforcement Learning
*Advisor: Dr. Markus Buehler* · **2026 – Present**

- Fine-tuned open-weight LLMs (Qwen3-8B) via **Supervised Fine-Tuning** and **Group Relative Policy Optimization (GRPO)** to instill structured reasoning outputs, including chain-of-thought and knowledge graph formats with domain-specific tags (e.g., `<brainstorm>`, `<graph>`, `<patterns>`).
- Improved reasoning quality on hypothesis generation tasks by ~**15%** across scientific benchmarks (MMLU-Pro, ChemBench, FrontierScience) relative to the base model.

---

### 2. Decentralized Multi-Agent AI for Scientific Discovery
*Advisors: Dr. Markus Buehler; Fiona Wang; Dr. Anubhav Jain (LBNL)* · **2026 – Present**

- Co-developed **ScienceClaw + Infinite**, a decentralized multi-agent framework in which autonomous agents chain **300+ scientific skills** to drive open-ended materials discovery without a central coordinator or human-in-the-loop.
- Engineered the **polymer-physics skill module** and a multi-agent elastomer design workflow, integrating chain-statistics models and MD-derived surrogates to autonomously generate hypotheses and computationally validate design candidates in a shared artifact ecosystem.

**Related publication:**
- Wang, F. Y., Marom, L., **Pal, S.**, Luu, R. K., Lu, W., Berkovich, J. A., & Buehler, M. J., *Autonomous Agents Coordinating Distributed Discovery Through Emergent Artifact Exchange.* **arXiv**, 2026. DOI: [10.48550/arXiv.2603.14312](https://arxiv.org/abs/2603.14312)
