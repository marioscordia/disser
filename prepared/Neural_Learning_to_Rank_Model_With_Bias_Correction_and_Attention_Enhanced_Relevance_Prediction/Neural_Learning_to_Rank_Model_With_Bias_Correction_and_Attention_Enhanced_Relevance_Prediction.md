
![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0001-00.png)


Received 26 September 2025, accepted 22 October 2025, date of publication 27 October 2025, date of current version 7 November 2025. _Digital Object Identifier 10.1109/ACCESS.2025.3625652_ 

## Neural Learning to Rank Model With Bias Correction and Attention Enhanced Relevance Prediction 

## K. J. AMALA AND D. RAJESWARI 

Department of Data Science and Business Systems, School of Computing, College of Engineering and Technology, SRM Institute of Science and Technology, Chengalpattu, Kattankulathur, Tamil Nadu 603203, India Corresponding author: K. J. Amala (ak7858@srmist.edu.in) 

- **ABSTRACT** Click data has emerged as an essential tool for training learning-to-rank systems in various sectors, including web search, recommender systems, and digital advertising. This data is fundamentally noisy and biased due to factors such as position bias and contextual influences, including document presentation, title length, and previous click patterns. This paper introduces the Probabilistic Click Prediction Network Based on Attention (APCP), which estimates document relevance and observation bias in a unified, attention-enhanced neural architecture. It examines the impact of contextual features on the likelihood of user observation and click behavior in a series of simulated use cases. In order to parameterize the probability of an observation, our framework integrates both static document attributes and dynamic user behavior signals. Experimental simulations utilizing synthetic click data indicate that the suggested model significantly mitigates the effects of positional and contextual bias, hence enhancing generalization and the accuracy of click-through rate predictions. APCP is trained using the MSLR-WEB30K dataset with simulated clicks and is validated on actual datasets Yahoo Learning to Rank Challenge dataset and Yandex click logs.It is evaluated against six robust baselines.Across five use-case situations, APCP consistently surpasses the most robust baseline, Implicit Intention Network (IIN), attaining AUC improvements ranging from +6.2% to +19.9% (all p _<_ 0.001, Cohen’s d _>_ 0.89, indicating a substantial impact size). Comparable enhancements are noted in NDCG@10, MAP, and MRR, substantiating APCP’s capacity to improve ranking quality and reduce bias in the MSLR WEB-30k dataset.On Yahoo, APCP enhances NDCG@1, @3, @5, and @10 by +3.45% to +5.28% compared to IIN, while on Yandex, it realizes AUC, MAP, and MRR improvements of +3.55% to +4.68%. All enhancements are statistically significant (p _<_ 0.05). These findings indicate that APCP not only efficiently reduces bias but also generalizes from simulated to actual click data, surpassing robust baselines across many ranking criteria. APCP offers a resilient and scalable methodology for improving search and recommendation systems. 

- **INDEX TERMS** Bias correction, click models, click-through rate prediction, context-aware ranking, examination bias, learning to rank, neural networks, position bias, self-attention, two-tower model. 

## **I. INTRODUCTION** 

In web search, recommender systems, and digital advertising, user actions are a critical signal for learning to rank systems. Nevertheless, click data is inherently biased: position bias is a phenomenon in which users are inclined to click on higher-ranked results regardless of their relevance. 

The associate editor coordinating the review of this manuscript and approving it for publication was Adamu Murtala Zungeru . 

Furthermore, contextual biases, such as the length of the title, the number of inlinks and outlinks, the quality score, and historical click patterns, also influence click behavior. These biases generate substantial noise during the training of ranking models, resulting in a suboptimal generalization and a degraded user experience. Additionally, neglecting biases during the training process can result in ranking models learning incorrect patterns from the data. In order to resolve this issue, a variety of click models have been 

2025 The Authors. This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/ 

188399 

VOLUME 13, 2025 

K. J. Amala, D. Rajeswari: Neural Learning to Rank Model With Bias Correction 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0002-01.png)


proposed, which explicitly model user behavior to decouple true relevance from observed interactions. Moreover, click models make an effort to predict and clarify why users click on search results. Numerous click models incorporate an examination hypothesis: A user clicks on a document only if they scrutinize the document ( _Examitem_ = 1 ) and find it appealing ( _Attractitem_ = 1). Mathematically it can be represented as follows [1]: 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0002-03.png)


Position Based Model (PBM) [1] uses probability theory for combining both attractiveness and examination. ie, 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0002-05.png)



![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0002-06.png)


Thus, click probability is the product of how likely a user is to view a result at a position and how appealing the document is for the query. Two-Tower Model [2] is a new neural version of the old PBM that was used for click modeling and learning to rank (LTR). By using two independent neural networks, which are sometimes called towers, this architecture separates the relevance estimate from the bias (observation) modeling. Document or item relevancy to a given query is determined by Relevance Tower. The output of this tower shows the estimated logit or probability that the document is relevant to the query. The second tower, Bias Tower (also called Examination or Observation), models the examination bias. It figures out how likely it is that a user will see a document even if it is not relevant. Then, the two towers’ outputs are merged together to build a model to find the possibility of a click. There are a number of ways that this combo can work. One is multiplicative (ie, P(click) = P(examined) × P(relevant)), other is additive in the logit space, and another is Dot product of learned embeddings from both towers. The next step, which follows concatenation, is a prediction layer. TwoTower Model is an effective way to debias clicks and improve Click-Through Rate (CTR) prediction in real-world ranking systems because it is modular and lets you learn the relevance and bias components independently and together. Adding position as a clear feature during training is a common way for organizations to get around problems. Even though this approach is simple, it does not work well for online inference because the actual position of the suggested item is often unknown. In this case, a default position number is used instead, but different defaults can cause CTR predictions to be very different, which lowers the quality of online recommendations in the long run. A position-bias-aware learning (PAL) structure has been suggested as a way to get around this problem. PAL [3] works on the assumption that 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0002-08.png)


By taking further assumptions taken from [4], 

a) the visibility of an item is solely determined by its position (items that are at the head of the list are more likely to be observed) and 

b) clicking on an item is dependent upon its content, rather than its location, once it has been observed. 

Eqn. (3) can be written as 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0002-13.png)


So PAL tries to make CTR prediction work even when there is missing position information during online inference, but it still mostly looks at position as an outside input. This makes it harder for the model to understand the complex perceptual and environmental factors that affect users’ attention in addition to rank. People decide whether to look at or click on items in real-life search and recommendation situations based on more than just their rank. They are also influenced by how the items are presented visually and thematically, such as by the way the titles are formatted, the amount of information in the snippets, or how noticeable they are. The Multi-Feature Integration Model (MFIM) [5] builds on the Two-Tower framework by adding the ability for examination bias to depend on document representations in addition to position. This lets us see these more subtle, feature-driven parts of how people see things.Although the MFIM incorporates bias variable and it improves upon the Position-Based Model (PBM), it still has numerous major drawbacks. Firstly, it keeps the fundamental idea that the product of examination probability and relevance probability is the best way to break down clicks. User intent, document visibility, and contextual bias interact in complicated ways, and this factorization imposes a rigid framework that fails to represent this. Also, in systems like query auto-completion or route recommendation, users often interact with unobserved but relevant items or irrelevant but mistakenly clicked items. MFIM models only observed documents, therefore it cannot handle these cases. The model’s capacity to debiase is diminished in domains where media type and SERP height features are either absent or too noisy. Finally, MFIM can’t differentiate presentation-induced behavior from intrinsic user interest since it doesn’t handle relevance as a latent variable independent from the click signal. In light of these restrictions, we present a two-tower approach to debias data in a more versatile and generalizable way, one that can adapt to different bias sources and manage all click circumstances. 

Our work extends the existing ideas by looking into feature-aware models of examination bias in more depth. The Two-Tower design is augmented so that the bias tower is affected by both positional and non-positional contextual variables. This way, the model can make accurate CTR or click predictions even when rank information is missing or not reliable. This contextual modeling is done through a set of situations. Each scenario shows a different way that document features, ranking position, and user interaction signals work together to make a click. Our architecture 

188400 

VOLUME 13, 2025 

K. J. Amala, D. Rajeswari: Neural Learning to Rank Model With Bias Correction 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0003-01.png)


didn’t just concatenate towers in the model. The ultimate click probability is instead calculated in a principled way by integrating the relevance prediction with the bias transition probabilities. Our suggested model, the Probabilistic Click Prediction Network, is based on attention and probability. Within an end-to-end architecture, our methodology suggests a neural CTR model that is both self-attention-enhanced and bias-aware, able to jointly predict document relevance and user observation bias. 

Our model includes: 

- 1) A self-attention layer in the Input Module records interactions at the feature level. This helps the model better show complex signs of relevance between the user and the item. 

- 2) The bias module utilizes a versatile concatenation-based input layer that integrates several contextual information into a unifying representation. 

- 3) A click noise matrix that clearly shows observation bias based on position and other bias factors, like presentation traits or signals from user behavior. 

- 4) The click is determined by the network after it has taken into account the user item features, bias information, and position. 

A schematic diagram of the application scenario for the work is shown in Figure 1. 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0003-09.png)


**FIGURE 1.** Application scenario of the proposed APCP for debiasing in CTR prediction. Note:The framework consists of an offline training phase (relevance and bias modules) and an online inference phase (relevance module only), which outputs unbiased CTR predictions applied in scenarios such as search, ads ranking, route recommendation, and e-commerce. 

This paper makes the following key contributions to click-through rate prediction and LTR: 

- **Attention-Enhanced Relevance Modeling** : We develop a self-attention mechanism specifically designed for CTR prediction that captures context-sensitive feature interactions, overcoming the limitations of traditional feedforward approaches. 

- **Advanced Contextual Observation Model** : We contribute a novel observation model that dynamically combines multiple document-level attributes to simulate 

- realistic examination bias, extending beyond basic position-based click simulation. 

- **Novel Click Simulation Framework** : We introduce a cost-effective alternative to human relevance annotations through realistic click simulation that maintains real-world noise characteristics while enabling controlled experimentation. 

The remainder of the paper is structured in the following manner: Section II reviews related work. Section III discusses preliminaries. Section IV introduces proposed methodology. Section V details the experimental setting, and Section VI is about results and discussion, Section VII ablation, and finally, concludes the paper. 

## **II. RELATED WORK** 

