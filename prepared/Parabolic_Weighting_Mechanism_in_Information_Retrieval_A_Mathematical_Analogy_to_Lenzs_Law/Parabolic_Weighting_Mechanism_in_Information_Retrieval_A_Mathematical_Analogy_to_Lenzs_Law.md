
![](prepared/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law/images/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law.pdf-0001-00.png)


Received 19 February 2025, accepted 10 March 2025, date of publication 13 March 2025, date of current version 2 April 2025. _Digital Object Identifier 10.1109/ACCESS.2025.3550964_ 

## Parabolic Weighting Mechanism in Information Retrieval: A Mathematical Analogy to Lenz’s Law 

## KRISHNAN BATRI 1, S. LAKSHMI 2, AND R. SOWRIRAJAN 3 

1School of Computer Science and Engineering, Jain (Deemed-to-be University), Bengaluru, Karnataka 562112, India 

2Department of Electronics and Communication Engineering, Jain (Deemed-to-be University), Bengaluru, Karnataka 562112, India 

3Department of Mathematics, Dr. N.G.P. Arts and Science College, Coimbatore, Tamil Nadu 641035, India 

Corresponding author: Krishnan Batri (krishnan.batri@jainuniversity.ac.in) 

**ABSTRACT** Conventional term-weighting techniques in information retrieval, such as term frequency-inverse document frequency and the probabilistic ranking framework, often place excessive emphasis on extreme term frequencies, which can distort document ranking. Inspired by Lenz’s Law in electromagnetism, which naturally resists sudden fluctuations in magnetic flux, this work introduces a novel parabolic weighting mechanism. By applying a parabolic function to reduce the impact of excessively frequent terms while enhancing moderately occurring words, the proposed method achieves a balanced contribution of term frequency. The mathematical formulation promotes equilibrium in term weighting by integrating term frequency with inverse document frequency. Experiments conducted on benchmark datasets, including BBC News and 20 Newsgroups, demonstrate that the parabolic weighting mechanism outperforms traditional techniques, yielding measurable improvements in accuracy with classification models such as the support vector classifier (0.44 percent increase) and logistic regression (0.30 percent increase). Furthermore, statistical validation using Cohen’s effect size measure confirms the significance of performance improvements, while bootstrap analysis ensures the reliability of the observed gains. These results establish a strong foundation for future integration with neural information retrieval models and highlight the potential of the proposed approach in domain-specific applications, such as legal document analysis and biological literature search. 

**INDEX TERMS** Information retrieval, term weighting, parabolic weighting, Lenz’s law, semantic analysis, computational linguistics, mathematical modeling. 

## **I. INTRODUCTION** 

The exponential growth of data in a variety of fields, including social media, corporate intelligence, healthcare, and academic research, poses serious information finding issues in the current digital era [1]. The capacity to efficiently search, categorise, and retrieve relevant content is crucial given the constantly growing amount of information [2]. A key component of this process are Information Retrieval (IR) systems, which assist users in finding the most pertinent information based on their queries in a timely and precise manner [3]. Numerous applications, such as recommendation systems, digital libraries, and search engines, rely on these systems as their foundation. 

The associate editor coordinating the review of this manuscript and approving it for publication was Yilun Shang. 

The core problem of modern IR systems is textual representation: how to convert unstructured material into machine-readable, structured formats while maintaining context and meaning. Within texts, the ranking of terms is a crucial step in this process. How a document is sorted in relation to a query is mostly determined by term weighting methods, which provide weight to certain words or keywords inside a document. However, the semantic richness and contextual nuances of language are frequently not adequately captured by current approaches, which results in problems like poor retrieval performance and imprecise rating results. In order to guarantee that terms are not only recognised but also appropriately interpreted within their contextual surroundings, effective term weighting is essential. Words in isolation can have more than one meaning, and their applicability frequently changes based on the context in 

2025 The Authors. This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/ 

54367 

VOLUME 13, 2025 

K. Batri et al.: PWM in Information Retrieval: A Mathematical Analogy to Lenz’s Law 


![](prepared/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law/images/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law.pdf-0002-01.png)


which they are used in a document or search query. However, this dynamic nature of word importance is difficult for traditional term weighting strategies to account for. 

Despite being commonly used in IR systems, the Term Frequency-Inverse Document Frequency (TF-IDF) method is a straightforward way for term weighting. It is based on the idea that a term’s significance is based on how frequently it appears in a text (TF) and how uncommon it is throughout the corpus (IDF). Despite being useful in many circumstances, TF-IDF and related techniques have a number of significant drawbacks. First, TF-IDF assumes a linear relationship between term frequency and importance [4]. This ignores the truth that a term’s importance does not always correspond to how frequently it appears in a document. For instance, depending on the context of a document, certain term occurrences may be more suggestive of its meaning than others. Second, traditional term weighting methods lack contextual sensitivity [5]. A word’s meaning is frequently context-dependent, changing according to the words that surround it, the document’s overarching subject, or the particular discourse domain. These crucial elements that affect terms’ meaning are ignored by TF-IDF, which regards terms as separate entities. Third, traditional weighting techniques tend to undervalue rare terms [6]. Although uncommon or domain-specific terms may have significant meaning in particular settings, they frequently earn lower weights in traditional models. In legal, scientific, or technical documents, for example, specialised terminology may be crucial to comprehending the content of the document, but they are often under-represented in conventional weighting methods. These restrictions lead to less accurate search results, inferior classification, and recommendation performance because they contribute to the semantic gap between how IR systems interpret concepts and how people comprehend them. 

We suggest a Parabolic Weighting Mechanism, which presents a non-linear method of term weighting, in order to get around the drawbacks of traditional techniques. In order to ensure a more equal contribution to document ranking across the corpus, the suggested technique dynamically modifies the relevance of terms by taking into account their frequency and reducing extreme values. Motivated by Lenz’s Law, an electromagnetism principle, the Parabolic Weighting Mechanism conceptually compares the dynamic adjustment of term importance in response to context changes to induced currents that oppose changes in magnetic flux. This paradigm models term significance as a parabolic function, allowing for adaptive weighting based on a number of variables, including the surrounding terms, and frequency of occurrence. Several significant benefits are offered by this innovative weighting mechanism: It acknowledges the non-linear nature of term importance; it adjusts to the context of terms both inside and between documents and domains; it offers a more dynamic, nuanced representation of text, which is essential for enhancing IR systems’ effectiveness. Beyond the constraints of conventional techniques, the 

Parabolic Weighting Mechanism provides a more precise, and adaptable approach to term representation by modifying term weights in accordance with these factors. 

The core objectives of this research are as follows: (1) To develop a mathematically rigorous, non-linear framework for term weighting that accounts for contextual and corpuslevel dynamics. (2) To empirically validate the proposed mechanism using a variety of benchmark IR datasets. (3) To demonstrate improvements in the precision, recall, and F1 score of IR systems using the Parabolic Weighting Mechanism compared to traditional methods like TF-IDF. This research seeks to address the dynamic challenges of traditional term weighting methods and provide a more adaptive, context-aware solution for information retrieval. 

The structure of this paper is organized as follows. Section II presents a thorough analysis of the literature on current term weighting techniques, emphasising the drawbacks of conventional strategies and the demand for creative fixes. Section III provides a thorough description of the Parabolic Weighting Mechanism’s theoretical underpinnings, including its conceptual framework and mathematical formulation. Section IV explains the experimental design, including the datasets, metrics for evaluation, methods for testing the effectiveness of the suggested mechanism, and an analysis of the findings, showing how the Parabolic Weighting Mechanism performs better than conventional techniques in terms of F1 score, precision, and recall. Finally, Section V provides a summary of the results, a discussion of their implications, and suggestions for future study possibilities. 

## **II. LITERATURE REVIEW OF TERM WEIGHTING MECHANISMS IN INFORMATION RETRIEVAL** 

## _A. TERM WEIGHTING’S HISTORICAL DEVELOPMENT_ 

Since its inception, the challenge of effectively encoding terms in information retrieval (IR) has remained central to the field [7]. Salton and McGill first emphasized the need for advanced term weighting techniques that account for the varying contributions of terms to a document’s semantics in the early 1980s [8]. Their work paved the way for numerous advancements, particularly in the development of statistical measures for assessing term importance. 

In 1972, Sparck Jones introduced _Inverse Document Frequency (IDF)_ , which revolutionized term importance by incorporating a term’s rarity across a document corpus [9]. This concept formed the basis of the widely used **TF-IDF** (Term Frequency - Inverse Document Frequency) model. Over time, **Term Frequency (TF)** and **IDF** have collectively established themselves as foundational components of IR, shaping the architecture of numerous retrieval systems [10]. 

Despite its widespread adoption, TF-IDF has notable limitations, particularly its inability to consider contextual importance and complex semantic relationships. Recent advancements have introduced more dynamic and sophisticated weighting mechanisms to address these shortcomings. For instance, neural term weighting [11] and entropy-based 

54368 

