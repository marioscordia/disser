# Thematic Clusters and Comparative Analysis

**Paper:** Relevance and Positioning: A Systematic Bibliometric Review of Context-Aware ML Ranking in Web Search and Recommendation Systems
**Papers analyzed:** 45

---

## 1. Thematic Clusters

### Cluster 1: Core IR, Ranking Architectures, and LLM Integration

| Dimension | Description |
|-----------|-------------|
| **Title** | Neural Architectures for Context-Aware Ranking and LLM-Based Retrieval |
| **Papers** | 10 |
| **Common Characteristics** | Studies developing or deploying neural architectures where context signals improve ranking relevance. Includes pre-training frameworks leveraging document structure (Webformer), session-level user embeddings (CoSeRNN), two-tower multimodal architectures for e-commerce, instruction-tuned LLMs as rankers (RecRanker), and efficient neural ranking indexes (Fast-Forward). |
| **Representative Studies** | Hansen et al. (2020) — CoSeRNN contextual music recommendation (127 citations); Wu et al. (2020) — passage-level cumulative gain for document ranking (40 citations); Leonhardt et al. (2022, 2024) — Fast-Forward indexes for CPU-only neural re-ranking; Luo et al. (2025) — RecRanker LLM-as-ranker (15 citations) |
| **Key Findings** | Contextual signals (session history, document structure, user behavior) consistently improve ranking relevance across domains. Efficient architectures (dual-encoder, pre-computed indexes, lightweight query encoders) approach cross-encoder quality at orders-of-magnitude lower cost. LLM-based ranking represents the newest architectural paradigm, with instruction-tuned models competing with conventional recommenders. |

### Cluster 2: Dense Retrieval and Contextualized Query Enhancement

| Dimension | Description |
|-----------|-------------|
| **Title** | Dense Retrieval, Pseudo-Relevance Feedback, and Query Expansion |
| **Papers** | 8 |
| **Common Characteristics** | Studies advancing BERT-based dense retrieval through pseudo-relevance feedback, query expansion with contextualized embeddings, embedding compression, and list-wise training objectives. Strong methodological cohesion — the ColBERT-PRF line of work (Wang et al., 2021, 2023) forms an intellectual core extended by multiple groups. |
| **Representative Studies** | Wang et al. (2021, 2023) — ColBERT-PRF for dense retrieval PRF (60 and 46 citations); Naseri et al. (2022) — CEQE/SQET contextualized query expansion (3 citations); Yang et al. (2022a, 2022b) — BECR and Contextual Quantization for efficient BERT re-ranking (15 and 4 citations) |
| **Key Findings** | Pseudo-relevance feedback is viable and highly effective for dense retrieval, with MAP improvements up to 26%. Contextualized embeddings (BERT) substantially outperform traditional query expansion (RM3). Embedding compression achieves 14:1 ratios with negligible quality loss, enabling CPU-only deployment. |

### Cluster 3: Position Bias, Counterfactual LTR, and Off-Policy Evaluation

| Dimension | Description |
|-----------|-------------|
| **Title** | Bias-Aware and Counterfactual Learning to Rank |
| **Papers** | 8 |
| **Common Characteristics** | Studies addressing how click-based implicit feedback is distorted by position bias, examination bias, and selection bias. Methodologies span counterfactual estimation (IPS, doubly robust), survival analysis, contextual bandits, and off-policy evaluation for ranking. |
| **Representative Studies** | Chen et al. (2020) — context-aware click model (47 citations); Kiyohara et al. (2022) — Cascade-DR off-policy evaluation (40 citations); Chen et al. (2021) — interactional observation bias modeling (23 citations); Yang et al. (2020) — permutation invariance for AutoULTR (6 citations) |
| **Key Findings** | Position bias remains the central methodological concern, but work increasingly addresses interactional and contextual biases. The cascade model provides a tractable user behavior model for doubly robust off-policy evaluation. Permutation invariance is theoretically necessary for AutoULTR convergence. Contextual bandits with position bias modeling improve online metrics (+5% clicks). |

### Cluster 4: Recommender Fairness, Popularity Bias, and Context-Aware Recommendation

| Dimension | Description |
|-----------|-------------|
| **Title** | Fairness, Popularity Bias, and User-Centered Evaluation in Recommendation |
| **Papers** | 10 |
| **Common Characteristics** | Studies examining how ranking and recommendation algorithms create or amplify unfairness — particularly popularity bias that systematically advantages already-popular resources regardless of contextual relevance. Work spans systematic surveys (Klimashevskaia, Mateos), user-centered evaluation frameworks (Abdollahpouri), LLM-era bias taxonomies (Dai), and algorithmic mitigation (Chang, Zerveas neutrality regularization, Palomino MILP re-ranking). |
| **Representative Studies** | Abdollahpouri et al. (2021) — user-centered popularity bias evaluation (125 citations); Dai et al. (2024) — LLM-era bias survey (121 citations); Klimashevskaia et al. (2024) — popularity bias systematic review (77 citations); Mateos & Bellogin (2025) — context-aware RS review (53 citations) |
| **Key Findings** | The most-cited papers in the entire corpus are in this cluster, indicating the field's intense concern with fairness outcomes. Most bias mitigation work is evaluated offline with abstract metrics; user studies are virtually absent ("abstraction trap"). Context-aware recommendation is increasingly neural but lacks consensus on context definition. Popularity bias mitigation that ignores user-level tolerance for popular items can harm user satisfaction. |