Position bias has long plagued LTR and CTR prediction systems. Traditional click models consider a click is the sum of an examination probability and a relevance probability. Although simple, these models contain too many independence assumptions and do not explain how position, user, and document features interact in sophisticated ways. New technologies like the Deep Position-wise Interaction Network (DPIN) [6] use deep learning to predict how position, human context, and object attributes interact in complex, non-linear ways. To evaluate rankings, it gives PAUC, a position-wise AUC metric. The goal is to obtain position and feature-based click data with sophisticated behavior. Even though, this model does not clearly distinguish between the concepts of relevance and bias, instead representing click-through rate (CTR) as a direct result of item-position interactions.This fused representation restricts interpretability and complicates the differentiation between user interest and positional advantage in item clicks. Secondly, DPIN assumes that clicks are restricted to observed items, thereby omitting instances where users may engage with unobserved yet relevant content. This represents a limitation in practical contexts, including recommendation systems. The model is limited to position bias and does not accommodate other types of bias, such as visual layout, font size, or user-specific behaviors. 

The examination hypothesis is a key part of traditional click models. It says that users look at things in a certain order and that position alone determines the chance of seeing something. These ideas are correct for simple list-based interfaces, but they do not work well for modern interfaces with grid layouts, which are popular in recommender systems and e-commerce platforms. Here to help, new research like Cross-Positional Attention (XPA) [7] suggests a neural model that learns study bias through a way of paying attention. XPA records more detailed patterns of user behavior and works in a wide range of user interface settings because it models interactions across all displayed positions. But the major thing is that XPA is not clear how to tell the difference between bias signals and relevant signals at inference time. This makes the model harder to understand and control. 

188401 

VOLUME 13, 2025 

K. J. Amala, D. Rajeswari: Neural Learning to Rank Model With Bias Correction 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0004-01.png)


Its attention-based examination module needs to see the whole session context, which means it cannot be used in real-time inference situations where all possible items might not be available at the same time. XPA mostly deals with position-based bias and does not easily cover other types of bias, like bias based on title length or user behavior trends. Lastly, the model’s reliance on attention over position makes it harder to scale up for large-scale industrial uses. 

A two-tower form is often used in real-world Unbiased LTR (ULTR) systems. The article [8] delves into a two-tower design in bias-free learning to rank, with an emphasis on disentangling bias from relevance. The authors initially identify a significant issue where the bias tower and relevance tower can be confused due to genuine relevance. Documents being placed are established by the preceding production model’s logging policy, which provides relevant information. This association may negatively impact relevance tower performance. The authors propose gradient reversal and observation dropout to better distinguish relevance and bias to reduce negative confounding effects. Using deep learning to boost search ranks was a major update that Airbnb [9] made to their products. To help customers make successful bookings, the Journey Ranker model implemented a multi-task architecture that takes use of intermediate visitor activities and uses contextual information to strike a compromise between hosts’ and guests’ preferences. The ranking model is modified by including position as a control variable. The relevance prediction is regularized down using dropout to make it less reliant on the position feature. 

The work by Le Yan et al. [10] explores the shortcomings of current two-tower models in ULTR and suggests alternative approaches such as Mixture Expectation-Maximization and embedding interaction to address the wide range of user behaviors observed in real-world datasets. ULTR approaches are commonly utilized; however, new empirical research disputes their efficacy. The study that employed the BaiduULTR [11], the largest public collection of user click logs and expert relevance annotations, stands out. The writers of this work extensively reviewed and expanded on previous testing. Despite enhanced feature representation and loss functions, older ULTR techniques did not consistently outperform simple baselines like BM25 in annotation-based measures. Despite their strength, click-based models performed poorly against expert-labeled relevance. This suggests that hits and relevancy are not optimized together. These results demonstrate the shortcomings of click modeling. This paper also shows that better methods are needed that operate better with human judgment or adjust for inaccurate user feedback. This is why probabilistic simulation scenarios and modeled click and observation behaviors with uncertainty are being used. 

In display advertising, in contrast to search, people do not explicitly indicate what they want. The system must infer user interests based on their previous behaviors. The Deep Interest Network (DIN) [12] is a model developed to 

enhance CTR prediction in display advertising when users’ intents remain implicit. DIN presents a local activation unit that dynamically modifies the user interest representation according to the relevance of a particular advertisement. This article also indicates that LSTM-based modeling was ineffective in these cases due to erratic and non-sequential user behaviors. PNNs [13] are designed to improve user response prediction utilizing multi-field categorical data for online advertising and recommender systems. These networks solve high-dimensional sparse data difficulties induced by one-hot encoding. PNN has three layers: embedding for distributed categorical data processing, product for field-to-field interaction capture, and completely connected for high-order feature interaction exploration. PNNs can recognize complex patterns and improve prediction accuracy due to their design. Although PNNs improve user response prediction, they have significant drawbacks. Model architectural complexity increases computational needs, and training these models requires large-scale data, which may limit their utility in data-poor scenarios. Tuning is needed since product and embedding layers affect performance in different datasets and applications. By combining factorization machines and deep learning, the DeepFM [14] model improves CTR prediction. This hybrid approach models simple and complex feature interactions without considerable feature engineering. The model’s ‘‘wide’’ and ‘‘deep’’ components share input, improving its efficiency and efficacy in online advertising and recommender systems. DeepFM displays promising results, but some researchers believe its prediction powers may be restricted by input data quality and feature representation biases. Further enhancements may improve its predictive abilities. 

Another work named FusionMatter [15] introduces a deep neural network architecture, aimed for enhancing CTR prediction by effectively capturing intricate feature interactions among users, items, and contextual factors such as position. But this fails to distinctly differentiate bias (e.g., position bias) from relevance, complicating the isolation of genuine user interest from presentation effects. The model functions as a opaque system due to its dense and layered fusion architecture. Interpreting or diagnosing the specific components of the input (e.g., user characteristics, position, item attributes) that affect predictions is challenging, hence constraining explainability. DLF (Deep Latent Fusion) [16] is a click-through rate prediction model that learns distinct latent vectors for users, objects, and contextual information such as device type, time, and position. It employs a multi-branch encoder to integrate latent representations in a systematic and disentangled manner. It also seeks to maintain the individuality of various feature groups during fusion. DLF integrates contextual data with user-item embeddings; nonetheless, it does not represent bias as an independent probabilistic element. DLF does not replicate the click-generation process for Clicked but irrelevant and Not clicked but relevant scenarios. Despite DLF’s efforts to maintain feature structure 

188402 

VOLUME 13, 2025 

K. J. Amala, D. Rajeswari: Neural Learning to Rank Model With Bias Correction 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0005-01.png)


using distinct encoders and contrastive learning, the resultant latent vectors remain opaque. There is no clear method to ascertain the contributions of user traits, position, and item to a particular forecast. 

The Enhanced Neural Click Model (ENCM) [17] advances conventional click models by employing neural networks to independently assess examination and relevance probabilities. Nevertheless, it possesses multiple fundamental constraints. Initially, it depends on a static click-generation assumption, which may inadequately reflect the complexities of actual user behavior affected by noise or user interface elements. Secondly, the concurrent training of relevance and examination networks may induce optimization instability, as inaccuracies in one component might adversely affect the other. Moreover, the model employs basic feedforward structures, which constrain its capacity to capture higher-order feature interactions or long-range relationships. The assessment is mostly performed on typical click logs, without evaluating resilience under diverse bias situations or scalability limitations. Ultimately, still based on a probabilistic framework, the model lacks interpretability tools to examine how relevance and bias are acquired or affect predictions. 

The CTRL [18] framework mitigates position bias in click-through rate prediction by utilizing both biased click data and supplementary unbiased feedback, either randomized impressions or human-assessed relevance. Although CTRL proficiently employs transfer learning using a cross-pair loss to synchronize the learning objectives of both data types, it possesses multiple drawbacks. Initially, it depends significantly on the accessibility of impartial data, which can be costly to gather and may not be available in adequate quantities in numerous practical scenarios. Secondly, the methodology lacks clear bias decomposition, complicating the interpretation or isolation of the effects of position or other contextual elements. The shared encoder utilized for both biased and neutral inputs may conflate relevance and bias signals, hence diminishing interpretability. The architecture presents issues for online implementation, as it presupposes access to static, unbiased references. The training procedure relies on meticulous sampling of cross-pairs and is partially validated under synthetic bias conditions, constraining its applicability to more intricate real-world user behavior. To disentangle relevance and bias, SimCEN [19] models click propensity using semantic similarity between user-item pairings. In noisy or sparse data, similarity may not indicate significance, which it relies on. The model’s bias and relevance components are still interwoven, restricting interpretability and modularity. The architecture adds training complexity with several interacting modules and does not directly express learned bias signals. 

To get rid of position bias in click data, the ensemble framework for unbiased learning to rank combines different relevance and observation models. Even though this split makes sense in theory, it’s not always practical in practice. 

It uses inverse propensity weighting (IPW) [20] to fix the bias, but IPW can become unstable when the datasets are small or skewed. The models are taught separately and don’t have endto-end optimization, which could make them less effective when used together. The framework also doesn’t have deep feature representations or position embeddings, which makes it less able to describe complex interactions. When you need to draw conclusions, combining results from different models can make the system more complicated and take longer. 

Moreover, rather than developing increasingly complex models, several researchers have recently shifted their focus to the data itself. It is recommended to extract a small portion of the user actions and feed it into the CTR model, as the complete sequence contains a lot of noise. An approach to learning to retrieve the most informative user behaviors according to each CTR estimation request is proposed in the article as the User Behavior Retrieval (UBR) [21] framework. In a separate study titled ‘‘Wide and Deep Learning’’ [22] the authors propose a hybrid method for recommender systems that combines the best features of memory and generalization. To overcome the difficulties caused by sparse user-item interactions, our approach uses a deep neural network to train low-dimensional embeddings and a wide linear model to capture feature interactions. However, there may be limitations to the model’s applicability due to its complexity, which could cause interpretability issues and higher computing demands. Another study introduces DIEN [23], a new model that aims to improve CTR prediction by capturing the changing interests of users over time. Two new layers are introduced: one that uses GRU with attentional updates to extract interests, and another that evolves interests. Various events that could trigger a click are currently the subject of ongoing studies. In order to address all possible situations in CTR prediction, [24] presented a general debiasing framework that does not simplify the relationships between variables. Taken together, the following factors— item information, user interest, item position, and bias of all contexts —determine a user’s likelihood of clicking on an item, regardless of whether the item is viewed or interesting to the user. This study has provided us with a wealth of ideas and inspiration for scenario handling. 

## **III. PRELIMINARIES** 

