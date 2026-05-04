
![](prepared/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning/images/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning.pdf-0001-00.png)


Received 24 June 2024, accepted 9 July 2024, date of publication 15 July 2024, date of current version 26 July 2024. _Digital Object Identifier 10.1109/ACCESS.2024.3428630_ 

## An Approach for Multi-Context-Aware Multi-Criteria Recommender Systems Based on Deep Learning 

## IFRA AFZAL , BURCU YILMAZEL , AND CIHAN KALELI 

Department of Computer Engineering, Eskişehir Technical University, 26555 Eskişehir, Türkiye 

Corresponding author: Cihan Kaleli (ckaleli@eskisehir.edu.tr) 

- **ABSTRACT** In an era where digital information is abundant, the role of recommender systems in navigating this vast landscape has become increasingly vital. This study proposes a novel deep learning-based approach integrating multi-context and multi-criteria data within a unified neural network framework. The model processes these dimensions concurrently, significantly improving the precision of personalized recommendations. Context-aware and multi-criteria recommender systems extend traditional two-dimensional user-item preference methods with context awareness and multiple criteria. In contrast to traditional methods, our approach intricately weaves together multi-context and multi-criteria data within its architecture. This concurrent processing enables sophisticated interactions between context and criteria, enhancing recommendation accuracy. While context-aware systems incorporate contextual information such as time and location when making recommendations, multi-criteria-based approaches offer a spectrum of evaluative criteria, enriching the user experience with more tailored and relevant suggestions. Although both approaches have advantages in producing more accurate and personalized referrals, context information and multi-criteria ratings have not been employed together for producing recommendations. Our research proposes a novel deep learning-based approach for the multi-context, multi-criteria recommender system to address this gap. In contrast to traditional approaches that process context-aware recommender systems and multi-criteria recommender systems separately, our deep learning model intricately weaves together multi-context and multi-criteria data within its architecture. This integration is not staged; both dimensions are concurrently processed through a unified neural network framework. The model facilitates a sophisticated interaction between context and criteria by embedding these elements into the core of the network’s multiple layers. This methodology enhances the system’s adaptability and significantly improves its precision in delivering personalized recommendations, leveraging the compounded effects of contextual and criteriaspecific insights. The proposed model shows superior performance in predictive tasks, achieving the lowest Mean Absolute Error (MAE) and Root Mean Square Error (RMSE) on the TripAdvisor and ITMRec datasets compared to other state-of-the-art recommendation techniques. Context-aware multi-criteria ratings data demonstrate the robustness and accuracy of the model. 

**INDEX TERMS** Context-aware, deep learning, multi-criteria, recommender systems. 

## **I. INTRODUCTION** 

In the digital age, where the abundance of online information continues to grow at an unprecedented rate, the World 

The associate editor coordinating the review of this manuscript and approving it for publication was Renato Ferrero . 

Wide Web has evolved into an intricate maze of data and choices. Popular platforms such as Google, Amazon, and Netflix are increasingly burdened with assisting users in navigating this vast and complex digital landscape. This scenario underscores the indispensability of recommender systems (RSs) [1], which have emerged as pivotal tools in 

2024 The Authors. This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4.0/ 

99936 

VOLUME 12, 2024 

I. Afzal et al.: Approach for Multi-Context-Aware Multi-Criteria Recommender Systems 


![](prepared/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning/images/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning.pdf-0002-01.png)


filtering and personalizing online content. RSs are no longer a luxury but a necessity, playing a crucial role in enhancing user experience by tailoring suggestions to individual preferences. RSs analyze users’ preferences and behaviours to help them find relevant goods, services, and content. It has been widely utilized across a variety of industries and applications, including movies (e.g., Netflix), e-news (e.g., Yahoo! News Today), music (e.g., Spotify), e-commerce (e.g., Amazon.com), social networks (e.g., Facebook), tourism (e.g., TripAdvisor), etc. The traditional recommendation system, also known as a two-dimensional recommender system, has limitations because it only considers two dimensions of information about users and items [2]. Moreover, conventional recommendation algorithms frequently experience cold start, data spars ity, and scalability problems, which may affect the accuracy of recommendations [3]. 

Recent advancements in RSs have led to the development of innovative models to enhance recommendation accuracy and support a broader range of applications. A notable instance of this evolution is the emergence of context-aware recommender systems (CARS) [4], representing a paradigm shift in RS technology. CARS distinguishes itself by integrating contextual information— such as temporal, spatial, and environmental factors—into the recommendation process, thereby refining its ability to deliver personalized and situation-specific suggestions. The dynamic nature of user preferences, which exhibit variations across different contextual scenarios, underscores the criticality of context awareness in the design of recommender systems. Specifically, user preferences are not static but are influenced by multiple contextual dimensions. For instance, the selection process in movie recommendations is not solely content-driven. Still, it is also shaped by an amalgamation of situational factors, including but not limited to the accompanying viewer(s), temporal aspects, geographic location, and the user’s current emotional state. Empirical research [5] provides evidence supporting the hypothesis that incorporating such multi-dimensional context parameters significantly enhances the efficacy and accuracy of recommender systems. On the other hand, multi-criteria recommender systems (MCRS) represent an alternative paradigm in recommendation technology, leveraging user preferences across a spectrum of criteria to generate more nuanced and compelling recommendations, as delineated in Adomavicius et al. [6]. A practical illustration of this approach is evident on platforms like TripAdvisor.com, where users are invited to evaluate hotels not merely on an overall satisfaction scale but across a diverse array of specific attributes, including room service quality, location convenience, cleanliness standards, and more. This multi-criteria evaluation framework is instrumental in capturing a more comprehensive and accurate representation of user tastes, a concept substantiated by the findings of Batmaz and Kaleli [7], despite their promise and efficacy, as documented in studies like [2], [8], and [9], both CARS and MCRS 

have predominantly been deployed in isolation in real-world applications, spanning the entertainment, music, and tourism sectors. This observation highlights a significant opportunity for synergistic integration in future recommender system design and application. 

Recommender system accuracy, relevance, and user satisfaction improve when context and multi-criteria ratings are integrated [10], [11], [12]. Personalization is enhanced when an RS can tailor recommendations to individual users more accurately by considering multiple contexts, such as time and location and multiple criteria, such as user preferences and item features. References [13] and [14]. Improved relevance is an additional benefit of integrating CARS with MCRS. When the recommender system leverages the contexts and criteria, it can better comprehend the user’s perspective and intent [15]. For instance, restaurant recommendations should be provided based on the user’s food preferences and factors like location, weather, and time of day. Overspecialization problems occur when users are exposed to a limited amount of content. This problem can be mitigated by both CARS and MCRS [16], [17]. Therefore, integrating both may provide more diverse recommendations instead of repeatedly providing the same recommendations to the users. So, a user can experience new and relevant items that he may not have encountered. The recommender system can make significant recommendations even for new users or items with little previous data when multi-criteria ratings and context are incorporated [18]. By utilising several factors like item features and user demographics, the system can provide well-informed recommendations without depending exclusively on past interactions, which leads to dealing with cold start problems [19]. Providing more relevant, tailored, and varied recommendations is the ultimate goal of combining multi-context and multi-criteria ratings, which also increases user satisfaction and engagement [20]. User loyalty and retention increase with the system when it comprehends their preferences and provides meaningful suggestions in various circumstances. Ultimately, the advantages of the integration lead to more effective and user-centric recommendations, which benefit both users and the recommendation platform. 