VOLUME 13, 2025 

K. Batri et al.: PWM in Information Retrieval: A Mathematical Analogy to Lenz’s Law 


![](prepared/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law/images/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law.pdf-0003-01.png)


term weighting [12] have emerged as promising approaches, integrating deep learning and statistical models to enhance retrieval performance. Furthermore, graph-based term weighting [13] has provided novel insights into term importance by leveraging network-based representations of textual data. 

## _B. TRADITIONAL TERM WEIGHTING APPROACHES_ 

## 1) TERM FREQUENCY-INVERSE DOCUMENT FREQUENCY (TF-IDF) 

Robertson and Jones’ TF-IDF model remains a fundamental method for term weighting in IR [14]. The model calculates a term’s importance within a document (term frequency, or TF) and its rarity throughout a corpus (inverse document frequency, or IDF). Despite its success in numerous IR applications, several concerns have been raised. According to Chen and Liu [15], the TF-IDF’s linear weighting algorithm does not account for diminishing returns when terms appear with increasing frequency, thereby distorting the relevance of extremely frequent phrases. Moreover, TF-IDF often assumes term independence, which is problematic given that words may be interdependent or share contextual nuances. 

To address these limitations, recent research has explored neural term weighting [16], adaptive term frequency scaling [17], and context-aware IDF variants [18]. These approaches incorporate deep learning models and probabilistic refinements to improve retrieval accuracy and adaptability in modern IR systems. 

## 2) OKAPI BM25 

An extension of TF-IDF, the BM25 model has gained widespread recognition for its probabilistic foundation and ability to account for document length variations. BM25 was developed by Robertson et al. [19] to enhance robustness across different IR settings by incorporating a document length normalization parameter and nonlinear term frequency scaling. Although BM25 is more adaptable than TF-IDF, it remains limited by the assumption of term independence and struggles to model term dependencies effectively [20]. 

Recent advancements in BM25-based models, such as neural BM25 [21] and graph-enhanced BM25 [22], aim to mitigate these constraints by integrating semantic relationships and context-aware scoring techniques. 

## _C. ADVANCED COMPUTATIONAL LINGUISTICS APPROACHES_ 

modelling approaches in IR. By considering the distribution of terms in the corpus, this model made it possible to describe term relevance more precisely and produced a more reliable estimate of document relevance. 

Freedman et al. [24] contributed to further developments in probabilistic models by proposing Bayesian-inspired models that dynamically modify term weights in response to contextual signals. More recently, adaptive probabilistic weighting schemes, such as those introduced by Li et al. [17], have further improved contextual relevance scoring by integrating hierarchical Bayesian networks. 

## 2) INCORPORATING MACHINE LEARNING 

Important advances in IR have resulted from the combination of term weighting models and machine learning. Adaptive learning methods were used by Chen and Wang [25] to modify word weights according to semantic features that were taken from documents. As the model adjusts to the meanings and contextual linkages of terms, this semantic adaptation has made it possible to determine term significance with greater precision. 

With Word2Vec, a method that learns distributed vector representations of words depending on their context, Savelli et al. [26] transformed term representation. Recent improvements, such as contrastive learning for term weighting introduced by Hambarde et al. [27], further enhance word representation by capturing fine-grained contextual dependencies across different document domains. 

## 3) DEEP AND NEURAL LEARNING METHODS 

By adding context-aware term representations, recent developments in deep learning have significantly enhanced term weighting [11]. Word embeddings, such as Word2Vec [26] and GloVe [28], allow models to learn rich, contextsensitive term representations by representing terms in high-dimensional spaces. 

Contextual embeddings from models like BERT [29] have more recently offered a dynamic comprehension of word meaning by taking into account both the syntactic and semantic context in which words emerge. Recent advancements include transformer-based models such as LongFormer and ColBERT [30], which provide more efficient contextual term weighting by incorporating late interaction mechanisms to enhance document retrieval relevance. These neural models hold great promise for upcoming IR systems since they have demonstrated greater efficacy in managing the intricacies of natural language. 

## 1) PROBABILISTIC AND STATISTICAL MODELS 

Researchers are increasingly using statistical and probabilistic models in response to the shortcomings of traditional models. By dynamically modifying word weights in response to contextual cues, these models seek to provide a more nuanced understanding of term importance. 

By considering document retrieval as a probabilistic process in which the likelihood of a document given a query is calculated, Ponte and Croft [23] presented language 

## _D. MULTIDISCIPLINARY VIEWS_ 

## 1) COMPUTATIONAL MODELS INSPIRED BY PHYSICS 

Multidisciplinary methods have shown significant promise in improving term weighting models, particularly those influenced by physics. Inspired by thermodynamic principles, Rodriguez and Garcia [31] introduced entropy-based models for term weighting. These models dynamically adjust term significance based on their distribution and uncertainty 

54369 

VOLUME 13, 2025 

K. Batri et al.: PWM in Information Retrieval: A Mathematical Analogy to Lenz’s Law 


![](prepared/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law/images/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law.pdf-0004-01.png)


within the corpus, providing enhanced adaptability in diverse contexts. The approach reflects the principle of energy minimization, wherein word distributions seek an equilibrium state over time. 

Recent advances have further explored physics-driven models in information retrieval. Li et al. [32] proposed a thermodynamic-inspired model for term weighting, leveraging entropy measures to enhance retrieval effectiveness by dynamically adjusting term importance in evolving corpora. Their approach has been shown to outperform traditional weighting schemes in handling contextual variations. 

Additionally, quantum-inspired models have gained traction. Kim and Park [33] applied concepts from quantum mechanics, such as entanglement and superposition, to model term relationships probabilistically. This approach captures complex semantic dependencies that traditional models often overlook. More recently, Zhang et al. [34] expanded on this idea by incorporating quantum interference mechanisms to refine relevance estimation in information retrieval systems. Their model demonstrated improved performance in handling polysemy and semantic ambiguity. 

With richer semantic representations and physics-based adaptability, these models offer a dynamic and flexible approach to term weighting, paving the way for more advanced and context-aware information retrieval systems. 

## _E. CRITICAL RESTRICTIONS IN CURRENT METHODS_ 

Despite these advancements, several significant limitations persist in existing term weighting strategies [35]. One of the key challenges is **contextual variability** , which traditional models like TF-IDF and BM25 fail to address adequately. This leads to what Johnson [36] describes as ‘‘contextual incompleteness,’’ where the same term may hold different meanings depending on its usage but is weighted uniformly. 

Furthermore, many existing models struggle to capture the **semantic** nuances of word meanings, particularly in cases involving polysemy and strong context dependence [37]. While embedding-based models have made progress in this area, they still face difficulties in effectively differentiating between multiple meanings of a term in varied linguistic contexts. Recent studies, such as by Liu et al. [38], have highlighted the ongoing challenge of integrating deep contextual understanding into term weighting. 

Another fundamental drawback is the lack of **adaptability** in most current models. Since they are largely static, they struggle to accommodate dynamic or real-time shifts in document collections or user queries [39]. More recent research by Zhang et al. [40] explores adaptive weighting mechanisms that adjust term importance in real time, yet these methods are still in early stages and require further refinement for practical applications. 

## _F. THEORETICAL FRAMEWORK AND RESEARCH GAPS_ 

Existing research highlights several critical areas where further advancements in term weighting are required. One of the most pressing challenges is the development of **dynamic** 

**and adaptive weighting mechanisms** . Traditional models, including TF-IDF and BM25, operate on static weighting schemes that do not adjust dynamically to evolving document collections or user queries. Zhang et al. [40] proposed an adaptive term weighting framework that incorporates real-time adjustments based on query context, but practical implementations at scale remain limited. Future research should explore reinforcement learning-based approaches and self-adjusting models capable of continuously refining term weights. 

Another significant challenge lies in the construction of **advanced semantic models** . Current methodologies struggle to fully capture polysemy, context dependence, and nuanced word ambiguities. While transformer-based models like BERT [29] and subsequent contextual embedding techniques [41] have improved semantic representations, challenges persist in their integration with retrieval systems, particularly in handling large-scale datasets efficiently. Enhancing term weighting through semantic-rich embeddings and hybrid approaches that combine statistical methods with deep learning remains an open research problem. 

Furthermore, **interdisciplinary approaches** have shown promise in enhancing term weighting methodologies, drawing inspiration from fields such as physics and cognitive sciences. Entropy-based models proposed by Rodriguez and Garcia [31] leverage thermodynamic principles to dynamically adjust term significance, while quantum-inspired approaches introduced by Kim and Park [33] model term relationships using probabilistic superposition and entanglement concepts. Despite their theoretical potential, these models require further empirical validation and optimization to be effectively deployed in real-world information retrieval applications. Addressing these gaps through interdisciplinary innovations and computational advancements will be crucial for the next generation of IR systems. 

## _G. PROPOSED APPROACH: PARABOLIC TERM WEIGHTING MECHANISM_ 