Take into consideration that the click data are displayed as including the click label, ranking or position of the document, and the query-id along with their corresponding features and contextual information of the documents. The label is called _Clicki_ , and it is set to 1 if the user clicks on the _i[th]_ item, and it is set to 0 otherwise. Contextual information is normally available as part of the features of the document. Features of the dataset are represented as Input and _n_ is the total count of features in the dataset. _Inputi_ is the _i[th]_ feature vector of the document. _positioni_ is the position of the _i[th]_ document and _p_ represents the dimension of the position. _Biasi_ represents the bias information including contextual data, and _b_ is the 

188403 

VOLUME 13, 2025 

K. J. Amala, D. Rajeswari: Neural Learning to Rank Model With Bias Correction 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0006-01.png)


dimension of the Bias. _y_ represents the relevence label [0-4] in the dataset. 

## **IV. PROPOSED METHOD** 

## _A. ARCHITECTURE_ 

Our architecture estimates the likelihood that a user will click on a particular item (e.g., document, link, or product) given certain inputs such as the position of the item on the page, the item’s content or features (title, length, etc.), the user’s past behavior, and other contextual signals. So the architecture is called a probabilistic click prediction model. The overall goal of the architecture is to predict clicks by separating true relevance from all the bias factors. The Probabilistic Click Prediction Network based on Attention (APCP) is the name of the novel architecture that is introduced in this paper. From the literature review conducted, it is observed that a user first sees an item based on its position. Then, if seen, the user may click based on the item’s attractiveness. That’s why the click probability is expressed as seen in Eqn (4). The factors influencing click to a document are not only position of the document but the overall contextual features it hold. So to represent other biasing factors other than position is represented by the term ‘bias’. As a result, the term ‘bias’ is assigned to the conditional probability. Further, position of the document affect visibility to all documents in the result page and if an item is clicked only when that one become visible to the user. So Eqn (4) can be written as 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0006-06.png)


An item is a representation of a web page or an object. It possesses its own unique characteristics. To indicate the features of an item, the variable ‘input’ is used. Thus Eqn (5) written as, 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0006-08.png)


The condition ‘seen’ is determined by position and all biasrelated factors [24]. So Eqn (6) becomes 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0006-10.png)


A user can seen a set of documents just because of their position and found it relevant because of the characteristics it contained. That means position makes a document relevant. So P(seen | position) is rewritten as P(r | input). i.e., clicks happen only when a user feel it is relevant and an item’s relevance is influenced by bias factors [24]. Hence finally it can be written as 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0006-12.png)


In light of the aforementioned Eqn (8), the architecture has two major modules: Input feature Module and Bias information Module which is shown in Figure 2. 

## 1) INPUT FEATURE MODULE 

Each of the queries has more than one document and each document represents a feature vector. This module analyzes the input feature vector to determine the probability of relevance P(r | input) using a self-attention layer to capture fine-grained feature interactions and fully connected layers. Attention-Based encoding [25] is performed by giving features as Input, and compute Q= _WQ_ Input, K= _WK_ Input, V= _WV_ Input and 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0006-16.png)


where _WQ, WK , WV_ ∈ R _[d]_[n][×] _[d][a]_ and _da_ is attention dimension and _dn_ is the input feature dimension. 

The attention output is passed through Multi-Layer Perceptron (MLP). The softmax layer converts the final logits into a probability distribution over binary relevance classes. It follows 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0006-19.png)


This formulation enables the model to capture fine-grained feature interactions and estimate document relevance accurately. 

## 2) BIAS INFORMATION MODULE 

The Bias Information Module is designed to replicate the effects of contextual and positional biases on user click behavior. P(Click=1| _r_ ,pos,bias) is a conditional probability distribution that maps from the input variables ( _r_ , position, bias) to the output variable Click. It is executed as a neural subnetwork that matches a 2×2 transition matrix, indicating the likelihood of a click based on the document’s latent relevance and contextual elements such as position or presentation bias. The position is given as an input into the module in the training pipeline. This lets it take into account bias caused by display rank. This design helps the model tell the difference between relevance and bias, that makes it more useful in real-world situations where clicks are always noisy and rely on position. Not only does the position of a content affect how a user behaves, but so do other contextual aspects. For example, a user might be more likely to look at a document with a shorter title (which is simpler to read quickly) or one that has had higher dwell times in the past. In this way, contextual variables affect position-dependent examination bias. 

Hence, this module is designed as a three-layer feedforward neural network and takes input as 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0006-24.png)



![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0006-25.png)


Here _b_ is the bias feature vector, _p_ is the position feature vector, and _d_ bias and _d_ position are their respective dimensions. Then bias and position are concatenated together. 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0006-27.png)


188404 

VOLUME 13, 2025 

K. J. Amala, D. Rajeswari: Neural Learning to Rank Model With Bias Correction 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0007-01.png)


The combined input goes through fully connected layers that are activated by ReLU. 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0007-03.png)


Four output values are projected by a third linear layer: 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0007-05.png)


Each of the four outputs is transformed into a 2×2 matrix: _M_ = reshape( _X_ 3) ∈ R[2][×][2] 

## 3) COMBINED MODULE 

According to Eqn (8), _P_ ( _r_ | _input_ ) is the actual learning objective of the model which will be utilized for online inference. P(Click = 1 | _r_ , position, bias) is conditional probability distribution that maps from the input variables ( _r_ , position, bias) to the output variable Click. The model shows that the chance of clicking on an item relies on both its relevance (how good it is) and its position bias (the tendency to click on items that are easy to see, no matter how good they are). Assume that _r_ can have two values; _r_ =0 means not relevant and _r_ =1 means relevant. For example in the case of recommendation a user clicks an item (Click=1) only if that user feels that item is relevant to him or by any kind of biasing (at that time that item may not be relevant to the query). 

_P_ (Click = 1 | input _,_ position _,_ bias) = _P_ ( _r_ = 0 | input) 

- _P_ (Click = 1 | _r_ = 0 _,_ position _,_ bias) + _P_ ( _r_ = 1 | input) 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0007-11.png)


Similarly for Click=0 the same can written as, 

_P_ (Click = 0 | input _,_ position _,_ bias) = _P_ ( _r_ = 0 | input) 

· _P_ (Click = 0 | _r_ = 0 _,_ position _,_ bias) + _P_ ( _r_ = 1 | input) 

- _P_ (Click = 0 | _r_ = 1 _,_ position _,_ bias) (10) 

_P_ ( _r_ = 0 | input) and _P_ ( _r_ = 1 | input) are handled by input feature module in the architecture. In general it is denoted as _r_ . 

_P_ (Click | _r,_ position _,_ bias) is handled by Bias information module in the architecture. 

_P_ (Click = 0 | _r_ =0 _,_ position _,_ bias) is represented by _M_ 1 _,_ 0. _P_ (Click = 0 | _r_ =1 _,_ position _,_ bias) is by _M_ 1 _,_ 1, P(Click = 1| _r_ = 0, position, bias) by _M_ 0 _,_ 0 and P(Click = 1 | _r_ = 1, position, bias) by _M_ 0 _,_ 1. 

The matrix _M_ is structured as follows and is represented as 

Hence Click prediction can be written as 

_Click_ pred = _r_ × _T_ 

Users are more interested in clicking on something which are relevant to them than something that is not relevant.However, the model could learn a wrong or noisy pattern during training because of bias, noise, or overfitting. To stop this from happening, a punishment is added whenever this assumption is broken. In order to guarantee that the model adheres to the assumptions of user behavior, a constraint loss is implemented that penalizes the network when the likelihood of a click on an irrelevant item surpasses that of a relevant item. Informally: 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0007-23.png)



![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0007-24.png)



![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0007-25.png)


aligning the model with intuitive click behavior patterns. In addition to the constraint loss, binary cross entropy (BCE) loss is also calculated. BCE loss naturally allows probabilistic outputs, which makes it a good choice for our task of figuring out what users will click on. It is calculated as 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0007-27.png)


ˆ + (1 − Click _i_ ) · log(1 − Click _i_ )� 

_B_ denotes the batch size, which is configured at 256. 

## **V. EXPERIMENTAL SETTINGS** 

## _A. DATASET_ 

To completely assess the proposed model, three benchmark datasets are employed. The MSLR-WEB30K dataset is used as the benchmark for training and comparing baselines in a safe and clean setting. The Yahoo LTR dataset is used to test whether the model can be used in a different area while keeping the testing environment noise-free. Lastly, the Yandex dataset, which comes from real-life search engine logs, includes query sessions with click information and position data. This lets us test how well the model works in real-life situations with real user behavior trends and biases. All together, these datasets make sure that our testing covers both controlled offline situations and search settings that are likely to be biased in the real world. 

_T_ 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0007-34.png)


Each row is a probability distribution (softmax applied row-wise), so 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0007-36.png)


## 1) MSLR WEB-30K 

The publicly accessible LTR dataset, MSLR WEB-30k, is utilized for training and evaluating our work. It is a huge-scale benchmarking dataset that was developed and released by Microsoft Research for the purpose of evaluating and refining learning-to-rank [26], [27] algorithms. There are 31,531 distinct queries in the database, divided across 5 folds, with each fold containing the training, validation, and test 

188405 

VOLUME 13, 2025 

K. J. Amala, D. Rajeswari: Neural Learning to Rank Model With Bias Correction 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0008-01.png)



![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0008-02.png)


**FIGURE 2.** Architecture: Input Feature Module (left) analyzes query-document features via self attention layer,three thick layers (n **×** 128, 128 **×** 64, 64 **×** 2) employing softmax normalization to produce relevance probabilities.Bias Module (right) manages multi-contextual bias features by utilizing position and document-specific contextual features as concatenated input. It processes these through dense layers (b+p) **×** 64, 64 **×** 32, 32 **×** 4) with softmax and reshape operations to generate bias probabilities. 

splits—including the quantity of queries and documents— provided in Table 1, and each query is accompanied by a number of documents that have been manually annotated with graded relevance scores. Typically, these scores range from 0 to 4, with 0 indicating that a document is irrelevant and 4 indicating that it is highly relevant to the query. Additionally, comprehensive statistics regarding this dataset is extensively utilized in information retrieval and machine learning, notably for training models that rank documents or web pages by relevance to a user’s query, like Bing or Google. An LibSVM-style query-document pair is represented by each dataset instance. That implies each dataset line has a relevance label, query ID, and feature-value pairs. Specifically, 136 characteristics capture document and query aspects. Examples include term frequency (TF), inverse document frequency (IDF), BM25 scores, click-through rates, PageRank, and URL elements. Relevance labels are binarized in our environment, meaning that any document with a relevance value higher than one is considered relevant. 