Deep Learning (DL) has profoundly impacted various research domains, notably RSs. Within this realm, Deep Neural Networks (DNNs) have demonstrated a remarkable capacity for modelling complex, nonlinear interactions between users and items, a capability extensively reviewed in Batmaz et al. [3]. The fusion of DNN architectures with the contextual sensitivity of CARS and the multifaceted evaluation approach of MCRS presents a compelling opportunity. This integration aims to harness the strengths of both CARS and MCRS, alongside leveraging the inherent nonlinearity in DNNs, to substantially elevate recommendations’ accuracy. The primary goal of the proposed research is to architect and implement a sophisticated recommendation framework based on advanced DNN algorithms. This framework will intricately consider multiple contextual dimensions and 

99937 

VOLUME 12, 2024 

I. Afzal et al.: Approach for Multi-Context-Aware Multi-Criteria Recommender Systems 


![](prepared/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning/images/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning.pdf-0003-01.png)


diverse user criteria, thereby delivering recommendations that are not only highly personalized but also profoundly aligned with users’ specific needs and preferences. The ambition is to transcend traditional recommendation models by infusing them with the analytical prowess of deep learning, thereby setting a new benchmark in personalized recommendation systems. 

Our proposed recommender system architecture is bifurcated into two distinct yet interconnected components. In the initial phase, we meticulously extract contextual conditions and multi-criteria item ratings, channelling them into a composite model leveraging a DNN framework. The second phase employs a sophisticated DNN-based Multi-Contextaware Multi-Criteria Recommender System (MCoMCRS) model. This model can predict overall item ratings by processing and synthesizing multiple contextual factors and criteria-based evaluations. 

Furthermore, our model has undergone rigorous testing in a variant configuration known as the Single-Context-aware Multi-Criteria Recommender System (SCoMCRS), where it operates under the constraint of a singular contextual dimension. To our knowledge, our research is pioneering in applying multi-contextual data within a DNN-based MCRS framework. While recent literature [10], [11], [12], [21] has made strides in integrating context-awareness and multicriteria decision-making with advanced computational techniques, these studies predominantly focus on single-context applications. Specifically, Zheng et al. [11] implemented traditional machine learning algorithms to fuse context awareness with multi-criteria decision-making processes in recommender systems, primarily focusing on educational data. This study serves as a foundational reference point, highlighting the potential of context integration in enhancing recommendation accuracy, albeit within a more traditional computational framework. Also, we observed that our proposed model leads to significant improvements over other state-of-the-art methods based on experiments on real-world Tripadvisor and ITM-Rec datasets. Our contributions to this research can be summed up as follows: 

- 1) We present a novel approach using deep learning by integrating multi-context and multi-criteria recommender systems. 

- 2) Using multi-criteria ratings based on multi-context, we employ the DNN model to predict the overall rating. 

- 3) On a real-world dataset, we evaluate the recommendation efficacy of the proposed approach against benchmark methods from the relevant state-of-the-art. 

- 4) Additionally, we compare the proposed approach with single-context MCRS to highlight the significance of multi-context in MCRS. 

The rest of the paper is organized as shown below. The literature review is given in Section II, and the background knowledge is briefly reviewed in Section III. Section IV presents our proposed deep learning approach for multicontext, multi-criteria recommender systems. The experiment is explained in Section V, along with the evaluation 

outcomes. The article is concluded in Section VII by summarizing the significant findings and outlining potential directions for further research. 

## **II. RELATED WORK** 

The deployment of DL techniques in RS has seen a notable expansion thanks to their advanced feature extraction and adaptive learning capabilities. The progression in DL methodologies has propelled the enhancement of complex RS, which now includes diverse strategies such as contextaware recommendations [22], group-centric recommendation models [23], multi-criteria recommendation systems [7], trust-based filtering approaches, and tag-driven recommendation mechanisms [24]. Rigorous empirical investigations, like those conducted in citebatmaz2019review, have corroborated that DL-based RSs predominantly surpass traditional models in performance. These systems are proficient in analyzing and interpreting complex user preferences and behaviours, enabling them to generate more precise and personalized recommendation outcomes. Therefore, integrating DL into RSs significantly advances their predictive efficacy and personalization aspect, which is tailored to individual user needs. 

CARS capitalizes on integrating contextual variables such as temporal factors, meteorological conditions, and geographical locations, which are pivotal in tailoring user preferences to enhance the effectiveness of recommendation outputs. The necessity for RSs to be context-sensitive stems from the variability of user preferences contingent on specific contexts. The seminal incorporation of contextual information into RSs was pioneered by Adomavicius et al. [25], illustrating its substantial influence on the refinement of recommendation accuracy. Since then, CARS has been instrumental in augmenting the functionality of RSs across diverse sectors. In recent developments, DL-based CARS have emerged, marking a significant enhancement in the capabilities of RSs and addressing prevalent challenges within the field. Unger et al. [26] proposed three deep context-aware recommendation models that employ explicit, unstructured, and structured latent representations of various contextual data. Their empirical analysis demonstrated that these DL-based context-aware models surpass traditional machine learning-based CARS models in performance. Further advancing the field, a DL-based CARS model delineated by Jeong and Kim [22] integrates autoencoders and neural networks to extract and analyze multiple contextual factors, thereby predicting user preferences with greater accuracy by considering both user and item characteristics. Additionally, a deep recurrent neural network-based contextaware restaurant recommender model, developed by Boppana and Sandhya [27], achieved a significant accuracy rate. Complementing these advancements, the DeepCARSKit, an open-source DL-based recommendation library developed by Zheng [28], offers specialized support for CARS-specific evaluations. Jeong and Kim [29] have introduced the latest 

99938 

VOLUME 12, 2024 

I. Afzal et al.: Approach for Multi-Context-Aware Multi-Criteria Recommender Systems 


![](prepared/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning/images/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning.pdf-0004-01.png)


innovation in this domain, focusing on the temporal evolution of user preferences. Their approach employs a preference transition matrix to trace alterations in user preferences, segmenting data into discrete time units to address temporality in recommendations effectively. 

MCRS has increasingly gained attention for its capability to generate refined recommendations by evaluating user preferences across multiple criteria. Integrating deep learning in MCRS models has recently been a focus of research. A pioneering approach using deep neural networks to incorporate multi-criteria ratings in RS was introduced by Tallapally et al. [30]. They innovated the network’s input layer and loss function to unravel the nonlinear associations between multi-criteria ratings and their overall ratings. Their research demonstrated the model’s superiority over traditional stateof-the-art recommendation methods by utilizing two realworld datasets. Further advancements in this field include the work of Batmaz and Kaleli [7], who implemented an autoencoder-based model to independently predict user ratings for each criterion and a multilayer perceptron (MLP) to estimate the overall ratings. Another significant contribution is the Deep Multi-Criteria Collaborative Filtering (DMCCF) by Nassar et al. [31], which uniquely combines deep learning, multi-criteria, and collaborative filtering. They utilized two DNNs to predict criteria ratings and their correlation to the overall rating, employing an aggregation-function-based methodology. Batmaz and Kaleli [32] proposed a novel similarity-based multicriteria collaborative filtering approach using autoencoders to tackle the data sparsity issue. This approach processes sparse multi-criteria user/item preferences to extract nonlinear, low-dimensional, dense features, showing effectiveness against the sparsity problem in their experimental findings. 

