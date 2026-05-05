
![](prepared/futureinternet-17-00360/images/futureinternet-17-00360.pdf-0001-00.png)


## _Article_ 

## **A Novel Framework Leveraging Large Language Models to Enhance Cold-Start Advertising Systems** 

**Albin Uruqi[1] , Iosif Viktoratos[1,] * and Athanasios Tsadiras[2]** 

- 1 Department of Computer Science, American College of Thessaloniki, 55535 Pilea, Greece; albinuruqi@gmail.com 

- 2 School of Economics, Aristotle University of Thessaloniki, 54124 Thessaloniki, Greece; tsadiras@econ.auth.gr ***** Correspondence: ivictor@act.edu 

## **Abstract** 

Academic Editors: Massimo Stella and Giulio Rossetti 

Received: 30 June 2025 Revised: 27 July 2025 Accepted: 6 August 2025 Published: 8 August 2025 

**Citation:** Uruqi, A.; Viktoratos, I.; Tsadiras, A. A Novel Framework Leveraging Large Language Models to Enhance Cold-Start Advertising Systems. _Future Internet_ **2025** , _17_ , 360. https://doi.org/10.3390/fi17080360 

**Copyright:** © 2025 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https://creativecommons.org/ licenses/by/4.0/). 

The cold-start problem remains a critical challenge in personalized advertising, where users with limited or no interaction history often receive suboptimal recommendations. This study introduces a novel, three-stage framework that systematically integrates transformer architectures and large language models (LLMs) to improve recommendation accuracy, transparency, and user experience throughout the entire advertising pipeline. The proposed approach begins with transformer-enhanced feature extraction, leveraging self-attention and learned positional encodings to capture deep semantic relationships among users, ads, and context. It then employs an ensemble integration strategy combining enhanced stateof-the-art models with optimized aggregation for robust prediction. Finally, an LLM-driven enhancement module performs semantic reranking, personalized message refinement, and natural language explanation generation while also addressing cold-start scenarios through pre-trained knowledge. The LLM component further supports diversification, fairnessaware ranking, and sentiment sensitivity in order to ensure more relevant, diverse, and ethically grounded recommendations. Extensive experiments on DigiX and Avazu datasets demonstrate notable gains in click-through rate prediction (CTR), while an in-depth real user evaluation showcases improvements in perceived ad relevance, message quality, transparency, and trust. This work advances the state-of-the-art by combining CTR models with interpretability and contextual reasoning. The strengths of the proposed method, such as its innovative integration of components, empirical validation, multifaceted LLM application, and ethical alignment highlight its potential as a robust, future-ready solution for personalized advertising. 

**Keywords:** artificial intelligence; machine learning; click-through rate (CTR); artificial neural networks; cold-start; large language models (LLMs) 

## **1. Introduction** 

The CTR prediction problem is central to personalized advertising systems, enabling real-time ad ranking and selection so as to maximize the click probability from a user. Even small improvements in prediction accuracy can yield measurable gains in conversions and revenue [1–3]. Deep learning models have transformed CTR prediction in recent years, using embeddings and deep Neural Nets (NNs) to model complex interactions and outperform traditional approaches like logistic regression [4,5]. 

A persistent limitation of deep CTR models is their reliance on historical data. In cold-start scenarios, common issues involve new users or ads lacking interaction history, 

https://doi.org/10.3390/fi17080360 

_Future Internet_ **2025** , _17_ , 360 

_Future Internet_ **2025** , _17_ , 360 

2 of 21 

or conventional deep learning methods that fail to personalize effectively [6]. This issue becomes even more critical in a special cold-start case when there is no historical data available, called frozen-start. Frozen-start refers to the challenge of providing accurate recommendations for new users/items with no historical interaction data [3]. Common industry workarounds include default profiles, content-based heuristics, and exploration methods to bootstrap data [7]. Yet, these models still falter with new IDs, as embeddings for unseen users or ads are often random or default, limiting model effectiveness in coldstart cases. 

To address the persistent cold-start problem in click-through rate (CTR) prediction, recent studies have increasingly focused on transformer-based architectures, which have demonstrated strong capabilities in sequence modeling and contextual representation learning [8,9]. Drawing inspiration from natural language-processing models such as BERT, these approaches enable the dynamic embedding of user behavior and advertisement content, thereby facilitating the modeling of temporal shifts in user interests and improving the interpretation of raw sequential data [10]. Notably, Meta’s implementation of a sequence-based ad recommender system yielded a 2–4% improvement in conversion rates, while large-scale language models that encode ad textual content have reported CTR gains of up to 2% [11]. The attention mechanisms inherent in transformers further enhance the modeling of complex feature interactions, positioning them as particularly effective tools for sparse-data contexts such as cold-start scenarios [12]. Moreover, large language models (LLMs), including GPT-4 and Gemini, have shown considerable potential in cold-start recommendation settings by leveraging their extensive world knowledge and zero-shot reasoning capabilities. These models can infer user preferences directly from textual descriptions, making them well-suited for content-based personalization when behavioral data is unavailable [13]. These developments collectively suggest that the integration of LLMs into advertising systems represents a promising research frontier. However, such integration presents non-trivial challenges: LLMs are computationally demanding and, in their default state, lack the domain-specific alignment necessary for effective personalization without additional adaptation. 

In response to these challenges, this work proposes a hybrid framework that integrates a deep CTR prediction model with an LLM-based semantic encoder to enhance performance in frozen-start advertising scenarios. This work presents a comprehensive three-stage implementation architecture that addresses frozen-start challenges in advertising platforms through the strategic integration of transformer-based CTR prediction with LLM capabilities. The first stage employs transformer-enhanced feature representation with self-attention mechanisms to capture semantic relationships among sparse user attributes and advertisement content. The second stage implements an ensemble methodology combining four transformer-enhanced models through learnable weighted aggregation to generate robust predictions and select top-performing candidates. The final stage utilizes Gemini 2.5 LLM for semantic reranking, runtime message personalization, and explanation generation, providing transparency and improved user trust. Through controlled experiments and user studies, the framework demonstrates quantitative improvements in user perception of relevance, system transparency, and overall recommendation quality, offering a practical and scalable solution for real-world advertising platforms facing frozen-user scenarios. 

The rest of the paper is structured as follows: Section 2 reviews the literature highlighting gaps and presents the contribution of this work. Section 3 details our three-stage framework, while Section 4 presents its validation methodology through large-scale experiments and user studies. Section 5 demonstrates the results and discusses them, while Section 6 concludes with implications for advertising platforms and future extensions. 

_Future Internet_ **2025** , _17_ , 360 

3 of 21 

## **2. Related Work and Contribution** 

## _2.1. CTR Prediction State-of-the-Art Models_ 

Deep CTR prediction models traditionally adopt an embedding-plus-MLP architecture, which efficiently handles high-cardinality categorical features and learns non-linear feature interactions. Pioneering work like Google’s Wide & Deep [14] and Deep Crossing [15] demonstrated the benefit of combining memorization (via wide features) and generalization (via deep layers), while Facebook’s DLRM extended this design to web-scale ad ranking with large embedding tables and deep networks. These models established the embedding– MLP structure as a production standard. 

To enhance interaction modeling, researchers introduced explicit feature-interaction mechanisms, such as in DeepFM [16] and xDeepFM [17], which fuse factorization machines with deep architectures. The Deep & Cross Network (DCN) series introduced cross layers that model bounded-degree interactions with low additional latency, improving performance in real-world systems like Google Ads. More recently, transformer-based models have gained traction due to their superior ability to capture high-order dependencies. Selfattention architectures such as AutoInt and STEC dynamically learn feature importance and co-dependencies, often boosting performance for rare events [18]. Retrieval-Augmented Transformers further integrate external memory or content indices, aiding in long-tail item recommendation without overwhelming model complexity [19]. 

Sequence modeling has emerged as a major trend, particularly for capturing temporal user behavior. Instead of relying solely on static feature aggregates, transformers now process raw event timelines to track interest evolution over time. In production settings, Meta’s sequence-based ad recommender has shown measurable conversion improvements by modeling recency and engagement order. 

While these approaches efficiently handle high-cardinality categorical features, they face three key limitations: (1) performance degrades significantly with feature sparsity, as rare categories fail to learn meaningful representations; (2) they require extensive historical interaction data (typically millions of examples) to achieve adequate performance; and (3) they exhibit severe cold-start problems, struggling to represent new users/items without substantial interaction history. 

## _2.2. Cold-Start-Related Approaches_ 

Because the above deep learning models struggle in cold-start scenarios, various strategies have been proposed to mitigate this. 

