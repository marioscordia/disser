
![](prepared/A_Retrieval_Model_with_Contextual_Correlation_Anal/images/A_Retrieval_Model_with_Contextual_Correlation_Anal.pdf-0001-00.png)



![](prepared/A_Retrieval_Model_with_Contextual_Correlation_Anal/images/A_Retrieval_Model_with_Contextual_Correlation_Anal.pdf-0001-01.png)



![](prepared/A_Retrieval_Model_with_Contextual_Correlation_Anal/images/A_Retrieval_Model_with_Contextual_Correlation_Anal.pdf-0001-02.png)


Indian Institute of Technology Kharagpur 

Indian Institute of Technology Kharagpur 

Indian Institute of Technology Kharagpur 

Verbose Query, Information Retrieval, Query Term Weighting, Document Ranking, Contextual Embeddings, Dense Representation 

July 10th, 2025 

https://doi.org/10.21203/rs.3.rs-6970571/v1 

  This work is licensed under a Creative Commons Attribution 4.0 International License. Read Full License 

No competing interests reported. 

## A Retrieval Model with Contextual Correlation Analysis for Verbose Queries 

Dipannita Podder[1*] , Jiaul H. Paik[1] and Pabitra Mitra[1] 

> 1*Indian Institute of Technology Kharagpur,Kharagpur, West Bengal, 721302, India. 

*Corresponding author(s). E-mail(s): dipannita@iitkgp.ac.in; Contributing authors: jiaul@ai.iitkgp.ac.in; pabitra@cse.iitkgp.ac.in; 

## Abstract 

Retrieving relevant documents using verbose queries is a key challenge in information retrieval, as such queries often include extraneous terms. Traditional retrieval models treat all query terms equally, which limits their effectiveness. Existing methods for verbose queries are typically supervised or rely on costly two-stage ranking pipelines. We propose a fully unsupervised, single-phase retrieval model that estimates the centrality of each query term by analyzing its contextual correlation with the entire query. A fully connected term graph is constructed, where edge weights capture the relative correlation of each term with the query context compared to others. Centrality scores are computed via power iteration over this graph. Dense representations of query terms and context are obtained using a pre-trained Bidirectional Encoder Representations from Transformers (BERT) model. To further reduce the influence of non-informative document terms, an additional weight based on term information content is introduced. These two weights are combined and integrated into a modified Markov Random Field Sequential Dependence Model (SDM) for ranking. Experiments show that our model outperforms unsupervised baselines, performs comparably to supervised baselines, and surpasses several neural rankers in zero-shot settings. Comparable results with both GloVe and BERT embeddings highlight its embedding independence nature. The model shows larger gains on longer queries, modest improvements on shorter ones, but never underperforms SDM. Therefore, the model’s independence from relevance judgments and top-ranked documents, along with its consistent, embedding-agnostic performance across query lengths, makes it well-suited for low-resource scenarios. 

Keywords: Verbose Query, Information Retrieval, Query Term Weighting, Document Ranking, Contextual Embeddings, Dense Representation 

1 

## 1 Introduction 

Search engines are an indispensable part of modern life for accessing information from the ever-growing digital information space. They operate at a large scale and handle billions of queries every day to support a wide range of tasks, from product searches and answering questions to retrieving academic articles and navigating legal or policy documents. Thus, to meet user needs, search engines rank documents by estimating their relevance to the query. Modern search engines typically employ multistage ranking pipelines to balance efficiency and effectiveness [11, 22, 46]. In these architectures, an initial set of documents is retrieved from the large collections using computationally inexpensive traditional retrieval models, which are then re-ranked by more computationally expensive neural models. However, a key limitation of multistage retrieval is its dependence on the initial ranker. If the most relevant documents are not retrieved by the first stage, re-rankers cannot rank them. 

The traditional term-based models are typically used as first-stage rankers, where query-document term matching is the fundamental building block. These models assign equal importance to all query terms during term matching. Thus, these models perform well for short, keyword-based queries and struggle with verbose queries that contain several extraneous terms. Meanwhile, with the rise of user-friendly interfaces such as voice search and natural language query reformulation [8, 9, 25, 26, 38, 55], verbose queries have become increasingly common. Users often submit free-form natural text, which challenges retrieval models to identify the core requirement. Thus, improving the performance of retrieval models for verbose queries is a timely research problem. 

Prior works that enhance retrieval effectiveness for verbose queries, focus on identifying and prioritizing central terms [4, 6, 47] in the ranking function. However, many of these approaches rely heavily on supervised learning frameworks [5–7, 60], and depend on large sets of training queries with relevance judgments data. Several unsupervised alternatives have been proposed [33, 47], but they assign weights to query terms based on their frequency in the top-ranked documents, retrieved by treating all query terms as equally important. While they avoid training data, they require two full passes over the document collection, one for initial retrieval and one for final ranking, which makes them computationally expensive for large collections and unreliable, given that the quality of early-stage retrieval significantly impacts the final ranking. 

In this work, we propose a single-stage, unsupervised retrieval model that determines the weights of terms in verbose queries and incorporates them into retrieval models to improve retrieval effectiveness. We assume that the core terms encapsulate the intent of the query [4, 60] and exhibit a strong correlation with the overall query context. Thus, we estimate the centrality scores of query terms by leveraging their contextual correlation with the query context. However, a key limitation with this assumption is that it may assign undue weights to semantically similar but extraneous terms, which often occur more frequently in verbose queries than the actual central terms. To mitigate this, we analyze each term’s correlation with the entire query context relative to the correlations of other terms, enabling a more discriminative estimation of term centrality. 

2 

In practice, we construct a fully connected graph wherein each node represents a query term and the edge weight between two nodes reflects the relative contextual correlation of terms. To obtain the dense vector representation of the query and the query terms, we leverage a pre-trained Bidirectional Encoder Representations from Transformers (BERT) model. A power iteration is then applied to this graph to estimate the centrality weight. Additionally, we incorporate another weighting factor based on the information content of terms to down-weight the matching with the noninformative document terms. These combined weights are integrated into the Markov Random Field (MRF)-based sequential dependency model (SDM) [44], which is the state-of-the-art traditional retrieval model. 

We demonstrate the effectiveness of the proposed method across multiple test collections containing verbose queries. Our model consistently outperforms traditional unsupervised baselines and remains competitive with supervised models, despite requiring no training data. It also surpasses several neural retrieval models under zeroshot settings. In addition, the model shows substantial gains for longer queries, modest improvements over SDM for shorter queries, but never underperforms SDM. The model also delivers comparable performance with both GloVe and BERT embeddings, further indicating its independence from specific embedding choices. 

Moreover, the major contributions of this work are 

1. The proposed retrieval model demonstrates consistent improvements over the existing baselines. Therefore, it can appropriately identify the core terms and prioritize these terms in the ranking function for effective retrieval with verbose queries. While it achieves substantial gains for longer queries, it never falls behind SDM across any query length. 

2. The model is fully unsupervised and does not require any annotated training data with relevance judgments. This makes it particularly suitable for low-resource scenarios where manually labeled data is limited or unavailable. 