By incorporating a **non-linear weighting function** , this work presents a novel **Parabolic Term Weighting Mechanism** that solves the drawbacks of conventional models. The suggested method, which draws inspiration from electromagnetic principles, offers a more flexible and dynamic way to evaluate term significance. The model seeks to improve the accuracy and context sensitivity of information retrieval systems by taking into account both term frequency and document context. 

## **III. THEORETICAL FOUNDATION OF PARABOLIC TERM WEIGHTING MECHANISM** 

The complex relationship between term frequency (TF) and its importance in information retrieval (IR) is addressed by the parabolic term weighting method. Unlike conventional linear or heuristic weighting schemes, this approach penalises both extremely common and overly rare terms by modelling term importance using a parabolic function. 

54370 

VOLUME 13, 2025 

K. Batri et al.: PWM in Information Retrieval: A Mathematical Analogy to Lenz’s Law 


![](prepared/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law/images/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law.pdf-0005-01.png)


Inspired by Lenz’s Law in electromagnetic theory, the mechanism incorporates a concept of opposition, ensuring a mathematically grounded and contextually aware framework for term weighting. 

## _A. LENZ’S LAW: THE PRINCIPLE OF OPPOSITION_ 

Lenz’s Law, a fundamental principle of electromagnetic theory, states that an induced current or force opposes the change that caused it. Mathematically, Lenz’s Law is expressed as: 


![](prepared/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law/images/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law.pdf-0005-05.png)


where _E_ represents the induced electromotive force (EMF), _�_ denotes the magnetic flux, and _[d] dt[�]_ represents the rate of change of magnetic flux. By maintaining equilibrium and preventing disruptive forces, this principle promotes system stability. In the context of information retrieval, term relevance is not merely a linear function of frequency but a dynamic balance. Instead of rewarding terms solely based on their frequency, this approach penalises both excessive and insufficient occurrences, forming the theoretical basis of the parabolic weighting mechanism. The weighting scheme adapts dynamically to the interaction between global rarity and local prominence. 

## _B. JUSTIFICATION OF THE PARABOLIC WEIGHTING MECHANISM_ 

The connection between Lenz’s Law and the parabolic weighting mechanism emerges through the idea of opposition in information retrieval. First, considering the analogy of energy minimization, Lenz’s Law implies that a system minimizes its energy or disruption. In information retrieval, a parabolic function is used to simulate a potential energy surface: 


![](prepared/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law/images/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law.pdf-0005-09.png)


where the system achieves minimal energy (optimal relevance) at _TF_ = _b_ · _IDF_ . The principle of dynamic opposition can be formulated by modeling the rate at which weight _w_ changes concerning term frequency _TF_ as: 


![](prepared/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law/images/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law.pdf-0005-11.png)


This resembles Lenz’s Law, where the induced effect opposes the cause of deviation. Integrating this equation results in the fundamental form: 


![](prepared/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law/images/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law.pdf-0005-13.png)


Incorporating scaling and offset parameters _a_ and _c_ , the final parabolic weighting function is given by: 


![](prepared/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law/images/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law.pdf-0005-15.png)


where _a_ controls the curvature, _b_ · _IDF_ sets the optimal balance point, and _c_ ensures non-negative weights. 

## _C. FUNDAMENTAL WEIGHTING FUNCTION_ 

The mathematical formulation of the parabolic weighting mechanism is based on the function: 


![](prepared/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law/images/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law.pdf-0005-19.png)


This equation captures the dynamic relationship between term frequency (TF) and inverse document frequency (IDF), balancing local term relevance with global rarity. The parabolic nature of the function ensures that terms that are either too common or too rare receive appropriate penalties, offering a generalised yet flexible weighting approach applicable across various IR scenarios. 

The steepness coefficient _a_ determines the function’s curvature and typically ranges between 0.1 and 10, modulating the intensity of penalisation. The balance point _b_ · _IDF_ merges local and global term significance, with _b_ usually taking values between 0.5 and 2.0. The baseline constant _c_ prevents negative weights and generally falls between 0 and 1. 

Figure 1 illustrates how variations in parameters _a_ , _b_ , and _c_ affect the shape and behaviour of the weighting function. 


![](prepared/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law/images/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law.pdf-0005-23.png)


**FIGURE 1.** Impact of _a_ , _b_ , and _c_ in term weighting. 

## _D. CONNECTION TO LENZ’S LAW IN THE WEIGHTING FUNCTION_ 

The parabolic weighting mechanism establishes a symmetrical weighting scheme that aligns with the fundamental oppositional principles of Lenz’s Law. This mechanism enforces a balance, penalizing deviations from an ideal term frequency balance point. The symmetry embedded in this approach mirrors the equilibrium observed in physical systems governed by Lenz’s Law, ensuring that term frequencies are dynamically regulated to maintain stability within the weighting function. 

## 1) MATHEMATICAL REPRESENTATION 

The oppositional nature of the parabolic weighting mechanism is mathematically expressed as: 


![](prepared/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law/images/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law.pdf-0005-29.png)


54371 

VOLUME 13, 2025 

K. Batri et al.: PWM in Information Retrieval: A Mathematical Analogy to Lenz’s Law 


![](prepared/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law/images/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law.pdf-0006-01.png)



![](prepared/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law/images/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law.pdf-0006-02.png)


**FIGURE 2.** Graphical representation of the parabolic weighting mechanism. 

This formulation ensures that terms deviating from the optimal balance point _b_ · _IDF_ are penalized accordingly. Specifically, as the term frequency (TF) moves away from this balance, the weight decreases, effectively discouraging both excessively frequent and overly rare terms. This dynamic weighting approach aligns with the opposition principle derived from Lenz’s Law, ensuring that term significance is neither overemphasized nor undervalued. 

## 2) VISUAL SYMMETRY 

The parabolic weighting function enforces a symmetric distribution of penalties around the ideal term frequency. Unlike linear or logarithmic weighting approaches, the parabolic structure allows for a balanced representation of local and global terms, dynamically adjusting their importance. This symmetry is analogous to the way Lenz’s Law maintains equilibrium in physical systems by counteracting disruptive influences. 

## 3) TYPES OF PARABOLIC OPENINGS 

The parameter _a_ dictates the orientation and impact of the parabolic weighting function, determining whether the function promotes moderation, emphasizes outliers, or remains neutral. 

## _a: UPWARD OPENING PARABOLA (A >_ 0 _)_ 

When _a >_ 0, the parabolic function assigns lower weights to terms that are excessively frequent or rare, favoring moderate term frequencies. This results in a peak weight near the balance point _b_ · IDF, making it particularly effective in applications where a balanced term importance is desirable. The parameter _a_ typically ranges from 0.1 to 2.0, while _b_ (reflecting the IDF weight) generally falls within 0.1 to 1.0. A small bias term _c_ , ranging from 0.01 to 0.5, provides fine-tuned adjustments to the weighting function. 

## _b: DOWNWARD OPENING PARABOLA (A <_ 0 _)_ 

For _a <_ 0, the parabolic function expands downward, prioritizing terms at both extremes—either extremely rare or highly 

frequent—while de-emphasizing moderate term frequencies. This configuration is advantageous for applications where outlier terms hold significant importance. The parameter _a_ generally falls between −2 _._ 0 and −0 _._ 1, while the ranges for _b_ and _c_ remain consistent with the upward case. 

## _c: FLAT BASELINE PARABOLA (A_ ≈ 0 _)_ 

As _a_ approaches 0, the parabolic weighting function flattens, reducing its influence on term importance. This results in a nearly uniform weighting effect, serving as a neutral baseline for comparative analyses. In this case, _a_ typically varies between 0.01 and 0.05, while the ranges for _b_ and _c_ remain unchanged. 

Overall, the flexibility provided by the parabolic weighting mechanism ensures a robust framework for balancing term significance, effectively capturing the oppositional and equilibrium principles inherent in Lenz’s Law. 

## _E. HOW IR GAINS FROM THE OPPOSITION PRINCIPLE_ 

Traditional information retrieval (IR) weighting functions, such as BM25 and Term Frequency-Inverse Document Frequency (TF-IDF), often rely on static models that fail to dynamically adjust to term distribution patterns. As a result, these methods may either underweight rare yet significant terms (e.g., domain-specific terms in technical literature) or overemphasize highly frequent words (e.g., common stopwords). The introduction of the opposition principle, inspired by Lenz’s Law, offers a novel approach to counteract these extremes and refine term representation. 

One key advantage is the ability to balance term relevance dynamically. In traditional models, high-frequency terms often receive disproportionately high weights due to the linear or logarithmic growth of significance. This leads to skewed rankings where commonly occurring words dominate despite their minimal contribution to semantic meaning. In contrast, the parabolic weighting mechanism mitigates this issue by introducing a non-linear function that penalizes both extremely frequent and exceedingly rare terms, ensuring that moderate-frequency terms receive appropriate emphasis. This results in a more balanced and semantically rich term representation. 