1. Content-based initialization uses ad metadata, visual descriptors, or textual content to seed embeddings for unseen entities. This allows models to assign a “best guess” representation even before interaction data accumulates. For example, meta-learning approaches such as RGMeta and Graph Meta Embedding create pseudo-cold-start episodes during training, enabling the model to infer embeddings based on feature similarities or graph neighborhoods [7]. Nevertheless, content-based initialization depends heavily on high-quality metadata or descriptors, which are often incomplete or uninformative for novel entities, limiting embedding quality. Also, meta-learning methods require artificially constructed training episodes that may not reflect realworld cold-start dynamics, risking poor generalization. 

2. Exploration-driven approaches treat the early recommendation phase as a contextual bandit problem, allocating impressions to gather information while minimizing immediate revenue loss. Large-scale video platforms have reported over 60% improvement in new-ad performance by applying such strategies in production deployments. Contextual bandits improve new-ad performance but incur exploration costs and require careful reward balancing to mitigate short-term revenue loss. 

_Future Internet_ **2025** , _17_ , 360 

4 of 21 

3. Graph neural networks (GNNs) represent features or users as nodes and propagate relational signals through edges, making them robust to sparse data. Fi-GNN and other graph-enhanced CTR models improve representation learning by capturing inter-feature and inter-entity structures [20]. However, graph neural networks suffer from computational inefficiency at scale. 

4. Two-tower architectures have gained popularity by separating user and item encoders, enabling efficient candidate retrieval via approximate nearest neighbors. The shortlisted candidates are then re-ranked using richer single-tower or cross-attention-based models, balancing efficiency and accuracy [21]. Nevertheless, two-tower architectures trade interaction modeling for speed, potentially missing key cross-feature signals. 

Overall, hybrid architectures aim to bridge memorization and generalization, making the system more robust across both dense and sparse data regimes. 

## _2.3. LLM-Based Systems_ 

Recent advances in large language models (LLMs) offer a new avenue for addressing cold-start challenges. With their ability to perform zero-shot and few-shot reasoning, LLMs can infer meaningful representations from textual descriptions alone, eliminating the need for historical interaction data. Prompted GPT-3 has been shown to rank items based on natural language preference statements, achieving accuracy comparable to collaborative filtering in near cold-start environments [22]. Similarly, LLMTreeRec recasts item recommendation as a language-modeling task, using large-scale LLMs like GPT-4 to cluster and rank items without domain-specific training [23]. However, these generalpurpose models may struggle with long-tail coverage or niche inventory due to their broad pretraining corpus. 

To address scalability and efficiency constraints in production environments, Alibaba’s FilterLLM introduced a distilled LLM that generates engagement-probability vectors directly from ad text. This approach supports billion-scale inventory filtering with a 30 _×_ efficiency gain and a measurable CTR lift in live deployments [24]. Google’s Gemini 2.0, deployed via Vertex AI, extends LLM capabilities further into multimodal reasoning by integrating text, image, and audio data to infer creative relevance and audience fit, which is especially valuable for cold-start ad selection and reranking [25]. However, domain adaptation remains critical. For example, LawLLM, a domain-specific model tailored for the U.S. legal domain, that significantly improves zero- and few-shot performance through task customization and retrieval-enhanced architecture [26]. This demonstrates the value of domain specialization for validating models such as Gemini-based rerankers in real-world applications. 

The integration of LLMs into explainable and interpretable recommendation systems is gaining traction. Applied language models for health prediction tasks, emphasizing explainability and demonstrating the utility of NLP-derived features for interpretable, domain-specific prediction across verticals like healthcare and nutrition [27]. These findings are highly relevant for advertising use cases that require transparent justifications for recommendations or decisions. 

Moreover, Zhang et al. (2025) present a comprehensive survey of cold-start recommendation approaches leveraging LLMs, encompassing prompt-based, generative, and hybrid architectures [28]. Their framework situates current efforts within a broader methodological landscape and underscores the importance of adapting LLM architectures to domain-specific, high-precision use cases. These insights reinforce the trajectory of hybrid LLM pipelines, where task-specific distilled models handle real-time scoring, while candidate generation is augmented through retrieval or caching mechanisms. Nonetheless, 

_Future Internet_ **2025** , _17_ , 360 

5 of 21 

caution is warranted as LLMs may hallucinate associations not supported by empirical data, necessitating calibration through real-time feedback loops and brand-safety constraints. 

LLM-based systems face three key barriers to production adoption: (1) prohibitive computational costs and latency that conflict with real-time ad serving requirements, (2) risks of hallucinated recommendations requiring extensive safety guardrails and calibration, and (3) domain adaptation challenges where general pretraining fails to capture advertising-specific nuances. Ongoing research focuses on optimizing LLMs via distillation, quantization, and modular integration—aligning their expressiveness with productionlevel latency demands. These developments suggest a future in which LLMs enhance traditional CTR prediction pipelines with world knowledge and robust generalization, especially under data-sparse or cold-start conditions. 

## _2.4. Contribution_ 

The most significant novelty of this work lies in its holistic approach to cold-start advertising that simultaneously addresses representation learning, prediction uncertainty, and semantic understanding through a unified framework. The proposed framework fundamentally differs from existing cold-start approaches through its multi-stage architecture that systematically addresses different aspects of the frozen-user problem. Previous literature typically focuses on individual aspects of the cold-start problem, such as either improving embedding methods or leveraging external knowledge, but rarely combines these approaches in a systematic manner. Also, traditional content-based initialization methods rely solely on metadata similarity, while this work combines transformer-enhanced feature representation with ensemble predictions and semantic reranking to create a more robust recommendation pipeline. The incorporation of contextual relevance, recommendation diversification, sentiment-aware ranking, and bias mitigation within the LLM stage represents a comprehensive approach to cold-start challenges that existing single-method solutions cannot achieve. 

Additionally, the components of this framework offer partial scientific contributions as well as potential societal benefits, which can be outlined as follows: 

1. Transformer-Enhanced Feature Extraction: We validate that replacing conventional embedding mechanisms with transformer-based architectures significantly improves feature representation for frozen-start users, yielding superior performance on standard CTR prediction benchmarks. Unlike conventional CTR prediction models that rely on static embeddings and struggle with sparse user data, this approach enables dynamic semantic relationship modeling between user attributes, advertisement content, and contextual information. 

2. Ensemble Learning Framework: We develop and validate a novel ensemble approach that effectively combines multiple transformer-enhanced models to produce more accurate CTR predictions than any individual model, addressing the variability inherent in frozen-start scenarios. This ensemble approach differs from traditional cold-start solutions by leveraging diverse modeling perspectives simultaneously rather than relying on individual techniques such as content-based initialization or explorationdriven approaches. The learnable weighted aggregation strategy ensures that model contributions are dynamically balanced based on performance rather than fixed predetermined weights. This adaptive weighting mechanism addresses the limitation of static ensemble approaches that cannot adjust to varying data distributions in cold-start scenarios. 

3. LLM-Powered Reranking and Refinement: This LLM-powered enhancement system addresses critical limitations observed in previous studies by combining the computational efficiency of traditional CTR models with the semantic understanding 

_Future Internet_ **2025** , _17_ , 360 

6 of 21 

capabilities of large language models. Unlike existing LLM-based systems that suffer from latency constraints and hallucination issues, this framework employs the LLM only for post-processing the top-five candidates, significantly reducing computational overhead while maintaining the benefits of semantic reasoning. Moreover, conventional approaches that either fully replace traditional models with LLMs or use them in isolation, while the proposed solution leverages the complementary strengths of both paradigms while systematically addressing their individual weaknesses through built-in fairness constraints, sentiment analysis, and real-time adaptation capabilities. This integrated approach not only enhances performance but also provides an ethically grounded solution to persistent cold-start challenges that are frequently neglected in existing systems. Finally, the integration of explainability features and real-time message refinement significantly enhances recommendation transparency and interpretability, enabling dynamic content adaptation that surpasses conventional static recommendation approaches. 

## **3. Materials and Methods—The Proposed Framework** 

Our framework addresses the frozen-user problem through a comprehensive threestage approach (Figure 1): 


![](prepared/futureinternet-17-00360/images/futureinternet-17-00360.pdf-0006-05.png)


**Figure 1.** Framework illustration. 

## _3.1. Stage 1: Transformer-Enhanced Feature Representation_ 