Integrating CARS with MCRS to enhance RS performance has also been a significant area of focus. Research efforts by Zheng et al. [11], Dridi et al. [10], [21], and Vu and Le [12] have explored combining CARS and MCRS using both machine learning and deep learning techniques. Zheng et al. integrated CARS into four MCRS baseline models using ITM-Rec, employing context-aware matrix factorization (CAMF) for contextual frameworks and various methods for multi-criteria rating predictions and aggregations. Dridi et al. [21] applied spectral partitioning graph techniques to identify contextually relevant participant sub-groups, using matrix factorization and aggregation operations for rating predictions and aggregations. Their subsequent work [10] explored a triplet data clustering method for users with similar contexts rating items based on similar criteria. Vu and Le [12] proposed a DNN-based approach for multi-criteria recommendations considering a single context. However, most studies, except [10], [11], have focused on a single context and predominantly employed traditional machine learning methods, indicating a need for further exploration in integrating CARS and MCRS using DL to enhance RS performance. However, we intend to use DNN for 

recommendations that consider multiple contexts and criteria, which differ from previous studies. 

## **III. BACKGROUND** 

Recommender systems play a crucial role in helping users navigate the overwhelming abundance of choices in various domains by providing personalized suggestions tailored to their preferences [33]. Traditional RS have historically employed a range of methodologies to anticipate user preferences, including content-based filtering (CBF), collaborative filtering (CF), and hybrid recommendation approaches [34], [35], [36]. CBF methodologies analyze item features users have previously favoured or disfavored [37]. Conversely, CF relies on the assumption that users with similar preferences tend to make comparable future selections, thus identifying affinities among users to formulate recommendations [38], [39]. Hybrid recommendation approaches combine elements of both CBF and CF methodologies to offer enhanced suggestions [40]. However, these methodologies are constrained to considering solely two dimensions of information—user-profiles and item content features—for predictive purposes [25]. The evolution of recommender systems has witnessed the development of more sophisticated approaches tailored to address diverse user needs and preferences. Key among these are Context-Aware Recommender Systems (CARS) and Multi-Criteria Recommender Systems (MCRS). MCRS evaluates multiple attributes such as price and quality to provide nuanced recommendations [6], [34], [41], [42]. Conversely, CARS enhances recommendation relevance by incorporating contextual factors such as temporal and spatial variables [4], [21], [25], [43]. The integration of these approaches holds the potential to yield more refined and precise recommendation outcomes. 

## _A. CONTEXT-AWARE RECOMMENDER SYSTEM_ 

Context in recommender systems is defined as any situational information that can affect the decision-making process, such as time, location, and user activity [25], [44]. CARS takes personalization to the next level by considering contextual information, refining user preference predictions and adapting suggestions to current circumstances. Unlike traditional systems that provide static recommendations, CARS adapt recommendations based on the user’s current context, enhancing relevance and utility. By leveraging contextual information, these systems provide recommendations that are more timely, relevant and aligned with the user’s current needs and preferences. CARS offer a more adaptable and user-centric experience, ensuring that recommendations remain relevant across diverse contexts and usage scenarios [4], [25], [45]. 

The mathematical representation of CARS is given by the rating function: 


![](prepared/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning/images/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning.pdf-0004-11.png)


99939 

VOLUME 12, 2024 

I. Afzal et al.: Approach for Multi-Context-Aware Multi-Criteria Recommender Systems 


![](prepared/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning/images/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning.pdf-0005-01.png)


This function _R_ extends to consider multiple contextual dimensions, shown as _C_ 1 _, C_ 2 _, . . . , Cn_ , which significantly improve the accuracy of predictions by adapting to the user’s specific situation. 

Consider an illustrative scenario involving two users, U1 and U2, interacting with two different music tracks, T1 and T2, under three different contextual features: _Location_ (at home, at work), _Weather_ (sunny, cloudy, snowy, rainy), and _Mood_ (happy, sad, angry, surprise). The impacts of these conditions on their ratings are illustrated in Table 1, which shows significant variations in ratings based on changes in context, such as different locations or times of the day. For instance, U1 rates T1 differently with the context (Home, Sunny, Happy) compared to the context (Work, Snowy, Angry), even though it is the same music track, which is also same for U2. This example highlights how contextual information can significantly influence recommendation outcomes [46]. 

**TABLE 1.** Impact of Context on Music Track Ratings. 


![](prepared/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning/images/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning.pdf-0005-05.png)


**TABLE 2.** Multi-Criteria Movie Ratings. 


![](prepared/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning/images/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning.pdf-0005-07.png)


contextually appropriate recommendations and is deeply aligned with user-specific criteria, promising a significantly enhanced user experience. 

## **IV. THE PROPOSED ALGORITHM** 

Our study spearheads the development of an advanced MultiContext Multi-Criteria (MCoMC) algorithm anchored in deep learning. This algorithm embodies a nuanced neural network architecture meticulously designed to amalgamate many contextual variables with a multi-dimensional spectrum of criteria assessments. The primary aim is to delineate an accurate forecast of user preferences. Since our model utilizes multi-criteria ratings along with multiple contexts, (1) and (2) can be combined as (3). 


![](prepared/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning/images/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning.pdf-0005-11.png)


## _B. MULTI-CRITERIA RECOMMENDER SYSTEM_ 

RSs are commonly assessed based on a single criterion, like the overall user rating for an item, which may present limitations as users often consider multiple factors in their decision-making process. MCRSs seek to overcome this constraint by incorporating item ratings across various criteria, such as quality, service, or price. This way, MCRS offers more comprehensive and personalized recommendations and provides users with a broader range of options that better align with their diverse preferences and constraints than single-criteria systems. Additionally, MCRSs can address conflicting objectives and trade-offs, enabling users to make more informed decisions [3], [42]. The function for an MCRS is given by: 


![](prepared/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning/images/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning.pdf-0005-14.png)


Here, _Ro_ is the overall rating, while _R_ 1 _, R_ 2 _, . . . , Rk_ represents the ratings for each criterion, allowing users to specify preferences on multiple dimensions. 

The table below shows an example of multi-criteria ratings, where users evaluate different aspects of movies. This multidimensional evaluation helps form a comprehensive understanding of user likes and dislikes, delivering highly personalized recommendations. 

These comprehensive evaluations from MCRS, combined with CARS’s contextual adaptability, could potentially lead to groundbreaking advances in the development of recommender systems. Integrating these two systems allows for 

In (3), _r_ signifies the predictive rating function, targeting an item _y_ for a user _x_ , factoring in criteria _cr_ within a specific context _co_ . This function is engineered to offer a holistic prediction across various items. A deep learningbased (MCoMC) model must undergo several phases to integrate multi-context and multi-criteria ratings, including dataset preparation, model design and training, loss function formulation, and model evaluation. Below is a thorough breakdown of every step: 

- 1) **Multi-context, multi-criteria Dataset preparation:** To construct a dataset that supports our deep learning model, we developed a systematic approach using Python to extract and preprocess data that includes multiple criteria and contexts. This method is designed to be adaptable to any dataset enriched with varied usergenerated content, focusing on ensuring the algorithm’s robustness across different application domains. The preparation process involves several critical steps to optimize the data for our model: 

   - **Data Extraction:** We extract relevant features that represent both the contextual information (such as time, location, and companion) and multiple evaluative criteria (such as quality, service, and value). This ensures a rich dataset that can capture the complexity of user preferences and scenarios. 

   - **Handling Missing Values:** We employ mean imputation to mitigate the effects of missing data, which can skew the analysis and model training. This technique helps maintain data integrity by 