## 2) YANDEX PERSONALIZED WEB SEARCH CHALLENGE DATASET 

Yandex [28] assesses practicality and robustness under realistic user biases. It contain 4.6 million query-document 

**TABLE 1.** Details of MSLR Web-30K dataset. 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0008-08.png)


interactions consists of user sessions derived from Yandex logs encompassing user IDs, queries, query terms, URLs, their corresponding domains, URL ranks, and click data which represent the search activity that occurred during one month. The objective of the re-ranking is to display the search results that are most useful to the user, based upon the user’s intent.It follows Sparse click patterns, 45% of queries get no clicks, and 38% get just one click. 

## 3) THE YAHOO LEARNING TO RANK CHALLENGE DATASET 

The LTR dataset from Yahoo (also known as C14) [29] is used to test generalizability. The dataset is made up of query-document pairs that are shown as feature vectors and their human-graded relevance labels (0-4). Set 1 and Set 2 are two versions of this dataset and here Set 2 is utilized to 

188406 

VOLUME 13, 2025 

K. J. Amala, D. Rajeswari: Neural Learning to Rank Model With Bias Correction 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0009-01.png)


validate our model.It Contain 172,870 query-document pairs and 700 features. 

## 4) TRAINING DETAILS 

Eight NVIDIA A100 GPUs with a 256 batch size were used to train the complete model, which was done using PyTorch [31]. Adam [32] is the optimizer used, and the learning rate is 0.001. 

## _B. DATASET PREPROCESSING_ 

The dataset that is being utilized is not normalized uniformly, and the features of this dataset are on varying dimensions. However, the sensitivity of neural networks is influenced by the incorporation of these features into the network. In order to prevent such an occurrence, the subsequent actions must be taken: 

**Step 1** : Feature transformation 

For this step log1p scaling method is used. This method apply transformation to every feature by using the formula 

## 2) DYNAMIC FEATURE ADAPTATION 

To get rid of the architectural rigidity, it is introduced. Dynamic resizing mechanism can automatically change its internal layers to fit the size of the active feature set. This change makes sure that dimensions stay the same across scenarios with different feature combinations, which stops mismatches that used to make learning harder. The model keeps the best representational capacity by constantly changing the architecture, no matter how many or what kind of contextual features are given. 

## 3) REGULARIZATION STRATEGY 

We added _L1_ regularization to the loss function to lower the chance of overfitting, especially when using more than one contextual feature. _L1_ penalization encourages learnt weights to be sparse, which means that less informative feature coefficients are pushed toward zero. This helps with feature selection. 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0009-13.png)


## _D. PARAMETER CONFIGURATION_ 

where _x_ represents the feature, log1p makes large values smaller and thus reduce scale variance, sign( _x_ ) ensures negative values retain their sign. This operation is done element-wise for each feature. 

**Step 2** : Features are normalized using min-max scaling. 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0009-17.png)


Upon commencing the experiment, the input feature module was deployed, employing a 3-layer feed-forward network with hidden layer sizes of 128, 64, and 2. In the bias information module, employ a three-layer feed-forward network with hidden layer dimensions of 64, 32, and 4. Batch normalization and dropout to both feed-forward networks are applied, where the dropout rate is set to 0.5. 

**Step 3** : Data augmentation 

Augmentation enhances robustness by mitigating overfitting. This step is accomplished by using Gaussian noise. Enhance training robustness by incorporating noise into features. Each input feature vector _x_[′] is augmented as follows: 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0009-21.png)


where _σ_ is a scalar hyperparameter for controlling noise strength, _N_ (0 _, σ_[2] _I_ ) denotes multivariate Gaussian noise with zero mean and diagonal covariance. Each feature and training case gets its own sample of noise. It is added during training only, and new noise is utilized each time for each sample. 

**Step 4** : Correlation-Based Feature Selection 

Use correlation filtering to get rid of unnecessary features (| _r_ | > 0.85) that could make it harder to learn contextual features. 

## _C. HANDLING MULTI-CONTEXTUAL FEATURE PERFORMANCE_ 

## 1) CONTEXT GATING MECHANISM 

Various contextual features can conflict with one another during learning, even with the best preprocessing. For solving a learnable gating system is put it in the place. By enabling selective feature activation, this layer enables the network to automatically identify inputs that positively contribute to bias modeling and suppress those that have a detrimental impact. 

## _E. CLICK SIMULATION_ 

Since the dataset does not contain click labels explicitly, click generation becomes necessary. To begin creating artificial clicks in the training set, the documents must be correctly positioned. To begin, for each query, the documents are sorted according to their dataset appearance order. Following prior studies’ lead [30], 1% of the labeled training data are used to train the ranker, with the production ranker (eg: Ranking SVM) serving as the initial ranker. This ranker is then used to generate an initial ranked list of documents for each query, and the synthetic serving position for the document is the one with the first ranking. Once these rankings are obtained, the next step is to simulate. This guarantees that the position variable accurately reflects the user’s viewing order of the final presentation. 

Following that, by using the use-cases to generate synthetic clicks in order to replicate various user behaviors. The first user behaviour is 

## **Use-Case 1: Click only if observed and relevant** 

Click happens Only after the user sees the document and thinks it’s relevant. Nothing happens when the document is unimportant or ignored. 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0009-33.png)



![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0009-34.png)


188407 

VOLUME 13, 2025 

K. J. Amala, D. Rajeswari: Neural Learning to Rank Model With Bias Correction 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0010-01.png)


Here _E_ ( _k_ ) is the exposure probability (which depends on the position _k_ ), and the indicator function ⊮[ _y_ ≥ 1] denotes a click only if the relevance label _y_ ≥ 1. 

## **Use-Case 2: Allow clicks on irrelevant observed documents, small random chance based on position.** 

Documents that are both Observed and Relevant (with a relevance label of _y_ ≥ 1 are sure to get clicks from users. Additionally, users may occasionally interact with observed documents that are not relevant to their needs (documents with relevance label _y_ =0). 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0010-05.png)



![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0010-06.png)


## Here: 

- _E_ ( _k_ ) = exposure probability (depends on rank) 

- ⊮[ _y_ ≥1] = 1 if the document is **relevant** , otherwise 0 

- ⊮[ _y_ =0] = 1 if the document is **irrelevant** , otherwise 0 1 

- min(position _,_ 5) + 3[is][the][small][click][probability][for] irrelevant observed documents based on position 

In this use-case, click behavior is enhanced with genuine human mistake. A user’s positional attraction could lead them to click on an irrelevant document even if it’s visible. It is crucial that documents be visible; there have been no clicks on those yet. 

## **Use-Case 3: Allow clicks even if document is not observed (relevant but hidden)** 

In this case, there is no strict rule that clicks can only happen when documents are seen. Instead, it agree that users may click on pertinent documents even if they are not very visible. So, the click likelihood is based on two things: whether or not the document is seen and whether or not it is relevant. 

If observed: 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0010-16.png)



![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0010-17.png)



![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0010-18.png)


Once it is relevant and visible, the click happens. Depending on the position, there’s a chance to click if it’s noticed and irrelevant. 

If not observed: 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0010-21.png)


A very small probability of 0.1 clicks if relevant but unseen. No click if it is irrelevant and unnoticed. 

## **Use- Case 4: Click even irrelevant and unobserved** 

## **documents (pure noise allowed)** 

This is the most versatile and loud user behavior model of all the ones we’ve looked at. It mimics how people really browse the web, when they might click on things that are not important or that they have not seen before. This model takes 

into account both planned clicks and random noise, which is what happens when people use search logs on a big scale. 

The likelihood of a click depends on how relevant the document is and how easy it is to see. 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0010-28.png)



![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0010-29.png)



![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0010-30.png)



![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0010-31.png)


That is, people consistently click on relevant documents they see, but they may also click on irrelevant ones by mistake, especially if they are ranked higher. 

If not observed: 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0010-34.png)


This makes it possible: 

a) A little possibility (0.1) to click on a document that is significant even if you don’t see it (for example, if you scan quickly). 

b) There is a very small probability (0.01) that you will click on a page that is not relevant and is not being watched. This is like random or unintentional clicks. 

## **Use-case 5: Observation is based upon position and stated contextual features (title length)** 

This use case considers how the contextual characteristic (title length, designated as feature number 13 in the dataset) influences the probability of being viewed, alongside its ranking. Documents with greater title length feature values at a specific rank are anticipated to attract increased attention. To mitigate such biases, normalization is necessary. Here the model utilizes min-max normalization. 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0010-40.png)


where _f(d)_ (normalized feature) is the feature value of the current document, and _f_ min, _f_ max are the minimum and maximum values of the feature among all documents associated with the same query. To guarantee non-zero observation likelihood and avoid inappropriate penalization of low-context documents, each contextual characteristic is normalized to the interval [0.5, 1.0] instead of the conventional [0, 1]. This ensures a minimum weight of 0.5 for any document, facilitating smoother gradients during training and enhancing the simulation of user attention bias. 

Exposure function becomes: 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0010-43.png)


here _f(d)_ is calculated as the feature weight. Click probability If observed: 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0010-45.png)


188408 

VOLUME 13, 2025 

K. J. Amala, D. Rajeswari: Neural Learning to Rank Model With Bias Correction 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0011-01.png)



![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0011-02.png)


If not observed: 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0011-04.png)


## **Use-case 6 - Observation is based upon position and stated contextual features (both title length and dwell time)** 

Use case 6 enhances case 5 by integrating two contextual information into the exposure probability to more accurately predict user interaction behavior. Use case 5 adjusts user attention according to a singular document-specific attribute ( title length), but case 6 incorporates a secondary feature (dwell duration) to encompass further aspects of perceived value. The observation probability is formally described as inversely proportional to the rank position, adjusted by an average weight generated from two normalized contextual characteristics. So, 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0011-07.png)


The exposure function and click probability are identical to those in the previous use case. 

Utilizing the equations delineated above, simulate over 10 million clicks on all queries within the training set of the MSLR-WEB30K/Fold1 dataset for every case, with each query being sampled an average of 66.5 times. The labeled test data are used (ground truth labels 0-4) from Fold1 of the MSLR-WEB30K dataset to see how well different models predict which documents are relevant to a search. 

## _F. STATISTICAL ANALYSIS_ 

All performance indicators are presented with 95% confidence intervals derived from bootstrapping (n=1000). The statistical significance was evaluated using _α_ = 0.05 for all tests. AUC differences was evaluated using DeLong’s test for correlated ROC curves. Effect sizes were computed with Cohen’s d to evaluate practical significance. For other performance metrics, two-tailed paired t-tests were used to evaluate the statistical significance of reported improvements. 