Traditional click-through rate (CTR) prediction models in recent years have predominantly utilized shallow embedding methods, which often fail to capture nuanced user attributes, particularly in scenarios where historical data is limited or unavailable. In this study, transformer-based architectures are explored and validated as a replacement for these conventional embedding mechanisms to more effectively encode the semantic relationships among user attributes, advertisement content, and contextual information. Specifically, the proposed approach incorporates self-attention with learned relative positional bias encoding, rather than relying on traditional embedding techniques. Experimental evaluations on 

_Future Internet_ **2025** , _17_ , 360 

7 of 21 

the DigiX and Avazu datasets demonstrate that these architectural enhancements result in significant performance improvements over state-of-the-art baseline methods. 

## _3.2. Stage 2: Ensemble Model Integration_ 

To address the inherent uncertainty in cold-start prediction, an ensemble methodology that combines predictions from multiple transformer-enhanced models was developed. DCN-V2, DIFM, FiBiNET, and MMOE were used [29,30]. This ensemble approach: 

- Leverages diverse modeling perspectives to improve prediction robustness; 

- Employs a learnable weighted aggregation strategy optimized through fine-tuning; 

- Outputs calibrated probability scores for candidate advertisements; 

- Selects top-performing candidates for further refinement. 

Below, we provide a mathematical formulation of the ensemble process: Let ( _M_ = _M_ 1, _M_ 2, _M_ 3, _M_ 4) denote the four pretrained transformer-enhanced models, where ( _M_ 1 = _DCN-V_ 2, _M_ 2 = _DIFM_ , _M_ 3 = _FiBiNET_ , _M_ 4 = _MMOE_ ). Each model _Mi_ takes a user–ad pair ( _u_ , _a_ ) as input and outputs a probability score ( _pi_ ( _u_ , _a_ ) _∈_ [0, 1]), representing the predicted likelihood of user _u_ clicking on advertisement _a_ . For a set of candidate advertisements _A_ = _a_ 1, _a_ 2, . . . , _aN_ the predictions form a vector: _Pi_ = [ _pi_ ( _u_ , _a_ 1), _pi_ ( _u_ , _a_ 2), . . . , _pi_ ( _u_ , _aN_ )] _∈_ [0, 1] _[N]_[�] for each model ( _i_ = 1, 2, 3, 4). � The ensemble combines these predictions using a linear weighted aggregation with weights _w_ = [ _w_ 1, _w_ 2, _w_ 3, _w_ 4]. To ensure _wi ≥_ 0 and ∑[4] _i_ =1 _[w][i]_[=][1,][the][weights] are derived from learnable parameters _z_ = [ _z_ 1, _z_ 2, _z_ 3, _z_ 4] _∈ R_[4] using the softmax function: _wi_ = _exp_ ( _zi_ )[The][ensemble’s][predicted][score][for][advertisement] _[a][j]_[is] ∑[4] _k_ =1 _[exp]_[(] _[z][k]_[)][.] _sensemble_ � _u_ , _aj_ � = ∑[4] _i_ =1 _[w][i][·][p][i]_ � _u_ , _aj_ � = ∑4 _i_ =1� ∑[4] _k_ = _ex_ 1 _p[exp]_ ( _zi_[(] ) _[z][k]_[)] � _· pi_ � _u_ , _aj_ �. The parameters _z_ are optimized by minimizing the binary cross-entropy loss: _L_ = _− N_[1][∑] _[N] j_ =1� _yjlog_ � _sensemble_ � _u_ , _aj_ �� + �1 _− yj_ � _log_ �1 _− sensemble_ � _u_ , _aj_ ��� where _yj ∈_ 0, 1 is the ground-truth click label. Optimization is performed using gradient descent to balance the contributions of each model, enhancing robustness in cold-start scenarios. The ensemble ranks all advertisements in set A based on their calibrated probabilities. The top 5 candidates are passed to the LLM for message refinement and explanation generation (Section 3.3). This ensemble approach ensures robust predictions by leveraging diverse transformer-enhanced models, with fine-tuned weights optimizing performance for cold-start advertising scenarios 

## _3.3. Stage 3: LLM-Powered Enhancement System_ 

The final stage employs the Gemini 2.5 LLM API to process the top five candidate advertisements _A_ top = _a_ 1, _a_ 2, _a_ 3, _a_ 4, _a_ 5 from the ensemble model (Section 3.2) through three operations: select the best-match advertisement, refine the advertisement message at runtime, and generate an explanation. These operations leverage the LLM’s semantic understanding to improve recommendation quality, personalization, and transparency in cold-start scenarios. In detail: 

1. Semantic reranking and best-match advertisement. The LLM evaluates the top five advertisements to select the one best aligned with the user’s profile, considering contextual relevance, category diversity, sentiment alignment, fairness, and available feedback. The LLM processes a prompt with the user profile (e.g., location, time, inferred preferences) and ad metadata (e.g., description, category). This process incorporates: 

   - Contextual Relevance: The LLM matches user attributes to ad metadata more effectively by processing sparse user data alongside rich ad descriptions and 

_Future Internet_ **2025** , _17_ , 360 

8 of 21 

categories [31]. We include in the prompt a directive to prioritize ads whose metadata aligns closely with user attributes. 

- Recommendation Diversification: Using techniques inspired by Maximal Marginal Relevance [32], the LLM ensures the top recommendations span varied categories rather than redundant offerings. We include a prompt instruction to favor ads from distinct categories, reducing redundancy among the top selections. 

- Sentiment-Aware Ranking: The LLM incorporates sentiment analysis on the content to prioritize ads that align with positive user preferences inferred from available data [33]. We include a directive to prioritize ads with positive sentiment that matches user preferences, based on the LLM’s natural languageprocessing capabilities. 

- Bias Mitigation: The system implements fairness constraints to prevent overrepresentation of certain ad categories and ensure balanced recommendations [34]. An instruction is added to ensure balanced category representation among the selected ads, using metadata to identify categories. 

- Real-Time Adaptation: The LLM framework can dynamically update rankings based on user feedback signals [35]. 

The mathematical formulation of the process can be written as follows: 

Let _U_ be the user profile, encoded as a feature vector. Each ad _aj ∈ Atop_ has metadata encoded as _vj_ . The LLM computes a semantic relevance score _r_ ( _u_ , _aj_ ) = _cosine_  similarity_ ( _LLMembed_ ( _U_ ), _LLMembed_ ( _vj_ )), where _LLMembed_ is the Gemini 2.5 embedding function [31]. The ad with the highest score is selected. 

2. Message Refinement: For the top-ranked advertisement, the LLM generates refined messaging that better aligns with the user’s profile characteristics while maintaining the core business proposition. This personalization process leverages: 

   - Inferred user preferences based on location, time, and domain context [36]; 

   - Semantic understanding of user attributes to tailor messaging tone and content; 

   - _•_ Adaptation to potential user needs even with limited historical data [37]. 

3. Explanation Generation: The system produces natural language explanations that articulate the reasoning behind the recommendation, increasing transparency and helping users understand why particular advertisements were selected or eliminated. These explanations: 

   - Reveal the factors influencing the recommendation decision; 

   - Build user trust by making the recommendation process transparent [38]; 

   - Address the “black box” nature of traditional recommendation systems. 

Table 1 below demonstrates the prompt message and LLM communication through API calls. 

4. Cold-Start Problem Mitigation: The LLM leverages its pre-trained knowledge to generate recommendations even in the absence of user interaction history. By employing transfer learning techniques [39], the system can: 

   - Use pre-trained embeddings to fill gaps in sparse data scenarios; 

   - Infer ad relevance based on content descriptions and categories; 

   - Generalize patterns from similar users or products to new entities. 

_Future Internet_ **2025** , _17_ , 360 

9 of 21 

## **Table 1.** LLM prompt. 

You are an expert copywriter and evaluator for targeted advertising. Given a user profile [attributes: location, time, website type etc.] and a list of five advertisements [categories, descriptions], perform the following: 

1. Select the best-matching ad by evaluating: 

   - Contextual Relevance: Prioritize ads whose metadata (description, category) closely aligns with user attributes, using semantic understanding for sparse data. 

   - Recommendation Diversification: Favor ads from distinct categories to avoid redundancy. 

   - Sentiment Alignment: Prioritize ads with positive sentiment matching user preferences. 

   - Bias Mitigation: Ensure balanced category representation, penalizing overrepresented categories. 

   - Real-Time Adaptation: If feedback signals [e.g., clicks, dwell time] are provided, adjust selection to favor ads with positive feedback. 

2. Craft a compelling one-sentence ad message (max 50 words) for the best-matched ad, tailored to the user’s profile while preserving the ad’s core proposition. 

3. Provide a one-sentence justification (20–30 words) explaining why the best-matched ad was selected, referencing relevant criteria (e.g., relevance, sentiment). 