99940 

VOLUME 12, 2024 

I. Afzal et al.: Approach for Multi-Context-Aware Multi-Criteria Recommender Systems 


![](prepared/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning/images/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning.pdf-0006-01.png)


   - providing a statistically reasonable substitute for missing entries. 

   - **Data Encoding:** Contextual and criteria data are often categorical and must be converted into a format suitable for machine learning models. We use one-hot encoding to transform these categorical variables into binary vectors, enabling efficient processing by neural networks. 

   - **Feature Scaling:** We apply Min-Max scaling to all features to normalize the data into a uniform scale of [0,1]. This step is crucial for avoiding the dominance of features simply because of their scale and helps speed up the model’s convergence during training. 

   - These preprocessing steps are essential for preparing the data to maximise the effectiveness of the subsequent modelling steps, ensuring that our model can learn from well-structured and consistent input data. 

   - The procedural blueprint of our model, extending from the initial stage of data ingestion to the culminating stage of predictive output generation, is systematically illustrated in Fig. 1. 

   - The preparatory phase of our algorithm is dedicated to curating datasets that encapsulate a wide range of contexts and criteria, all of which are subject to user ratings. This phase involves meticulously assembling a multidimensional array, drawing data from the extensively detailed TripAdvisor [7] and the comprehensive ITM-Rec [47]. These datasets are characterized by their multi-criteria ratings, encompassing both overall ratings and a multitude of contextual variables.We used multi-context with multi-criteria ratings as an interlock throughout the DL model. 

   - When a user has not provided a rating for a particular item, the dataset defaults to a mean value, ensuring continuity and consistency in data interpretation. 

- 2) **Deep neural network Construction:** Following dataset preparation, we construct a bespoke DNNbased MCoMCRS. This network is not merely a collection of layers but a carefully calibrated system of interconnected nodes, each playing a pivotal role in processing and interpreting complex data patterns. The architectural design of the network includes an input layer, which acts as the gateway for the multicriteria and contextual data. Multiple hidden layers are employed to enable the network to uncover and learn intricate data relationships, with the number of these layers being a deliberate choice based on the complexity of the dataset and the problem at hand. For our specific application, we have opted for three hidden layers. The activation function selected is the Rectified Linear Units (ReLU), elegantly described by (4) as follows: 


![](prepared/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning/images/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning.pdf-0006-10.png)


where _z_ represents any hidden layer’s input. The choice of ReLU is strategic, given its proven efficacy 

in introducing non-linearity, thereby enhancing the network’s ability to model complex functions. A dropout regularization technique with a rate of 0.2 is incorporated to augment the network’s robustness and prevent overfitting. Furthermore, the Adam optimizer is integrated into the network for its renowned efficiency and resilience to noisy data. 

- 3) **Loss Function:** Loss functions guide the network’s learning process - specifically, Mean Absolute Error (MAE) and Root Mean Square Error (RMSE). These functions are pivotal in fine-tuning the network’s parameters, a process achieved through rigorous experimentation to identify the optimal configuration. 

- 4) **Neural Network Training:** In the concluding phase, the MCoMCRS model undergoes rigorous training and testing using the earlier dataset. The dataset is strategically divided into distinct segments: 70% for training, 10% for validation, and the remaining 20% for testing purposes. The objective of this phase is twofold: to refine the neural network weights for minimal loss function values and to elevate the model’s predictive prowess. Through empirical testing, we identified 150 epochs as the ideal number for training iterations. Upon completing the training process, the model’s predictions incorporate multi-criteria ratings and diverse contextual variables to compute an aggregate prediction for each item, as shown in Fig. 1. 

- 5) **Model Evaluation:** The final stage thoroughly evaluates the model, juxtaposing its performance against other baseline models. This comparative analysis is pivotal in ascertaining the efficacy and superiority of our proposed MCoMCRS algorithm over existing methodologies. 

The detailed pseudo-code for the algorithm is delineated in Algorithm 1 for comprehensive understanding and replication. 

It is essential to confirm that our newly proposed method, which includes a DNN, multi-contextual conditions, and Multi-criteria ratings, is superior to the existing methods, which use either DNN on MCRS or DNN on CARS. 

## **V. EXPERIMENTAL WORKS** 

## _A. DATASETS AND EVALUATION MEASURES_ 

In this section, we detail the datasets utilized for evaluating the proposed MCoMCRS model, describing their scale and the context in which they were applied. These datasets demonstrated the model’s effectiveness in handling multi-criteria and multi-context data in real-world scenarios. 

We conducted extensive experiments using the TripAdvisor and ITM-Rec datasets (Table 3). The TripAdvisor dataset, sourced from [7], contains 3,708 ratings across 485 hotels, with ratings from 3,494 users. It includes four contextual dimensions: trip companion, trip reason, meal, and season, each with various contextual conditions (e.g., trip companion includes nine conditions like family, friend, etc.). Additionally, the dataset has six item criteria: location, 

99941 

VOLUME 12, 2024 

I. Afzal et al.: Approach for Multi-Context-Aware Multi-Criteria Recommender Systems 


![](prepared/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning/images/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning.pdf-0007-01.png)


## **Algorithm 1** MCoMCRS Algorithm 

**Input:** dataset _Rco_ × _c_ × _x_ × _y_ // co: context, c: rating criteria, x: user, y: item 

**Output:** _Px_ × _y_ // overall prediction of ratings 

**Phase 1:** Multi-context, Multi-criteria Dataset Preparation 

- 1) Extract the number of criteria, context, users, and items from _Rco_ × _c_ × _x_ × _y_ 

- 2) For each criterion, context Do: 

   - a) Fill missing values with mean 

   - b) Split dataset into the random train, validation, and test sets 

- **Phase 2:** Deep Neural Network Construction 

- 1) Define input and output layer sizes based on feature dimensions 

- 2) Define the architecture of hidden layers (e.g., number of layers, neurons per layer) 

- 3) Initialize weights (consider advanced initialization techniques) 

- 4) Define activation function: ReLU 

- 5) Define regularization (Dropout = 0.2, explore other regularization methods) 

- 6) Define optimizer: Adam 

- 7) Define loss function: MAE 

- 8) Define the number of epochs 

- **Phase 3:** Training Validation and Testing 

- 1) For each epoch Do: 

   - a) Input contexts, criteria, user, and item features into the neural network 

   - b) Forward pass through the layers 

   - c) Calculate loss 

   - d) Update weights and biases using backpropagation and Adam optimizer 

- 2) Compute the overall rating for the test set using the trained model 

- 3) Calculate test set loss 

- 4) Report model performance 

cleanliness, value, rooms, service, and sleep quality, with an overall rating scale of 1 to 5. 

The ITM-Rec dataset from [47], spanning 2017 to 2022, includes 5,230 ratings from 454 users for 70 students. It features three contextual dimensions: Class (DB, DS, DA), Semester (Spring and Fall), and COVID-19 lockdown periods (PRE, DUR, POS). Ratings include an overall score and three item criteria: App, Data, and Ease. 

**TABLE 3.** Dataset Description. 


![](prepared/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning/images/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning.pdf-0007-31.png)


The substantial volume and variety of these datasets underscore the robustness of our experimental results and 