Another significant improvement is the dynamic adjustment of weights based on contextual relevance. Conventional models generally assume that term frequency alone is sufficient to determine importance, often failing to account for specialized or domain-specific terms. As a result, rare but highly relevant terms may be undervalued, particularly in fields like medicine or law. The parabolic weighting mechanism rectifies this by adjusting term weights in a context-aware manner, ensuring that rare but meaningful terms contribute effectively to document ranking. By preventing excessive weight accumulation for highly frequent terms, the model ensures that document representations remain nuanced and context-sensitive. 

Finally, the opposition principle enhances stability and equilibrium in ranking. Conventional IR models frequently 

54372 

VOLUME 13, 2025 

K. Batri et al.: PWM in Information Retrieval: A Mathematical Analogy to Lenz’s Law 


![](prepared/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law/images/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law.pdf-0007-01.png)


suffer from static term weighting, which may lead to inconsistencies in retrieval effectiveness. For example, certain search queries may yield inaccurate results if highly frequent words are assigned disproportionately high importance. The parabolic function, inspired by Lenz’s Law, introduces a dynamic stabilization effect, ensuring that term weights converge toward an optimal balance. This prevents abrupt shifts in word significance and promotes a more consistent and accurate ranking of documents, particularly for complex search queries. 

In summary, the parabolic weighting mechanism, grounded in the opposition principle, addresses fundamental limitations in traditional IR weighting models. By dynamically balancing term significance, adjusting weights contextually, and promoting stability in ranking, it provides a more effective and theoretically grounded approach to information retrieval. 

The procedure used for the experiment was methodical. Tokenisation and text cleaning were used to pre-process the text data, eliminating non-alphanumeric characters, punctuation, and stop words. To maintain consistency, the text was then lowercased. Both TF-IDF and Parabolic Weighting were used in the feature extraction process, and each weighting method was applied independently to transform the text into numerical data. Both classifiers underwent hyperparameter adjustment. While the kernel types (linear and radial basis function (RBF)) and regularisation parameter (C) were evaluated for SVC, the regularisation strength parameter (C) was adjusted for Logistic Regression. 

Accuracy, precision, recall, and F1-score were among the metrics used to evaluate performance and determine how effective the weighting methods were. Five-fold crossvalidation was used to reduce overfitting and produce more dependable results in order to guarantee robust evaluation. 

## _B. RESULTS OF THE BBC NEWS DATASET_ 

## **IV. RESULTS AND DISCUSSION** 

## _A. EXPERIMENTAL SETUP_ 

The 20 Newsgroups dataset serves as a standard for problems involving text categorisation and clustering. Four classes were chosen for this study: talk.politics.mideast, sci.space, rec.sport.hockey, and comp. graphics. These categories were selected to provide a wide variety of subjects, offering a solid assessment of the weighting systems. The BBC News dataset, on the other hand, consists of stories categorised into five areas: tech, politics, business, sport, and entertainment. Comparing results over a wider range of topics is made possible by this dataset’s well-rounded categorisation challenge. 

In this investigation, two weighing procedures were used. The first, known as TF-IDF, is a conventional approach that allocates term weights according to how frequently they occur in a document as opposed to how frequently they occur throughout the corpus. This makes it possible for the model to concentrate on more unique terms by downweighting common terms. The new Parabolic Weighting Mechanism, which was presented in this paper, is the second weighting mechanism. By using a parabolic function that takes into account term frequency and inverse document frequency in a non-linear way, it modifies the weight of terms. It is hypothesised that phrases with moderate frequencies, which may be under-represented in the TF-IDF technique, are more significant when captured by this method. 

Two popular models for classifier evaluation were selected. A logistic function is used by the linear classifier Logistic Regression to evaluate the likelihood of class membership. Logistic regression, which is well-known for its computing efficiency, is frequently used as a standard for comparison in text categorisation. In contrast, the Support Vector Classifier (SVC) is a potent classifier that seeks to identify the best hyperplane for classifying data, which makes it very useful for high-dimensional data like text. 

## 1) BASELINE PERFORMANCE 

We performed preliminary tests utilising the TF-IDF approach in order to create a reliable standard for assessing the effectiveness of the suggested Parabolic Weighting Mechanism. A key method in text categorisation, TF-IDF determines a term’s weight by taking into account both its rarity throughout the corpus (inverse document frequency, or IDF) and its frequency in a document (term frequency, or TF). This dual consideration minimises the impact of common phrases while emphasising unique ones. 

We used the BBC News dataset for these trials, which included 2,225 stories in five different categories: tech, business, entertainment, politics, and sports. This dataset offers a wide and well-balanced collection of textual data that is perfect for evaluating classification techniques. 

## _a: PERFORMANCE OF SVC_ 

The SVC obtained a remarkable accuracy of **96.86%** by using TF-IDF characteristics. Table 1 displays specific performance metrics, such as Precision, Recall, and F1-Score for every category. The findings show that the SVC consistently distinguishes between the five categories with high recall values and precision, particularly in ‘‘Sport’’ and ‘‘Tech.’’ 

## _b: PERFORMANCE OF LOGISTIC REGRESSION_ 

Aside from SVC, Logistic Regression was used as an alternate baseline model. A competitive accuracy of **96.71%** was attained by Logistic Regression, which is well-known for its efficiency and interpretability. Table 2 presents the model’s performance metrics, which show slightly different strengths than SVC. In the ‘‘Entertainment’’ and ‘‘Sport’’ categories, logistic regression performed quite well, demonstrating its capacity to manage unbalanced or complex data distributions. 

## _c: CONFUSION MATRIX ANALYSIS_ 

To gain deeper insights into the performance of both models, confusion matrices were generated. For the SVC 

54373 

VOLUME 13, 2025 

K. Batri et al.: PWM in Information Retrieval: A Mathematical Analogy to Lenz’s Law 


![](prepared/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law/images/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law.pdf-0008-01.png)


**TABLE 1.** Performance Comparison of TF-IDF and PWM with SVC on BBC News Dataset. 


![](prepared/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law/images/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law.pdf-0008-03.png)


**TABLE 2.** Performance Comparison of TF-IDF and PWM with Logistic Regression on BBC News Dataset. 


![](prepared/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law/images/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law.pdf-0008-05.png)



![](prepared/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law/images/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law.pdf-0008-06.png)


**FIGURE 3.** Confusion Matrix for TF-IDF with SVC on BBC News Dataset. 


![](prepared/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law/images/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law.pdf-0008-08.png)


**FIGURE 4.** Confusion Matrix for TF-IDF with Logistic Regression on BBC News Dataset. 

model (Figure 3), the distribution of correctly classified instances and misclassifications reveals its high precision across all categories, with minimal confusion between similar categories. Similarly, the confusion matrix for Logistic Regression (Figure 4) highlights its comparable performance, with slightly varied misclassification patterns. 

in ‘‘Entertainment,’’ demonstrating its resilience in a variety of text classification tasks. These findings offer a reliable starting point for further research on the Parabolic Weighting Mechanism, allowing for a straightforward comparison with the recognised TF-IDF benchmark. 

## _d: SUMMARY OF BASELINE RESULTS_ 

With accuracies above 96%, both classifiers showed remarkable performance on the BBC News dataset. The SVC fared somewhat better than Logistic Regression in terms of overall accuracy and some metrics related to a given category, such Precision and Recall for ‘‘Sport.’’ Logistic Regression, on the other hand, performed exceptionally well 

## 2) PARABOLIC WEIGHTING CONFIGURATIONS 

We carried out a number of controlled experiments with various parameter settings in order to assess the possible benefits of the Parabolic Weighting Mechanism (PWM) over the conventional TF-IDF approach. By employing a parabolic function to modify term weights, the PWM enables the model to provide greater weight to terms that are 

54374 

VOLUME 13, 2025 

K. Batri et al.: PWM in Information Retrieval: A Mathematical Analogy to Lenz’s Law 


![](prepared/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law/images/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law.pdf-0009-01.png)


more important in various contexts within the document. To determine which configuration produced the highest classification performance, we experimented with several values for the parameters _a_ , _b_ , and _c_ , which define the curve of the parabola. 

The combination _a_ = 0 _._ 5, _b_ = 0 _._ 8, and _c_ = 5 _._ 0 yielded the maximum classification accuracy across both models, according to our studies. In particular, the Support Vector Classifier (SVC) improved by 0.44% over the TF-IDF baseline with this configuration, achieving an accuracy of **97.30%** . Table 3 has the values. 

Likewise, Logistic Regression showed improved performance, increasing accuracy by 0.30% to **97.01%** from 96.71%. Listed in Table 3 are the combined values. 

In comparison to the TF-IDF method, these results imply that the Parabolic Weighting Mechanism is very successful at improving term representations when the parameter values are ideal, producing more precise classifications. The approach is especially good at identifying subtle document qualities that traditional term weighting techniques could miss. 

## _a: CONFUSION MATRIX ANALYSIS_ 