4. For each of the four remaining ads, generate an alternative one-sentence ad message (max 50 words) and a concise reason (10–20 words) explaining why it was not selected. 

## Output format: 

- 1: “Best-fit ad message”. (Reason: Why this ad was selected based on relevance, sentiment, diversity, fairness, feedback) 

- 2: “Alternative ad message”. (Reason: Why this ad was not selected) 

- 3: “Alternative ad message”. (Reason: Why this ad was not selected) 

- 4: “Alternative ad message”. (Reason: Why this ad was not selected) 

- 5: “Alternative ad message”. (Reason: Why this ad was not selected) 

## Constraints: 

- Keep each ad message to one sentence (max 50 words). 

- Keep reasons objective, relevant, and concise (20–30 words for best-match justification, 10–20 words for rejections). 

- Use a consistent, professional tone across all entries. 

## **4. Validation Methodology** 

The validation strategy recognizes that each stage of the framework requires distinct evaluation methods: quantitative performance assessment for the computational stages (Stages 1 and 2) and qualitative user experience evaluation for the LLM-powered enhancement system (Stage 3). This multi-faceted approach ensures both technical efficacy and practical usability of the proposed framework. 

## _4.1. Dataset Selection for Validation of Stages 1 and 2_ 

To validate the computational components of our framework (transformer-enhanced feature representation and ensemble model integration), we identified and selected two established datasets from the computational advertising domain that are widely accepted by the scientific community for CTR prediction research. The first dataset selected for validation is the Avazu dataset (https://www.kaggle.com/c/avazu-ctr-prediction/overview 

_Future Internet_ **2025** , _17_ , 360 

10 of 21 

(accessed on 13 January 2025)). This dataset provides a robust foundation for testing our approach due to its comprehensive representation of mobile advertising scenarios. The dataset contains nearly 1.1 million records with 23 discrete attributes, offering sufficient data volume for transformer training while maintaining manageable computational requirements. A total of 150K random rows were used in the experiments to reduce training overhead. 

Based on relevance criteria for frozen-start scenarios, to simulate a case like this, the following attributes were selected as model inputs: 

- Temporal attributes: Time period for capturing temporal patterns; 

- Contextual information: Application and site category and domain, application name and ID for content understanding; 

- Placement characteristics: Advertisement position indicating display location; 

- Device specifications: Device type and model for user profiling; 

- Network conditions: Connection type for contextual awareness; 

All selected variables are categorical in nature, with the binary ‘click’ variable (0 or 1) serving as the prediction target. This attribute selection enables a comprehensive evaluation of our transformer-enhanced feature representation capabilities across diverse feature types commonly encountered in cold-start scenarios. 