demonstrate the capability of our model to handle complex, large-scale data environments. 

We divided each dataset into training, validation, and testing segments following a 70-10-20 split to ensure a comprehensive evaluation of the model’s performance across different configurations. Preprocessing steps included one-hot encoding of categorical variables and normalization of continuous variables to ensure uniform input scales for the neural network. 

We adopted MAE and RMSE as our primary evaluation metrics, following the standard in rating prediction tasks [48]. These metrics are defined in (5) and (6), respectively, where _xi_ is the actual rating, _x_ ˆ _i_ is the predicted rating, and n is the total amount of rating data in the testing dataset, and thereby lower values denote higher prediction accuracy. 


![](prepared/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning/images/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning.pdf-0007-36.png)


## _B. IMPLEMENTATION DETAILS_ 

Python has been used to implement the proposed MCoMC recommendation algorithm using Keras 2.11.0 and TensorFlow backend. 

After empirical evaluations, the parameter values were subsequently established as constants to ascertain optimal parameter configurations. Detailed in Table 4, the DNN utilized for training both MCoMCRS datasets incorporates an input layer with 64 neurons,three-layer hidden architecture (128→128→64) with several predetermined hyperparameters: batch size set to 50, activation function specified as Rectified Linear Unit (ReLU), and a learning rate of 0.01. Additionally, the network employs a dropout regularization rate of 0.2. For both datasets, the training epochs were standardized at 150. The network’s output is derived from a singular neuron in the output layer, responsible for generating the overall rating. The DNN employs both MSE and RMSE as loss functions. 

The flowchart in Fig. 2 illustrates the flowchart of the proposed DNN-based MCoMCRS. This diagram outlines each step, from data preprocessing to the final recommendation output, providing a clear overview of the model’s operational framework. This DNN model is trained iteratively; preprocessing and splitting the data are the first steps, followed by initializing inputs and training the model. Next, the model is evaluated, and the final output is generated. If the minimum error value is not attained, hyperparameter tuning and parameter updates are carried out until optimal performance is reached. 

## **VI. EXPERIMENTAL RESULTS** _A. BASELINE ALGORITHMS_ 

Extensive experiments were conducted on tourism and educational datasets to validate the proposed MCoMCRS’s 

99942 

VOLUME 12, 2024 

I. Afzal et al.: Approach for Multi-Context-Aware Multi-Criteria Recommender Systems 


![](prepared/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning/images/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning.pdf-0008-01.png)



![](prepared/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning/images/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning.pdf-0008-02.png)


**FIGURE 1.** Operational Framework of the Proposed Model. 

**TABLE 4.** MCoMCRS DNN Settings. 


![](prepared/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning/images/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning.pdf-0008-05.png)


- Additionally, it was imperative to ascertain if a DNN-based integration of CARS and MCRS surpasses existing deep learning methods in prediction accuracy. For this purpose, separate implementations of MCRS and CARS using a DNN approach were conducted as per [31]. 

## _B. RESULTS AND DISCUSSION_ 

efficacy. Our model was benchmarked against five distinct baselines within CARS and MCRS. 

- The baseline SCRS (Single Criteria Recommender System) employs a Matrix Factorization (MF) technique as delineated in [49]. 

- In the MCRS framework, Matrix Factorization is utilized to forecast individual criterion ratings, with linear regression determining the weighting of each criterion [50]. The overall rating is then deduced using a linear regression-based aggregation of these criterionspecific ratings. 

- For CARS, both single-context (Single-Context Recommender System, SCoRS) and multi-context (MultiContext Recommender System, MCoRS) variants were considered. The models selected for comparison include Item Splitting-BiasdMF, User Splitting-BiasdMF, User Item Splitting-BiasdMF, CAMF (Context-aware Matrix Factorization), CAMF-C, CAMFCI (CAMF ContextItem), and CAMF-CU (CAMF Context-User), all referenced from [51]. 

In this study, we developed a novel model predicated on multi-context principles to enhance rating prediction by amalgamating CARS with MCRS. Regarding predictive accuracy, the objective was to ascertain if this integration could surpass traditional RS, including SCRS, MCRS, and CARS. The comparative analysis, detailed in Tables 5 and 6, evaluated two specific models: (i) a DNN-integrated singlecontext MCRS and (ii) a DNN-integrated multi-context MCRS. These evaluations were conducted on TripAdvisor and ITM-Rec datasets, respectively, with MAE and RMSE as the performance metrics. Lower values of MAE and RMSE, as evidenced in Table 5 and 6, indicate the superior efficacy of the proposed models. 

The proposed MCoMCRS model stands out in both datasets, achieving the lowest MAE and RMSE. This consistent performance across different data types – one from a travel review platform (TripAdvisor) and the other from an educational context – underlines the model’s robustness and adaptability. The superiority of MCoMCRS suggests that its underlying methodology, possibly involving advanced 

99943 

VOLUME 12, 2024 

I. Afzal et al.: Approach for Multi-Context-Aware Multi-Criteria Recommender Systems 


![](prepared/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning/images/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning.pdf-0009-01.png)



![](prepared/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning/images/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning.pdf-0009-02.png)



![](prepared/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning/images/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning.pdf-0009-03.png)



![](prepared/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning/images/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning.pdf-0009-04.png)



![](prepared/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning/images/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning.pdf-0009-05.png)



![](prepared/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning/images/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning.pdf-0009-06.png)



![](prepared/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning/images/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning.pdf-0009-07.png)



![](prepared/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning/images/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning.pdf-0009-08.png)



![](prepared/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning/images/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning.pdf-0009-09.png)


**FIGURE 2.** Flowchart of the DNN-based MCoMCRS. 

**TABLE 5.** Comparative Performance of The Proposed Models with Various Predictive Models on the TripAdvisor Dataset. 

**TABLE 6.** Comparative Performance of The Proposed Models with Various Predictive Models on the ITM-Rec Dataset. 


![](prepared/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning/images/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning.pdf-0009-13.png)



![](prepared/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning/images/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning.pdf-0009-14.png)


feature handling or sophisticated interaction modelling, effectively captures the nuances of user preferences and item characteristics across varied domains. 

Deep learning-based models like DL-MCRS and SCoMCRS also exhibit strong performance, particularly compared to traditional matrix factorization methods such as MF and MF-LR. This difference in performance can be attributed to the ability of deep learning models to capture non-linear 

99944 

VOLUME 12, 2024 

I. Afzal et al.: Approach for Multi-Context-Aware Multi-Criteria Recommender Systems 


![](prepared/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning/images/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning.pdf-0010-01.png)


relationships and complex patterns in the data, which traditional linear models might miss. The high performance of these models, especially in the TripAdvisor dataset, could also indicate the presence of complex, non-obvious patterns in user-item interactions that are more effectively captured by deep learning architectures. 

The varying success of user, item, and UI-splitting strategies in the SCoRS and MCoRS models suggests that how data is partitioned and processed can significantly impact model performance. While improving upon basic matrix factorization approaches, these strategies still do not match the efficacy of deep learning models, hinting at their limitations in fully capturing the intricacies of user-item interactions. 

The CAMF variants, with their context-aware mechanisms, show mixed results. Their performance fluctuations between the datasets indicate a sensitivity to the type of data and the specific contextual factors at play. This variability points to the importance of tailoring context-aware models to the specific features and characteristics of the dataset. 