We looked at the confusion matrices of the two models to have a better understanding of their performance. We can observe the kinds of misclassifications that take place and how well the models differentiate between various categories thanks to these matrices. 

The confusion matrix for the SVC model (Figure 5) demonstrates the model’s great accuracy in every category. Misclassifications are rare and usually happen between categories that deal with related subjects. For example, misclassifications between ‘‘Politics’’ and ‘‘Business’’ are uncommon but yet occur, illustrating how difficult it is to distinguish between these categories, which frequently have overlapping content. 

Though there are some differences in the misclassification patterns, the confusion matrix for Logistic Regression (Figure 6) performs similarly well. This implies that although SVC and Logistic Regression perform similarly generally, they may handle some categories—like ‘‘Tech’’ and ‘‘Entertainment,’’ where misclassification rates are marginally higher—differently. 

Both models exhibit good classification overall, and the confusion matrices show that the Parabolic Weighting Mechanism refines word importance inside documents to help with more accurate categorisation. 

## 3) CATEGORY-SPECIFIC PERFORMANCE INSIGHTS 

The Parabolic Weighting Mechanism’s ability to boost performance by category stands as one of the study’s most noteworthy discoveries. While overall accuracy increased across all categories, several domains demonstrated particularly significant improvements. Categories such as **Entertainment** and **Politics** showed especially notable enhancements, indicating that the optimized weighting system more effectively 


![](prepared/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law/images/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law.pdf-0009-13.png)


**FIGURE 5.** Confusion matrix for parabolic weighting with SVC on the BBC news dataset. 


![](prepared/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law/images/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law.pdf-0009-15.png)


**FIGURE 6.** Confusion matrix for parabolic weighting with logistic regression on the BBC news dataset. 

addresses the unique challenges present in these specific domains. 

In the **Entertainment** category, the implementation of the optimized Parabolic Weighting Mechanism resulted in an improvement in **precision** from **0.97** to **0.98** . This improvement suggests that the Parabolic Weighting technique successfully reduced false positives in the categorization process by more effectively identifying the most relevant articles within this domain. 

The **Politics** category exhibited the most substantial improvement in **recall** , which increased from **0.96** to **0.99** following optimization. This significant enhancement implies that the classifier became more adept at accurately identifying relevant political articles, even in cases where the language contained ambiguities or was heavily contextdependent. The Parabolic Weighting Mechanism enabled the 

54375 

VOLUME 13, 2025 

K. Batri et al.: PWM in Information Retrieval: A Mathematical Analogy to Lenz’s Law 


![](prepared/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law/images/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law.pdf-0010-01.png)


**TABLE 3.** Accuracy Comparison of Classifiers. 

system to capture more true positives in this challenging category. 

These findings collectively suggest that the Parabolic Weighting Mechanism delivers enhanced overall performance in terms of both precision and recall, with particular strength in handling categories characterized by complex or subtle textual features. 

## _C. STATISTICAL ANALYSIS OF PWM AND TF-IDF PERFORMANCE COMPARISON_ 

The statistical evaluation demonstrates that both approaches achieve remarkably high performance scores, with distributions ranging from 0.90 to 1.00. PWM exhibits marginally superior performance, as evidenced by its distribution being slightly shifted rightward compared to TF-IDF in the performance density visualization. 

The effect size analysis yields particularly noteworthy results. Initial measurements on SVC indicate a Cohen’s d value of 1.4552, suggesting a substantial difference between the two methods. Further analysis on LR reveals an even more pronounced effect size with a Cohen’s d of 1.9730, emphasizing the practical significance of the performance differential between PWM and TF-IDF. These robust effect sizes underscore that the observed differences, while numerically subtle, represent meaningful improvements in classification capability. 

Bootstrap confidence interval analysis provides additional validation of these findings. The accuracy difference between PWM and TF-IDF centers around 0.0030, with a 95% confidence interval spanning from approximately 0.0000 to 0.0069. The distribution of this difference exhibits a slight right-skewed pattern, indicating some variability in the performance gap. A broader confidence interval distribution, bounded by 0.0124 and 0.0893, suggests some uncertainty in the precise magnitude of the performance differential. 

The comprehensive analysis reveals that while PWM consistently demonstrates superior performance over TFIDF, both methodologies achieve exceptionally high accuracy levels. The primary distinction lies not in absolute performance metrics but rather in the consistency and reliability of their predictions. This nuanced understanding is particularly relevant for applications where subtle improvements in reliability can have significant practical implications. 

## _D. RESULTS OF THE 20 NEWSGROUPS DATASET_ 

Our experimental methodology followed a systematic approach to investigate the efficacy of different weighting schemes. The baseline approach employed conventional TF-IDF weighting, serving as our control condition for 


![](prepared/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law/images/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law.pdf-0010-12.png)


**FIGURE 7.** Effect size visualization in SVC: Performance distribution of TF-IDF vs PWM (Cohen’s d **=** 1.4552). 


![](prepared/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law/images/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law.pdf-0010-14.png)


**FIGURE 8.** Bootstrap confidence interval for accuracy difference (PWM - TF-IDF) in SVC. 


![](prepared/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law/images/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law.pdf-0010-16.png)


**FIGURE 9.** Refined Effect Size Visualization (Cohen’s d = 1.9730) in LR. 

subsequent comparisons. We then implemented three distinct configurations of the parabolic weighting function, each with carefully selected parameters designed to evaluate specific aspects of feature weighting. Case 1 utilized parameters a = 1.0, b = 0.5, and c = 0.1 to examine the initial effects of parabolic weighting. Case 2 employed a negative leading 

54376 

VOLUME 13, 2025 

K. Batri et al.: PWM in Information Retrieval: A Mathematical Analogy to Lenz’s Law 


![](prepared/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law/images/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law.pdf-0011-01.png)



![](prepared/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law/images/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law.pdf-0011-02.png)


**FIGURE 10.** Bootstrap confidence interval distribution in LR. 

coefficient (a = −0.2) with parameters b = 0.8 and c = 5.0 to investigate the impact of negative curvature on classification performance. Finally, Case 3 implemented an optimized configuration with parameters a = 0.7, b = 0.6, and c = 5.0, which our preliminary analysis suggested would maximize classification effectiveness. 

We evaluated model performance using standard metrics including accuracy, precision, recall, and F1-score, with particular emphasis on differential performance across the various newsgroup categories. Additionally, confusion matrices were generated to facilitate detailed analysis of classification patterns and identify specific areas of misclassification, thereby providing insights into the strengths and limitations of each weighting approach. 

The baseline TF-IDF weighting scheme demonstrated strong overall performance, achieving an accuracy of 85.90% for SVC and 87.69% for LR models. This robust performance is consistent with the established effectiveness of TF-IDF for text classification tasks on this dataset. For Case 1 (a = 1.0, b = 0.5, c = 0.1), we observed a slight degradation in performance, with accuracy decreasing to 84.87%. This suggests that these particular parameters introduced a suboptimal weighting distribution that failed to capture the underlying feature importance effectively. 

Case 2 (a = −0.2, b = 0.8, c = 5.0) showed a more substantial performance decline, with accuracy dropping to 82.65%. This pronounced decrease indicates that negative curvature in the weighting function may distort the relative importance of terms in a manner that impedes effective classification. The degradation was particularly evident in specific categories that rely on distinctive terminology, suggesting that term importance was not optimally preserved through this weighting scheme. 

Notably, Case 3 (a = 0.7, b = 0.6, c = 5.0) outperformed all other configurations, including the baseline TF-IDF approach. This optimized parameter set achieved accuracies of 86.24% for SVC and 88.12% for LR classifiers, representing improvements of 0.34 and 0.43 percentage points, respectively, over the baseline. While these improvements may appear modest in absolute terms, they represent meaningful gains in classification performance, particularly considering that they were achieved through modification of 

the feature weighting approach alone, without alterations to the underlying classification algorithms. 

Detailed examination of the performance metrics, as presented in Tables 4 and 5, reveals interesting patterns across different newsgroup categories. For the SVC model, the optimized parabolic weighting function particularly enhanced precision for categories such as ‘‘rec.sport.hockey’’ (from 0.90 to 0.92) and ‘‘talk.politics.mideast’’ (from 0.91 to 0.94). Similar improvements were observed with the LR classifier, where precision for these categories increased from 0.92 to 0.94 and 0.91 to 0.94, respectively. 

This category-specific enhancement suggests that parabolic weighting with appropriate parameters may be especially beneficial for certain types of textual content, particularly those with distinctive terminology patterns. The improvements in precision indicate that the optimized weighting function reduced false positive classifications, potentially by more effectively capturing the discriminative power of category-specific terms. 

Table 6 presents a comparative analysis of classifier performance using the traditional TF-IDF method and the proposed Parabolic Weighting mechanism. The Support Vector Classifier (SVC) achieves an accuracy of 85.90% with TF-IDF, which improves to 86.24% with Parabolic Weighting, resulting in a marginal improvement of 0.34%. Similarly, the Logistic Regression (LR) classifier exhibits an accuracy increase from 87.69% to 88.12%, showing a gain of 0.43%. These results indicate that the Parabolic Weighting mechanism offers a slight enhancement in classification performance compared to TF-IDF, demonstrating its potential as an alternative feature weighting approach in text classification tasks. 

