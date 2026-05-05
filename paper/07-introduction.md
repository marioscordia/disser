# Introduction

## Relevance of the Topic

In modern web search and recommendation systems, the relevance of retrieved results and their positioning in the ranked output directly determine which information reaches users. Context-aware machine learning ranking algorithms — models that dynamically adjust result ordering based on situational, behavioral, and environmental signals — have emerged as a central mechanism for improving both relevance estimation and result personalization. These algorithms incorporate diverse contextual factors: session history and query context in web search (Chen et al., 2020), user embeddings and sequential behavior in music recommendation (Hansen et al., 2020), document-level contextual signals in neural re-ranking (Zerveas et al., 2022), and spatio-temporal context in service ranking. By adapting ranking decisions to context, these systems promise more accurate relevance assessment and more personalized resource positioning.

However, the relationship between context-awareness and positioning outcomes is not straightforward. Contextual signals can improve relevance — as demonstrated by BERT-based dense retrieval augmented with pseudo-relevance feedback (Wang et al., 2021, 2023) and context-aware click models that disentangle examination from relevance (Chen et al., 2020). Yet contextual signals can also amplify existing distortions: popularity bias in recommender systems systematically advantages already-popular resources regardless of contextual relevance (Klimashevskaia et al., 2024; Abdollahpouri et al., 2021), and position bias creates feedback loops where highly-positioned resources accumulate clicks irrespective of merit (Kiyohara et al., 2022). Understanding how context-aware ML ranking algorithms affect both the relevance and the positioning of web resources — and developing methods for analyzing this dual impact — is therefore critical for building information access systems that are both effective and fair.

## Literature Gap

Existing surveys have addressed individual dimensions of this problem. Gupta et al. (2023) provided a tutorial on unbiased learning to rank foundations. Klimashevskaia et al. (2024) and Abdollahpouri et al. (2021) surveyed popularity bias in recommender systems. Dai et al. (2024) examined bias and unfairness in the LLM era. Mateos and Bellogin (2025) systematically reviewed context-aware recommender systems. However, no existing review integrates the two outcome dimensions — relevance and positioning — into a unified analytical framework. Specifically, no review examines how context-aware ranking algorithms simultaneously affect (a) the relevance of retrieved results and (b) the positioning of web resources in ranked outputs, nor does any review combine systematic literature review methodology with bibliometric network analysis to quantify the structural relationships among these research themes.

## Research Goal and Questions

The primary goal of this review is to provide a comprehensive, structured synthesis of research on context-aware ML ranking in web search and recommendation systems, with specific focus on the dual impact on relevance and resource positioning. The review is guided by four research questions:

1. **RQ1**: What are the main thematic clusters in context-aware ML ranking research for web search and recommendation systems (2020–2025)?
2. **RQ2**: What methodologies dominate — neural ranking architectures, bias correction frameworks, or context modeling approaches?
3. **RQ3**: How does context-aware ML ranking affect the relevance and positioning of web resources?
4. **RQ4**: What are the key research gaps at the intersection of context-awareness, ranking fairness, and result positioning?

## Structure of the Paper

The remainder of this paper is organized as follows. Section 2 presents the review methodology, including the PRISMA-guided search strategy, inclusion and exclusion criteria, data extraction process, and the hybrid systematic-bibliometric synthesis approach employing VOSviewer. Section 3 reports the results, organized around five thematic clusters identified through combined content analysis and bibliometric mapping. Section 4 discusses the findings, interpreting the cluster structure, comparing with prior surveys, and examining implications for relevance-oriented and positioning-aware ranking system design. Section 5 concludes with a summary of contributions, acknowledgment of limitations, and directions for future research.