The smaller performance gaps among models in the ITM-Rec dataset compared to the TripAdvisor dataset suggest differences in dataset complexity or structure. The ITM-Rec dataset could be more homogeneous or less sparse, making it easier for various models to achieve similar levels of accuracy. This observation underscores the importance of understanding dataset characteristics when evaluating and selecting models for specific applications. 

The consistency in the performance of most models across both datasets speaks to their robustness and generalizability. However, the exception, seen in the performance of DL-CARS in the ITM-Rec dataset, raises important questions about model overfitting or the model’s adaptability to different types of user-item interaction data. 

Consequently, to prevent overfitting and underfitting, hyper-parameter tuning is performed for the proposed MCoMCRS on both datasets. This involves changing the method’s parameters, such as learning rate, epochs, number of layers, etc., and observing changes in its performance. Then, select a model with a minimum error rate. 

This study uses a three-layered model, as explained in Section V. There are 64 neurons in the input layer, (128→128→64) neurons in the three hidden layers, and 1 neuron in the output layer. ‘‘ReLU’’ activation function is used for the input and hidden layers. Our model uses a deep learning framework like Keras to build a sequential neural network. This model has several dense (fully connected) layers and dropout layers. Fig 3 illustrates the interconnections between layers in the model. The number of parameters is calculated by multiplying the number of inputs by the number of outputs and adding the number of biases in the layer. Based on the calculation, the input layer has ((40 × 64) + 64 = 2560) parameters. To prevent overfitting, the dropout layer with a dropout rate of 0.2 randomly sets 20% of input units to 0 during training. There are three hidden layers with the 

parameters ((64 × 128) + 128 = 8320), ((128 × 128) + 128 = 16512) and ((128 × 64) + 64 = 8256) respectively. The output layer has (64 × 1) + 1 = 65 parameters. The total parameters for this model are 35713. We trained parameters using Keras’s ‘‘model.fit()’’ method. The model.summary() method produces the summary output shown in Figure 3. 


![](prepared/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning/images/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning.pdf-0010-10.png)


**FIGURE 3.** Model_Summary. 

Our model’s generalization ability was rigorously evaluated through a series of experiments detailing the training loss versus validation loss over the number of epochs for both datasets, as illustrated in Fig. 4. These plots demonstrate that the gap between training and validation loss remains stable as the number of epochs increases, suggesting robust generalizability of our model. 

In Fig. 4, the SCoMCRS and MCoMCRS models are represented, showing the validation and training losses for the TripAdvisor and ITM-Rec datasets. The Y-axis represents the loss levels, while the X-axis represents the number of epochs. It is observed that both training and validation losses decrease sharply within the initial 20 epochs and continue to decline more gradually up to 150 epochs. The minimal gap between the training and validation losses and their concurrent reduction suggests effective handling of overfitting. 

To combat overfitting specifically, our deep neural network employs techniques such as dropout regularization, batch normalization, and early stopping. Dropout regularization helps prevent the model from becoming overly dependent on any single or small group of neurons by randomly dropping units during the training process. Batch normalization 

99945 

VOLUME 12, 2024 

I. Afzal et al.: Approach for Multi-Context-Aware Multi-Criteria Recommender Systems 


![](prepared/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning/images/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning.pdf-0011-01.png)


contributes by normalizing each layer’s inputs to improve the stability and speed of the network’s training. Lastly, early stopping monitors the validation loss and stops the training process if the loss increases, signalling potential overfitting. The consistent decrease in loss across both datasets without significant spikes in validation loss further supports the effectiveness of these techniques. This graphical analysis confirms our model’s high accuracy and validates our approach to mitigating overfitting risks, thereby ensuring the model’s reliability and performance across varied data scenarios. 


![](prepared/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning/images/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning.pdf-0011-03.png)



![](prepared/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning/images/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning.pdf-0011-04.png)



![](prepared/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning/images/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning.pdf-0011-05.png)



![](prepared/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning/images/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning.pdf-0011-06.png)


**FIGURE 4.** (a) MCoMCRS Model on TripAdvisor: Plot of the Training vs Validation Loss (b) MCoMCRS Model on ITM-Rec: Plot of the Training vs Validation Loss (c) SCoMCRS Model on TripAdvisor: Plot of the Training vs Validation Loss (d) SCoMCRS Model on ITM-Rec: Plot of the Training vs Validation Loss. 

Overall, the results highlight the efficacy of the proposed MCoMCRS model and the general advantage of deep learning approaches in handling complex, real-world datasets. The adaptability of our model to various domains is underpinned by its flexible architecture and the universal applicability of its preprocessing steps. While our experiments focused on the travel and education sectors, the methodologies employed are relevant across various scenarios where personalized recommendations are valuable, such as healthcare for personalized patient recommendations or e-commerce for dynamic product suggestions. These findings emphasize not only the need to consider dataset-specific characteristics in model development and selection but also the potential of our model to be extended to other domains, providing a robust test of its flexibility and effectiveness across different contexts and criteria. For future research, it would be valuable to explore the factors contributing to the superior performance of MCoMCRS. Understanding the model’s inner workings could provide insights into practical strategies for handling diverse recommendation scenarios. Additionally, investigating the reasons behind the varying performance 

of context-aware models and the relative underperformance of certain strategies in specific datasets could lead to more tailored and effective recommendation systems. In conclusion, these findings contribute significantly to the field of recommendation systems, demonstrating the importance of model selection based on dataset characteristics and highlighting the potential of deep learning methods in this domain. 

## **VII. CONCLUSION AND FUTURE WORK** 

A modern approach to improving recommendations includes deep learning techniques in recommender systems. Many studies have used DL-based methods to improve recommendations for multi-criteria and context-aware recommender systems individually. However, using deep learning-based recommender systems to integrate context with multi-criteria ratings is still an open issue. This study aims to experiment with how deep learning could integrate contextual information into multi-criteria recommender systems using multi-context since most research combines single contexts with traditional ML methods. We specifically used the Deep Neural Network model to predict the multi-criteria ratings based on multi-context. We have conducted experiments on real-world datasets to determine the performance of methods. We conclude that our methods are more effective at generating recommendations than existing state-of-the-art methods. 

It is important to note that this is the first endeavour to use deep learning to integrate multiple contextual information into multi-criteria RSs. Our work will be expanded by integrating contextual data with multi-criteria ratings into deep-learning methods such as Autoencoder, Convolutional Neural Network, and Recurrent Neural Network. Additionally, we used a single deep neural network model for multi-criteria recommender systems instead of several models for multi-criteria ratings. In the future, we will employ multiple models to predict multi-criteria ratings because multi-criteria ratings help us to understand why users like an item. In contrast, the overall rating tells us how much the user likes it. Furthermore, these methods will be integrated with other well-known recommendation systems approaches, like the group-aware and personality-aware recommender systems. As the first model to explore the integration of Context-Aware Recommender Systems and Multi-Criteria Recommender Systems within the MCoMCRS framework, our initial research has primarily focused on validating the feasibility and effectiveness of combining these systems to enhance recommendation accuracy. This groundbreaking approach lays the foundation for future enhancements. Recognizing the inherent challenges of data sparsity and the cold start problems, which are common in recommender systems and could impact prediction accuracy, our subsequent efforts will address these issues. Future developments will include the implementation of advanced learning algorithms and novel strategies specifically designed to manage these challenges, ensuring that our system provides superior 

99946 