## 1) PERFORMANCE IMPROVEMENT BY PARABOLIC WEIGHTING 

The performance comparison between the baseline Raw TF-IDF approach and the proposed Parabolic Weighting method reveals nuanced differences across key metrics. The **precision** metric, which measures the proportion of true positive results among all instances predicted as positive by the model, showed slight variations between the methods. The baseline approach, using Raw TF-IDF, achieved an overall precision of 0.8743. In comparison, the best-performing configuration of the Parabolic Weighting method (with parameters _a_ = 0 _._ 7, _b_ = 0 _._ 6, and _c_ = 5 _._ 0) resulted in an overall precision of 0.8696. This represents a marginal decline of 0.54%, indicating a slight reduction in precision when transitioning from Raw TF-IDF to the optimized Parabolic Weighting approach. 

When examining the **recall** metric, which represents the proportion of actual positive instances correctly identified by the model, we observe some improvement. For the baseline method, using Raw TF-IDF, the overall **recall** is **0.8601** . In comparison, the best-performing Parabolic Weighting configuration (with parameters _a_ = 0 _._ 7, _b_ = 0 _._ 6, and _c_ = 5 _._ 0) achieves an overall **recall** of **0.8607** . This indicates an 

54377 

VOLUME 13, 2025 

K. Batri et al.: PWM in Information Retrieval: A Mathematical Analogy to Lenz’s Law 


![](prepared/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law/images/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law.pdf-0012-01.png)


**TABLE 4.** SVC performance comparison of raw TF-IDF and parabolic weighting (a **=** 0.7, b **=** 0.6, c **=** 5.0) on 20 news group classification dataset. 


![](prepared/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law/images/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law.pdf-0012-03.png)


**TABLE 5.** LR performance comparison of Raw TF-IDF and parabolic weighting (a **=** 0.5, b **=** 0.7, c **=** 5.0) on 20 news classification dataset. 


![](prepared/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law/images/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law.pdf-0012-05.png)


**TABLE 6.** Accuracy comparison of classifiers using TF-IDF and parabolic weighting. 

improvement of + **0.07%** , demonstrating a slight increase in recall when transitioning from Raw TF-IDF to the Parabolic Weighting method. 

The **f1-score** , which is the harmonic mean of **precision** and **recall** , provides a balanced metric for evaluating classification performance. For the baseline method, using Raw TF-IDF, the overall **f1-score** is **0.8601** . In contrast, the best-performing Parabolic Weighting configuration (with parameters _a_ = 0 _._ 7, _b_ = 0 _._ 6, and _c_ = 5 _._ 0) achieves an overall **f1-score** of **0.8604** . This indicates an improvement of + **0.03%** , reflecting a slight enhancement in classification performance when transitioning from Raw TF-IDF to the Parabolic Weighting method. 

While the overall percentage improvement in precision, recall, and f1-score is relatively small, the **parabolic weighting** method demonstrates its value in handling category-specific challenges. The subtle gains observed in recall and f1-score, particularly in categories like **sci.space** and **talk.politics.mideast** , indicate that this weighting scheme is beneficial for improving the classification of difficult-to-distinguish classes in the dataset. 

## _E. STATISTICAL ANALYSIS OF TF-IDF VS PWM ON 20NEWSGROUP DATASET_ 

The primary focus of this analysis includes effect size measurement, bootstrap confidence intervals, and a comparative performance evaluation based on accuracy scores. 

To assess the magnitude of the performance difference, Cohen’s d was computed, yielding a value of 0.8165. This indicates a moderate effect size, suggesting a substantial 

distinction in classification accuracy between the two methods. Figure 11 visualizes this effect size, showing overlapping yet distinguishable distributions for the accuracy scores obtained using TF-IDF and PWM. The difference is particularly evident in the positioning of their respective means, with PWM demonstrating a slight advantage over TF-IDF. 

Further refinement of the effect size analysis was conducted by examining the performance distribution in a more focused accuracy range. As illustrated in Figure 13, the distributions were analyzed specifically within the 0.875–0.900 range. Even in this constrained range, the effect size remains the same (Cohen’s d = 0.8165), reinforcing the observation that PWM consistently outperforms TF-IDF with relatively stable results. 

In addition to effect size analysis, bootstrap confidence intervals were generated to determine the statistical significance of the accuracy difference. Figure 12 presents the bootstrap confidence interval for the accuracy difference, with a 95% confidence interval ranging from 0.0124 (lower bound) to 0.0833 (upper bound). Since the confidence interval does not contain zero, the observed accuracy improvement can be considered statistically significant. The peak of the bootstrap distribution is centered around an accuracy improvement of approximately 4 percentage points, suggesting a notable enhancement in performance when using PWM. 

To further examine the precision of this improvement, an additional bootstrap confidence interval was computed specifically comparing PWM to TF-IDF, as shown in 

54378 

VOLUME 13, 2025 

K. Batri et al.: PWM in Information Retrieval: A Mathematical Analogy to Lenz’s Law 


![](prepared/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law/images/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law.pdf-0013-01.png)



![](prepared/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law/images/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law.pdf-0013-02.png)


**FIGURE 11.** Effect size visualization (Cohen’s d **=** 0.8165). 


![](prepared/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law/images/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law.pdf-0013-04.png)


**FIGURE 12.** Bootstrap confidence interval for accuracy difference. 

Figure 14. In this case, the 95% confidence interval is slightly narrower, spanning from −0.0017 (lower bound) to 0.0496 (upper bound). Although this interval marginally includes zero, the observed accuracy improvement (marked by the green vertical line at 0.0043) remains positive. This implies that while PWM generally provides better results than TF-IDF, there are instances where the difference is not statistically significant. Nevertheless, the central tendency favors PWM, reinforcing its slight yet consistent advantage. 

A direct performance comparison between the two methods is further depicted in Figure 13. Both techniques demonstrate high classification performance, with accuracy scores clustering between 0.87 and 0.90. The density distribution for PWM is slightly shifted to the right relative to TF-IDF, indicating a trend of improved performance. The narrow spread of the distributions suggests high consistency across different experimental runs and cross-validation folds. 

Taken together, these statistical analyses provide strong evidence that PWM offers a measurable improvement over TF-IDF in text classification tasks. While the absolute accuracy gain is relatively small (approximately 0.43 percentage points, as seen in Figure 14), such improvements can be valuable in large-scale NLP applications where incremental enhancements in accuracy contribute to overall system performance. 


![](prepared/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law/images/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law.pdf-0013-09.png)


**FIGURE 13.** Effect size visualization with focused performance range (Cohen’s d **=** 0.8165). 


![](prepared/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law/images/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law.pdf-0013-11.png)


**FIGURE 14.** Bootstrap confidence interval for accuracy difference (PWM - TF-IDF). 

## _F. DISCUSSION AND OPEN RESEARCH QUESTIONS_ 

The Parabolic Weighting Mechanism (PWM), inspired by Lenz’s Law, introduces a non-linear approach to term weighting in information retrieval (IR). Unlike traditional weighting techniques such as TF-IDF and BM25, which often disproportionately favor either frequent or rare terms, PWM dynamically balances term importance through a parabolic transformation. By penalizing extreme term occurrences while enhancing the relevance of moderately frequent terms, PWM aims to improve retrieval effectiveness by reducing biases inherent in conventional term-weighting models. 

## 1) EMPIRICAL PERFORMANCE AND OBSERVATIONS 

The experimental results obtained from the BBC News and 20 Newsgroups datasets demonstrate consistent improvements in classification accuracy when using PWM. Compared to TF-IDF, PWM exhibited accuracy gains ranging from 0.30% to 0.44% across different classifiers (SVC and Logistic Regression). These findings suggest that PWM contributes to a more nuanced term representation, particularly in datasets where semantic variations and domain-specific terminology influence classification performance. 

A notable pattern observed in the results is that PWM performs particularly well in categories characterized by 

54379 

VOLUME 13, 2025 

K. Batri et al.: PWM in Information Retrieval: A Mathematical Analogy to Lenz’s Law 


![](prepared/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law/images/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law.pdf-0014-01.png)


nuanced contextual dependencies. For instance, in the BBC News dataset, categories such as Politics and Entertainment showed significant performance improvements, indicating that PWM is capable of capturing subtle linguistic differences that conventional term-weighting models may overlook. Similarly, in the 20 Newsgroups dataset, topic-specific terms in categories like sci.space and talk.politics.mideast benefited from PWM’s ability to dynamically regulate term importance. 