they are in the ranked list. It is apt for graded relevance assessments and calculated as 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0011-13.png)


where _reli_ is the relevance score of the document at position _i_ , and IDCG@ _k_ is the ideal DCG computed using the optimal ranking. Here report NDCG@1, NDCG@3, NDCG@5 and NDCG@10 to evaluate performance at different cut-off levels. 

Mean Average Precision (MAP): assumes that there are two levels of relevance grades: 1 and 0. For a given query, Average Precision for each query is defined as follows: 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0011-16.png)


where _R_ is the total number of relevant documents, _P@k_ is the precision at cut-off _k_ , and rel( _k_ ) is a binary indicator of relevance at position _k_ . MAP is then averaged across all queries. 

Mean Reciprocal Rank (MRR): Focuses on the position of the first relevant document 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0011-19.png)


where _Q_ is the number of queries and _ranki_ is the position of the first relevant document for query i. 

## 2) BINARY CLASSIFICATION METRICS 

AUC: To get started, train our model using simulated data based on distinct use cases. It generally makes use of the Area Under the ROC Curve (AUC) in order to evaluate the performance of the model. This is because AUC is an effective measurement of the model’s ranking abilities, which is especially significant in situations where relative order is more relevant than absolute likelihood. In addition, AUC is resistant to class imbalance, which makes it an appropriate option for our environment. 

Log Loss (Logarithmic Loss): measures the accuracy of probabilistic predictions for binary classification tasks. 

Precision at _K_ (P@ _K_ ): measures the fraction of relevant documents among the top- _K_ retrieved documents. 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0011-25.png)


## _G. EVALUATION METRIC_ 

Our evaluation framework includes both the effectiveness of graded relevance ranking and the performance of binary classification. 

## 1) RANKING-SPECIFIC METRICS 

Normalized Discounted Cumulative Gain (NDCG): calculate both how relevant the retrieved documents are and where 

## _H. COMPARED BASELINES_ 

The following robust baselines are used to compare our model. 

- MMoE-bias [4]: The debiasing framework in this study predicts the user click by combining logit for user engagement and logit for positional bias and models the positional bias by a shallow side tower independently. 

188409 

VOLUME 13, 2025 

K. J. Amala, D. Rajeswari: Neural Learning to Rank Model With Bias Correction 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0012-01.png)


- PAL [3]: This model contains two modules: one module handles probability of P(seen | pos), and the other manages probability of P(click= item, seen).This method is used to figure out the chance of being examined and to figure out the click rate based on what was viewed. The end result click rate is the product of the two modules’ outputs. 

- IIN [24]: This model works based on a probabilistic graphical model and takes the assumption that regardless of whether an object is viewed or recognized as relevant by the user, it may still be clicked by them. 

- MFIM [5]: This model is typically a multi-layer fully connected network, to estimate examination probability based on SERP. 

- XPA [6]: This model follows the theory that the attention of users and the likelihood that they would click on an item may depend not only on the position of the item itself, but also on what is displayed above or below it. 

- DPIN [7]: The most important goal is to increase ranking fairness while taking into account position bias, as well as to guarantee consistency between training and inference (by using actual positions during training and inferred positions during serving). 

## **VI. RESULTS AND DISCUSSION** 

This section explores the comparison results between our approach and other baselines across various use cases. 

## _A. ANALYSIS OF TRAINING EFFICIENCY AND CONVERGENCE_ 

During training phase, the changing trends of AUC on the test set are displayed in Figure 3. (a) to (e), in that order. In addition, the AUC values that were earned by different models after seventy thousand training iterations are presented in Table 2. 

_Model Convergence Behavior in Use Case 1:_ Figure 3(a) shows how APCP (our method) trains compared to other methods— MMoE-Bias, PAL, IIN,MFIM, XPA, DPIN — on case 1, where clicks are based just on relevance and observation (i.e., there is no contextual bias). The x-axis displays the number of training steps ( from 0 to 70,000), and the y-axis denotes AUC. APCP converges quickly, with a big AUC gain in the first 10,000 steps. It levels off at about 92.5% AUC, which is far better than the baselines throughout the training process. Baseline models keep becoming better, but their performance levels off considerably earlier and at lower AUC levels (around 77–78%). This trend shows that APCP works well at finding basic click patterns in situations when there is no bias. The steep learning curve at first also shows that it can swiftly apply what it has learned to new situations, which could be useful in situations when time or resources are limited. 

_Model Convergence Behavior in Use Case 2:_ In this case, clicks are mostly based on how relevant a document is and how easy it is to see, with additional position bias for documents that are not relevant but are still visible. 

This probabilistic approach models ideal clicks for relevant documents, but non-related documents get fewer clicks based on their position. This illustrates how rank bias affects clicks on items that are not relevant. Figure 3(b) shows that proposed model, APCP, has the best generalization and the fastest convergence among all the evaluated baselines. APCP quickly gets an AUC above 0.83 after 10,000 iterations and stays there, beating all other baselines all the way through training. These results show that attention-based probabilistic modeling works better at reducing bias and getting user preferences during training. 

_Model Convergence Behavior in Use Case 3:_ The goal of use case 3 is to create a realistic scenario where not all relevant papers are necessarily seen and not all documents that are not seen are ignored. APCP always does better than all the other baselines, with an AUC of about 0.85 and early convergence by 10,000 steps. The IIN and PAL models both get AUCs in the range of 0.77 to 0.78, which means they are somewhat effective when just some information is available. MMoE-Bias is behind with a slower convergence and a peak AUC that is a little lower, settling at 0.76. APCP’s better performance shows that it is good at simulating noisy, probabilistic feedback and dealing with partial observability. This strength is very important for rating systems that work in the real world, because user feedback is always unreliable and biased. 

_Model Convergence Behavior in Use Case 4:_ This situation makes things as complicated as possible for current scenarios, forcing models to develop strong representations even when random clicks on irrelevant documents happen. The significant level of randomness in user response goes against established models that think click patterns are mostly based on relevancy. APCP gets a top AUC of about 0.825, which is better than all the baselines at all training levels. IIN is still the second-best, with an AUC of about 0.78, which shows that it can handle noise fairly well. PAL and MMoE-Bias have a hard time in this loud environment, dropping below 0.77. APCP’s better performance shows that it can predict bias based on attention and probabilistic resilience. This lets it find significant patterns even when there is a lot of observation noise and uncommon click oddities. 

## _Model Convergence Behavior in Use Case 5:_ 

In case 5, the simulation framework is expanded to include document-specific features in the observation process. This adds a layer of contextual perception bias that goes beyond position alone. APCP has a maximum AUC of about 0.84, which is better than all other baselines. IIN, PAL, and MMoE-bias all level off at around 0.77–0.78, which means they can’t predict contextual observation bias very well. MFIM,XPA and DPIN show very poor performance. APCP converges faster, stabilizing within the first 10,000 iterations. This shows that it learns bias quickly. The fact that APCP did better in this situation shows that modeling contextual elements works for simulating user attention. Position-only models, like IIN and PAL, don’t take into consideration perception cues that affect how visible a document is. Adding 

188410 

VOLUME 13, 2025 

K. J. Amala, D. Rajeswari: Neural Learning to Rank Model With Bias Correction 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0013-01.png)



![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0013-02.png)



![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0013-03.png)



![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0013-04.png)



![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0013-05.png)



![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0013-06.png)


**FIGURE 3.** AUC changes on the test set throughout training with different approaches. 

title length to the observation function helps APCP tell the difference between click noise and biased clicks, which helps it figure out what is relevant. The simulation helps capture different types of user behavior, especially when longer or more informative titles get more attention than rank alone. 

## _B. OVERALL PERFORMANCE_ 

Table 2 provides a presentation of the evaluation metrics that were gained by unique models, namely MMOE-Bias, PAL, IIN, MFIM, XPA, DPIN and APCP, which were examined across five different use cases. In click simulation, each use case correlates to a separate behavioral scenario. These scenarios range from simple clicks based on relevance to more complicated and noisy user actions. 

It has been demonstrated that the APCP model consistently achieves the highest AUC across all use cases.The fact that its performance under Use-Case 1 is almost flawless (AUC = 0.9332) indicates that it is highly successful in circumstances where there is no background noise. It maintains strong performance (AUC > 0.82), exhibiting its resistance to observational and behavioral noise, even when it is subjected to noisy click scenarios such as Use-Cases 4.The IIN consistently gives high performance, with AUC 

values that are relatively steady across all five scenarios. This demonstrates that it is effective at capturing complex interactions and in dealing with signals that are biased or noisy. In MMoE-Bias, PAL,XPA and DPIN models, the sensitivity to noise is considerable, and there is a discernible decrease in the area under the curve (AUC) from UseCase 1 to Use-Case 2 and beyond. The performance of these models is satisfactory in cleaner circumstances; however, they demonstrate a limited resistance when confronted with click ambiguity or unpredictable user behavior.The overall performance of MFIM is disappointing particularly in cases 3 to 5. 

## _C. ENHANCED RESULTS INTERPRETATION_ 

## 1) LOG LOSS INTERPRETATION 

Table 3 presents the comprehensive results for CTR prediction performance using log loss as evaluation metric. The suggested APCP technique consistently surpasses all baseline methods across five use scenarios, with log loss values between 0.1102 and 0.2550. Significant enhancements are shown in Use Case 1, where APCP attains a log loss of 0.1102, indicating a 31.5% decrease relative to the optimal baseline approach (IIN: 0.1608). In Use Case 5, 

188411 

VOLUME 13, 2025 

K. J. Amala, D. Rajeswari: Neural Learning to Rank Model With Bias Correction 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0014-01.png)


**TABLE 2.** Models performance across different scenarios on MSLR-WEB-30K Dataset. 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0014-03.png)



![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0014-04.png)



![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0014-05.png)



![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0014-06.png)



![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0014-07.png)


APCP exhibits a 5.7% enhancement compared to IIN (0.1935 against 0.2052). The uniform performance across 

various applications demonstrates the strength and applicability of the suggested method.Significantly, Use Case 4 is 

188412 

VOLUME 13, 2025 

K. J. Amala, D. Rajeswari: Neural Learning to Rank Model With Bias Correction 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0015-01.png)


**TABLE 3.** Log Loss values of different use-cases on CTR prediction. 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0015-03.png)


the most challenging prediction case, as all approaches demonstrate elevated log loss values. Nonetheless, APCP retains its competitive edge in this challenging scenario, attaining a log loss of 0.2550, in contrast to the optimal baseline IIN (0.2786), signifying an 8.5% enhancement. This indicates that APCP is especially proficient at managing complex prediction situations. 