VOLUME 12, 2024 

I. Afzal et al.: Approach for Multi-Context-Aware Multi-Criteria Recommender Systems 


![](prepared/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning/images/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning.pdf-0012-01.png)


recommendations and maintains robust performance across diverse user scenarios.Additionally, the proposed method can be applied to other real-world datasets with different and multiple features from various fields to evaluate its efficacy and adaptability further. 

## **REFERENCES** 

- [1] I. Gunes, C. Kaleli, A. Bilge, and H. Polat, ‘‘Shilling attacks against recommender systems: A comprehensive survey,’’ _Artif. Intell. Rev._ , vol. 42, no. 4, pp. 767–799, Dec. 2014. 

- [2] A. Bilge and C. Kaleli, ‘‘A multi-criteria item-based collaborative filtering framework,’’ in _Proc. 11th Int. Joint Conf. Comput. Sci. Softw. Eng. (JCSSE)_ , May 2014, pp. 18–22. 

- [3] Z. Batmaz, A. Yurekli, A. Bilge, and C. Kaleli, ‘‘A review on deep learning for recommender systems: Challenges and remedies,’’ _Artif. Intell. Rev._ , vol. 52, no. 1, pp. 1–37, Jun. 2019. 

- [4] G. Adomavicius and A. Tuzhilin, ‘‘Context-aware recommender systems,’’ in _Recommender Systems Handbook_ . Cham, Switzerland: Springer, 2011, pp. 217–253. 

- [5] S. Raza and C. Ding, ‘‘Progress in context-aware recommender systems— An overview,’’ _Comput. Sci. Rev._ , vol. 31, pp. 84–97, Feb. 2019. 

- [6] G. Adomavicius and Y. Kwon, ‘‘Multi-criteria recommender systems,’’ in _Recommender Systems Handbook_ . Cham, Switzerland: Springer, 2015, pp. 847–880. 

- [7] Z. Batmaz and C. Kaleli, ‘‘AE-MCCF: An autoencoder-based multicriteria recommendation algorithm,’’ _Arabian J. Sci. Eng._ , vol. 44, no. 11, pp. 9235–9247, Nov. 2019. 

- [8] A. Odic, M. Tkalcic, J. F. Tasic, and A. Košir, ‘‘Relevant context in a movie recommender system: Users’ opinion vs. statistical detection,’’ _ACM Rec. Syst._ , vol. 12, pp. 1–21, Oct. 2012. 

- [9] Y. Zheng, ‘‘Criteria chains: A novel multi-criteria recommendation approach,’’ in _Proc. 22nd Int. Conf. Intell. User Interface_ , Mar. 2017, pp. 29–33. 

- [10] R. Dridi, L. Tamine, and Y. Slimani, ‘‘Exploiting context-awareness and multi-criteria decision making to improve items recommendation using a tripartite graph-based model,’’ _Inf. Process. Manage._ , vol. 59, no. 2, Mar. 2022, Art. no. 102861. 

- [11] Y. Zheng, S. Shekhar, A. A. Jose, and S. K. Rai, ‘‘Integrating contextawareness and multi-criteria decision making in educational learning,’’ in _Proc. 34th ACM/SIGAPP Symp. Appl. Comput._ , Apr. 2019, pp. 2453–2460. 

- [12] S.-L. Vu and Q.-H. Le, ‘‘A deep learning based approach for context-aware multi-criteria recommender systems,’’ _Comput. Syst. Sci. Eng._ , vol. 44, no. 1, pp. 471–483, 2023. 

- [13] Z. Hou, F. Bu, Y. Zhou, L. Bu, Q. Ma, Y. Wang, H. Zhai, and Z. Han, ‘‘DyCARS: A dynamic context-aware recommendation system,’’ _Math. Biosciences Eng._ , vol. 21, no. 3, pp. 3563–3593, 2024. 

- [14] R. Rismala, N. U. Maulidevi, and K. Surendro, ‘‘Personalized neural network-based aggregation function in multi-criteria collaborative filtering,’’ _J. King Saud Univ. Comput. Inf. Sci._ , vol. 36, no. 1, Jan. 2024, Art. no. 101922. 

- [15] R. Yera Toledo, A. A. Alzahrani, and L. Martínez, ‘‘A food recommender system considering nutritional information and user preferences,’’ _IEEE Access_ , vol. 7, pp. 96695–96711, 2019. 

- [16] S. Abinaya and R. Ramya, ‘‘Enhancement in context-aware recommender system—A systematic review,’’ in _Proc. 2nd Int. Conf. Emerg. Trends Inf. Technol. Eng. (ICETITE)_ , Feb. 2024, pp. 1–13. 

- [17] D. Jo, ‘‘Enhancing multi-criteria recommendation: Incorporating edge weights in graph convolution,’’ Ph.D. dissertation, Dept. Comput. Eng. Comput. Sci., California State Univ., Long Beach, CA, USA, 2024. [Online]. Available: https://scholarworks.calstate.edu/ concern/projects/kw52jg93t 

- [18] E. Ashley-Dejo, S. M. Ngwira, and T. Zuva, ‘‘A context-aware proactive recommender system for tourist,’’ in _Proc. Int. Conf. Adv. Comput. Commun. Eng. (ICACCE)_ , Nov. 2016, pp. 271–275. 

- [19] M. A. Abbas, S. Ajayi, M. Bilal, A. Oyegoke, M. Pasha, and H. T. Ali, ‘‘A deep learning approach for context-aware citation recommendation using rhetorical zone classification and similarity to overcome coldstart problem,’’ _J. Ambient Intell. Humanized Comput._ , vol. 15, no. 1, pp. 419–433, Jan. 2024. 

- [20] T. N. Nguyen and A. T. Nguyen, ‘‘Weighing the role of multi-criteria communities for recommender systems,’’ _Int. J. Intell. Eng. Informat._ , vol. 3, no. 4, p. 330, 2015. 

- [21] R. Dridi, L. Tamine, and Y. Slimani, ‘‘Context-aware multi-criteria recommendation based on spectral graph partitioning,’’ in _Proc. 30th Int. Conf._ , 2019, pp. 211–221. 

- [22] S.-Y. Jeong and Y.-K. Kim, ‘‘Deep learning-based context-aware recommender system considering contextual features,’’ _Appl. Sci._ , vol. 12, no. 1, p. 45, Dec. 2021. 

- [23] Z. Huang, Y. Liu, C. Zhan, C. Lin, W. Cai, and Y. Chen, ‘‘A novel group recommendation model with two-stage deep learning,’’ _IEEE Trans. Syst. Man, Cybern. Syst._ , vol. 52, no. 9, pp. 5853–5864, May 2021. 

- [24] S. Ahmadian, M. Ahmadian, and M. Jalili, ‘‘A deep learning based trust- and tag-aware recommender system,’’ _Neurocomputing_ , vol. 488, pp. 557–571, Jun. 2022. 

- [25] G. Adomavicius, R. Sankaranarayanan, S. Sen, and A. Tuzhilin, ‘‘Incorporating contextual information in recommender systems using a multidimensional approach,’’ _ACM Trans. Inf. Syst._ , vol. 23, no. 1, pp. 103–145, Jan. 2005. 

- [26] M. Unger, A. Tuzhilin, and A. Livne, ‘‘Context-aware recommendations based on deep learning frameworks,’’ _ACM Trans. Manage. Inf. Syst._ , vol. 11, no. 2, pp. 1–15, Jun. 2020. 