### Cluster 5: Context-Aware Search and Cross-Cutting Applications

| Dimension | Description |
|-----------|-------------|
| **Title** | Context Modeling in Diverse Retrieval Settings |
| **Papers** | 9 |
| **Common Characteristics** | Studies investigating how different types of context — digital activity context (Vuong et al.), seasonal and temporal context (Chen et al. Amazon), session and cross-session context (Chen), legal retrieval context (Ma et al.) — affect search and recommendation outcomes. This cluster is methodologically heterogeneous, covering supervised learning, simulation-based training, and survey/tutorial contributions. |
| **Representative Studies** | Vuong et al. (2022) — digital activity context for Web search (11 citations); Zhang et al. (2023) — user behavior simulation for RL re-ranking (9 citations); Gupta et al. (2023) — ULTR tutorial (5 citations) |
| **Key Findings** | Digital activity context beyond search sessions (including non-search applications) improves retrieval. Rich context (full activity, 1-hour windows) consistently outperforms narrow context (session-only). Domain-specific contexts (legal, e-commerce seasonal) require specialized modeling. User behavior simulation shows promise for training ranking agents without costly online interaction. |

---

## 2. Cross-Cluster Comparative Analysis

### Similarities

All five clusters share a commitment to neural architectures as the dominant modeling paradigm: BERT-based encoders, Transformer attention mechanisms, and dual-encoder/two-tower architectural patterns appear in every cluster. A second shared characteristic is the concern with how context — whether session history, document structure, user behavior, or digital activity — can be operationalized to improve ranking outcomes. The two-tower architecture (separately modeling relevance or user preference from bias or context) emerges as a recurring pattern, appearing in Cluster 1 (e-commerce EBR), Cluster 3 (counterfactual LTR), and Cluster 4 (context-aware recommendation). A third commonality is evaluation methodology: NDCG and MAP dominate as evaluation metrics across all clusters, with online A/B testing concentrated in industry-authored papers (Meta, Amazon, Tencent, JD.com).

### Differences

The clusters diverge in their treatment of context as either a relevance-enhancing signal or a fairness-distorting factor. Clusters 1 and 2 treat context as an opportunity — a richer representation that improves relevance estimation. Cluster 4 treats context as a risk — a signal that can encode and amplify existing popularity disparities. Cluster 3 occupies a middle ground, modeling how context (specifically position context) distorts user behavior signals, requiring counterfactual correction. Methodologically, Cluster 2 (dense retrieval) is the most cumulative, with successive papers building directly on prior work (ColBERT → ColBERT-PRF → ColBERT-PRF journal extension). Cluster 5 is the most exploratory, investigating diverse context types without a shared methodological framework.

### Research Gaps

Three critical gaps emerge. **First**, the context-as-opportunity (Clusters 1-2) and context-as-risk (Clusters 3-4) perspectives operate in near-total isolation — confirmed bibliometrically by the TLS 1 link between context-aware and fairness in the keyword network. No paper in the corpus simultaneously optimizes for relevance improvement through context while mitigating context-encoded fairness distortions. **Second**, evaluation of context-aware ranking systems is overwhelmingly offline: of 45 papers, only 6 report online A/B results. Real-world evidence of how context-aware ranking affects resource positioning — which resources gain or lose visibility — is virtually absent. **Third**, context is narrowly operationalized: session history, document structure, and temporal signals dominate. Affective context, social context, cross-device context, and multimodal context (combining text, image, and behavioral signals) are explored in isolated papers but lack systematic treatment.

---

## 3. Future Research Directions

Future research should prioritize: (1) **Unified relevance-positioning frameworks** that simultaneously optimize context-aware ranking for relevance while measuring and mitigating context-driven positioning distortions — bridging the gap between Clusters 1-2 (relevance) and Cluster 4 (fairness). (2) **Online and user-centered evaluation** of how context-aware ranking affects resource positioning in production systems — addressing the "abstraction trap" identified by Klimashevskaia et al. (2024) where bias mitigation is validated only through offline metrics. (3) **Richer context taxonomies** that move beyond session and document context to incorporate affective, social, cross-device, and multimodal signals, with systematic evaluation of how each context type affects both relevance and positioning outcomes. (4) **Cross-platform generalizability studies** establishing whether context-aware ranking methods effective in one domain (e.g., e-commerce) transfer to others (e.g., web search, legal retrieval). (5) **Reproducibility infrastructure** addressing the code and data availability gap documented by Mateos and Bellogin (2025) — fewer than 25% of context-aware recommender system papers provide public implementations.

---

✅ Thematic clustering and comparative synthesis successfully generated.