3. It employs a single-pass retrieval strategy. Therefore, it reduces the dependency on the quality of top-ranked documents from an initial retrieval stage and reduces the computational overhead typically associated with ranking large-scale collections twice. 

4. The model maintains comparable performance across different embedding techniques, without significant variation. This embedding-agnostic behavior makes it broadly applicable across diverse retrieval settings. 

## 2 Related Work 

With the recent advancement of search engine, the user can provide query in any form, and the search engine manipulate the given query for better retrieval [9, 26, 27, 38, 41, 49]. For the first time, Kumaran and Allan [35] showed that the shorter reformulations of long queries can improve retrieval performance. Then Kumaran and Carvalho [36] reduce the query into sub-queries by modeling them as learning to rank problems. On the other hand, Di Buccio et al. [16] showed that any long query is not necessarily verbose. Hence detecting verbosity and accordingly modifying the ranking model is necessary. 

3 

One of the major contributory works for weighting the terms of verbose query is attempted by Bendersky and Croft [4]. They propose a general probabilistic model that incorporates the information about key concepts (noun phrases) into the original query, and the weights of concepts are estimated through supervised learning. However, this model cannot outperform the state-of-the-art sequential dependence model [44] which considers each term with equal importance. To our knowledge, Lease [37] for the first time, incorporates concept weights to the sequential dependence model and improves the retrieval effectiveness. They use a regression rank-based learning algorithm to find out the concept weight. Besides, Bendersky et al. [5] proposed the Weighted Dependence Model, which parameterizes weights for query terms and phrases using both endogenous (collection-based) and exogenous (external) features and trains them with learning-to-rank methods, yielding consistent gains over both bag-of-words and unweighted SDM. Then, Bendersky et al. [6] extended this approach by incorporating both explicit and latent concepts, derived via pseudo-relevance feedback and integrated into a parameterized concept weighting framework. 

To reduce reliance on relevant judgment data, several unsupervised methods are proposed which use top-ranked documents to estimate term weight. Paik and Oard [47] construct a fully connected graph from the query terms, where the edge weights are determined from the relative term frequency of top-ranked documents. They finally, employ a fixed-point power iteration on this graph to estimate the weight of terms. Similarly, Karisani et al. [33] utilize a pseudo-relevance feedback method to estimate term weights. They calculate the distance of each document containing the term to all other documents in the retrieved set, which is then combined with the similarity between the query and the retrieved documents. As these unsupervised approaches utilize the top-ranked documents, their efficiency decreases as the collection size grows. 

However, none of these methods exploit the strength of word embeddings [45, 50] to estimate term importance, although word embeddings have been widely adopted in several IR tasks for incorporating semantic information and expanding query terms [3, 19, 52, 58]. Therefore, Zheng et al. [60] introduced an approach that uses Word2Vec to create representations for terms and queries, which are then compared to target term weights that are inferred from relevance judgments. A regularized linear regression model is then used to predict term weights. However, the major drawback of this model is that it relies on relevant judgment data and often uses learning-torank frameworks. Besides, the extraordinary success of the BERT model in various applications has motivated the IR research community to leverage BERT in several IR tasks. For example, DeepCT [13] uses a fine-tuned BERT model to reweight document terms, emphasizing the important ones. Besides, a preliminary version of the approach proposed in this paper was presented as an abstract [51], where the query term importance is estimated by analyzing the correlation between individual term vectors and the full query using a pre-trained BERT model, and incorporates the resulting weights into sequential dependence models. 

Furthermore, in recent times several neural retrieval models have been proposed that capture the complex relationship between queries and documents [12, 14, 20, 23, 30, 43, 53]. Among them, two noteworthy types of models are (a) learned dense retriever and (b) learned sparse retrievers. Dense retrieval models [21, 28, 29, 56] 

4 

generate dense vector representations of queries and documents and store document representations in a dense index and retrieve them through Nearest Neighbours search [32, 56]. Conversely, learned sparse retrieval models produce sparse vector representations for each document token, offering straightforward integration into existing inverted indexing engines. ColBERT [34] stands out among the top-performing dense retrievers, while UniCOIL [39] is a prominent sparse retrieval model. Both of them match the query document tokens followed by the max pooling operation. However, Formal et al. [18] demonstrate that ColBERT does not have a notion of token importance. Thus, the use of all tokens with equal importance can reduce the retrieval effectiveness, especially when the query contains extraneous terms. Although neural ranking models demonstrate substantial improvement, they require expensive computational resources for retrieving information from large document collections [24]. 

## 3 Proposed Approach 

In this work, we determine the centrality weights of terms in verbose queries and incorporate them into the Markov Random Field (MRF)-based Sequential Dependence Model (SDM) [44]. This section begins by introducing our modified ranking function, which integrates the centrality weights to prioritize core terms. We then outline the key principles governing our term centrality estimation, followed by how dense vectors are generated to represent the query terms and the entire query. Finally, we detail the complete methodology for estimating these term weights. 

## 3.1 Proposed Ranking Function 

We use the Markov Random Field-based (MRF) Sequential Dependence Model [44] as our basic ranking function, following prior research [5]. This model has remained a strong state-of-the-art retrieval approach over the decades, as it effectively captures dependencies among query terms and outperforms traditional models [59] that assume term independence. 

The MRF model captures the joint distribution (PΛ(D, Q)) for a document random variable D and query term random variables Q = q1q2 · · · qn. The ranking function based on the joint distribution is defined as 


![](prepared/A_Retrieval_Model_with_Contextual_Correlation_Anal/images/A_Retrieval_Model_with_Contextual_Correlation_Anal.pdf-0006-06.png)


where C(G) is the set of cliques in G, which comprises query nodes Q = q1q2 · · · qn and a document node D. The neighboring query terms of graph G are dependent 

5 


![](prepared/A_Retrieval_Model_with_Contextual_Correlation_Anal/images/A_Retrieval_Model_with_Contextual_Correlation_Anal.pdf-0007-00.png)


Fig. 1: An example of MRF graph for query Q = q1q2q3q4q5 and document D 

on each other, and other query terms are independent, given D. ψ(.; Λ) is a nonnegative potential function over clique configurations parameterized by Λ. These clique potentials are defined as ψ(c; Λ) = exp[λcg(c)], where g(c) is some real-valued feature function over the clique values, and λc is the weight given to that particular feature function. 