## 2) MODEL STABILITY EVALUATION 

Model stability is assessed through constant relative gains in performance rather than absolute metric values.We compare our APCP model against the base line IIN because it achieves competitive performance across all evaluation metrics, including AUC, NDCG@k, MAP, and MRR. However, as shown in Table 4, APCP exhibits consistent superiority, with effect sizes varying from large (d = 0.89) in Use-case 4 to extremely large (d = 1.85) in Use-case 1. The log loss pattern, peaking at 0.2755 for Use-case 4 and thereafter declining to 0.2035 for Usecase 5, substantiates model robustness, indicating superior performance under realistic conditions compared with fabricated simulate scenarios.Beyond AUC, APCP shows consistent improvements across all ranking and precision metrics. The proposed method achieves a remarkable 13.2% average improvement in NDCG@10 performance across all experimental configurations. The performance range demonstrates consistent superiority, with scores improving from the baseline range of 0.6115-0.7288 to the enhanced range of 0.6556-0.8253.The proposed method achieves the most substantial improvement in MAP, with an average increase of 14.5% across all experimental scenarios. The performance distribution shifts significantly from 0.48010.5869 in baseline methods to 0.5415-0.7470 in the proposed approach.The MRR improvements demonstrate enhanced early precision, with the minimum performance increasing by 1.5% (from 0.6112 to 0.6201) and the maximum performance reaching 0.8201, representing a 13.2% improvement over the best baseline. 

## _D. VALIDATION ON REAL-TIME DATASET_ 

## 1) REAL-WORLD VALIDATION ON YAHOO LTR DATASET 

To clarify concerns regarding the generalizability of our method beyond simulated settings, we perform extensive validation on the Yahoo LTR dataset, which represents real 

search engine data accompanied by valid user relevance assessments. The Yahoo LTR dataset lets us test how well our model ranks data that is more complex and noisy, which is what happens in real-world search systems. This is different from the controlled simulation tests on MSLR-WEB30K. 

Our APCP model shows steady and statistically significant improvements over all baseline techniques on all evaluation metrics as shown in the Table 5. Most importantly, we have the greatest results in all 10 metrics, with gains of 1.10% (P@10) to 5.28% (NDCG@3) over the strongest baseline (IIN).Our improvements over IIN vary from 1.10% to 5.28%, which shows that our position bias correction methodology makes a real difference, even compared to more advanced methods. The slight but steady improvements over this strong baseline show that our bias correction technique works. Our technique is much better than MMoE-bias (9.33% to 18.05% better), PAL (33.98% to 66.90% better), MFIM (37.93% to 150.05% better), and DPIN (37.71% to 108.38% better). This big difference in performance shows how important it is to handle bias correctly in ranking systems. Our improvements stay the same at all cutoff levels: NDCG@1 (+5.14%), NDCG@5 (+4.24%), and NDCG@10 (+3.45%). This pattern illustrates that our bias correction works well for all positions on the ranking list, but it works best for the top positions, where position bias has the biggest effect.All reported improvements are statistically significant (p < 0.05), which shows that the increases in our performance are not just random changes. The fact that our benefits are broad and apply to all measures and all baselines is solid proof that our strategy works and is reliable. 

## 2) CTR PREDICTION VALIDATION ON YANDEX DATASET 

To offer thorough validation beyond mere ranking quality assessment, we examine our APCP model using the Yandex Personalized Web Search Challenge dataset, comprising genuine user click logs from Yandex’s search engine. The Yandex dataset lets you directly test how well CTR forecast works with real user interaction data. The dataset includes query-document combinations with genuine user click behavior, which shows the natural complexities and biases that come with real search encounters. Our APCP model gets an AUC score of 0.8567, which is strong and shows a substantial improvement of +4.36% over the best baseline technique as shown in Table 6. This shows that our bias correction approach works well with real user interaction data to make click predictions better.Statistical significance testing verifies that the observed enhancements are not attributable to random fluctuation. 

## 3) DETAILED PERFORMANCE ANALYSIS 

A comprehensive computational performance analysis was conducted to assess the practical deployment viability of the proposed method. The inference latency and memory requirements for all evaluated methods across various batch sizes and model configurations are presented in Tables 7 and 8. In resource-constrained environments that 

188413 

VOLUME 13, 2025 

K. J. Amala, D. Rajeswari: Neural Learning to Rank Model With Bias Correction 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0016-01.png)


**TABLE 4.** Comparison of APCP with strongest baseline in various usecases. 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0016-03.png)


**TABLE 5.** Performance comparison of APCP with baseline models on Yahoo. 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0016-05.png)


**TABLE 6.** Performance comparison of APCP with baseline models on Yandex. 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0016-07.png)


are typical of online recommendation systems, these metrics are essential for evaluating their real-world applicability. The suggested technique works quite well on NVIDIA A100 GPUs, with a maximum throughput of 40,582 queries per second when processing batches. Single query latency is 1.07 ms, while batch processing is far more efficient, with a per-sample latency of 0.01 ms (batch size 128), which is 99% better than processing each sample separately. Conservative estimates clarify that that each instance can handle 938 QPS, with enough safety margins for real-world use.The method is very efficient with resources because the model size is only 0.11 MB and the peak memory usage is only 17.9 MB. The system is cost-effective for large-scale production environments because it only needs 0.017 MB of memory per sample, which allows for highdensity deployments.Consistent P95 latency (1.1–1.4 ms) across all batch configurations guarantees dependable service level compliance. The linear scalability and stateless design make it easy to scale horizontally, and the small resource footprint makes it possible to deploy on a wide range of hardware setups, from high-end GPUs to cheap CPU-only instances. 

**TABLE 7.** Inference latency. 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0016-10.png)


**TABLE 8.** Memory requirements. 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0016-12.png)


design choices were good ones and shows us which factors have the biggest effect on the model’s ability to predict the future. 

## _A. IMPORTANCE OF NUMBER OF ATTENTION LAYERS_ 

## **VII. ABLATION STUDY** 

A detailed ablation study is conducted to learn more about how the different parts and design choices in our model work together. The aim is to understand how different parts of the architecture affect total performance by changing or removing them one by one. This study helps us see if our 

To assess the impact of the self-attention mechanism, an ablation study is performed by altering the number of self-attention layers with {1, 2, 3, 4, 5, 6 } in the architecture. It examines how the depth of attention influences performance. The effect is tested in four carefully selected cases with different contextual bias complexity: 

188414 

VOLUME 13, 2025 

K. J. Amala, D. Rajeswari: Neural Learning to Rank Model With Bias Correction 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0017-01.png)



![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0017-02.png)



![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0017-03.png)



![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0017-04.png)



![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0017-05.png)



![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0017-06.png)



![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0017-07.png)



![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0017-08.png)



![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0017-09.png)



![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0017-10.png)



![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0017-11.png)



![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0017-12.png)



![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0017-13.png)



![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0017-14.png)



![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0017-15.png)



![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0017-16.png)



![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0017-17.png)


**FIGURE 4.** Attention layer integration across baseline methods. 

case (1)—ideal observations; case (4)—noise, even irrelevant documents; case (5)—hybrid static-positional interactions with title length and position; and case (6)-a difficult scenario with dwell duration to analyze multi-feature entanglement.Moreover, ablation analysis had been expanded beyond APCP to determine if the reported improvements in the number of attention layers were exclusive to APCP or could be similarly attained in other models. We assessed four distinct model architectures: APCP (our suggested model), PAL (Position-Aware Learning), MFIM (Multi-Feature Interaction Model), and IIN (Implicit Intention Network) to validate the generalizability of our findings. We systematically incorporated attention layers into each baseline approach while preserving their fundamental algorithmic structures. To make sure the comparisons were fair, we used the identical datasets, assessment measures (AUC, NDCG@5, NDCG@10, MAP, MRR), and experimental methodologies for each configuration. The attention layer implementation followed to the architectural concepts employed in APCP to delineate the effects of attention integration across various methodologies. 

Figure 4 illustrates the distinct heterogeneity of responses to attention layer integration that our cross-method analysis reveals. The findings indicate that attention mechanisms generate method-specific effects rather than universal enhancements: 

PAL shows a complicated, metric-dependent reaction to attention integration. PAL starts out by breaking Layer 1 (AUC lowering from 0.779 to 0.500 for case-1), but then 

it slowly becomes better with more attention layers. It’s interesting that PAL acts the opposite way for NDCG measurements, where attention layers always make performance better from the first layer onward. This different behavior of the metric shows that PAL’s design can eventually adapt to use attention methods, but it needs numerous layers to fix the initial architectural misalignment for some evaluation criteria. MFIM shows a big drop in performance when attention is added to all settings. The AUC reduces steadily from 0.65 (no attention) to 0.50 across all attention layers (1-6), which represents a 23% drop in performance. The drop is considerably bigger for NDCG@5, which goes from 0.4504 to 0.1210 (73% drop) with just one attention layer. This significant degradation pattern stays the same no matter how the attention layers are set up, which shows that MFIM’s architecture and attention mechanisms are fundamentally incompatible. IIN exhibits a pattern of stabilization where attention Layer 1 improves the performance of both the AUC and NDCG@5 metrics, but adding more layers (2-6) doesn’t help. This plateau effect shows that IIN can benefit from attention mechanisms, but it can’t use deeper attention architectures very well. 

Robustness of the APCP in four different cases as follows: Case-1: The best performance is with four attention layers, and it becomes better with each layer until it gets worse with five or six levels. 

Case-4: A similar pattern, with the best performance at 4 layers, proving that it can handle position bias and click noise. 

188415 

VOLUME 13, 2025 

K. J. Amala, D. Rajeswari: Neural Learning to Rank Model With Bias Correction 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0018-01.png)


Case-5: Four layers of optimality that stay the same even when the observation patterns are complicated. 

Case-6: Keeps 4 layers of optimal performance even when there are many features to observe. 