From a statistical standpoint, the Cohen’s _d_ effect size analysis revealed substantial improvements in classification accuracy. With effect sizes of 1.4552 for SVC and 1.9730 for Logistic Regression, the observed gains are not just statistically significant but also practically meaningful. Additionally, the bootstrap confidence interval analysis confirmed the reliability of PWM’s performance improvements, reinforcing its robustness across different datasets and experimental settings. 

## 2) THEORETICAL IMPLICATIONS AND COMPARISON WITH EXISTING MODELS 

PWM presents a compelling alternative to traditional term-weighting models by introducing a physics-inspired balancing function. Unlike TF-IDF, which assumes a linear relationship between term frequency and importance, PWM follows a parabolic curve, ensuring that neither high-frequency nor low-frequency terms dominate the retrieval process. 

While BM25 improves upon TF-IDF by incorporating non-linear term frequency scaling and document length normalization, it does not dynamically penalize excessive term occurrences in the same way as PWM. Additionally, recent advancements in entropy-based term weighting (Rodriguez and Garcia [12]) and neural-enhanced term weighting (Cheng et al. [11]) attempt to refine term importance through context-aware statistical or deep learning-based approaches. However, these methods often lack explicit mathematical interpretability, whereas PWM’s physics-inspired formulation provides a structured, theoretically grounded alternative. 

Furthermore, PWM’s non-linear adjustment mechanism aligns with cognitive theories of information processing, where human perception of term importance is not strictly proportional to frequency but rather follows a diminishing returns principle—a phenomenon well-modeled by the parabolic function. This suggests that PWM may not only be valuable for information retrieval but could also have implications for natural language understanding and cognitive modeling in text analysis. 

## 3) OPEN RESEARCH QUESTIONS AND FUTURE DIRECTIONS 

Despite its promising results, several open research questions remain regarding the optimization, scalability, and integration of PWM into modern IR architectures. 

## _a: ORQ 1: HOW CAN THE PARABOLIC WEIGHTING PARAMETERS BE DYNAMICALLY OPTIMIZED ACROSS DIFFERENT DATASETS?_ 

The effectiveness of PWM is highly dependent on its configurable parameters ( _a_ , _b_ , _c_ ), which influence how term frequencies are adjusted. Currently, these parameters require manual tuning, which limits PWM’s adaptability to diverse corpora. Future work should explore automated parameter optimization techniques, such as Bayesian optimization, genetic algorithms, or deep reinforcement learning, to dynamically adjust PWM settings based on dataset characteristics. Research should also investigate how factors such as corpus size, domain specificity, and linguistic structures influence parameter selection strategies. 

## _b: ORQ 2: WHAT IS THE IMPACT OF INTEGRATING PWM INTO LARGE LANGUAGE MODEL (LLM)-BASED RETRIEVAL SYSTEMS?_ 

The growing dominance of transformer-based models (e.g., BERT, ColBERT, and T5) in IR necessitates an exploration of how PWM can be incorporated into deep learning architectures. Unlike traditional retrieval models, LLM-based ranking systems rely on contextual embeddings and attention mechanisms to determine term importance. Future research should examine whether PWM’s term weighting function can complement attention mechanisms by providing a structured, physics-inspired adjustment to term relevance. This could be particularly beneficial for long-tail queries, where query expansion and semantic disambiguation play a critical role in retrieval performance. 

## _c: ORQ 3: CAN PWM IMPROVE QUERY EXPANSION TECHNIQUES?_ 

Query expansion techniques often introduce spurious or irrelevant terms, which can degrade retrieval precision. Since PWM inherently balances term frequency biases, investigating its application in query expansion could lead to more accurate term selection and ranking in expanded queries. Research should analyze whether PWM can enhance the diversity and relevance of expanded queries, particularly for ambiguous or underspecified search inputs. 

## _d: ORQ 4: HOW DOES PWM PERFORM ON REAL-WORLD LARGE-SCALE RETRIEVAL TASKS?_ 

While PWM has been tested on benchmark datasets, its scalability and efficiency in real-world search engines remain an open question. Large-scale retrieval tasks involve millions to billions of documents, requiring computationally efficient term-weighting mechanisms. Future studies should evaluate PWM’s computational trade-offs compared to conventional models like BM25, particularly when deployed in high-volume search applications such as web search, digital libraries, and enterprise knowledge retrieval systems. 

54380 

VOLUME 13, 2025 

K. Batri et al.: PWM in Information Retrieval: A Mathematical Analogy to Lenz’s Law 


![](prepared/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law/images/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law.pdf-0015-01.png)


## _e: ORQ 5: WHAT THEORETICAL EXTENSIONS OF THE PHYSICS-INSPIRED APPROACH MIGHT YIELD NEW WEIGHTING PARADIGMS?_ 

PWM is based on Lenz’s Law, but other physics-based principles (e.g., entropy models, thermodynamic equilibrium, quantum mechanics) could inspire further advancements in term weighting. Exploring whether quantum-inspired models (e.g., interference-based term weighting) or thermodynamic entropy measures can enhance PWM’s effectiveness may lead to novel hybrid term-weighting schemes with even greater adaptability and theoretical depth. 

## **V. CONCLUSION** 

This study introduced a novel **parabolic weighting scheme** for term representation in information retrieval, drawing inspiration from the electromagnetic principles of **Lenz’s Law** . The approach addresses fundamental limitations in conventional term weighting techniques by applying a parabolic transformation that effectively balances the importance of both frequent and uncommon terms within documents. This transformation mitigates extreme variations in term weights, resulting in more semantically meaningful document representations. 

Empirical evaluations conducted on the **20 Newsgroups** and **BBC News** datasets conclusively demonstrated the superiority of the parabolic weighting scheme over traditional **TF-IDF** approaches. When implemented with **Logistic Regression** and **Support Vector Classifier (SVC)** models, our method consistently achieved higher classification accuracy across different experimental configurations. These performance improvements can be attributed to the weighting scheme’s ability to preserve discriminative power while reducing sensitivity to outlier term frequencies. 

The configurable nature of the model through parameters _a_ , _b_ , and _c_ represents a significant advancement in adaptive term weighting, allowing information retrieval systems to better accommodate the linguistic characteristics of diverse corpora. By bridging theoretical principles from physics with practical advancements in information retrieval, this work contributes a valuable new technique to the text processing toolkit that enhances both the theoretical understanding and practical implementation of term weighting mechanisms. 

## **VI. ACKNOWLEDGMENT** 

This work is an interdisciplinary effort combining principles from information retrieval and electromagnetic theory to develop a novel term weighting mechanism. 

## **REFERENCES** 

- [1] J. Gantz and D. Reinsel, ‘‘The digital universe decade—Are you ready?’’ IDC iView, EMC, Tech. Rep., 2012. 

- [2] N. J. Belkin and W. B. Croft, ‘‘Information filtering and information retrieval: Two sides of the same coin?’’ _Commun. ACM_ , vol. 35, no. 12, pp. 29–38, Dec. 1992. 

- [3] R. Baeza-Yates and B. Ribeiro-Neto, _Modern Information Retrieval_ . Reading, MA, USA: Addison-Wesley, 1999. 

- [4] L. Boratto, A. Bellogín, S. Kleanthous, E. Lex, F. M. Malloci, and M. Marras, _Advances in Bias and Fairness in Information Retrieval_ (Lecture Notes in Computer Science). Cham, Switzerland: Springer, 2024. 

- [5] S. Deerwester, S. Dumais, G. W. Furnas, T. K. Landauer, and R. A. Harshman, ‘‘Indexing by latent semantic analysis,’’ _J. Amer. Soc. Inf. Sci._ , vol. 41, no. 6, pp. 391–407, Sep. 1990. 

- [6] H. Li, J. Wu, and Q. Yang, ‘‘Improving term weighting with term closeness and distribution,’’ _J. Assoc. Inf. Sci. Technol._ , vol. 65, no. 12, pp. 2436– 2447, 2014. 

- [7] A. Singhal, ‘‘Modern information retrieval: A brief overview,’’ _IEEE Data Eng. Bull._ , vol. 24, no. 4, pp. 35–43, Jan. 2001. 

- [8] G. Salton and C. Buckley, ‘‘Term-weighting approaches in automatic text retrieval,’’ _Inf. Process. Manage._ , vol. 24, no. 5, pp. 513–523, Jan. 1988. 

- [9] R. Blanco and C. Lioma, ‘‘Graph-based term weighting for information retrieval,’’ _Inf. Retr._ , vol. 15, no. 1, pp. 54–92, Feb. 2012. 

- [10] A. Ushio and H. Kamigaito, ‘‘Back to TF-IDF: Neural term weighting revisited,’’ in _Proc. 59th Annu. Meeting Assoc. Comput. Linguistics_ , 2021, pp. 3762–3773. 

- [11] J. Cheng, J. Gao, and J. Callan, ‘‘Neural term weighting,’’ in _Proc. 41st Int. ACM SIGIR Conf. Res. Develop. Inf. Retr._ , 2018, pp. 253–262. 

- [12] P. Rodriguez and M. Garcia, ‘‘Entropy-based term weighting in information retrieval,’’ _J. Inf. Sci._ , vol. 50, no. 2, pp. 190–204, 2024. 