- [27] V. Boppana and P. Sandhya, ‘‘Web crawling based context aware recommender system using optimized deep recurrent neural network,’’ _J. Big Data_ , vol. 8, no. 1, pp. 1–24, Dec. 2021. 

- [28] Y. Zheng, ‘‘DeepCARSKit: A deep learning based context-aware recommendation library,’’ _Softw. Impacts_ , vol. 13, Aug. 2022, Art. no. 100292. 

- [29] S.-Y. Jeong and Y.-K. Kim, ‘‘Deep learning-based context-aware recommender system considering change in preference,’’ _Electronics_ , vol. 12, no. 10, p. 2337, May 2023. 

- [30] D. Tallapally, R. S. Sreepada, B. K. Patra, and K. S. Babu, ‘‘User preference learning in multi-criteria recommendations using stacked auto encoders,’’ in _Proc. 12th ACM Conf. Recommender Syst._ , Sep. 2018, pp. 475–479. 

- [31] N. Nassar, A. Jafar, and Y. Rahhal, ‘‘A novel deep multi-criteria collaborative filtering model for recommendation system,’’ _Knowl.-Based Syst._ , vol. 187, Jan. 2020, Art. no. 104811. 

- [32] Z. Batmaz and C. Kaleli, ‘‘A new similarity-based multicriteria recommendation algorithm based onautoencoders,’’ _Turkish J. Electr. Eng. Comput. Sci._ , vol. 30, no. 3, pp. 855–870, Mar. 2022. 

- [33] R. East, K. Hammond, W. Lomax, and H. Robinson, ‘‘What is the effect of a recommendation?’’ _Marketing Rev._ , vol. 5, no. 2, pp. 145–157, May 2005. 

- [34] G. Adomavicius and A. Tuzhilin, ‘‘Toward the next generation of recommender systems: A survey of the state-of-the-art and possible extensions,’’ _IEEE Trans. Knowl. Data Eng._ , vol. 17, no. 6, pp. 734–749, Jun. 2005. 

- [35] J. Bobadilla, F. Ortega, A. Hernando, and A. Gutiérrez, ‘‘Recommender systems survey,’’ _Knowledge-Based Syst._ , vol. 46, pp. 109–132, Jul. 2013. 

- [36] M. Sridevi, R. R. Rao, and M. V. Rao, ‘‘A survey on recommender system,’’ _Int. J. Comput. Sci. Inf. Secur._ , vol. 14, no. 5, p. 265, 2016. 

- [37] P. Lops, M. De Gemmis, and G. Semeraro, ‘‘Content-based recommender systems: State of the art and trends,’’ _Recommender Syst. handbook_ , vol. 1, pp. 73–105, Sep. 2011. 

- [38] J. B. Schafer, D. Frankowski, J. Herlocker, and S. Sen, ‘‘Collaborative filtering recommender systems,’’ in _The Adaptive Web_ . Cham, Switzerland: Springer, 2007, pp. 291–324. 

- [39] C. Kaleli, ‘‘An entropy-based neighbor selection approach for collaborative filtering,’’ _Knowl.-Based Syst._ , vol. 56, pp. 273–280, Jan. 2014. 

- [40] R. Burke, ‘‘Hybrid recommender systems: Survey and experiments,’’ _User Model. User-Adapted Interact._ , vol. 12, no. 4, pp. 331–370, Nov. 2002. 

- [41] N. Manouselis and C. Costopoulou, ‘‘Analysis and classification of multi-criteria recommender systems,’’ _World Wide Web_ , vol. 10, no. 4, pp. 415–441, Oct. 2007. 

- [42] G. Adomavicius and Y. Kwon, ‘‘New recommendation techniques for multicriteria rating systems,’’ _IEEE Intell. Syst._ , vol. 22, no. 3, pp. 48–55, May 2007. 

- [43] A. Livne, M. Unger, B. Shapira, and L. Rokach, ‘‘Deep contextaware recommender system utilizing sequential latent context,’’ 2019, _arXiv:1909.03999_ . 

- [44] M. Bazire and P. Brézillon, ‘‘Understanding context before using it,’’ in _Proc. 5th Int. Interdiscipl. Conf._ , 2005, pp. 29–40. 

- [45] Z. Yujie and W. Licai, ‘‘Some challenges for context-aware recommender systems,’’ in _Proc. 5th Int. Conf. Comput. Sci. Educ._ , Aug. 2010, pp. 362–365. 

- [46] L. Baltrunas, ‘‘Exploiting contextual information in recommender systems,’’ in _Proc. ACM Conf. Recommender Syst._ , Oct. 2008, pp. 295–298. 

99947 

VOLUME 12, 2024 

I. Afzal et al.: Approach for Multi-Context-Aware Multi-Criteria Recommender Systems 


![](prepared/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning/images/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning.pdf-0013-01.png)


- [47] Y. Zheng, ‘‘ITM-rec: An open data set for educational recommender systems,’’ 2023, _arXiv:2303.10230_ . 

- [48] G. Shani and A. Gunawardana, ‘‘Evaluating recommendation systems,’’ in _Recommender Systems Handbook_ . New York, NY, USA: Springer, 2011, pp. 257–297. 

- [49] Y. Koren, R. Bell, and C. Volinsky, ‘‘Matrix factorization techniques for recommender systems,’’ _Computer_ , vol. 42, no. 8, pp. 30–37, Aug. 2009. 

- [50] G. S. Majumder, P. Dwivedi, and V. Kant, ‘‘Matrix factorization and regression-based approach for multi-criteria recommender system,’’ in _Information and Communication Technology for Intelligent Systems_ . Cham, Switzerland: Springer, 2017, pp. 103–110. 


![](prepared/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning/images/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning.pdf-0013-06.png)


BURCU YILMAZEL received the Ph.D. degree in computer engineering from Anadolu University. She is currently an Assistant Professor with the Department of Computer Engineering, Eskişehir Technical University, Türkiye. Her research interests include recommender systems, shilling attacks, distributed data, artificial intelligence, machine learning, digitalization, and sustainability. 

- [51] Y. Zheng, B. Mobasher, and R. Burke, ‘‘CARSKit: A java-based contextaware recommendation engine,’’ in _Proc. IEEE Int. Conf. Data Mining Workshop (ICDMW)_ , Nov. 2015, pp. 1668–1671. 


![](prepared/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning/images/An_Approach_for_Multi-Context-Aware_Multi-Criteria_Recommender_Systems_Based_on_Deep_Learning.pdf-0013-09.png)


IFRA AFZAL received the bachelor’s degree in computer science from COMSATS University. She is currently pursuing the Ph.D. degree in computer engineering with Eskişehir Technical University, Türkiye. Her research interests include recommender systems in general and context-aware recommender systems and multi-criteria recommender systems in particular. She has actively collaborated with other researchers in machine learning and artificial intelligence. 

CIHAN KALELI received the M.Sc. and Ph.D. degrees in computer engineering from Anadolu University, Türkiye, in 2008 and 2012, respectively. He is currently a Professor with the Department of Computer Engineering, Eskişehir Technical University, Türkiye. He has published numerous articles in renowned journals and conferences, contributing significantly to data privacy and recommender systems. He is also actively involved in various research projects and a reviewer of several prestigious journals. His primary research interests include privacy-preserving data mining, distributed data-based collaborative filtering, and machine learning. 

99948 

VOLUME 12, 2024 