The sequential dependence model (illustrated in Figure 1) has three different clique sets. The first set includes cliques with one query term and the document node ({q1, D}, {q2, D}, {q3, D}, {q4, D}, {q5, D}). The second set has cliques containing the document node and two query terms appearing sequentially in the query ({#O(q1, q2), D}, {#O(q2, q3), D}, {#O(q3, q4), D}, {#O(q4, q5), D}). The third set has cliques containing the document node and two query terms ({#U (q1, q2), D}, {#U (q2, q3), D}, {#U (q3, q4), D}, {#U (q4, q5), D}) appearing in any order in the query. Thus, this model considers unigram, ordered bigram, and unordered bigram while ranking the documents. The ranking function of SDM is 


![](prepared/A_Retrieval_Model_with_Contextual_Correlation_Anal/images/A_Retrieval_Model_with_Contextual_Correlation_Anal.pdf-0007-04.png)


where T denotes matching with unigram, O denotes matching with ordered bigram (i.e., exact phrase), and U considers unordered matches, and λT , λO, and λU are the parameters. 

We incorporate the estimated term weights, which reflect the centrality of query terms, into the ranking function (Eq. 2) by modifying the corresponding potential functions as 


![](prepared/A_Retrieval_Model_with_Contextual_Correlation_Anal/images/A_Retrieval_Model_with_Contextual_Correlation_Anal.pdf-0007-07.png)


The proposed final ranking function is obtained by applying the modified potential (Eq. 3) to the original ranking function (Eq. 2) as 


![](prepared/A_Retrieval_Model_with_Contextual_Correlation_Anal/images/A_Retrieval_Model_with_Contextual_Correlation_Anal.pdf-0007-09.png)


6 


![](prepared/A_Retrieval_Model_with_Contextual_Correlation_Anal/images/A_Retrieval_Model_with_Contextual_Correlation_Anal.pdf-0008-00.png)


where A = {αT , αO, αU } represents the estimated weights for unigrams and bigrams. The method for estimating these weights is described in the following subsections. 

In our experiment, we fix λT = 0.85, λO = 0.1, λU = 0.05, as reported to be optimal in the original paper [44]. We use the language model with dirichlet smoothing [44, 59] as the feature function g(qc, D). 

This allows the ranking function to assign more weight to core terms during querydocument term matching, while reducing the influence of extraneous terms often present in verbose queries. Therefore, the retrieval function prioritizes matches with the most central terms and is better able to align the ranked documents with the user’s actual information need. 

## 3.2 Key Principles of Weight Estimation 

The proposed term centrality estimation builds on the following principles 

1. The central query terms are assumed to encapsulate the inherent meaning of the query [4, 60]. Thus, a term whose dense vector exhibits a high correlation with the contextual vector of the entire query can be inferred to represent the core term. 

2. Relying solely on the correlation of individual terms with the entire query vector can inadvertently overemphasize frequent, semantically related terms. This occurs because such terms may exhibit similar correlation scores to the overall query representation. Although central terms will likely have strong correlations, they appear in smaller numbers. On the other hand, several less important semantically similar terms appear in greater frequency in verbose queries, and get a higher score when the correlation score of all the terms is normalized. Therefore, accurately determining term centrality requires evaluating a term’s correlation with the entire query representation relative to the correlations of other terms within the query. 

3. Verbose queries often contain many extraneous terms, and traditional retrieval models typically rely on direct term matching between queries and documents. However, a term may appear in documents due to its general distribution across the collection, rather than its relevance to the document’s specific topic [1, 48]. These are considered non-informative terms. When query terms match with such non-informative terms, retrieval effectiveness can degrade. Since verbose queries include more non-central terms, the likelihood of such misleading matches increases. While the principles discussed earlier focus on identifying terms highly correlated with the query context, they do not explicitly account for this issue. Therefore, an additional weight should be introduced to mitigate the impact of matching with non-informative document terms. 

## 3.3 Dense Vector Generation 

To estimate term weights in verbose queries, it is important to understand how each term relates to the overall query context. This requires generating semantically rich 

7 

dense representations for individual query terms as well as for the entire query. For this purpose, we use pre-trained Bidirectional Encoder Representations from Transformers (BERT) model[1] [15], that has demonstrated strong performance across a wide range of natural language processing tasks. BERT is particularly well-suited for this task as it generates contextualized embeddings by considering the full input sequence through attention, which is essential for capturing the nuanced relationships present in verbose queries. The input query is first tokenized and fed into pre-trained BERT model to obtain contextualized token-level embeddings. To represent the overall query context, we use the final hidden state corresponding to the special [CLS] token, which serves as the embedding of the entire input sequence. 

As described in Section 3.1, the underlying MRF-based Sequential Dependence Model considers unigrams, ordered bigrams, and unordered bigrams during query-document matching. Thus, for individual unigrams, we directly use the BERTgenerated contextualized embeddings of the corresponding tokens as their dense vectors. In addition to the unigram embeddings, to obtain the embedding for an unordered bigram, we compute the average of the embeddings of its two constituent unigrams. For ordered bigrams, we input the phrase into BERT as a sequence and use the [CLS] token embedding to obtain the representation. These dense vectors are subsequently used by the proposed algorithm for estimating the centrality weights of query terms. 

## 3.4 Context-Driven Centrality Estimation 

This section describes our proposed methodology for estimating the centrality of query terms, based on their relevance to the overall query context. 

Following the first principle outlined in Section 3.2, we assume that central terms are those that encapsulate the inherent meaning of the query [4, 60]. Therefore, to identify such core terms, we primarily measure the correlation between each individual term and the context of the entire query. 

Let vQ denote the dense vector representation of the entire query (obtained from the vector of [CLS] token) and vti represent the contextualized embedding of a term ti ∈C, where C is the set of candidate terms from the query. The correlation between the term ti and the overall query context is computed as 


![](prepared/A_Retrieval_Model_with_Contextual_Correlation_Anal/images/A_Retrieval_Model_with_Contextual_Correlation_Anal.pdf-0009-06.png)


Here, ⟨vQ, vti⟩ denotes the dot product between the two vectors, and d is a hyperparameter. 

However, while the raw term correlation ρ(Q, ti) provides a basic measure of relation of a term with the entire query context, it is insufficient to accurately estimate the centrality of each term within the query. Because, as highlighted in the second key principle, semantically similar terms may receive comparable correlation scores, especially in verbose queries, where frequently occurring but non-central terms might dominate. To address this issue, the relative correlation of each term with the query context is examined by considering its relationship to other terms in the query. 

> 1https://huggingface.co/google/bert ~~u~~ ncased ~~L~~ -12 ~~H~~ -768 ~~A~~ -12 

8 

To model these relationships, a graph Gc = (Vc, Ec) is constructed, where Vc = {t1, t2, . . . , tm} represents the terms in the query, and Ec contains edges weighted by the relative correlation between terms. The weight of an edge between two terms ti and tj is defined as RC(ti | tj), which quantifies the correlation of ti relative to tj in the context of the query. This is computed as 


![](prepared/A_Retrieval_Model_with_Contextual_Correlation_Anal/images/A_Retrieval_Model_with_Contextual_Correlation_Anal.pdf-0010-01.png)


If RC(ti | tj) > 1, then term ti is more strongly correlated with the context vector than tj, indicating higher relatedness with query context. Conversely, if RC(ti | tj) < 1, term tj has a stronger correlation with the context vector. And, when RC(ti | tj) ≈ 1, both terms exhibit similar importance within the context. 

The final centrality weight σti for each term is computed iteratively using power iteration as 


![](prepared/A_Retrieval_Model_with_Contextual_Correlation_Anal/images/A_Retrieval_Model_with_Contextual_Correlation_Anal.pdf-0010-04.png)


This recursive nature of this computation allows the centrality score of each term to be influenced by its relative importance to all other terms in the query. The initial value of σti is set to 1 for all terms, and the scores are iteratively updated. The power iteration is a crucial step in this process. It allows the centrality scores to stabilize over multiple iterations, ensuring that each term’s weight is appropriately adjusted based on its relationship to the others in the query. 

To ensure convergence, the process is repeated for 20 iterations [47], which has been found sufficient for the query length used, based on experimental results. After each iteration, the scores are normalized to ensure their total sum equals 1, providing a balanced weighting scheme. 

## 3.5 Alleviating Non-Informative Matches 

As discussed in the third key principle, many terms appear in documents not because they are relevant to the document’s specific topic, but due to their general distribution across the collection. These are considered non-informative terms. Verbose queries, which often include numerous extraneous terms, have a higher chance of matching such non-informative terms in documents, thereby reducing retrieval effectiveness. 

To address this issue, we primarily estimate the information content of each term t as 


![](prepared/A_Retrieval_Model_with_Contextual_Correlation_Anal/images/A_Retrieval_Model_with_Contextual_Correlation_Anal.pdf-0010-10.png)


where Prob(t ∈ D) =[n] N[t][denotes][the][probability][of][term][t][,][with][n][t][representing] the document frequency of t, and N the total number of documents in the collection. This assigns lower values to the non-informative terms. Thus, using it as a weight can improve the retrieval effectiveness by prioritizing matching with informative terms. 

9 

However, since verbose queries contain many such non-informative terms, their cumulative effect can still reduce retrieval effectiveness. To mitigate this, we normalize the information content of each term relative to the cumulative information content of the entire query, while introducing a non-linear adjustment that favors highly informative terms and further suppresses less informative ones. Specifically, we define the adjusted weight as 


![](prepared/A_Retrieval_Model_with_Contextual_Correlation_Anal/images/A_Retrieval_Model_with_Contextual_Correlation_Anal.pdf-0011-01.png)


where the cumulative information content of the query Q is 


![](prepared/A_Retrieval_Model_with_Contextual_Correlation_Anal/images/A_Retrieval_Model_with_Contextual_Correlation_Anal.pdf-0011-03.png)


and β is a tunable scaling parameter. 

Final Term Weight: 

The final weight of each query term qi ∈ C(Q) is computed as 


![](prepared/A_Retrieval_Model_with_Contextual_Correlation_Anal/images/A_Retrieval_Model_with_Contextual_Correlation_Anal.pdf-0011-07.png)


This weight αqi is used in Eq. 4. This formulation ensures that terms are weighted based on both their contextual importance within the query and their information content within the document collection. 

## 4 Experimental Setup 

Throughout this article, the proposed method is referred to as RCC. This section outlines the datasets used for experimentation. It also describes the retrieval system setup and the selected hyperparameters used during the implementation of RCC. Additionally, we also present the baseline methods here against which RCC is compared. 

## 4.1 Datasets and Retrieval System 

To validate the proposed approach, the experiments are conducted using multiple datasets, as summarized in Table 1. For the TREC678 and GOV2 collections, both the description and narrative fields of the topics are utilized for evaluation. However, since only the description field is available for ClueWeb09B, it is exclusively used for our analysis. 

Table 1: Test collection statistics. 

||Table 1:|Test collecti|on statist|ics.|ics.|
|---|---|---|---|---|---|
|Dataset|Collection Type|# Docs|Topics|Query Length (# terms)<br>description<br>narrative||
|TREC678|newswire|528,155|301-450|8.7 ± 4.6|25.5 ± 13.2|
|GOV2|homogeneous web|25,205,179|701-850|5.9 ± 2.5|25.6 ± 11.3|
|Clueweb09B|heterogeneous web|50,220,423|1-200|5.2 ± 1.9|-|



10 

The document collections are indexed, and posting lists are retrieved using the Indri[2] [54] search engine. To ensure consistency, all documents and queries are preprocessed by removing stopwords using a standard list of 731 stopwords and applying the Porter stemming algorithm. 

## 4.2 Selected Hyperparameters 

The proposed weighting method involves two hyperparameters, i.e., d and β. To determine effective values, we vary d from −5000 to 5000 in increments of 100 and evaluate retrieval performance across all datasets. We observe that near-optimal performance consistently occurs when d lies in the range of 3000 to 5000 for all three datasets. Similarly, we experiment with β values ranging from 5 to 20 in increments of 2. We find that setting β between 7 and 10 yields stable and effective performance across datasets and query types. Based on these observations, we fix d = 4000 and β = 8 in all subsequent experiments, as this combination consistently provides strong performance. 

## 4.3 Baselines 

We compare the performance of our proposed method against nine baselines from four different categories: unsupervised traditional baselines, two-stage unsupervised baselines, fully supervised baselines, and recent neural models. 

## Unsupervised Baselines: 

We compare our method with the two traditional models, (i) the standard bag-ofwords query likelihood Dirichlet language model (QL) [59] and (ii) the Markov Random Field-based Sequential Dependence Model (SD) [44], along with two unsupervised term reweighting approaches, (iii) TA [47] and (iv) DSW [33]. Both TA and DSW estimate the weight of query terms utilizing a ranked list. For all the experiments, we employ QL as the primary ranking function. 

In our experiments, we set the smoothing parameter (µ) of the Dirichlet smoothed language model to 1000. SD encompasses three parameters (λT , λO, λU ), which we fix at 0.85, 0.1, and 0.05, respectively, as reported to be optimal in the original paper [44]. Furthermore, following the recommendation in the original paper, we fix the regulated idf factor for TA to 10 and set the values of K and L for DSW to 0.9 and 4. 

## Supervised Baselines: 

We take three supervised models, such as (v) KC [4], (vi) WSD [5], and (vii) deepTR [60]. We use the weights for TREC678 and GOV2 that are provided by the authors [4] for KC. However, the KC results for ClueWeb09B can not be reported as they did not publish the queries for ClueWeb09B. We do not implement the WSD model but use results from [47] (only NDCG@20 is mentioned). And, we implement DeepTR on our own and report the results, following the parameters reported in their paper. 

> 2http://www.lemurproject.org/indri/ 

11 

## Neural Retrieval Models: 

Recent advancements in neural retrieval models have significantly improved retrieval performance by capturing contextual nuances in queries and documents. To ensure a comprehensive comparison across all major model categories, we include various retrieval model types from both sparse (UniCOIL [39], DeepCT [13]) and dense (ANCE [17], ColBERT [34]) retrieval models that are able to perform full collection ranking. Since RCC is fully unsupervised and uses pre-trained BERT embeddings to generate dense representations, we adopt a zero-shot retrieval setup for all neural baselines using Pyserini[3] [40]. The retrieval is performed using publicly available checkpoints of UniCOIL, ColBERT, and ANCE. In our experiments, documents are segmented into overlapping passages of size 150 with a stride of 75, following prior studies [42, 57], and the MaxP aggregation is used to produce the final ranked list of documents. For DEEPCT [13], which is not yet supported in Pyserini, we report results from the original paper. 

## 5 Experimental Results and Discussions 

In this section, we present the experimental results and discuss the effectiveness of the proposed approach. We measure retrieval effectiveness using the Normalized Discounted Cumulative Gain (NDCG) [31] and Expected Reciprocal Rank (ERR) [10]. We estimate statistically significant performance differences using a paired t-test at a 95% confidence level (p < 0.05). 

## 5.1 Comparison with unsupervised baselines 

Table 2, and Table 3 show that the proposed approach outperforms all unsupervised baselines in terms of NDCG and ERR for description queries, with statistically significant improvements over QL and SD on all three datasets. The proposed approach also exhibits significant improvement in all metrics compared to TA and DSW on GOV2, and outperforms TA and DSW in all metrics on ClueWeb09B. For narrative queries, RCC consistently outperforms all unsupervised baselines QL, SD, TA, and DSW with a huge margin in terms of NDCG and ERR, and the shown improvements are statistically significant. The narrative queries tend to contain more extraneous terms, and RCC shows larger improvement for the narrative query. This observation can help in concluding that RCC effectively mitigates the impact of matching of these extraneous terms on the ranking function. 

The results suggest that improvement of RCC is less on TREC678 compared to larger collections like GOV2 and ClueWeb09B. A possible reason is that since the collection size of TREC678 is smaller than that of GOV2 and ClueWeb09B, the number of relevant documents within the top 20 retrieved documents is higher and thus, the methods such as TA and DSW generate better weights for TREC678. This is the major disadvantage of TA and DSW, i.e., estimating good quality term weights is challenging if the initial ranker fails to retrieve a sufficient number of relevant documents [47]. 

> 3https://github.com/castorini/pyserini 

12 

Table 2: Retrieval effectiveness comparison with all the unsupervised baselines for description queries. The integer superscripts denote that the proposed approach is significantly better (p < 0.05) than the ith baseline. The baselines are numbered from 1 (top) to 4 (bottom). The best result in each category is boldfaced. 

||TREC678 (description)|TREC678 (description)||
|---|---|---|---|
||NDCG@10|NDCG@20|ERR@10|
|QL|0.388|0.354|0.385|
|SDM|0.418|0.372|0.408|
|TA|0.421|0.383|0.400|
|DSW|0.428|0.392|0.408|
|RCC|0.43712|0.400123|0.41612|
||GOV2 (description)|||
||NDCG@10|NDCG@20|ERR@10|
|QL|0.430|0.427|0.397|
|SDM|0.455|0.452|0.436|
|TA|0.434|0.437|0.420|
|DSW|0.442|0.442|0.419|
|RCC|0.4781234|0.4721234|0.4481234|
||Clueweb09B (description)|||
||NDCG@10|NDCG@20|ERR@10|
|QL|0.183|0.188|0.162|
|SDM|0.188|0.206|0.174|
|TA|0.194|0.199|0.169|
|DSW|0.200|0.201|0.181|
|RCC|0.21112|0.2231234|0.193123|



Table 3: Retrieval effectiveness comparison with all the unsupervised baselines for narrative queries. The integer superscripts denote that the proposed approach is significantly better (p < 0.05) than the ith baseline. The baselines are numbered from 1 (top) to 4 (bottom). The best result in each category is boldfaced. 

||TREC678 (narrative)|TREC678 (narrative)||
|---|---|---|---|
||NDCG@10|NDCG@20|ERR@10|
|QL|0.300|0.270|0.302|
|SD|0.314|0.283|0.322|
|TA|0.338|0.310|0.327|
|DSW|0.337|0.308|0.331|
|RCC|0.3811234|0.3541234|0.3891234|
||GOV2|(narrative)||
||NDCG@10|NDCG@20|ERR@10|
|QL|0.335|0.321|0.342|
|SD|0.361|0.343|0.360|
|TA|0.356|0.345|0.317|
|DSW|0.362|0.362|0.322|
|RCC|0.4231234|0.4181234|0.4221234|



On the other hand, RCC is not reliant on top-ranked documents to estimate term weights, and it can produce high-quality term weights independently. Additionally, RCC demonstrates significant improvement, particularly in larger collections. 

13 

Table 4: Retrieval effectiveness comparison with all the Supervised baselines for description queries. The integer superscripts denote that the proposed approach is significantly better (p < 0.05) than the ith baseline. The baselines are numbered from 5 (top) to 8 (bottom). The best result in each category is boldfaced. 

|er (p <0.05) th<br>tom). The best|an the ith baseline. The b<br> result in each category is|an the ith baseline. The b<br> result in each category is|aselines are<br> boldfaced.|
|---|---|---|---|
||TREC678 (description)|||
||NDCG@10|NDCG@20|ERR@10|
|KC|0.404|0.374|0.398|
|WSD|-|0.416|-|
|DEEPTR-BOW|0.438|0.403|0.418|
|DEEPTR-SD|0.438|0.412|0.430|
|RCC|0.4375|0.4005|0.4165|
||GOV2 (description)|||
||NDCG@10|NDCG@20|ERR@10|
|KC|0.444|0.440|0.426|
|WSD|-|0.439|-|
|DEEPTR-BOW|0.429|0.425|0.416|
|DEEPTR-SD|0.451|0.446|0.433|
|RCC|0.47857|0.47257|0.44857|
|Clueweb09B (description)||||
||NDCG@10|NDCG@20|ERR@10|
|KC|-|-|-|
|WSD|-|0.188|-|
|DEEPTR-BOW|0.206|0.216|0.179|
|DEEPTR-SD|0.204|0.214|0.186|
|RCC|0.211|0.223|0.193|



Table 5: Retrieval effectiveness comparison with the supervised baselines for narrative queries. The integer superscripts denote that the proposed approach is significantly better (p < 0.05) than the ith baseline. The baselines are numbered from 7 (top) to 8 (bottom). The best result in each category is boldfaced. 

|||TREC678 (narrative)|TREC678 (narrative)||
|---|---|---|---|---|
|||NDCG@10|NDCG@20|ERR@10|
|DeepTR|(bow)|0.345|0.321|0.345|
|DeepTR|(sd)|0.356|0.324|0.352|
|RCC||0.38178|0.35478|0.38978|
|||GOV2 (narrative)|||
|||NDCG@10|NDCG@20|ERR@10|
|DeepTR|(bow)|0.379|0.372|0.331|
|DeepTR|(sd)|0.383|0.380|0.342|
|RCC||0.42378|0.41878|0.42278|



## 5.2 Comparison with supervised baselines 

We extend the comparison to four supervised baselines, such as KC [4], WSD [5], deepTR-BOW, and deepTR-SD [60] and all the experimental findings for description and narrative queries are presented in Table 4 and Table 5, respectively. Table 4 shows that RCC performs significantly better than KC on TREC678 and GOV2 in 

14 

Table 6: Retrieval effectiveness comparison with the neural baselines for description queries. The alphabet superscripts denote that the proposed approach is significantly better (p < 0.05) than the baseline. The best result in each category is boldfaced. 

|05) than the baseline. The best result in each|05) than the baseline. The best result in each|05) than the baseline. The best result in each|category is|
|---|---|---|---|
|TREC678 (description)||||
||NDCG@10|NDCG@20|ERR@10|
|ColBERT|0.376|0.345|0.393|
|ANCE|0.389|0.368|0.401|
|UniCOIL|0.373|0.344|0.383|
|RCC|0.437cau|0.400cau|0.416cau|
|GOV2 (description)||||
||NDCG@10|NDCG@20|ERR@10|
|BOW-DeepCT-Query|-|0.430 [13]|-|
|SDM-DeepCT-Query|-|0.446 [13]|-|
|ColBERT|0.433|0.412|0.411|
|ANCE|0.448|0.427|0.413|
|UniCOIL|0.369|0.367|0.363|
|RCC|0.478cau|0.472cau|0.448cau|