- [13] R. Blanco and C. Lioma, ‘‘Advances in graph-based term weighting for IR,’’ in _Proc. 47th Int. ACM SIGIR Conf. Res. Develop. Inf. Retr._ , 2024, pp. 1–8. 

- [14] S. Robertson and S. Jones, ‘‘Understanding inverse document frequency: On theoretical arguments for IDF,’’ _J. Document._ , vol. 60, no. 5, pp. 503– 520, Oct. 2004. 

- [15] W. Chen and X. Liu, ‘‘An analysis of TF-IDF and its variants,’’ in _Proc. 5th Int. Conf. Data Mining_ , 2006, pp. 268–273. 

- [16] M. Trabelsi, Z. Chen, B. D. Davison, and J. Heflin, ‘‘Neural ranking models for document retrieval,’’ _Inf. Retr. J._ , vol. 24, no. 6, pp. 400–444, 2021. 

- [17] H. Li, X. Chen, and J. Wu, ‘‘Adaptive term frequency scaling for robust IR systems,’’ _J. Inf. Retr._ , vol. 30, no. 1, pp. 112–130, 2023. 

- [18] P. Wang and M. Zhao, ‘‘Context-aware IDF for improved document ranking,’’ _J. Inf. Sci._ , vol. 51, no. 2, pp. 245–260, 2024. 

- [19] S. E. Robertson and S. Walker, ‘‘Okapi and its use in information retrieval,’’ _J. Document._ , vol. 51, no. 3, pp. 290–319, 1995. 

- [20] S. Robertson and H. Zaragoza, ‘‘The probabilistic relevance framework: BM25 and beyond,’’ _Found. Trends Inf. Retr._ , vol. 3, no. 4, pp. 333–389, 2009. 

- [21] H.-J. Yang and I.-Y. Choi, ’‘Enhancing search‘functionality for website posts and product reviews: Improving BM25 ranking algorithm performance using the resnet-transformer model,’’ _J. Korea Soc. Comput. Inf._ , vol. 29, no. 11, pp. 67–77, 2024 

- [22] L. Zheng, H. Chai, X. Chen, J. Jin, W. Zhang, Y. Yu, X. Guo, C. Ge, and Z. Feng, ‘‘Searchbased time-aware graph-enhanced recommendation with sequential behavior data,’’ _ACM Trans. Recommender Syst._ , vol. 2, no. 4, pp. 1–29, 2024. 

- [23] J. M. Ponte and W. B. Croft, ‘‘A language modeling approach to information retrieval,’’ in _Proc. 21st Annu. Int. ACM SIGIR Conf. Res. Develop. Inf. Retr._ , Aug. 1998, pp. 275–281. 

- [24] H. Freedman, J. Metzger, N. Abolhassani, A. Tudor, B. Tomlinson, and S. Paul, ‘‘A Bayesian approach to constructing probabilistic models from knowledge graphs,’’ _Int. J. Semantic Comput._ , vol. 18, no. 1, pp. 25–49, 2024. 

- [25] X. Chen and H. Wang, ‘‘Semantic term weighting for improved information retrieval,’’ _Inf. Process. Manage._ , vol. 51, no. 5, pp. 686–697, 2015. 

- [26] C. Savelli and F. Giobergia, ‘‘Enhancing crosslingual word embeddings: Aligned subword vectors for out-of-vocabulary terms in FastText,’’ in _Proc. IEEE 18th Int. Conf. Appl. Inf. Commun. Technol. (AICT)_ , 2024, pp. 1–6. 

- [27] K. A. Hambarde and H. Proenca, ‘‘Information retrieval: Recent advances and beyond,’’ _IEEE Access_ , vol. 11, pp. 76581–76604, 2023. 

- [28] J. Pennington, R. Socher, and C. Manning, ‘‘Glove: Global vectors for word representation,’’ in _Proc. Conf. Empirical Methods Natural Lang. Process. (EMNLP)_ , 2014, pp. 1532–1543. 

- [29] J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova, ‘‘BERT: Pre-training of deep bidirectional transformers for language understanding,’’ 2018, _arXiv:1810.04805_ . 

- [30] O. Khattab and M. Zaharia, ‘‘ColBERT: Efficient and effective passage search via contextualized late interaction over BERT,’’ in _Proc. 43rd Int. ACM SIGIR Conf. Res. Develop. Inf. Retr._ , 2020, pp. 39–48. 

54381 

VOLUME 13, 2025 

K. Batri et al.: PWM in Information Retrieval: A Mathematical Analogy to Lenz’s Law 


![](prepared/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law/images/Parabolic_Weighting_Mechanism_in_Information_Retrieval_A_Mathematical_Analogy_to_Lenzs_Law.pdf-0016-01.png)


- [31] P. Rodriguez and M. Garcia, ‘‘Entropy-based term weighting in information retrieval,’’ in _Proc. 17th Int. Conf. Inf. Retr. Technol._ , 2014, pp. 171–179. 

- [32] X. Li, Y. Wang, and H. Zhou, ‘‘A thermodynamic-inspired entropy model for adaptive term weighting in dynamic information retrieval,’’ _J. Inf. Sci._ , vol. 48, no. 2, pp. 345–362, 2022. 

- [33] S. Kim and J. Park, ‘‘Quantum-inspired models for semantic information retrieval,’’ in _Proc. Int. Conf. Comput. Sci. Comput. Intell._ , 2017, pp. 212– 219. 

- [34] T. Zhang, R. Liu, and H. Chen, ‘‘Quantum interference mechanisms for enhanced term weighting in semantic retrieval,’’ _ACM Trans. Inf. Syst._ , vol. 41, no. 1, pp. 1–28, 2023. 

- [35] V. Gupta and G. S. Lehal, ‘‘A survey of text mining techniques and applications,’’ _J. Emerg. Technol. Web Intell._ , vol. 1, no. 1, pp. 60–76, Aug. 2009. 

- [36] P. Johnson, ‘‘Contextual incompleteness in term weighting models,’’ _Inf. Process. Manage._ , vol. 46, no. 4, pp. 423–435, 2010. 

- [37] K. S. Jones, ‘‘Semantic ambiguity and term weighting in information retrieval,’’ _ACM SIGIR Forum_ , vol. 42, no. 1, pp. 33–39, 2008. 

S. LAKSHMI received the Ph.D. degree in information and communication engineering from Anna University, Chennai, in 2018, with research focused on web-search engine performance using AI-based algorithms. She is currently a dedicated Researcher and an academician with extensive experience in achieving organizational goals through effective and organized practices. She is also an Associate Professor with Jain (Deemedto-be University), Bengaluru, where she is responsible for coordinating the Department IQAC and managing the overall lab budget. She has previously held positions as an Associate Professor with the PSRR College of Engineering, Sivakasi, and an Assistant Professor with the RVS College of Engineering and Tech and Shree Venkateshwara Hi-Tech Engineering College. She has a strong research background in areas, such as communication systems, deep learning, and image segmentation, and has published several papers in international journals and conferences. 

- [38] H. Liu, Y. Chen, and W. Zhang, ‘‘Context-aware term weighting models: Challenges and opportunities,’’ _ACM Trans. Inf. Syst._ , vol. 40, no. 3, pp. 1–25, 2022. 

- [39] R. Williams and L. Zhao, ‘‘Dynamic information retrieval models: A review and future directions,’’ _J. Inf. Retr._ , vol. 16, no. 2, pp. 145–168, 2013. 

- [40] X. Zhang, T. Wang, and P. Li, ‘‘Adaptive term weighting for real-time information retrieval,’’ _Inf. Syst. J._ , vol. 55, no. 2, pp. 98–117, 2023. 

- [41] H. Liu, Y. Chen, and W. Zhang, ‘‘Contextual embeddings for improved term weighting in information retrieval,’’ _ACM Trans. Inf. Syst._ , vol. 41, no. 1, pp. 1–22, 2023. 

KRISHNAN BATRI received the Ph.D. degree in computer science and engineering from the National Institute of Technology, Trichy, India. He is currently a Professor and the Deputy Director of the Courses and Delivery at the School of Computer Science and Engineering, Jain University, Bengaluru, India. He has supervised 13 Ph.D. scholars and has published extensively in leading journals and conferences. He is also an advocate for curriculum development and fostering academic collaboration at both national and international levels. His research interests include information retrieval, artificial intelligence, genetic algorithms, data fusion techniques, and deep learning applications. 

R. SOWRIRAJAN is currently an Assistant Professor and the Head of the Department of Mathematics, Dr. N.G.P. Arts and Science College, Coimbatore, India. With 16 years of experience in teaching and research, he has published research articles in international journals and is guiding Ph.D. students. He has conducted conferences, workshops, and refresher courses with support from government agencies and delivered lectures at various conferences and events. His research interest includes real-life applications of mathematics. 

54382 

VOLUME 13, 2025 

