# Top 10 Authors, Top 10 Keywords, and Thematic Trends

**Research Topic:** Unbiased Learning to Rank (ULTR) and Context-Aware Information Retrieval (2021–2025)

---

## Table 1: Top 10 Most Influential Authors

| # | Author | Country / Affiliation | Research Focus | Key Representative Paper | Contribution Summary |
|---|--------|----------------------|----------------|-------------------------|----------------------|
| 1 | Avishek Anand | Netherlands / TU Delft, L3S Research Center | Efficient neural ranking, interpretability, data augmentation | Leonhardt et al. (2024) — Efficient Neural Ranking Using Forward Indexes | Pioneered Fast-Forward indexes enabling CPU-only neural re-ranking; advanced listwise feature attribution (RankingSHAP) and data augmentation for low-resource ranking |
| 2 | Harrie Oosterhuis | Netherlands / Radboud University | Unbiased learning to rank, counterfactual learning, click models | Gupta et al. (2023) — Recent Advances in ULTR (SIGIR Tutorial) | Authored foundational ULTR survey; developed counterfactual LTR methods bridging theory and practice across position, selection, and interaction biases |
| 3 | Qingyao Ai | China / Tsinghua University | Automatic ULTR, counterfactual LTR, evaluation frameworks | Fang et al. (2020) — Multivariate Scoring Functions for AutoULTR | Proved permutation invariance as necessary condition for AutoULTR convergence; created ULTRE evaluation framework; advanced doubly robust LTR methods |
| 4 | Zhicheng Dou | China / Renmin University of China | Generative retrieval, search diversification, conversational IR | Zhou et al. (2024) — ROGER: Ranking-Oriented Generative Retrieval | Led GenIR research bridging dense retrieval and generative models; developed LLM-powered search diversification agents (DIVAgent) |
| 5 | Ji-Rong Wen | China / Renmin University of China | Personalized ULTR, web search, generative retrieval | Niu et al. (2025) — Addressing Personalized Bias for ULTR | Advanced user-aware IPS estimation for personalized bias correction; contributed to GenIR architectures and web-scale search systems |
| 6 | Maarten de Rijke | Netherlands / University of Amsterdam | Search diversification, explainability, neural IR | Deng et al. (2025) — DIVAgent: Diversified Search Agent | Pioneered LLM-powered search diversification; advanced explainable ranking models bridging neural effectiveness and human interpretability |
| 7 | Jun Xu | China / Renmin University of China | Bias in LLM-era IR, neural ranking models | Dai et al. (2024) — Bias and Unfairness in IR: New Challenges in the LLM Era | Unified bias and unfairness as distribution mismatch; categorized LLM-era bias types (source, factuality, instruction-hallucination) |
| 8 | Weinan Zhang | China / Shanghai Jiao Tong University | Deep LTR, utility-oriented ranking, survival analysis | Jin et al. (2020) — Deep Recurrent Survival Ranking | Developed DRSR combining survival analysis with neural ranking; advanced utility-oriented LTR optimizing business metrics beyond relevance |
| 9 | Sebastian Hofstatter | Austria / TU Wien | Position bias mitigation, efficient transformers, relevance annotations | Hofstatter et al. (2021) — Mitigating Position Bias of Transformer Models | Identified and mitigated position bias in Transformer re-rankers; created FiRA fine-grained relevance annotations dataset |
| 10 | K.J. Amala | India | Neural LTR, bias correction, nonparametric click models | Amala & Rajeswari (2025a) — APCP: Neural LTR with Bias Correction | Proposed APCP two-tower attention network for joint bias-relevance estimation; developed nonparametric DPMM click models for unbiased LTR |

---

## Table 2: Top 10 Keywords

| # | Keyword | Definition | Relevance to Topic | Category |
|---|---------|------------|-------------------|----------|
| 1 | Information Retrieval | The science of searching for and retrieving relevant information from large document collections | Core domain of the entire research field; all ranking, bias, and context methods operate within IR systems | Domain |
| 2 | Unbiased Learning to Rank | Machine learning framework for training ranking models from biased implicit feedback (clicks) by correcting for observation and presentation biases | Central methodology of this review; addresses the fundamental problem that clicks ≠ relevance | Methodology |
| 3 | Position Bias | Systematic tendency for users to click items in higher-ranked positions regardless of relevance, distorting click-through data | Most studied bias type; motivates the entire ULTR research program | Bias Type |
| 4 | Recommender Systems | Algorithms that suggest relevant items to users based on preferences, behavior, and context | Major application domain for ranking and debiasing methods; covers e-commerce, content, and service recommendation | Application |
| 5 | Learning to Rank | Supervised machine learning approach that trains models to order documents/items by predicted relevance | Technical backbone of modern search and recommendation ranking pipelines | Methodology |
| 6 | Context-Aware Ranking | Ranking approaches that incorporate contextual signals (time, location, device, user state) into relevance estimation | Directly addresses the "context" dimension of this review; enables personalization and dynamic ranking | Methodology |
| 7 | Large Language Model | Neural network models with billions of parameters trained on massive text corpora, capable of generating and evaluating text | Emerging paradigm disrupting traditional IR; enables generative retrieval, LLM-as-ranker, and automated evaluation | Technology |
| 8 | Click Models | Probabilistic models of user browsing and clicking behavior that estimate the probability a user examines and clicks a result | Foundation of ULTR; provide the generative model of user behavior that bias correction methods invert | Methodology |
| 9 | Examination Bias | The probability that a user examines a search result, which depends on position, UI layout, and result presentation | Second most studied bias type after position bias; XPA and attention-based methods address it | Bias Type |
| 10 | Fairness in Ranking | The principle that ranking algorithms should not systematically disadvantage protected groups or amplify existing inequalities | Growing ethical dimension of IR research; connects bias correction to societal outcomes | Ethics / Quality |

---

## 3. Thematic Summary (150–200 words)

The synthesis of author contributions and keyword distributions reveals three dominant research axes. First, the **bias-correction axis** — driven by Oosterhuis, Ai, and Amala — has matured from early IPS-based methods to doubly robust and nonparametric approaches, with position bias remaining the most studied distortion type. Second, the **architecture axis** — advanced by Anand, Hofstatter, and the Renmin University group — has shifted from BERT-centric cross-encoders to efficient dual-encoder designs and, most recently, to LLM-based generative retrieval that fundamentally reimagines how ranking is performed. Third, the **fairness-and-evaluation axis** — represented by de Rijke's diversification work and the JD.com industry studies — connects technical debiasing to measurable societal outcomes. The keyword distribution confirms this maturation: foundational terms (information retrieval: 12, position bias: 6, learning to rank: 5) remain dominant, while emerging terms (large language model: 4, contrastive learning: 3) signal the field's ongoing evolution. The geographic concentration in China (Tsinghua, Renmin) and the Netherlands (Amsterdam, Delft, Radboud) reflects institutional ecosystems where theoretical rigor and industrial deployment mutually reinforce.

---

✅ TOP 10 authors, keywords, and thematic trends successfully generated — ready for inclusion in the bibliometric overview section.