all metrics where the results for the description query are reported. Additionally, RCC improves over WSD on GOV2 and ClueWeb09B, although there is a marginal variation on TREC678. When we compare RCC to DEEPTR-BOW and DEEPTR-SD, we find that DEEPTR performs better than RCC on TREC678 for description query only. On the other hand, RCC exhibits a considerable improvement in performance over both DEEPTR-BOW and DEEPTR-SD on GOV2, with statistically significant differences observed with DEEPTR-BOW. On ClueWeb09B, RCC outperforms both DEEPTR-BOW and DEEPTR-SD, but the difference is not statistically significant. RCC outperforms both DEEPTR-BOW and DEEPTR-SD on TREC678 and GOV2, showing statistically significant improvements in all metrics. However, we could not compare its performance with KC and WSD for narrative queries as Bendersky and Croft [4] cannot publish the weights and Paik and Oard [47] did not report the results for narrative queries. 

Additionally, RCC demonstrates more improvement as query length increases, consistent with earlier findings. These results suggest that the proposed unsupervised RCC yields significant improvements over the majority of supervised baselines. Thus, it can be suitable when the availability of training queries is limited. 

## 5.3 Comparison with Neural Retrieval Models 

We compare RCC against recent neural retrieval models. The results, presented in Table 6, highlight RCC’s effectiveness and its competitive performance relative to strong neural baselines. Since RCC operates in a fully unsupervised manner and uses pre-trained BERT embeddings to generate dense representations, we adopt a zero-shot retrieval setup for all neural models using Pyserini[4] [40]. Specifically, we construct indexes for the TREC678 and GOV2 collections and perform retrieval using publicly 