The second validation dataset is the DigiX dataset (https://www.kaggle.com/ louischen7/2020-digix-advertisement-ctr-prediction (accessed on 17 January 2025)), which provides large-scale validation capabilities with over 40 million records and 36 different attributes. This dataset enables robust testing of our ensemble approach under high-volume, real-world conditions typical of modern advertising platforms. Once again, 200K random rows were used in the experiments to reduce training overhead. 

The selected input attributes from this dataset include: 

- Temporal dimensions: Time period for temporal pattern recognition; 

- Application categorization: Application and site category for content classification; 

- Advertisement characteristics: Display form of ad material, app level 1 and 2 categories, application ID, tag, and score/rating for comprehensive ad profiling; 

- Device metadata: Device name, size, and model release time for user device understanding; 

- Network specifications: Connection type for contextual adaptation. 

## _4.2. Validation of Stages 1 and 2_ 

For Stages 1 and 2, a quantitative experimental design comparing the transformerenhanced ensemble approach against established baseline methods was performed. The validation process involves: 

- Stage 1 Validation: Several state-of-the-art recommendation models: DCN-V2, DIFM, FiBiNET, and MMO, were used as strong baselines for comparison. These models were evaluated on the two benchmark datasets using standard performance metrics, including AUC and accuracy. Subsequently, we modified their embedding mechanisms by integrating transformer-based enhancements, replacing the traditional shallow embeddings. Comparative experiments were then conducted to systematically assess the impact of these transformer-enhanced representations against the original architectures in frozen-start scenarios. 

- Stage 2 Validation: To evaluate the effectiveness of ensemble integration, we implemented the weighted ensemble model that combines the outputs of the individually enhanced models (DCN-V2, DIFM, FiBiNET, and MMOE). The ensemble was tested on the same datasets, and its performance was compared directly against each individual model. This allowed us to assess whether combining transformer-enhanced 

_Future Internet_ **2025** , _17_ , 360 

11 of 21 

architectures could yield further gains in AUC and accuracy beyond what each model achieved independently. 

## _4.3. Stage 3 and Integrated Framework Validation Through User Study_ 

To validate the LLM-powered enhancement system (Stage 3) and the integrated framework performance, a dedicated website was developed to facilitate comprehensive user interaction and evaluation. Built upon this web-based platform, a systematic user study methodology was designed to evaluate the model’s overall performance alongside LLM utilization for semantic reranking, message refinement, and explanation generation capabilities through direct user feedback. 

A between-subjects comparative survey design was employed to investigate user responses to online advertisements under two distinct presentation conditions. The study received appropriate ethical clearance, and informed consent was obtained from all participants prior to participation. A total of 46 participants were recruited via convenience sampling through social media platforms (Facebook, LinkedIn). Volunteers were invited to participate through anonymous recruitment messages that did not collect or store any personal identifying information. All data collection maintained strict anonymity protocols. No personal identifying information (names, email addresses, IP addresses, or social media profiles) was collected or stored. Participants were assigned random alphanumeric codes for data-tracking purposes. Participants ( _n_ = 46) were randomly assigned to one of two experimental conditions using block randomization to ensure equal group sizes (Condition 1: _n_ = 23; Condition 2: _n_ = 23). A Randomized Control Trial (RCT) design was implemented to moderate selection bias and support causal interpretation. Eligibility criteria required participants to be active users of the internet or social media platforms and over the age of 18. 

Comprehensive statistical analyses were conducted to verify equivalent group distribution across key demographic variables: 

Gender Distribution: 

- Condition 1: 54% male ( _n_ = 12), 46% female ( _n_ = 11); 

- Condition 2: 58% male ( _n_ = 13), 42% female ( _n_ = 10); 

- Chi-square test: χ[2] (1, _N_ = 46) = 0.089, _p_ = 0.778. Age Category Distribution: 

- 18–24 years: Condition 1 ( _n_ = 5), Condition 2 ( _n_ = 4); 

- 25–34 years: Condition 1 ( _n_ = 6), Condition 2 ( _n_ = 5); 

- 35–44 years: Condition 1 ( _n_ = 5), Condition 2 ( _n_ = 6); 

- 45–54 years: Condition 1 ( _n_ = 4), Condition 2 ( _n_ = 5); 

- 55+ years: Condition 1 ( _n_ = 3), Condition 2 ( _n_ = 3); 

- Chi-square test: χ[2] (4, _N_ = 46) = 0.542, _p_ = 0.969. 

Internal consistency reliability was assessed for all multi-item Likert scale measures using Cronbach’s alpha: 

- Advertisement Relevance (3 items): α = 0.89, 7%; 

- Behavioral Intention (3 items): α = 0.81, 95%; 

- Explanation Effectiveness (3 items): α = 0.87, 9%; 

- Comparative Relevance (3 items): α = 0.85, 8%; 

- Message Quality (3 items): α = 0.88, 3%. 

All reliability coefficients exceeded the conventional threshold of 0.70, indicating acceptable to excellent internal consistency for the measurement scales employed in this study. 

The experiment simulated a realistic online browsing scenario. Each participant was presented with a mock website, with the site type randomly assigned from one of several 

_Future Internet_ **2025** , _17_ , 360 

12 of 21 

categories (e.g., food, travel, health). Although each participant was shown a different website type, the structural and visual design of the websites remained identical across all conditions, ensuring experimental control. The website category was clearly displayed to reinforce the simulated context of user interest in a particular domain. Following website exposure, participants were shown five advertisements. The selection and presentation of these advertisements varied by condition: 

- Condition 1: AI-enhanced Recommendation System Advertisements were initially selected from an experimentally curated ad pool using the ensemble prediction model, which estimated the likelihood of ad engagement based on both user-profile data and the assigned website category. The top five ads with the highest predicted click-through probabilities were passed to a large language model (LLM) API for further personalization. The LLM dynamically refined the content of the most relevant ad message and provided a brief explanation based on the user profile and context. It also evaluated whether a reranking of the selected ads was necessary. Participants in this condition were shown the final recommended advertisement (post-refinement), a system-generated explanation message, and the four excluded ads that were not selected as optimal. 

- Condition 2: Baseline (Random Selection) Participants were shown five randomly selected advertisements from the same ad pool. One was randomly labeled as the recommended ad, and the remaining four were presented as excluded. No personalization or explanation was provided. 

After viewing the website and advertisements, participants completed an online survey (see Appendix A) designed to assess their perceptions, attitudes, and reactions to the ads. The survey was identical across both experimental conditions, with the exception of one question group specific to Condition 1, which addressed the explanation message. The entire experimental session took approximately 10 min per participant. 

Participants responded to key components using 5-point Likert scales (1 = lowest, 5 = highest). Each component was measured using a group of three related questions to ensure reliability. The measured components included: 

1. Advertisement Relevance: A set of three questions assessing how relevant participants perceived the ad to be. 

2. Behavioral Intention: A three-question group evaluating the likelihood of participants engaging with the ad (e.g., clicking on it). 

3. Explanation Effectiveness: 

   - Condition 1: Questions focused on whether the provided explanation helped participants understand why the ad was shown and whether it increased their likelihood of engaging with the ad. 

   - Condition 2: Questions asked participants whether an explanation (hypothetically) would increase their receptiveness to the ad. 

4. Comparative Relevance: Three questions assessing the perceived relevance of the displayed ad compared to potential alternatives that were not shown. 

5. Message Quality: A question group evaluating the clarity and communicative effectiveness of the ad’s message. 

Additionally, participants were asked to select one or more factors that influence their clicking decisions from a list including relevance/interest, explanation, transparency, advertisement message, design, and brand. 

Finally, to also evaluate the linguistic clarity of the LLM-generated explanations and compare them with the user study findings, we employed the Flesch–Kincaid readability test. This is a widely used computational metric that assesses how easily a text can be 

_Future Internet_ **2025** , _17_ , 360 

13 of 21 

understood by readers. This test is applied programmatically and provides two scores: the Flesch Reading Ease, which rates readability on a scale from 0 to 100 (with higher values indicating easier comprehension), and the Flesch–Kincaid Grade Level, which estimates the U.S. school grade required to understand the text. We applied this test to all LLM-generated explanations in our study and calculated the average to quantitatively assess their accessibility and alignment with our prompt constraints (e.g., professional tone, concise length). 

## **5. Results and Discussion** 

## _5.1. Transformer-Based Feature Representation and Ensembler Model Evaluation Results_ 

Following data preprocessing, a systematic evaluation of the transformer-enhanced ensemble approach on the DigiX and Avazu datasets was conducted, focusing on frozenstart advertising scenarios. The experimental design involved two stages as discussed above: optimizing individual state-of-the-art models (DCN-V2, DIFM, FiBiNET, MMOE) and evaluating their transformer-enhanced versions, followed by assessing the weighted ensemble model. To establish robust baselines, we optimized the architectures and hyperparameters of DCN-V2, DIFM, FiBiNET, and MMOE using grid search and iterative testing to maximize AUC and accuracy on both datasets. Common parameters across all models included a batch size of 2086, ReLU activation in hidden layers, sigmoid activation in the output layer, binary cross-entropy (BCE) loss, Xavier weight initialization, and 20 epochs, with learning rates of 0.001 for DigiX and 0.001 for Avazu, using the Adam optimizer (Table 2 below). Model-specific parameters, such as the number of neurons (ranging from 32 to 400), layers (2 to 4), and dropout rates (0.1 to 0.3), were tuned individually to optimize performance, with configurations selected based on validation set performance. Subsequently, each model was modified by replacing traditional shallow embeddings with transformer-based feature representations, incorporating single-head attention and positional encoding to capture semantic relationships in sparse data. To ensure fairness in evaluating these modifications, we applied the same optimized parameters as the baselines, maintaining consistency across experiments. The transformer-enhanced models were evaluated on the same data. Finally, the weighted ensemble model, combining the outputs of the transformer-enhanced DCN-V2, DIFM, FiBiNET, and MMOE, was evaluated to assess its effectiveness against individual models. The ensemble used a softmax-derived weighting scheme (Section 3.2), with weights optimized via grid search to minimize BCE loss on validation sets. The same common parameters were applied to ensure consistency. 

**Table 2.** Common optimal parameters. 

|**Parameter**|**DigiX**|**Avazu**|
|---|---|---|
|Learning rate|0.001|0.001|
|Optimizer|Adam|Adam|
|Batch size|2086|2086|
|Embedding size|32|32|
|Activation functions|ReLU in hidden layers, Sigmoid in output|ReLU in hidden layers, Sigmoid in output|
|Loss function|BCE|BCE|
|Epochs|20 with early stopping|20 with early stopping|
|Weight initialization|Xavier|Xavier|



Starting with the Avazu dataset (Table 3—PI stands for performance improvement over its original counterpart and for ensemble over the best model), the experimental results demonstrate consistent performance improvements across all base models when enhanced with self-attention and positional bias (transformer-based feature extraction). 

_Future Internet_ **2025** , _17_ , 360 

14 of 21 

Notably, AUC ROC scores improved for every model variant, outperforming their original counterparts. For instance, DIFM improved from 0.7179 to 0.7229 (0.69%), and DCN from 0.7192 to 0.7224 (0.45%). While the AUC gains may seem modest (generally under 1%), such improvements are meaningful in large-scale recommendation tasks and especially in frozen-user scenarios. Also, in terms of accuracy, enhanced models again show favorable trends, with MMOE-TR and DCN-TR reaching the highest accuracy values (0.8283 and 0.8273, respectively). The ENSEMBLER model achieved the top AUC ROC (0.7251, 0.3% improvement over the best) and accuracy (0.8286), suggesting that combining models further leverages the benefits. Overall, the results indicate that the TR mechanism contributes positively to both discrimination (AUC) and classification performance (accuracy), supporting its value across different model architectures. 

**Table 3.** Initial results using Avazu dataset. 

|**Model Name**|**AUC ROC**|**Accuracy**|**AUC—PI (%)**|
|---|---|---|---|
|DIFM<br>DIFM-TR|0.7179<br>0.7229|0.8255<br>0.8256|0.69|
|DCN<br>DCN-TR|0.7192<br>0.7224|0.8256<br>0.8273|0.45|
|MMOE<br>MMOE-TR|0.7188<br>0.7202|0.8254<br>0.8283|0.19|
|FiBiNET<br>FiBiNET-TR|0.7203<br>0.7214|0.8271<br>0.8272|0.15|
|ENSEMBLER|0.7251|0.8286|0.3|



In DigiX (Table 4), the results also confirm that integrating the transformer-based feature representation module yields consistent improvements across various base models in terms of AUC ROC and accuracy (Table 2). The DIFM model shows the most notable gain, with a 3.45% increase in AUC ROC, rising from 0.6581 to 0.6808. Similarly, MMOE improves from 0.6777 to 0.6870 (1.36%), and FiBiNET from 0.6087 to 0.6178 (1.78%). Although DCN exhibits a smaller improvement (0.33%), it still benefits from transformer integration. These gains are reflected in accuracy metrics as well, where all the enhanced models either match or outperform their baseline versions. The ENSEMBLER model, combining multiple enhanced models, achieves the highest AUC ROC (0.6893) and maintains competitive accuracy, highlighting the additive strength of ensemble learning. 

**Table 4.** Results using DigiX dataset. 

|**Model Name**|**AUC ROC**|**Accuracy**|**PI (%)**|
|---|---|---|---|
|DIFM<br>DIFM-TR|0.6581<br>0.6808|0.9497<br>0.9626|3.45|
|DCN<br>DCN-TR|0.6598<br>0.6619|0.9614<br>0.9623|0.33|
|MMOE<br>MMOE-TR|0.6777<br>0.6870|0.9630<br>0.9630|1.36|
|FiBiNET<br>FiBiNET-TR|0.6087<br>0.6178|0.9267<br>0.9462|1.78|
|ENSEMBLER|0.6893|0.9684|0.33|



Statistical significance was assessed using the DeLong test for AUC comparison, revealing significant improvements of the proposed ensemble over DIFM ( _p_ < 0.05) and 

_Future Internet_ **2025** , _17_ , 360 

15 of 21 

FiBiNET ( _p_ < 0.05) on the DigiX dataset. The absence of statistical differences among most state-of-the-art models is common and reflects the maturity of the field and similar performance levels, making the ensembler’s significant improvements over established models particularly noteworthy. On the other hand, even a small AUC improvement is critical at scale because it translates to millions of additional accurate recommendations in real-world systems, directly impacting revenue and user engagement. For advertising platforms, this marginal gain can significantly reduce wasted impressions and improve targeting efficiency across billions of served ads. 

Overall, the transformer-based feature representation and ensemble method consistently enhance model performance, supporting its integration as an effective mechanism across diverse model architectures. 

## _5.2. Integrated Framework Evaluation Results_ 

A detailed statistical analysis was performed on the questionnaire data. Each construct was measured using a group of three items, and the average of those items was used to compute a composite score per participant. Differences between the two experimental conditions were analyzed using the Mann–Whitney U test, due to non-parametric distribution of responses. 

- Advertisement Relevance: Participants in Survey 1 rated advertisements as significantly more relevant (M = 4.15) than those in Survey 2 (M = 3.25), U = 435.0, _p_ = 0.014. 

- Behavioral Intention: Survey 1 participants reported significantly greater likelihood of clicking on the ad (M = 4.15) compared to Survey 2 (M = 2.69), U = 542.0, _p_ < 0.001. 

- Explanation Effectiveness: Participants in Survey 1, who were shown an explanation, reported higher scores on explanation effectiveness (M = 4.15) than Survey 2 participants (M = 3.23), U = 492.0, _p_ = 0.0017. 

- Comparative Relevance: Survey 1 participants rated the displayed ad as more relevant compared to unseen alternatives (M = 4.00) than Survey 2 participants did (M = 2.69), U = 472.0, _p_ = 0.0015. This difference shows that LLM-enhanced reranking produces ad selections users perceive as substantially more relevant than unrefined alternatives. A limitation in evaluating the complete ensembler + LLM system versus the ensembler is that traditional AUC metrics cannot be directly applied, as the LLM operates as a post-processing reranking layer that selects advertisements based on semantic relevance rather than click probability prediction. Since ground-truth click labels correspond to the original dataset interactions and not to the LLM’s semantic reranking decisions, the system’s final output represents a qualitatively different recommendation paradigm that requires alternative evaluation methodologies beyond standard CTR prediction metrics. 

- Message Quality: Survey 1 participants rated the clarity of the ad’s message higher (M = 4.23) than Survey 2 participants (M = 3.38), U = 548.0, _p_ < 0.001. 

Also, regarding the factors influencing clicking decisions for both conditions, the following results are reported: 

- Relevance/interest: 92.3%; 

- Advertisement message: 84.6%; 

- Brand 61.5%; 

- Design: 53.8%; 

- Explanation: 46.2%; 

- Transparency: 38.4%. 

_Future Internet_ **2025** , _17_ , 360 

16 of 21 

It is worth mentioning that no statistically significant differences were found between groups ( _p_ > 0.05), suggesting that the core perception about the factors that influence ad clicking and emotional response remained consistent across conditions. 

Last, the LLM-generated explanations achieved a Flesch Reading Ease score of 68.73, indicating they are easily understandable by readers with a middle school education. The corresponding Flesch–Kincaid Grade Level of 7.57 suggests the content is suitable for readers around the 7th to 8th grade level. These scores confirm that the explanations maintain a balance between clarity and professionalism, aligning with our prompt constraints. 

This study demonstrates significant differences in user responses to online advertisements based on the advertisement selection process and presentation format. Across five key dimensions—ad relevance, click likelihood, explanation effectiveness, comparative relevance, and message clarity—participants exposed to hybrid model (Survey 1) consistently reported more favorable evaluations than those in the control condition (Survey 2). These results suggest that both the relevance and the presentation context of an advertisement, including the presence of explanations, play critical roles in shaping user engagement and perceptions. The findings align with established theoretical frameworks in personalization and persuasive communication. Specifically, the results support Personalization Theory [40], which argues that tailoring content to individual user preferences enhances satisfaction and engagement. The improved performance in Survey 1 suggests that personalized explanations not only increase perceived relevance but may also create a sense of alignment between user expectations and content delivery. Moreover, the study contributes to the Elaboration Likelihood Model (ELM) of persuasion [41]. According to ELM, when users perceive content as personally relevant, they are more likely to process it via the central route, resulting in stronger and more enduring attitude changes. The use of explanation messages in Condition 1 appears to have triggered such central-route processing, leading to higher engagement intentions, including greater willingness to click on ads. Importantly, these findings intersect with emerging work in Explainable AI (XAI). The explanation mechanism offered in Condition 1 can be seen as a practical application of XAI principles [42], which emphasize transparency in algorithmic systems to foster user trust, perceived fairness, and informed decision-making. Results suggest that explanations can act as cognitive bridges, enhancing the perceived integrity and relevance of AI-driven advertising. Taken together, these insights underscore the potential of large language models (LLMs) not only in optimizing ad relevance but also in enhancing presentation quality, message clarity, and user trust through real-time, context-aware explanations. These improvements could have meaningful impacts on user engagement and conversion rates in digital marketing. 

Further research employing larger and more diverse samples, and a broader range of advertisement types and explanation formats, needs to be conducted. Investigating how explanation length, complexity, and personalization level influence user responses could provide deeper insights. Longitudinal studies could also help determine whether explanationinduced engagement persists over time. Furthermore, incorporating behavioral metrics such as actual click-through rates or dwell time would complement self-reported intentions and offer a more comprehensive understanding of advertising effectiveness. 

The LLM-powered enhancement module delivers substantial improvements in personalization, explainability, and semantic alignment, but these benefits come with computational costs that require careful system-level optimization. In production deployments, we observed that real-time inference using state-of-the-art models like Gemini 2.5 introduces latency between 200 and 500 ms for typical queries ( _≤_ 512 tokens) when using GPU-accelerated API endpoints. To maintain real-time performance while preserving 

_Future Internet_ **2025** , _17_ , 360 

17 of 21 

model capabilities, response caching was used to reduce latency for frequent queries. To further reduce latency and computational costs, we plan to investigate: 

- Knowledge distillation—Training a lightweight student model to replace the current ensemble approach, preserving most accuracy while significantly improving inference speed. 

- Simplified architectures—Evaluating whether slightly less accurate but more efficient models could provide suitable performance for certain use cases [43]. 

The framework’s design explicitly addresses the tension between computational requirements and practical deployment constraints, ensuring suitability for real-world advertising platforms through measurable performance guarantees and cost-efficient resource utilization. 

## **6. Conclusions** 

This manuscript presents a novel framework that addresses the frozen-user problem in personalized advertising through a holistic, three-stage architecture integrating transformer-enhanced feature extraction, ensemble modeling, and LLM-powered semantic refinement. This innovative approach bridges the gap between traditional CTR prediction and advanced semantic understanding, delivering superior accuracy, transparency, and user trust in cold-start scenarios. Key contributions include (1) a transformer-driven feature representation that dynamically models semantic relationships in sparse data, surpassing conventional embeddings; (2) a robust ensemble methodology with learnable weighted aggregation, enhancing prediction stability over single-model approaches; and (3) an LLM-powered stage that ensures contextual relevance, recommendation diversification, sentiment alignment, and fairness while generating transparent explanations. Unlike existing methods that focus narrowly on embedding improvements or external knowledge, our framework systematically tackles the limitations of feature sparsity, computational overhead, and lack of interpretability. Empirical validation on the DigiX and Avazu datasets shows significant AUC and accuracy gains, while a user study confirms enhanced ad relevance, message clarity, and trust. 

The work advances the state of the art by demonstrating how LLMs can be effectively integrated into traditional recommendation pipelines to address the frozen-user problem while simultaneously improving user experience through enhanced transparency and personalization. The multi-faceted application of LLMs for contextual relevance, diversification, sentiment awareness, and bias mitigation shows particular promise for future research directions. The manuscript represents a significant advancement over several state-of-the-art approaches: 

1. Versus Traditional CTR Models: Compared to classic approaches this framework adds semantic understanding and explainability that addresses fundamental limitations in these models. 

2. Versus Pure LLM Approaches: Unlike recent work that uses LLMs as end-toend recommendation engines, this hybrid approach leverages the strengths of both statistical modeling and natural language processing while mitigating their respective weaknesses. 

3. Versus Other Cold-Start Solutions: The framework offers advantages over traditional cold-start techniques such as meta-learning and content-based filtering by incorporating dynamic contextual understanding and transparent explanations. 

4. Versus Explainable Recommendation Systems: While explainable recommendation systems have gained attention, this framework goes beyond post hoc explanations by integrating explanation generation directly into the recommendation process. 

_Future Internet_ **2025** , _17_ , 360 

18 of 21 

On the other hand, the framework presents opportunities for optimization in production environments, particularly regarding the computational efficiency of ensemble models and Gemini 2.5 integration in latency-critical applications. In future work, we plan to enhance the framework’s energy efficiency by exploring knowledge distillation techniques to train lightweight student models that retain the ensemble’s accuracy with reduced computational overhead. Additionally, we will investigate spiking neural networks, which offer inherent energy efficiency for CTR prediction, as demonstrated in prior work [42]. To address latency concerns with Gemini 2.5, we plan to incorporate lighter and faster LLMs (e.g., DistilBERT), which may provide comparable semantic reranking and personalization capabilities with lower resource demands. Furthermore, we will conduct more extensive user studies with larger, diverse samples across varied ad contexts to validate explanation quality and assess further the longitudinal effects on user engagement. These studies will incorporate real-world behavioral metrics, such as click-through rates, to provide a comprehensive evaluation of the framework’s practical impact in production environments. 

**Author Contributions:** Conceptualization, I.V.; methodology, I.V., A.U. and A.T.; software, A.U. and I.V.; validation, A.U. and I.V.; formal analysis, A.U.; investigation, I.V.; resources, A.U. and I.V.; data curation, A.U. and I.V.; writing—original draft preparation, A.U.; writing—review and editing, I.V. and A.T.; visualization, A.U.; supervision, I.V. and A.T.; project administration, I.V. and A.T. All authors have read and agreed to the published version of the manuscript. 

**Funding:** This research received no external funding. 

**Institutional Review Board Statement:** This study involved a non-interventional, fully anonymous questionnaire conducted in accordance with Greek national regulations. No personal data or identifying information was collected. Based on national legislation governing human research ethics (Law 4523/2018 and Law 4692/2020), formal IRB approval was not required for this type of study. 

**Data Availability Statement:** The training datasets presented in the study are openly available in Kaggle, at the following links: Avazu dataset (https://www.kaggle.com/c/avazu-ctr-prediction/ overview); and DigiX dataset (https://www.kaggle.com/louischen7/2020-digix-advertisement-ctrprediction). The raw survey data supporting the conclusions of the third stage in this article will be made available by the corresponding author on request. 

**Conflicts of Interest:** The authors declare no conflicts of interest. 

## **Abbreviations** 

The following abbreviations are used in this manuscript: 

AI Artificial Intelligence ML Machine Learning ANN Artificial Neural Networks CTR Click-Through Rate 

_Future Internet_ **2025** , _17_ , 360 

19 of 21 

## **Appendix A** 

Questionnaire 

## **Demographic Information** 

1. Gender: Male/Female/Other/Prefer not to say 

2. Age: 18–24/25–34/35–44/45–54/55+ 

3. Do you actively use the internet or social media? Yes/No 

## **Advertisement Relevance (3 items); Scale: 1 = Strongly Disagree, 5 = Strongly Agree** 

4. This advertisement is relevant to my interests and needs. 

5. The content of this advertisement applies to me personally. 

6. This advertisement matches what I am looking for. 

## **Behavioral Intention (3 items); Scale: 1 = Very Unlikely, 5 = Very Likely** 

7. How likely are you to click on this advertisement? 

8. I would consider clicking on this ad if I saw it online. 

9. This advertisement would capture my attention enough to click on it. 

## **Explanation Effectiveness (3 items)—Survey 1 Only; Scale: 1 = Strongly Disagree, 5 = Strongly Agree** 

10. The explanation provided helped me understand why this ad was shown to me. 

11. The explanation made the advertisement more meaningful to me. 

12. The explanation increased my confidence in the advertisement’s relevance. 

## **Comparative Relevance (3 items); Scale: 1 = Much Less Relevant, 5 = Much More Relevant** 

13. Compared to other advertisements I typically see, this ad is more relevant to me. 

14. This advertisement is more suited to my preferences than most ads I encounter. 

15. Relative to alternative advertisements, this one better matches my interests. 

## **Message Quality (3 items); Scale: 1 = Strongly Disagree, 5 = Strongly Agree** 

16. The message in this advertisement is clear and easy to understand. 

17. This advertisement communicates its message effectively. 

18. The content of this advertisement is well-presented and comprehensible. 

## **Factors Influencing Clicking Decisions** 

19. Instructions: Please select all factors that would influence your decision to click on an advertisement (check all that apply): 

   - ✔ Relevance/interest in the product or service 

   - ✔ Quality and clarity of the advertisement message 

   - ✔ Brand reputation and trustworthiness 

   - ✔ Visual design and appeal of the advertisement 

   - ✔ Explanation of why the ad was shown to me 

   - ✔ Transparency about data collection and targeting 

## **References** 

1. Zhang, W.; Qin, J.; Guo, W.; Tang, R.; He, X. Deep Learning for Click-Through Rate Estimation. _arXiv_ **2021** , arXiv:2104.10584. [CrossRef] 

2. Reddy, S.; Beg, H.; Overwijk, A.; O’Byrne, S. Sequence Learning: A Paradigm Shift for Personalized Ads Recommendations. 2024. Available online: https://engineering.fb.com/2024/11/19/data-infrastructure/sequence-learning-personalized-adsrecommendations/ (accessed on 19 November 2024). 

3. Viktoratos, I.; Tsadiras, A. A Machine Learning Approach for Solving the Frozen User Cold-Start Problem in Personalized Mobile Advertising Systems. _Algorithms_ **2022** , _15_ , 72. [CrossRef] 

4. Wang, R.; Shivanna, R.; Cheng, D.; Jain, S.; Lin, D.; Hong, L.; Chi, E. DCN V2: Improved Deep & Cross Network and Practical Lessons for Web-scale Learning to Rank Systems. In Proceedings of the WWW ’21: The Web Conference 2021, Ljubljana, Slovenia, 19–23 April 2021; Volume 2, pp. 1785–1797. 

_Future Internet_ **2025** , _17_ , 360 

20 of 21 

5. Zhao, F.; Huang, C.; Xu, H.; Yang, W.; Han, W. RGMeta: Enhancing Cold-Start Recommendations with a Residual Graph Meta-Embedding Model. _Electronics_ **2024** , _13_ , 3473. [CrossRef] 

6. Ye, Z.; Zhang, D.J.; Zhang, H.; Zhang, R.; Chen, X.; Xu, Z. Cold Start to Improve Market Thickness on Online Advertising Platforms: Data-Driven Algorithms and Field Experiments. _Manag. Sci._ **2022** , _69_ , 3838–3860. [CrossRef] 

7. Ouyang, W.; Zhang, X.; Ren, S.; Li, L.; Zhang, K.; Luo, J.; Liu, Z.; Du, Y. Learning Graph Meta Embeddings for Cold-Start Ads in Click-Through Rate Prediction. In Proceedings of the SIGIR ’21: The 44th International ACM SIGIR Conference on Research and Development in Information Retrieval, Online, 11–15 July 2021; Volume 1, pp. 1157–1166. 

8. Liu, Y.; Ma, L.; Wang, M. GAIN: A Gated Adaptive Feature Interaction Network for Click-Through Rate Prediction. _Sensors_ **2022** , _22_ , 7280. [CrossRef] 

9. Wang, Z.; She, Q.; Zhang, P.; Zhang, J. ContextNet: A Click-Through Rate Prediction Framework Using Contextual in-formation to Refine Feature Embedding. _arXiv_ **2017** . [CrossRef] 

10. Dilbaz, S.; Saribas, H. STEC: See-Through Transformer-based Encoder for CTR Prediction. _arXiv_ **2023** . [CrossRef] 

11. Wang, D.; Salamatian, K.; Xia, Y.; Deng, W.; Zhang, Q. BERT4CTR: An Efficient Framework to Combine Pre-trained Language Model with Non-textual Features for CTR Prediction. In Proceedings of the KDD ’23: The 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining, Long Beach, CA, USA, 6–10 August 2023; Volume 1, pp. 5039–5050. 

12. Muhamed, A.; Keivanloo, I.; Perera, S.; Mracek, J.; Xu, Y.; Cui, Q.J.; Rajagopalan, S.; Zeng, B.; Chilimbi, T. CTR-BERT: Cost-effective knowledge distillation for billion-parameter teacher models. In Proceedings of the 35th Conference on Neural Information Processing Systems, Online, 6–14 December 2021; Available online: https://neurips2021-nlp.github.io/accepted_papers.html (accessed on 5 August 2025). 

13. Huang, J.; Qu, M.; Li, L.; Wei, Y. AdGPT: Explore Meaningful Advertising with ChatGPT. _ACM Trans. Multimedia Comput. Commun. Appl._ **2025** , _21_ , 1–23. [CrossRef] 

14. Cheng, H.-T.; Koc, L.; Harmsen, J.; Shaked, T.; Chandra, T.; Aradhye, H.; Anderson, G.; Corrado, G.; Chai, W.; Ispir, M.; et al. Wide & Deep Learning for Recommender Systems. In Proceedings of the 1st Workshop on Deep Learning for Recommender Systems—DLRS 2016, Boston, MA, USA, 15 September 2016; pp. 7–10. 

15. Wang, R.; Fu, B.; Fu, G.; Wang, M. Deep & Cross Network for Ad Click Predictions. In Proceedings of the ADKDD’17: The 23rd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, Halifax, NS, Canada, 13–17 August 2017; Volume 1, pp. 1–7. 

16. Guo, H.; Tang, R.; Ye, Y.; Li, Z.; He, X. DeepFM: A Factorization-Machine based Neural Network for CTR Prediction. _arXiv_ **2017** , arXiv:1703.04247. 

17. Xi, X.; Leng, S.; Gong, Y.; Li, D. An accuracy improving method for advertising click through rate prediction based on enhanced xDeepFM model. _arXiv_ **2022** . [CrossRef] 

18. Song, W.; Shi, C.; Xiao, Z.; Duan, Z.; Xu, Y.; Zhang, M.; Tang, J. AutoInt. In Proceedings of the CIKM ’19: The 28th ACM International Conference on Information and Knowledge Management, Beijing, China, 3–7 November 2019; pp. 1161–1170. 

19. Li, Y.; Wang, J.; Dai, T.; Zhu, J.; Yuan, J.; Zhang, R.; Xia, S.-T. RAT: Retrieval-Augmented Transformer for Click-Through Rate Prediction. In Proceedings of the WWW ’24: The ACM Web Conference 2024, Singapore, 13–17 May 2024; pp. 867–870. 

20. Li, Z.; Cui, Z.; Wu, S.; Zhang, X.; Wang, L. Fi-GNN: Modeling Feature Interactions via Graph Neural Networks for CTR Prediction. In Proceedings of the CIKM ’19: The 28th ACM International Conference on Information and Knowledge Management, Beijing, China, 3–7 November 2019; pp. 539–548. 

21. Schifferer, B. Solving the Cold-Start Problem using Two-Tower Neural Networks for NVIDIA’s E-Mail Recommender Systems. Available online: https://medium.com/nvidia-merlin/solving-the-cold-start-problem-using-two-tower-neural-networks-fornvidias-e-mail-recommender-2d5b30a071a4 (accessed on 4 February 2025). 

22. Sanner, S.; Balog, K.; Radlinski, F.; Wedin, B.; Dixon, L. Large Language Models are Competitive Near Cold-start Recommenders for Language- and Item-based Preferences. In Proceedings of the RecSys ’23: Seventeenth ACM Conference on Recommender Systems, Singapore, 18–22 September 2023; pp. 890–896. 

23. Zhang, W.; Wu, C.; Li, X.; Wang, Y.; Dong, K.; Wang, Y.; Dai, X.; Zhao, X.; Guo, H.; Tang, R. LLMTreeRec: Unleashing the Power of Large Language Models for Cold-Start Recommendations. _arXiv_ **2024** . [CrossRef] 

24. Liu, R.; Chen, H.; Bei, Y.; Zhou, Z.; Chen, L.; Shen, Q.; Huang, F.; Karray, F.; Wang, S. FilterLLM: Text-To-Distribution LLM for Billion-Scale Cold-Start Recommendation. _arXiv_ **2025** . [CrossRef] 

25. Ramel, D. Google Expands AI Portfolio with Gemini 2.0, Enhancing Multimodal Capabilities. Available online: https://pureai. com/articles/2025/02/10/google-unveils-gemini-2-0.aspx (accessed on 6 February 2025). 

26. Shu, D.; Zhao, H.; Liu, X.; Demeter, D.; Du, M.; Zhang, Y. LawLLM: Law Large Language Model for the US Legal System. In Proceedings of the CIKM ’24: The 33rd ACM International Conference on Information and Knowledge Management, Boise, ID, USA, 21–25 October 2024; pp. 4882–4889. 

27. Choi, I.; Kim, J.; Kim, W.C. An explainable prediction for dietary-related diseases via language models. _Nutrients_ **2024** , _16_ , 686. [CrossRef] [PubMed] 

_Future Internet_ **2025** , _17_ , 360 

21 of 21 

28. Zhang, W.; Bei, Y.; Yang, L.; Zou, H.P.; Zhou, P.; Liu, A.; Li, Y.; Chen, H.; Wang, J.; Wang, Y.; et al. Cold-Start Recommendation towards the Era of Large Language Models (LLMs): A Comprehensive Survey and Roadmap. _arXiv_ **2025** . [CrossRef] 

29. Han, W.; Zhang, Z.; Zhang, Y.; Yu, J.; Chiu, C.-C.; Qin, J.; Gulati, A.; Pang, R.; Wu, Y. ContextNet: Improving Convolutional Neural Networks for Automatic Speech Recognition with Global Context. _arXiv_ **2020** . [CrossRef] 

30. Ma, J.; Zhao, Z.; Yi, X.; Chen, J.; Hong, L.; Chi, E.H. Modeling Task Relationships in Multi-task Learning with Multi-gate Mixture-of-Experts. In Proceedings of the KDD ’18: The 24th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, London, UK, 19–23 August 2018; pp. 1930–1939. 

31. Devlin, J.; Chang, M.-W.; Lee, K.; Toutanova, K. BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. _arXiv_ **2019** , arXiv:1810.04805. [CrossRef] 

32. Carbonell, J.; Goldstein, J. The use of MMR, diversity-based reranking for reordering documents and producing summaries. In Proceedings of the SIGIR98: 21st Annual ACM/SIGIR International Conference on Research and Development in Information Retrieval, Melbourne, Australia, 24–28 August 1998; pp. 335–336. 

33. Li, X.; Zhang, Z.; Stefanidis, K. Sentiment-aware Analysis of Mobile Apps User Reviews Regarding Particular Updates. In Proceedings of the in The Thirteenth International Conference on Software Engineering Advances, ICSEA, Nice, France, 14–18 October 2018. 

34. Mehrabi, N.; Morstatter, F.; Saxena, N.; Lerman, K.; Galstyan, A. A survey on bias and fairness in machine learning. _ACM Comput. Surv._ **2021** , _54_ , 1–35. [CrossRef] 

35. Grbovic, M.; Cheng, H. Real-time Personalization using Embeddings for Search Ranking at Airbnb. In Proceedings of the 24th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining, London, UK, 19–23 August 2018; pp. 311–320. 

36. Viktoratos, I.; Tsadiras, A.; Bassiliades, N. Combining community-based knowledge with association rule mining to alleviate the cold start problem in context-aware recommender systems. _Expert Syst. Appl._ **2018** , _101_ , 78–90. [CrossRef] 

37. Covington, P.; Adams, J.; Sargin, E. Deep Neural Networks for YouTube Recommendations. In Proceedings of the RecSys’16: 10th ACM Conference on Recommender Systems, Boston, MA, USA, 15–19 September 2016; pp. 191–198. 

38. Ribeiro, M.T.; Singh, S.; Guestrin, C. “Why Should I Trust You?” Explaining the Predictions of Any Classifier. In Proceedings of the KDD’16: 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, San Francisco, CA, USA, 13–17 August 2016; pp. 1135–1144. [CrossRef] 

39. Pan, S.J.; Yang, Q. A Survey on Transfer Learning. _IEEE Trans. Knowl. Data Eng._ **2010** , _22_ , 1345–1359. [CrossRef] 

40. Tam, K.Y.; Shuk, Y.H. Understanding the Impact of Web Personalization on User Information Processing and Decision Outcomes. _MIS Q._ **2006** , _30_ , 865–890. [CrossRef] 

41. Petty, R.E.; Cacioppo, J.T. The Elaboration Likelihood Model of Persuasion. In _Advances in Experimental Social Psychology_ ; Berkowitz, L., Ed.; Academic Press: Cambridge, MA, USA, 1986; Volume 19, pp. 123–205. 

42. Doshi-Velez, F.; Kim, B. Towards A Rigorous Science of Interpretable Machine Learning. _arXiv_ **2017** . [CrossRef] 

43. Uruqi, A.; Viktoratos, I. Exploiting Spiking Neural Networks for Click-Through Rate Prediction in Personalized Online Advertising Systems. _Forecasting_ **2025** , _7_ , 38. [CrossRef] 

**Disclaimer/Publisher’s Note:** The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content. 

