# Introduction

## Relevance of the Topic

In recent years, information retrieval (IR) and recommender systems have undergone a fundamental transformation driven by the integration of neural architectures and the growing demand for context-aware, personalized ranking. Modern search engines, e-commerce platforms, and content recommendation systems process billions of user interactions daily, using implicit feedback signals — clicks, dwell time, scroll depth — to train ranking models that determine which information reaches users. However, these signals are systematically distorted by multiple biases: users preferentially click higher-positioned results regardless of relevance (position bias), are never exposed to items the system does not surface (selection bias), and are influenced by the surrounding presentation context (context bias). Unbiased Learning to Rank (ULTR) has emerged as the primary methodological framework for addressing these distortions, employing counterfactual estimation and causal inference to recover true relevance from biased observations.

The significance of this research area extends beyond academic interest. Commercial platforms — including Google Search, Amazon, JD.com, Tencent, and Meituan — have reported measurable business impact from bias correction methods, with improvements ranging from 2.4% click-through rate increases to 6.5% gross merchandise volume gains. Simultaneously, the rapid emergence of Large Language Models (LLMs) is disrupting core assumptions about how retrieval systems are architected, introducing both new capabilities (generative retrieval, LLM-as-ranker) and new bias types (hallucination bias, instruction bias). Understanding the intersection of ULTR, context-aware ranking, and generative retrieval is therefore critical for both the theoretical advancement and responsible deployment of modern information access systems.

## Literature Gap

Several surveys have addressed aspects of this landscape. Gupta et al. (2023) provided a comprehensive tutorial on ULTR foundations. Dai et al. (2024) surveyed bias and unfairness in LLM-era IR systems. Li et al. (2025) systematically reviewed Generative Information Retrieval. Mateos and Bellogin (2025) conducted a systematic review of context-aware recommender systems. However, these reviews address individual subfields in isolation. No existing review integrates the three dimensions — bias correction, context-aware ranking, and generative retrieval — into a unified analytical framework. Furthermore, existing surveys do not combine systematic literature review methodology with bibliometric analysis, limiting their ability to quantify research trends, map author networks, and identify structural patterns in the field's evolution.

The present review addresses this gap by conducting a hybrid systematic-bibliometric analysis of 69 peer-reviewed publications (2021–2025) at the intersection of ULTR, context-aware IR, and neural ranking, supplemented by bibliometric data from 71 Scopus-indexed records. This integrated approach enables both qualitative synthesis of research themes and quantitative analysis of keyword trends, author productivity, and temporal evolution.

## Research Goal and Questions

The primary goal of this review is to provide a comprehensive, structured synthesis of research at the intersection of ULTR and context-aware information retrieval, identifying the dominant thematic clusters, methodological approaches, research trends, and gaps that define the field's current state and future trajectory. The review is guided by four research questions:

1. **RQ1**: What are the main thematic clusters in ULTR and context-aware information retrieval research from 2021 to 2025?
2. **RQ2**: What methodologies dominate the field — neural ranking architectures, bias correction frameworks, or context modeling approaches?
3. **RQ3**: What are the key research gaps at the intersection of ULTR and context-aware information retrieval?
4. **RQ4**: Who are the most prolific authors, what are the dominant keywords, and how has the field evolved temporally?

## Structure of the Paper

The remainder of this paper is organized as follows. Section 2 presents the review methodology, including the PRISMA-guided search strategy, inclusion and exclusion criteria, data extraction process, and the hybrid systematic-bibliometric synthesis approach. Section 3 reports the results, organized around five thematic clusters identified through content analysis: bias detection and correction in LTR, context-aware neural ranking architectures, recommender system bias and fairness, generative IR and LLM-based ranking, and evaluation and cross-cutting methodologies. Section 4 discusses the findings, comparing clusters, interpreting temporal trends, and examining the implications of the LLM-driven paradigm shift for the field. Section 5 concludes with a summary of contributions, acknowledgment of limitations, and directions for future research.