> 4https://github.com/castorini/pyserini 

15 

available pre-trained checkpoints of UniCOIL, ColBERT, and ANCE. Due to the substantial size of the ClueWeb09B collection, we are unable to construct a complete index and thus omit its results. Additionally, as several pre-trained neural models impose a maximum query length of 32 tokens, we exclude narrative queries exceeding this limit to avoid truncating important terms, which could negatively affect retrieval performance. For DEEPCT [13], which is not yet integrated with Pyserini, we report results directly from the original publication. 

The results in Table 6 show that RCC significantly outperforms these neural models. This demonstrates that the proposed method effectively estimates the centrality scores of query terms, and when these scores are integrated into the SDM framework, the ranking function is able to prioritize core terms, thereby enhancing retrieval effectiveness. These findings highlight that, even without any training data, a traditional model with proper term weighting can outperform advanced neural models in zero-shot retrieval scenarios. 

## 5.4 Effectiveness with Query Length 

To further investigate the effectiveness of RCC across different query lengths, we experiment with title (very short keyword-based), description (medium to long natural language), and narrative (very long) fields of topics as queries, and estimate the retrieval effectiveness of two models, namely SDM and RCC. The results are shown in Table 7. The results indicate that RCC demonstrates a more pronounced improvement over SDM for narrative queries, which have significantly longer lengths. Improvements on description queries are substantial, and for title queries, where the queries contain mainly keywords based on very short texts, the improvement of RCC over SDM is negligible. This is because title queries contain few extraneous terms, so the effect of prioritizing core terms in the ranking function is limited. However, it is also worth noting that although the improvement is smaller for shorter queries, RCC never falls behind SDM. This confirms that RCC works effectively across different query lengths. 