To validate the importance of our findings, we calculated performance statistics over all four scenarios and performed thorough hypothesis testing. APCP attained a mean AUC of 0.743 ± 0.031 with one attention layer, which increased to 0.821 ± 0.028 with two layers and further improved to 0.876 ± 0.024 with three layers. The optimal configuration was achieved with four attention layers, resulting in a mean AUC of 0.923 ± 0.019. The addition of more layers did not result in further enhancements, as performance slightly declined to 0.918 ± 0.022 for five layers and 0.911 ± 0.025 for six layers. The application of paired t-tests across the four scenarios as repeated measures validated the statistical significance of these results. The 4-layer model demonstrated a significant advantage over the 3-layer variant, with a difference of _�_ = +0.047 AUC, representing a 5.4% improvement. Statistical analysis yielded t(3) = 4.12, p = 0.026 after Holm correction, and Cohen’s dz = 2.06, indicating a very large effect size. The difference between 4 and 5 layers was minimal and not statistically significant ( _�_ = +0.005 AUC, p = 0.155; dz = 0.95, large effect). In contrast, the comparison between 4 and 6 layers indicated a trend toward improvement ( _�_ = +0.012 AUC, p = 0.066; dz = 1.42, very large effect), although it did not reach significance after correction. The 4-layer configuration demonstrated a significant and practically substantial performance gain over the single-layer baseline, with a change of _�_ = +0.180 AUC (p < 0.001; dz = 6.23), indicating an extremely large effect. 

The results indicate that an increase in the number of attention layers initially improves predictive accuracy; however, performance gains level off after four layers, leading to diminishing returns in relation to computational cost. Unless stated otherwise, the ‘‘±’’ values represent the standard deviation of AUC across the four evaluation scenarios. 

## _B. EFFECT OF DIMENSION OF ATTENTION ON RELEVANCE PREDICTION_ 

We examine the impact of the attention dimension solely on the proposed APCP model, as this hyperparameter is intrinsic to its architectural framework. The purpose of this ablation study is to see how changing the attention dimensions affects model performance in a number of synthetic click scenarios, each of which is meant to mimic a different sort of user behavior and bias. The goal is to find the best attention dimension that consistently increases the AUC by looking at how well it works in each case, which are shown in Figure 5. 

Model performance is evaluated with different attention dimensions (32, 64, 128, and 256) in each of the six scenarios. The findings (Figure 5) provide crucial information: 

The best performance is frequently seen around 256 in Scenarios 1-4, where AUC continuously improves as the 

**TABLE 9.** Contextual features used in different use cases. 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0018-11.png)


attention dimension rises. Higher attention capacity allows for the effective capture of position and relevance signals, which are crucial in these settings.The model performs consistently across attention sizes in Scenario 5, even with the addition of document-level bias. Although there are still some improvements at 256, this shows that the attention mechanism successfully adjusts to the increased feature-based complexity.Performance in Scenario 6 actually peaks at the lowest value (32) and demonstrates minimal benefit with bigger attention dimensions. At high dimensions, the addition of numerous contextual factors may result in noise or overfitting, suggesting that compact attention representations are more resilient in these situations. 

## _C. INFLUENCE OF CONTEXTUAL FEATURES ON BIAS_ 

An in-depth study is conducted in four main scenarios to see how different contextual bias factors affect click modeling. Details are described in Table 9. Each scenario changes the observation probability function to include several levels of context beyond only position and relevance. 

Our objective is to determine the individual and combined effects of contextual features on observation modeling by comparing evaluation metrics across all of these configurations. Table 10 shows the comparative analysis of scenarios and Figure 6 shown the performance of usecases. 

Usecase 5- Title Length: In this case, the observation likelihood is modified by the length of the document title, which reflects the way in which presentation-related textual variables influence visibility. This static feature makes a significant contribution to user engagement signals, as indicated by the model’s performance, which is satisfactory (AUC = 0.8456). When contrasted with other behavior characteristics that are more dynamic, however, its limits become more evident. 

Case 6 - Title length and dwell time: 

Use case 6 aims to enhance contextual understanding by utilizing both a static feature (title length) and a dynamic behavioral signal (dwell duration). 

Use case 7 - Bias in Isolated Dwell Time: 

188416 

VOLUME 13, 2025 

K. J. Amala, D. Rajeswari: Neural Learning to Rank Model With Bias Correction 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0019-01.png)



![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0019-02.png)



![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0019-03.png)



![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0019-04.png)



![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0019-05.png)



![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0019-06.png)



![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0019-07.png)


**FIGURE 5.** AUC vs Attention dimension for use cases. 

**TABLE 10.** Comparative analysis of contextual bias. 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0019-10.png)


This case looks at the effect of dwell time as the only contextual bias element. This feature shows how long a user has been engaged with a document and gives dynamic, behavior-based cues about how relevant and visible it is. This scenario had the best overall performance, as shown in Figure 6, which shows that dwell time is a robust and trustworthy way to measure observation. The success of this scenario shows how important dynamic behavioral cues are for modeling user interaction biases compared to static content features. 

Use case 8- Title Length + Dwell Time + URL Click Count + Query URL click Count: 

With an AUC of 0.8861, it is clear that our improved bias module can tell the difference between relevant and irrelevant materials. This means that it can learn how the four contextual features interact in a sophisticated way. Different evaluation metrics (AUC, NDCG, and MAP) all show that our changes make the model stable and usable across all of them, instead of just improving it for one metric. 

## _D. EFFECT OF DROPOUT REGULARIZATION AND BIAS MODULE DEPTH_ 

To address concerns regarding the sensitivity of our model to key hyperparameters, we conducted a systematic ablation study focusing on dropout regularization and bias module depth. Each configuration was assessed using five independent random seeds ( _n_ = 5). For each statistic, we report the mean ± standard deviation along with the 95% confidence intervals. Statistical significance was evaluated using paired t-tests across seeds, with the Holm–Bonferroni correction applied to control the family-wise error rate ( _α_ = 0 _._ 05). In total, 120 training runs were executed (24 configurations × 5 seeds). The assessed parameter ranges were: Dropout Rate ∈{0 _._ 0 _,_ 0 _._ 1 _,_ 0 _._ 2 _,_ 0 _._ 3 _,_ 0 _._ 4 _,_ 0 _._ 5}, applied to both attention and feed-forward layers; and Bias Module Depth ∈{1 _,_ 2 _,_ 3 _,_ 4}, which regulates the intricacy of bias modeling. 

The table 11 presents the sensitivity of APCP to the dropout rate. Performance consistently improves until a dropout rate of 0.2 (Mean AUC = 0.9012 ± 0.0019, 95% CI [0.8988, 0.9036]; NDCG@5 = 0.5512 ± 0.0021), beyond which it begins to decline. Paired t-tests demonstrated that a dropout 

188417 

VOLUME 13, 2025 

K. J. Amala, D. Rajeswari: Neural Learning to Rank Model With Bias Correction 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0020-01.png)



![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0020-02.png)



![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0020-03.png)



![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0020-04.png)



![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0020-05.png)


**FIGURE 6.** Comparison of performance curves across different use cases. 

**TABLE 11.** Effect of dropout rate on model performance. 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0020-08.png)


**TABLE 12.** Effect of bias module depth on model performance. 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0020-10.png)


rate of 0.2 significantly outperforms 0.0 ( _t_ (4) = 15 _._ 32, _p <_ 0 _._ 001[∗∗∗] ), 0.1 ( _t_ (4) = 8 _._ 41, _p <_ 0 _._ 001[∗∗∗] ), 0.4 ( _t_ (4) = 10 _._ 87, _p <_ 0 _._ 001[∗∗∗] ), and 0.5 ( _t_ (4) = 13 _._ 21, _p <_ 0 _._ 001[∗∗∗] ). The difference between 0.2 and 0.3 was not statistically significant ( _t_ (4) = 1 _._ 41, _p_ = 0 _._ 35). 

The 3-layer architecture demonstrated significant superiority over most alternatives. Compared with 1 layer (t(8) = 8.64, p < 0.001***), 4 layers (t(8) = 7.11, p < 0.001***), and 5 layers (t(8) = 10.42, p < 0.001***), the improvements were highly significant. In contrast, the difference between 3 and 2 layers was marginal and did not reach significance (t(8) = 2.19, p = 0.057). 

## **VIII. CONCLUSION AND FUTURE DIRECTION** 

In this study, a new approach was introduced for probabilistic models to predict click-through rates that is bias-aware and attention-enhanced. This approach solves the main problem of differentiating real user preferences from presentation artifacts, which makes it easier to estimate relevance more accurately. This improvement is especially important for search engines and recommendation systems, since knowing what a user really wants is important for the system to work well and for users to be contented.Through comprehensive 

assessments on the Yandex and Yahoo datasets, we established that APCP routinely surpasses robust baseline models across all evaluation measures. Analyses of parameter interactions, statistical significance, and resilience indicate that the enhancements of the model are dependable and applicable across many contexts.Although our suggested framework exhibits robust performance, some unresolved difficulties persist, indicating potential avenues for future exploration. Despite the gating technique proficiently captures feature importance, a certain level of manual feature engineering is necessary. 

Future research should concentrate on automated feature discovery, utilizing gradient-based or attention-driven selection to diminish dependence on manual preprocessing.The existing methodology addresses position and biases in isolation. Future research should provide collaborative modeling frameworks that explicitly account for interactions among various bias types. Moreover, the implementation of A/B testing with actual search traffic will be essential for confirming CTR enhancement, user satisfaction, and computational efficiency in production settings, thereby connecting offline experimentation with real-world application. 

## **CODE AND DATA AVAILABILITY** 

The source code and processed datasets used in this study are available at github.com/amalaajkamal. 

## **REFERENCES** 

- [1] A. Chuklin, I. Markov, and M. de Rijke, _Click Models for Web Search_ . Cham, Switzerland: Springer, 2022. 

- [2] S. Gupta, P. Hager, J. Huang, A. Vardasbi, and H. Oosterhuis, ‘‘Unbiased learning to rank: On recent advances and practical applications,’’ in _Proc. 17th ACM Int. Conf. Web Search Data Mining_ , Mar. 2024, pp. 1118–1121. 

- [3] H. Guo, J. Yu, Q. Liu, R. Tang, and Y. Zhang, ‘‘PAL: A position-bias aware learning framework for CTR prediction in live recommender systems,’’ in _Proc. 13th ACM Conf. Recommender Syst._ , New York, NY, USA, Sep. 2019, pp. 452–456, doi: 10.1145/3298689.3347033. 

- [4] Z. Zhao, L. Hong, L. Wei, J. Chen, A. Nath, S. Andrews, A. Kumthekar, M. Sathiamoorthy, X. Yi, and E. Chi, ‘‘Recommending what video to watch next: A multitask ranking system,’’ in _Proc. 13th ACM Conf. Recommender Syst._ , New York, NY, USA, Sep. 2019, pp. 43–51, doi: 10.1145/3298689.3346997. 

- [5] X. Chen, X. Li, K. Wei, B. Hu, L. Jiang, Z. Huang, and Z. Kang, ‘‘Multi-feature integration for perception-dependent examination-bias estimation,’’ 2023, _arXiv:2302.13756_ . 