Table 7: Analysis of retrieval effectiveness of RCC across queries of varying length. 

|able 7:||Analysis of retrieval e|Analysis of retrieval e|Analysis of retrieval e|f|ectiveness of RCC acro|ectiveness of RCC acro|ectiveness of RCC acro|s|s queries of varying lengt|s queries of varying lengt|
|---|---|---|---|---|---|---|---|---|---|---|---|
|||TREC678 (title)<br>NDCG@10<br>ERR@10||||TREC678 (description)<br>NDCG@10<br>ERR@10||||TREC678 (narrative)<br>NDCG@10<br>ERR@10||
|||||||||||||
|SDM||0.455||0.429||0.418||0.408||0.314|0.322|
|RCC||0.458||0.431||0.437||0.416||0.381|0.389|
|||GOV2 <br>NDCG@10||(title)<br>ERR@10||GOV2 (description)<br>NDCG@10<br>ERR@10||||GOV2 (narrative)<br>NDCG@10<br>ERR@10||
|||||||||||||
|SDM||0.505||0.483||0.455||0.436||0.361|0.360|
|RCC||0.506||0.487||0.478||0.448||0.423|0.422|
|||||||||||||
|||||ClueWeb09B (title)<br>NDCG@10<br>ERR@10||||ClueWeb09B (description)<br>NDCG@10<br>ERR@10||||
|||SDM||0.191||0.163||0.188||0.174||
|||RCC||0.193||0.171||0.211||0.193||



16 

Table 8: Variation of retrieval effectiveness of RCC with the variation of embedding techniques. 

|ble 8: Variation of retrieval efectiveness of RCC with the variation of embedd<br>hniques.|ble 8: Variation of retrieval efectiveness of RCC with the variation of embedd<br>hniques.|etrieval efectiveness of RCC wit|h the variation of embedd|
|---|---|---|---|
|TREC678 (description)<br>TREC678 (narrative)<br>NDCG@10<br>ERR@10<br>NDCG@10<br>ERR@10<br>SDM<br>0.418<br>0.408<br>0.314<br>0.322<br>RCC (BERT)<br>0.437<br>0.416<br>0.381<br>0.389<br>RCC (GLOVE+SIF)<br>0.438<br>0.418<br>0.378<br>0.380<br>GOV2 (description)<br>GOV2 (narrative)<br>NDCG@10<br>ERR@10<br>NDCG@10<br>ERR@10<br>SDM<br>0.455<br>0.436<br>0.361<br>0.360<br>RCC (BERT)<br>0.478<br>0.448<br>0.423<br>0.422<br>RCC (GLOVE+SIF)<br>0.479<br>0.450<br>0.412<br>0.408<br>ClueWeb09B (description)<br>NDCG@10<br>ERR@10<br>SDM<br>0.188<br>0.174<br>RCC (BERT)<br>0.211<br>0.193<br>RCC (GLOVE+SIF)<br>0.213<br>0.195||TREC678 (description)<br>NDCG@10<br>ERR@10|TREC678 (narrative)<br>NDCG@10<br>ERR@10|
||SDM<br>RCC (BERT)<br>RCC (GLOVE+SIF)|0.455<br>0.436<br>0.478<br>0.448<br>0.479<br>0.450|0.361<br>0.360<br>0.423<br>0.422<br>0.412<br>0.408|
||ClueWeb09B (description)<br>NDCG@10<br>ERR@10<br>SDM<br>0.188<br>0.174<br>RCC (BERT)<br>0.211<br>0.193<br>RCC (GLOVE+SIF)<br>0.213<br>0.195|||