188418 

VOLUME 13, 2025 

K. J. Amala, D. Rajeswari: Neural Learning to Rank Model With Bias Correction 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0021-01.png)


- [6] J. Huang, K. Hu, Q. Tang, M. Chen, Y. Qi, J. Cheng, and J. Lei, ‘‘Deep position-wise interaction network for CTR prediction,’’ in _Proc. 44th Int. ACM SIGIR Conf. Res. Develop. Inf. Retr._ , Jul. 2021, pp. 1885–1889. 

- [7] H. Zhuang, Z. Qin, X. Wang, M. Bendersky, X. Qian, P. Hu, and D. C. Chen, ‘‘Cross-positional attention for debiasing clicks,’’ in _Proc. Web Conf._ , Apr. 2021, pp. 788–797. 

- [8] Y. Zhang, L. Yan, Z. Qin, H. Zhuang, J. Shen, X. Wang, M. Bendersky, and M. Najork, ‘‘Towards disentangling relevance and bias in unbiased learning to rank,’’ in _Proc. 29th ACM SIGKDD Conf. Knowl. Discovery Data Mining_ , New York, NY, USA, Aug. 2023, pp. 5618–5627, doi: 10.1145/3580305.3599914. 

- [9] M. Haldar, P. Ramanathan, T. Sax, M. Abdool, L. Zhang, A. Mansawala, S. Yang, B. Turnbull, and J. Liao, ‘‘Improving deep learning for airbnb search,’’ in _Proc. 26th ACM SIGKDD Int. Conf. Knowl. Discovery Data Mining_ , New York, NY, USA, Aug. 2020, pp. 2822–2830, doi: 10.1145/3394486.3403333. 

- [10] L. Yan, Z. Qin, H. Zhuang, X. Wang, M. Bendersky, and M. Najork, ‘‘Revisiting two-tower models for unbiased learning to rank,’’ in _Proc. 45th Int. ACM SIGIR Conf. Res. Develop. Inf. Retr._ , New York, NY, USA, Jul. 2022, pp. 2410–2414, doi: 10.1145/3477495.3531837. 

   - [26] T. Qin, T.-Y. Liu, J. Xu, and H. Li, ‘‘LETOR: A benchmark collection for research on learning to rank for information retrieval,’’ _Inf. Retr._ , vol. 13, no. 4, pp. 346–374, Aug. 2010. 

   - [27] T. Qin and T.-Y. Liu, ‘‘Introducing LETOR 4.0 datasets,’’ 2013, _arXiv:1306.2597_ . 

   - [28] E. Serdyukov and W. Cukierski. (2013). _Personalized Web Search Challenge_ . [Online]. Available: https://kaggle.com/competitions/yandexpersonalized-web-search-challenge 

   - [29] O. Chapelle and Y. Chang, ‘‘Yahoo! Learning to rank challenge overview,’’ in _Proc. Learn. Rank Challenge, Proc. Mach. Learn. Res._ , vol. 14, 2011, pp. 1–24. [Online]. Available: https://proceedings.mlr.press/v14/ chapelle11a.html 

   - [30] Q. Ai, T. Yang, H. Wang, and J. Mao, ‘‘Unbiased learning to rank: Online or offline?’’ _ACM Trans. Inf. Syst._ , vol. 39, no. 2, pp. 1–29, Apr. 2021. 

   - [31] N. Ketkar and J. Moolayil, ‘‘Introduction to PyTorch,’’ in _Deep Learning With Python: Learn Best Practices of Deep Learning Models With PyTorch_ . Berkeley, CA, USA: Apress, 2021, pp. 27–91. 

   - [32] D. P. Kingma and J. Ba, ‘‘Adam: A method for stochastic optimization,’’ 2014, _arXiv:1412.6980_ . 

- [11] P. Hager, R. Deffayet, J.-M. Renders, O. Zoeter, and M. de Rijke, ‘‘Unbiased learning to rank meets reality: Lessons from Baidu’s large-scale search dataset,’’ in _Proc. 47th Int. ACM SIGIR Conf. Res. Develop. Inf. Retr._ , Jul. 2024, pp. 1546–1556. 

- [12] G. Zhou, X. Zhu, C. Song, Y. Fan, H. Zhu, X. Ma, Y. Yan, J. Jin, H. Li, and K. Gai, ‘‘Deep interest network for click-through rate prediction,’’ in _Proc. 24th ACM SIGKDD Int. Conf. Knowl. Discovery Data Mining_ , New York, NY, USA, Jul. 2018, pp. 1059–1068, doi: 10.1145/3219819.3219823. 

- [13] Y. Qu, B. Fang, W. Zhang, R. Tang, M. Niu, H. Guo, Y. Yu, and X. He, ‘‘Product-based neural networks for user response prediction over multifield categorical data,’’ _ACM Trans. Inf. Syst._ , vol. 37, no. 1, pp. 1–35, Jan. 2019, doi: 10.1145/3233770. 

- [14] H. Guo, R. Tang, Y. Ye, Z. Li, and X. He, ‘‘DeepFM: A factorizationmachine based neural network for CTR prediction,’’ 2017, _arXiv:1703.04247_ . 

- [15] K. Zhang, F. Lyu, X. Tang, D. Liu, C. Ma, K. Ding, X. He, and X. Liu, ‘‘Fusion matters: Learning fusion in deep click-through rate prediction models,’’ in _Proc. 18th ACM Int. Conf. Web Search Data Mining_ , Mar. 2025, pp. 744–753. 

- [16] K. Wang, H. Wang, W. Guo, Y. Liu, J. Lin, D. Lian, and E. Chen, ‘‘DLF: Enhancing explicit-implicit interaction via dynamic low-orderaware fusion for CTR prediction,’’ in _Proc. 48th Int. ACM SIGIR Conf. Res. Develop. Inf. Retr._ , Jul. 2025, pp. 2213–2223. 

- [17] K. Mao, J. Zhu, L. Su, G. Cai, Y. Li, and Z. Dong, ‘‘FinalMLP: An enhanced two-stream MLP model for CTR prediction,’’ in _Proc. AAAI Conf. Artif. Intell._ , 2023, vol. 37, no. 4, pp. 4552–4560, doi: 10.1609/aaai.v37i4.25577. 

K. J. AMALA received the B.Tech. degree in computer science and engineering from Cochin University of Science and Technology, and the M.E. degree in computer science from the Noorul Islam Centre for Higher Education. She is currently pursuing the Ph.D. degree in computer science and engineering with the Data Science and Business Systems, SRM Institute of Science and Technology, Tamil Nadu, India. 


![](prepared/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction/images/Neural_Learning_to_Rank_Model_With_Bias_Correction_and_Attention_Enhanced_Relevance_Prediction.pdf-0021-22.png)


She has qualified for the University Grants Commission (UGC) National Eligibility Test (NET) and has over 12 years of teaching experience in undergraduate and postgraduate computer science education. Her research interests include learning to rank, machine learning, and artificial intelligence. Her current research focuses on integrating contextual and positional biases into attention-based two-tower models for click prediction and modeling dynamic user behaviors using Bayesian nonparametric approaches. She has experience working with large-scale web search datasets and is dedicated to developing interpretable, adaptive, and user-centric information retrieval systems. 

- [18] X. Li, B. Chen, L. Hou, and R. Tang, ‘‘CTRL: Connect collaborative and language model for CTR prediction,’’ _ACM Trans. Recommender Syst._ , vol. 2023, pp. 1–24, Feb. 2023. 

- [19] H. Li, L. Sang, Y. Zhang, and Y. Zhang, ‘‘SimCEN: Simple contrastenhanced network for CTR prediction,’’ in _Proc. 32nd ACM Int. Conf. Multimedia_ , Oct. 2024, pp. 2311–2320. 

- [20] X. Liu, Z. Zeng, X. Liu, S. Yuan, W. Song, M. Hang, Y. Liu, C. Yang, D. Kim, W.-Y. Chen, J. Yang, Y. Han, R. Jin, B. Long, H. Tong, and P. S. Yu, ‘‘A collaborative ensemble framework for CTR prediction,’’ 2024, _arXiv:2411.13700_ . 

- [21] J. Qin, W. Zhang, R. Su, Z. Liu, W. Liu, G. Zhao, H. Li, R. Tang, X. He, and Y. Yu, ‘‘Learning to retrieve user behaviors for click-through rate estimation,’’ _ACM Trans. Inf. Syst._ , vol. 41, no. 4, pp. 1–31, Oct. 2023. 

- [22] H. T. Cheng, L. Koc, J. Harmsen, T. Shaked, T. Chandra, H. Aradhye, G. Anderson, G. Corrado, W. Chai, M. Ispir, and R. Anil, ‘‘Wide and deep learning for recommender systems,’’ in _Proc. 1st Workshop Deep Learn. Recomm. Syst._ , Sep. 2016, pp. 7–10. 

- [23] G. Zhou, N. Mou, Y. Fan, Q. Pi, W. Bian, C. Zhou, X. Zhu, and K. Gai, ‘‘Deep interest evolution network for click-through rate prediction,’’ in _Proc. AAAI Conf. Artif. Intell._ , 2019, vol. 33, no. 1, pp. 5941–5948, doi: 10.1609/aaai.v33i01.33015941. 

- [24] W. Chu, S. Li, C. Chen, L. Xu, H. Cui, and K. Liu, ‘‘A general framework for debiasing in CTR prediction,’’ 2021, _arXiv:2112.02767_ . 

- [25] Y. Deng, Z. Li, and Z. Song, ‘‘Attention scheme inspired softmax regression,’’ 2023, _arXiv:2304.10411_ . 

D. RAJESWARI received the B.Tech. degree in information technology from the Annai Mathammal Sheela Engineering College, Anna University, in 2008, the M.Tech. degree in information technology from the PSG College of Technology, Coimbatore, Anna University, in 2010, and the Ph.D. degree from the College of Engineering, Guindy, Anna University, in 2017, under the guidance of Dr. V. Jawahar Senthilkumar at the College of Engineering, Guindy, Anna University. She received a GATE stipend from 2008 to 2010 for completing M.Tech. degree. She received International Travel Support (ITS) from SERB to attend the 2023 POMS Annual Conference from 21 May to 25 May in USA. She is currently a Professor with the Department of Data Science and Business Systems, School of Computing, College of Engineering and Technology, SRM Institute of Science and Technology, Kattankulathur, India. 

188419 

VOLUME 13, 2025 