## 5.5 Effectiveness across Embedding Techniques 

To assess the effectiveness of RCC across different dense representation techniques, we experiment with the GloVE embedding technique along with BERT. BERT generates contextualized embeddings for each term, while, GloVe provides static word-level embeddings that do not change with context. To adapt these static embeddings for sentence-level representations, we employ the SIF sentence embedding technique [2], which constructs dense query vectors by averaging word embeddings while downweighting the influence of frequent or generic words. The results are shown in Table 8. It is shown that RCC consistently outperforms the SDM baseline with both embedding strategies. This finding highlights the generality of the proposed approach. Even with pre-transformer-era embeddings such as GloVe, RCC is able to significantly enhance retrieval performance, confirming its utility as a versatile and embedding-agnostic solution for improving ranking quality. 

## 6 Conclusion 

In this work, we propose a fully unsupervised, single-pass retrieval model tailored to improve the effectiveness of document retrieval for verbose queries. The method estimates the importance of each query term by analyzing its contextual correlation with the overall query representation. A fully connected graph is constructed over query terms, where edge weights reflect their relative contextual association. Centrality scores are computed using power iteration over this graph structure. Additionally, a specificity-based term weighting component is introduced for penalizing the matches with non-informative document terms. The combined weights are integrated into a modified Markov Random Field Sequential Dependence Model (SDM) for final ranking. 

17 

Extensive experiments conducted on multiple benchmark collections demonstrate that the proposed method consistently outperforms traditional unsupervised baselines and achieves competitive performance relative to supervised approaches, all while requiring no labeled training data. Notably, it surpasses several neural retrieval models in zero-shot scenarios. The model delivers substantial gains for longer queries and modest improvements for shorter ones, but never underperforms the backbone retrieval model SDM. Furthermore, it maintains stable retrieval effectiveness across different embedding types, such as GloVe and BERT, showcasing its embedding-agnostic behavior. These findings indicate that the proposed model is both effective and practically deployable even in low-resource retrieval environments. 

Funding. No funds, grants, or other financial support were received for conducting this study. 

## References 

- [1] Amati G, Van Rijsbergen CJ (2002) Probabilistic models of information retrieval based on measuring the divergence from randomness. ACM Transactions on Information Systems (TOIS) 20(4):357–389 

- [2] Arora S, Liang Y, Ma T (2017) A simple but tough-to-beat baseline for sentence embeddings. In: International conference on learning representations 

- [3] Balaneshin-kordan S, Kotov A (2017) Embedding-based query expansion for weighted sequential dependence retrieval model. In: Proceedings of the 40th International ACM SIGIR Conference on Research and Development in Information Retrieval, pp 1213–1216 

- [4] Bendersky M, Croft WB (2008) Discovering key concepts in verbose queries. In: Proceedings of the 31st Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, SIGIR ’08, p 491–498 

- [5] Bendersky M, Metzler D, Croft WB (2010) Learning concept importance using a weighted dependence model. In: Proceedings of the Third ACM International Conference on Web Search and Data Mining, WSDM ’10, p 31–40 

- [6] Bendersky M, Metzler D, Croft WB (2011) Parameterized concept weighting in verbose queries. In: Proceedings of the 34th International ACM SIGIR Conference on Research and Development in Information Retrieval, SIGIR ’11, p 605–614 

- [7] Bendersky M, Metzler D, Croft WB (2012) Effective query formulation with multiple information sources. In: Proceedings of the fifth ACM international conference on Web search and data mining, pp 443–452 

- [8] Biega AJ, Schmidt J, Roy RS (2020) Towards query logs for privacy studies: On deriving search queries from questions. In: European Conference on Information Retrieval, pp 110–117 

18 

- [9] Bilal D, Gwizdka J (2018) Children’s query types and reformulations in google search. Information Processing & Management 54(6):1022–1041 

- [10] Chapelle O, Metlzer D, Zhang Y, et al (2009) Expected reciprocal rank for graded relevance. In: Proceedings of the 18th ACM conference on Information and knowledge management, pp 621–630 

- [11] Chen RC, Gallagher L, Blanco R, et al (2017) Efficient cost-aware cascade ranking in multi-stage retrieval. In: Proceedings of the 40th International ACM SIGIR Conference on Research and Development in Information Retrieval, pp 445–454 

- [12] Dai Z, Callan J (2019) Deeper text understanding for ir with contextual neural language modeling. In: Proceedings of the 42nd International ACM SIGIR Conference on Research and Development in Information Retrieval, pp 985–988 

- [13] Dai Z, Callan J (2020) Context-aware term weighting for first stage passage retrieval. In: Proceedings of the 43rd International ACM SIGIR conference on research and development in Information Retrieval, pp 1533–1536 

- [14] Dai Z, Xiong C, Callan J, et al (2018) Convolutional neural networks for soft-matching n-grams in ad-hoc search. In: Proceedings of the eleventh ACM international conference on web search and data mining, pp 126–134 

- [15] Devlin J, Chang MW, Lee K, et al (2018) Bert: Pre-training of deep bidirectional transformers for language understanding. arXiv preprint arXiv:181004805 

- [16] Di Buccio E, Melucci M, Moro F (2014) Detecting verbose queries and improving information retrieval. Information Processing & Management 50(2):342–360 

- [17] Fang H, Tao T, Zhai C (2004) A formal study of information retrieval heuristics. In: Proceedings of the 27th annual international ACM SIGIR conference on Research and development in information retrieval, pp 49–56 

- [18] Formal T, Piwowarski B, Clinchant S (2021) A white box analysis of colbert. In: Advances in Information Retrieval: 43rd European Conference on IR Research, ECIR 2021, Virtual Event, March 28–April 1, 2021, Proceedings, Part II 43, Springer, pp 257–263 

- [19] Ganguly D, Roy D, Mitra M, et al (2015) Word embedding based generalized language model for information retrieval. In: Proceedings of the 38th international ACM SIGIR conference on research and development in information retrieval, pp 795–798 

- [20] Gao L, Dai Z, Callan J (2020) Modularized transfomer-based ranking framework. arXiv preprint arXiv:200413313 

19 

- [21] Gao L, Dai Z, Chen T, et al (2021) Complement lexical retrieval model with semantic residual embeddings. In: Advances in Information Retrieval: 43rd European Conference on IR Research, ECIR 2021, Virtual Event, March 28–April 1, 2021, Proceedings, Part I 43, Springer, pp 146–160 

- [22] Geigle G, Pfeiffer J, Reimers N, et al (2022) Retrieve fast, rerank smart: Cooperative and joint approaches for improved cross-modal retrieval. Transactions of the Association for Computational Linguistics 10:503–521 

- [23] Guo J, Fan Y, Ai Q, et al (2016) A deep relevance matching model for adhoc retrieval. In: Proceedings of the 25th ACM international on conference on information and knowledge management, pp 55–64 

- [24] Guo J, Cai Y, Fan Y, et al (2022) Semantic models for the first-stage retrieval: A comprehensive review. ACM Transactions on Information Systems (TOIS) 40(4):1–42 

- [25] Gupta M, Bendersky M (2015) Information retrieval with verbose queries. In: Proceedings of the 38th International ACM SIGIR Conference on Research and Development in Information Retrieval, pp 1121–1124 

- [26] Guy I (2016) Searching by talking: Analysis of voice queries on mobile web search. In: Proceedings of the 39th International ACM SIGIR conference on Research and Development in Information Retrieval, pp 35–44 

- [27] Guy I (2018) The characteristics of voice search: Comparing spoken with typedin mobile web search queries. ACM Transactions on Information Systems (TOIS) 36(3):1–28 

- [28] Hofst¨atter S, Althammer S, Schr¨oder M, et al (2020) Improving efficient neural ranking models with cross-architecture knowledge distillation. arXiv preprint arXiv:201002666 

- [29] Hofst¨atter S, Lin SC, Yang JH, et al (2021) Efficiently teaching an effective dense retriever with balanced topic aware sampling. In: Proceedings of the 44th International ACM SIGIR Conference on Research and Development in Information Retrieval, pp 113–122 

- [30] Huang PS, He X, Gao J, et al (2013) Learning deep structured semantic models for web search using clickthrough data. In: Proceedings of the 22nd ACM international conference on Information & Knowledge Management, pp 2333–2338 

- [31] J¨arvelin K, Kek¨al¨ainen J (2002) Cumulated gain-based evaluation of ir techniques. ACM Transactions on Information Systems (TOIS) 20(4):422–446 

20 

- [32] Johnson J, Douze M, J´egou H (2019) Billion-scale similarity search with gpus. IEEE Transactions on Big Data 7(3):535–547 

- [33] Karisani P, Rahgozar M, Oroumchian F (2016) A query term re-weighting approach using document similarity. Information Processing & Management 52(3):478–489 

- [34] Khattab O, Zaharia M (2020) Colbert: Efficient and effective passage search via contextualized late interaction over bert. In: Proceedings of the 43rd International ACM SIGIR conference on research and development in Information Retrieval, pp 39–48 

- [35] Kumaran G, Allan J (2007) A case for shorter queries, and helping users create them. In: Human Language Technologies 2007: The Conference of the North American Chapter of the Association for Computational Linguistics; Proceedings of the Main Conference, pp 220–227 

- [36] Kumaran G, Carvalho VR (2009) Reducing long queries using query quality predictors. In: Proceedings of the 32nd international ACM SIGIR conference on Research and development in information retrieval, pp 564–571 

- [37] Lease M (2009) An improved markov random field model for supporting verbose queries. In: Proceedings of the 32nd International ACM SIGIR Conference on Research and Development in Information Retrieval, SIGIR ’09, p 476–483 

- [38] Li X, Schijvenaars BJ, de Rijke M (2017) Investigating queries and search failures in academic search. Information processing & management 53(3):666–683 

- [39] Lin J, Ma X (2021) A few brief notes on deepimpact, coil, and a conceptual framework for information retrieval techniques. arXiv preprint arXiv:210614807 

- [40] Lin J, Ma X, Lin SC, et al (2021) Pyserini: A python toolkit for reproducible information retrieval research with sparse and dense representations. In: Proceedings of the 44th International ACM SIGIR Conference on Research and Development in Information Retrieval, pp 2356–2362 

- [41] Lin SH, Jan EE, Chen B (2011) Handling verbose queries for spoken document retrieval. In: 2011 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), IEEE, pp 5552–5555 

- [42] MacAvaney S, Yates A, Cohan A, et al (2019) Cedr: Contextualized embeddings for document ranking. In: Proceedings of the 42nd international ACM SIGIR conference on research and development in information retrieval, pp 1101–1104 

- [43] MacAvaney S, Nardini FM, Perego R, et al (2020) Efficient document re-ranking for transformers by precomputing term representations. In: Proceedings of the 43rd International ACM SIGIR Conference on Research and Development in 

21 

Information Retrieval, pp 49–58 

- [44] Metzler D, Croft WB (2005) A markov random field model for term dependencies. In: Proceedings of the 28th Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, SIGIR ’05, p 472–479 

- [45] Mikolov T, Sutskever I, Chen K, et al (2013) Distributed representations of words and phrases and their compositionality. arXiv preprint arXiv:13104546 

- [46] Nogueira R, Yang W, Cho K, et al (2019) Multi-stage document ranking with bert. arXiv preprint arXiv:191014424 

- [47] Paik JH, Oard DW (2014) A fixed-point method for weighting terms in verbose informational queries. In: Proceedings of the 23rd ACM International Conference on Conference on Information and Knowledge Management, CIKM ’14, p 131–140 

- [48] Paik JH, Parui SK, Pal D, et al (2013) Effective and robust query-based stemming. ACM Trans Inf Syst 31(4). https://doi.org/10.1145/2536736.2536738, URL https: //doi.org/10.1145/2536736.2536738 

- [49] Pal D, Ganguly D (2021) Effective query formulation in conversation contextualization: A query specificity-based approach. In: Proceedings of the 2021 ACM SIGIR International Conference on Theory of Information Retrieval, pp 177–183 

- [50] Pennington J, Socher R, Manning CD (2014) Glove: Global vectors for word representation. In: Proceedings of the 2014 conference on empirical methods in natural language processing (EMNLP), pp 1532–1543 

- [51] Podder D, Paik JH, Mitra P (2023) Neural language model based attentive term dependence model for verbose query (student abstract). In: Proceedings of the AAAI Conference on Artificial Intelligence, pp 16300–16301 

- [52] Roy D, Bhatia S, Mitra M (2019) Selecting discriminative terms for relevance model. In: Proceedings of the 42nd International ACM SIGIR Conference on Research and Development in Information Retrieval, pp 1253–1256 

- [53] Shen Y, He X, Gao J, et al (2014) Learning semantic representations using convolutional neural networks for web search. In: Proceedings of the 23rd international conference on world wide web, pp 373–374 

- [54] Strohman T, Metzler D, Turtle H, et al (2005) Indri: A language model-based search engine for complex queries. In: Proceedings of the international conference on intelligent analysis, Citeseer, pp 2–6 

- [55] Trippas JR (2021) Spoken conversational search: audio-only interactive information retrieval. In: ACM SIGIR Forum, pp 106–107 

22 

- [56] Xiong L, Xiong C, Li Y, et al (2020) Approximate nearest neighbor negative contrastive learning for dense text retrieval. arXiv preprint arXiv:200700808 

- [57] Yang Y, Qiao Y, Shao J, et al (2022) Lightweight composite re-ranking for efficient keyword search with bert. In: Proceedings of the Fifteenth ACM International Conference on Web Search and Data Mining, pp 1234–1244 

- [58] Zamani H, Croft WB (2016) Embedding-based query language models. In: Proceedings of the 2016 ACM international conference on the theory of information retrieval, pp 147–156 

- [59] Zhai C, Lafferty J (2004) A study of smoothing methods for language models applied to information retrieval. ACM Trans Inf Syst 22(2):179–214 

- [60] Zheng G, Callan J (2015) Learning to reweight terms with distributed representations. In: Proceedings of the 38th international ACM SIGIR conference on research and development in information retrieval, pp 575–584 

23 

