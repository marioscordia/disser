
![](prepared/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm/images/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm.pdf-0001-00.png)


Received 2 December 2024, accepted 4 January 2025, date of publication 7 January 2025, date of current version 13 January 2025. _Digital Object Identifier 10.1109/ACCESS.2025.3526885_ 

## A Novel Method for News Recommendation on Websites Using the Clustered-Vectors Optimization Algorithm 

## PIYANUCH CHAIPORNKAEW AND THEPPARIT BANDITWATTANAWONG 

Department of Computer Science, Faculty of Science, Kasetsart University, Bangkok 10900, Thailand 

Corresponding author: Thepparit Banditwattanawong (thepparit.b@ku.th) 

This work was supported by the Department of Computer Science, Faculty of Science, Kasetsart University, Thailand. 

- **ABSTRACT** Recommendation systems have been extensively implemented across various sectors, including e-commerce, social media, and banking. Numerous studies have employed established machine learning techniques to enhance the performance of recommendation models to a certain degree. This research introduces a recommendation model for news content utilizing a novel machine learning technique known as the ‘‘Clustered-Vectors Optimization (CVO)’’ algorithm. The proposed algorithm aims to optimize the clustering of news titles to improve the performance of news recommendations. Once the news titles are effectively clustered, a recommendation list is generated for website visitors based on their experiences. The recommendation list for each visitor is selected from news titles within the same cluster that previous visitors have accessed. This study utilized two sources of news datasets. The primary dataset, collected from a backend website, was provided by a private digital television company in Thailand, while additional datasets were sourced from publicly available data on Kaggle. Experimental results indicated that the proposed CVO algorithm outperformed five well-known algorithms, which were TF-IDF, Word2Vec, Doc2Vec, Bag-ofWords (BoW), and Transformer, in terms of predictive performance. For instance, on the Thai news dataset, the CVO algorithm achieved an accuracy of 97.56%, a precision of 94.59%, a recall of 97.36%, and an F1-score of 97.46%. Similarly, the English language dataset, such as Indian news, also demonstrated high performance, with the CVO algorithm achieving an accuracy of 99.90%, a precision of 99.41%, a recall of 99.62%, and an F1-score of 99.53%. 

**INDEX TERMS** Clustering, news titles, optimization, recommendation system, website. 

## **I. INTRODUCTION** 

A recommendation system is a system that is used to find new items or services which are related to the interests of users [1]. In regard to websites, users are visitors who surf the internet. According to recent research, daily time spent on social networking by internet users worldwide from 2012 to 2022 has increased every year. In 2012, each user spent approximately 90 minutes per day, while time spent increased to 147 minutes per day in 2022 [2]. As a result, online channels are inevitably of more interest to expand business than in the previous era. 

The associate editor coordinating the review of this manuscript and approving it for publication was Yiming Tang . 

It is therefore prudent to offer company website visitors contents that meet their needs. This is an effective method to improve customer engagement, and customers are more likely to buy services or products. In order to provide what a customer needs, information about the customers must be collected. In the case of commercial websites, customer preferences could be implicitly gathered from the webpages that customers visit. Once such data are analyzed, new content that meets customer needs can be provided via the website, which is hereafter referred to as ‘‘an intelligent website’’ [3], [4]. The definition of an intelligent website is a website that can offer what customers need at an early stage without any request from them. 

In order to develop an intelligent website, many techniques based on the machine learning approach have been widely 

2025 The Authors. This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/ 

6685 

VOLUME 13, 2025 

P. Chaipornkaew, T. Banditwattanawong: Novel Method for News Recommendation on Websites 


![](prepared/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm/images/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm.pdf-0002-01.png)


employed in recent years. In terms of representation of text data, much research applied word embedding techniques to evaluate how important a word is in a collection of documents [5], [6], [7], [8], [9], [10]. Regarding clustering techniques, k-means, Gaussian Mixture Model, and Density-Based Spatial Clustering of Applications with Noise (DBSCAN) have been widely adopted [11], [12], [13], [14], [15], [16], [17], [18], [19]. Classification problems are solved by Logistic Regression, Support Vector Machine (SVM), Tree-Based algorithm, and Neuro-Fuzzy [6], [20], [21]. Machine Learning algorithms can also be applied to data concerning website visitor behaviors to construct a content recommendation model. Nowadays, there are more news readers who read news online [22]. The news recommendation model has become more important because it can help users to find news of interest and improve their reading experience. Much research worked on recommendation models in regard to various issues, such as reducing recommendation biases, increasing user representation dimensions, and combining news representation and user representation [23], [24], [25], [26], [27], [28], [29], [30], [31], [32]. 

Several challenges are inherent in recommendation models, such as imbalanced datasets, low accuracy, and high computational costs. Erra et al. [5] emphasized that managing large volumes of data is a critical task due to constraints related to time and space complexity. Similarly, Padurariu and Breaban [6] noted that real-world data frequently exhibit significant imbalances, complicating text classification tasks. Their research also aimed to mitigate computational costs by employing a cost-sensitive classifier for text processing. 

Much research worked on recommendation models in many ways. Some research focused on lowering computational time and memory usage than other metrics like accuracy [14]. The research of Song and Wu [17] improved the traditional Slope One recommendation algorithm by integrating user clustering and scoring preference. This methodology reduced the mean absolute error and root mean square error of the traditional algorithm, and it provided higher accuracy and better recommendation quality. Although there is much research that involves text processing, only a few researchers have conducted on Thai sites, especially news content, on web-based systems. Therefore, adopting machine learning techniques for Thai language content, especially news content, is still challenging for many researchers. 

This research proposes a novel method for news recommendation on websites using the Clustered-Vectors Optimization Algorithm. The proposed approach focuses on improving the performance of text clustering for Thai language content, which includes news titles provided on commercial websites. Thus, we can improve recommendation system performance because the recommendation system utilizes the results from the clustering process. The Clustered-Vectors Optimization (CVO) algorithm is the integration of text vectorization, clustering, and optimization techniques. Text vectorization means transforming text to 

vectors in order to be ingested into a machine learning algorithm. This process is achieved by using the Python library designed for the Thai language. Clustering is categorizing news titles into groups based on their vectors. Optimization is performing the best clustering, which gives the highest accuracy of prediction. These groups of news titles are also applied to categorize website visitors based on their visit logs. Finally, the recommendation list is generated from the news titles in the same group to which the visitor belongs. The contributions of this study are as follows: 

- 1) A novel algorithm for news recommendation on websites called Clustered-Vectors Optimization (CVO) which performs well with imbalanced datasets without the need of class rebalancing techniques. 

- 2) A novel optimization method in text clustering, especially for the Thai language. 

The remainder of the paper is structured as follows: Section II surveys prior studies on text classification, optimization, and recommendation systems. Section III outlines the proposed framework. Section IV details the experimental setup. Section V discusses the results, provides a discussion, and suggests future work. Section VI concludes the paper, and the final section acknowledges contributions. 

## **II. LITERATURE REVIEW** 

## _A. RECOMMENDATION MODELS_ 

In recent years, news recommendation has become increasingly important, especially for online news services. Several issues arise in news recommendation, with bias being a prominent concern. Two notable papers by Wu et al. [23] and Chen et al. [24] addressed different aspects of bias in news recommendation systems. Wu’s study focused on reducing biases related to sensitive user attributes, such as gender, by proposing a fairness-aware approach that employed decomposed adversarial learning and orthogonality regularization to separate and eliminate bias from user interest models. Conversely, Chen’s paper introduced the Time and Content-aware Causal Model (TCCM) to mitigate popularity bias by incorporating the timeliness and content-based popularity of news. TCCM used a causal graph to analyze user interactions, ensuring timely and relevant news recommendations. Both approaches demonstrated significant improvements in recommendation accuracy and fairness through extensive experiments. 

There have been three notable research works on news recommendations concerning user representation and user profiles. Existing methods typically learned single representations of users, which might have been insufficient. An et al. [25] proposed a neural news recommendation approach that learned both long- and short-term user representations. Wu et al. [26] employed both user representations and topic information of news, using a topic-aware news encoder and a user encoder. The news encoder learned representations from news titles, while the user encoder learned from users’ browsed news. Experimental results from these studies showed that their approaches effectively improved news 

6686 

VOLUME 13, 2025 

P. Chaipornkaew, T. Banditwattanawong: Novel Method for News Recommendation on Websites 


![](prepared/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm/images/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm.pdf-0003-01.png)


recommendation performance. The research of Xiao [33] investigated a personalized news recommendation system utilizing deep learning to enhance user experience. It addressed the precise construction of user interest profiles by integrating user search records with interest preferences. The system used a parallel convolutional neural network to compile user interest features and a recursive neural network to uncover hidden time series patterns. By tackling challenges such as data sparsity and cold start issues, the proposed method enhanced recommendation accuracy. Tests on real news datasets confirmed the method’s effectiveness in delivering high-quality, personalized news recommendations. 

Our previous researches [3], [4] employed news recommendation models on commercial websites. The first research [3] employed Term Frequency-Inverse Document Frequency (TF-IDF), k-means, and the Apriori algorithm. The second research [4] applied the TKD-NM algorithm which integrated TF-IDF, k-means, and NelderMead algorithm. TF-IDF was applied to form word vectorization and k-means was utilized for clustering news titles in both researches. The Apriori algorithm in the first research was utilized to determine the association of news clusters. In regard to clustering, there was no optimization algorithm in the first research while the second research employed the Nelder-Mead algorithm. Although the Nelder-Mead algorithm was applied to determine the best clustering, there were some challenges. For example, the running time took too long to complete. 

Recommendation systems have been widely applied in various platforms, utilizing several algorithms for recommendation models. Collaborative filtering algorithms are one of the main algorithms used in these systems due to their simplicity and efficiency. However, they face limitations such as data sparsity and scalability issues, which hinder their performance and make it difficult to further improve the quality of recommendations. To address these issues, a model combining collaborative filtering with deep learning technology has been proposed in the research of Zhang et al. [34]. This model consisted of two parts: first, it used a feature representation method based on a quadratic polynomial regression model to obtain latent features more accurately by improving upon the traditional matrix factorization algorithm. These latent features were then used as input data for a deep neural network model to predict rating scores. Similarly, the paper of Li and Xia [35] presented an approach that combined Alternating Least Squares (ALS) collaborative filtering with deep learning techniques. The proposed method, Convolutional Multimodal Auto Multilayer Graph with ALS Collaborative Filtering (CMAMG_ALSCF), processed user preference data, reduced noise, normalized it, and classified it using a convolutional neural network (CNN) to identify similarities between users and movies. The system dynamically incorporated temporal features to adapt to changing user preferences and item popularity. Experimental results on various movie recommendation datasets demonstrated that 

the proposed method achieved high training and validation accuracy, as well as improved precision and reduced error rates compared to existing techniques. 

Mostly, recommendation systems consider only the content of users and ignore their sequential information which also provides useful insights regarding user behaviors. In the research of Mishra et al. [36], the sequential information was considered along with content information. The proposed model considers sequential information to predict a user’s next visit. The first step was to form clusters to acquire knowledge regarding web users and the classification technique was then used to enhance the learning capability and to generate recommendations. In order to capture the sequential behavior of the user, the S[3] M similarity measure was utilized. Once the clusters were formed, the Singular Value Decomposition (SVD) was applied to classify the web user sessions. For any new user, top M clusters were identified based on the similarity between the user and the cluster centers. A response matrix was created with the top M clusters. After generating the response matrix, a weight vector was created. Generated predictions were compared with the original values of the datasets to evaluate the accuracy of the prediction. 

Research on imbalanced data in recommendation models has highlighted the significant impact of data imbalance on prediction performance. Various sampling methods can improve prediction performance, but selecting the optimal method for a specific dataset remains challenging. Sun et al. [37] emphasized the importance of studying how to choose suitable sampling methods based on data characteristics. They proposed an algorithm that automatically recommended applicable sampling methods for new defect data by ranking existing methods using historical defect data and by analyzing data similarity with meta-features. This information was combined to build a recommendation network, utilizing a user-based collaborative filtering algorithm to suggest appropriate sampling methods for new defect data. Additionally, the paper of Taneja et al. [38] introduced a novel sentiment analysis method using Transformer architecture, specifically DistilBERT, on an imbalanced women’s clothing e-commerce dataset. The study addressed Sentiment Classification (SC) and Product Recommendation (PR), achieving high performance metrics with F1 scores of 0.79 for SC and 0.85 for PR, and AUC scores of 0.98 for SC and 0.96 for PR. The results demonstrated that Transformer-based models significantly outperformed traditional supervised approaches and other state-of-the-art models, showing robustness in regard to data imbalance issues and contributing to a better understanding of consumer sentiment. 

## _B. TEXT PROCESSING_ 

Erra et al. [5] worked on text processing in regard to topic extraction. The paper focused on how to improve running time when a large message stream was processed. The approximate TF–IDF was introduced to extract topics from a massive message stream. Moreover, the parallel implementations of the calculation of the approximate 

6687 

VOLUME 13, 2025 

P. Chaipornkaew, T. Banditwattanawong: Novel Method for News Recommendation on Websites 


![](prepared/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm/images/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm.pdf-0004-01.png)


TF–IDF based on GPUs were adopted to speed up the processing time. The parallel GPU architecture met the fast response requirements and overcame storage constraints when processing a continuous flow of data stream in real time. In addition, the GPU implementation was stable and performed well while the memory was limited. Furthermore, the time to compute the approximate TF–IDF measure on the GPU did not vary on different data sources. 

The research of Wang [9] enhanced the TF-IDF algorithm for automatic keyword extraction from online news texts by integrating semantic analysis using the Word to Vector (Word2vec) model. The study compared traditional TF-IDF and TextRank algorithms, incorporating news title weights and semantic similarities to improve keyword extraction accuracy. Experimental results on the ACE2005 dataset demonstrated that the semantics-combined TF-IDF algorithm outperformed traditional methods in terms of precision, recall, and F-measure, especially when extracting five keywords. This approach shows significant potential for practical applications in text classification and information retrieval. However, the study had some limitations, such as the relatively small number of languages studied and the limited number of texts. 

Asudani et al. [10] provided a comprehensive overview of various word embedding techniques and their applications in natural language processing tasks. They discussed the significance of word embeddings, which are n-dimensional representations of text that capture word meanings, and their integration with deep learning models to enhance text analytics tasks. The research highlighted the strengths and weaknesses of different word embedding models, including Bag-of-Words (BoW), n-gram, TF-IDF, Word2Vec, Global Vector (GloVe), fastText, Embeddings from Language Model (ELMo), Generative Pre-Training (GPT), and Bidirectional Encoder Representations from Transformer (BERT). BoW easily represented words in the corresponding vector form, while TF-IDF kept relevant word scores and reduced the score for frequent words. Word2Vec captured the syntactic and semantic information about the text. However, these algorithms had some drawbacks. TF-IDF only considered the terms, and BoW and Word2Vec were unable to extract outof-vocabulary words from a corpus. The research proposed that the Continuous Bag-of-Words model could be the first preference for performing operations like text classification tasks. 

Another research on topic extraction was the work of Zhang et al. [12]. The paper extracted topics from bibliometric data using a word embedding technique and a polynomial kernel function integrated into a cosine similarity-based k- means clustering algorithm. The research focused on the methodology to better extract the key features from the given text. A word embedding technique was applied in data pre-processing to extract a small set of key features. A polynomial kernel function incorporated with a cosine similaritybased k-means clustering algorithm was then implemented to enhance the performance of the topic extraction. The 

polynomial function-based kernel k-means clustering method was adopted with the Word2Vec model. When comparing the proposed method with five traditional baselines, namely k-means, fuzzy c-means, principal component analysis, and topic models, the experimental results demonstrated that the proposed algorithm gave higher effectiveness than others. 

There has been some research in regard to sentiment analysis based on Thai language content. The paper of Arreerard and Senivongse [39] explored methods to classify defamatory text in Thai language on social media platforms. The study employed various text classification techniques, including word n-grams, character n-grams, specific terms, grammatical dependency structures, and sentiment polarity. The research compared the performance of Support Vector Machine (SVM) and Naïve Bayes classifiers, finding that SVM, combined with word and character n-grams, achieves the highest accuracy and F-score. The paper highlighted the challenges posed by linguistic variations in Thai and suggests improvements for future work, such as enhancing the dictionary of defamatory terms and better handling of named entities and sound-alike terms. Similarly, the paper of Boonyarat et al. [40] explored the use of advanced BERT models to identify suicidal ideation and emotional distress in Thai tweets during the COVID-19 pandemic. The authors created a dataset of 2,400 manually annotated Thai tweets and developed a deep learning model that outperformed baseline models. They found a significant increase in tweets expressing suicidal thoughts and sadness during the pandemic. The study highlighted the pandemic’s impact on mental health in Thailand and provides a valuable tool for monitoring and preventing suicide through social media analysis. 

In regard to word embeddings, Fernandez et al. [41] conducted research, namely unsupervised sentence representations as word information series: Revisiting TF-IDF. The paper aimed at learning unsupervised sentence representations from unlabeled text. An unsupervised method modeling a sentence as a weighted series of word embeddings was introduced. The weights of the series were calculated using Shannon’s Mutual Information (MI) between words, sentences and the corpus. Sentences were represented by using the link between contexts, learning by word embeddings, and the amount of information in the words within a sentence. The research exploited the mentioned link to learn the weights of a series of word embeddings without supervision. Although the proposed model outperformed the usual baselines of sentence representation, the experiments only considered a basic version of a threelevel Shannon’s information structure. Since the usual IDF weights used in the experiment made Naive assumptions in terms of the probability measures of words and sentences, the latent important language structures may not be revealed. 

The research by Yuan et al. [55] and Sufi [56] delved into sophisticated frameworks for news categorization, utilizing neural networks and Generative Pre-trained 

6688 

VOLUME 13, 2025 

P. Chaipornkaew, T. Banditwattanawong: Novel Method for News Recommendation on Websites 


![](prepared/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm/images/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm.pdf-0005-01.png)


Transformer (GPT). Yuan et al. introduced a domainknowledge-based reconstruction framework that effectively classified both in-domain and out-of-domain news titles through a CNN-based autoencoder and BERT for pre-trained embeddings, demonstrating high performance on the Belt and Road Initiative news dataset. Sufi’s work combined neural networks and CNNs with GPT to categorize a large corpus of news articles into various categories, achieving remarkable precision, recall, and F1-scores. Both studies emphasized the practical and theoretical benefits of these advanced methodologies, including anomaly detection and predictive trend analysis, highlighting their efficacy in large-scale text data analysis and representing significant progress in computational news classification. 

## _C. CLUSTERING TECHNIQUES_ 

There are several well-known techniques for clustering, such as k-means, DBScan, and the Guassian Mixture Model. The research of Curiskis et al. [18] worked on document clustering using TF-IDF and word embedding models combined with four clustering methods, namely k-means, k-medoids, Hierarchical Agglomerative Clustering, and Non-Negative Matrix Factorization. The research focused on text data provided in two online social networks: Twitter and Reddit. The results revealed that Document to Vector (Doc2Vec) and TF-IDF weighted mean word embedding representations gave better results than simple averages of word embedding vectors in terms of document clustering. In addition, k-means clustering delivered the best performance with Doc2Vec embeddings. The research revealed that the proposed algorithm should perform well on most online social network text data. 

In their seminal work, Tianda et al. [19]. presented evidence of the k-means algorithm’s superior performance. Their study delved into the classification strategies for ‘Fake News’ articles through the utilization of k-means and Agglomerative Clustering techniques, underpinned by Word2Vec embeddings. This involved the extraction of salient features from textual content, their subsequent conversion into vector formats via Word2Vec, and the application of clustering algorithms to group similar articles. Notably, the k-means clustering demonstrated enhanced effectiveness over Agglomerative Clustering with the Ward method, as reflected in the higher Purity Scores and Adjusted Rand Scores. For future research, the adoption of more sophisticated models, such as Transformer embeddings, was suggested to further refine clustering results. 

K-means clustering and decision tree algorithm were employed in the research of Wang et al. [8]. The research proposed a novel algorithm which was a linear multivariate decision tree classifier. The proposed algorithm adopted a Binary Decision Tree based on k-means Splitting. K-means clustering served as a node splitting method and also proposed the non-split condition. Therefore, the proposed algorithm could provide good generalization ability and enhanced the classification performance. Furthermore, 

the k-means centroid based model was converted into the hyperplane-based decision tree; as a result, the speed of the classification process was improved. The research demonstrated that the proposed algorithm matched or outperformed the traditional decision trees. 

In regard to aspect-phrase analysis, Xiong and Ji [14] developed a novel weighted context representation model based on semantic relevance. The algorithm exploited the word embedding method to represent aspect-phrase, which is an important task for aspect finding in sentiment analysis. The research encoded lexical knowledge as constraints with a degree of belief, and further proposed a flexibleconstrained k-means algorithm to cluster aspect-phrases. The research applied the latest neural language model to learn word vectors, and then represented each aspect-phrase with a novel weighted context by using semantic relevance. The cosine distance of the word vector was calculated to determine semantic relevance. Even though the proposed method outperformed existing state-of-the-art methods, some other similarity measure methods could be employed to determine semantic relevance. 

Mhiri et al. [15] researched clustering for handwritten content. Due to the difficulties of automatic segmentation-free and training-free word spotting, the research proposed a novel unsupervised hierarchical handwriting representation. K-means algorithm was applied to learn a hierarchy of features for representing document images. An efficient matching system was then adopted for word spotting. Firstly, a fast pre-selection stage applying a sliding-window approach over compressed document image-representations was conducted. Secondly, a re-ranking stage based on a discriminative description that encoded the spatial layout of local features was carried out. The results showed that the proposed method yielded a better competitive performance compared to state-of-the-art approaches. Since the proposed framework had low computational and memory complexity, it was suitable for large datasets. However, the proposed matching system could be improved using a more powerful matching algorithm, such as SVM. 

Another paper that utilized the concept of k-means was authored by Li and Wang [42]. They introduced a novel clustering algorithm that integrated k-means++ and power k-means within a collaborative neurodynamic optimization framework. The proposed method employed k-means++ to select initial cluster centers, applied power k-means to generate multiple sets of centers, and used particle swarm optimization to reinitialize centers in subsequent iterations. This approach proposed to enhance clustering performance by leveraging better initial seeding, smoother objective functions, and diversified alternatives. Experimental results on twelve benchmark datasets illustrated that the proposed algorithm outperformed seven baseline clustering algorithms across 21 internal and external indices. 

The paper by Lu et al. [43] tackled the challenge of clustering dynamic text documents by capturing evolving topics over time. They introduced the DEDC-IMAE model, 

6689 

VOLUME 13, 2025 

P. Chaipornkaew, T. Banditwattanawong: Novel Method for News Recommendation on Websites 


![](prepared/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm/images/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm.pdf-0006-01.png)


which integrated an inherited mixed autoencoder (IMAE) and a deep evolutionary document clustering (DEDC) module. The IMAE was employed to learn semantic representations that incorporate both historical and current topic information, while the DEDC module dynamically refined clustering partitions. This approach could enhance the representation and clustering of documents as topics evolve. Experimental results on real-world datasets demonstrated that DEDC-IMAE outperformed existing methods in terms of clustering accuracy and robustness, marking a significant advancement in evolutionary document clustering. 

## _D. OPTIMIZATION MODELS_ 

Research on optimization algorithms has explored various aspects, including time complexity, model accuracy, and model generalization. The research of Chen et al. [44] proposed optimal replenishment policies with allowable shortages for a product life cycle, applying the Nelder-Mead algorithm to determine the optimum number for inventory replenishment, the inventory replenishment time points, and the beginning time points of shortages, aiming to minimize the total relevant costs of the inventory replenishment system. They recommended for future research to consider the deteriorating nature of the product and the discounting effects due to the time value of money. In addition, the research of Villegas-Ch et al. [45] presented a computer vision platform designed to enhance warehouse inventory management by integrating machine learning and computer vision. Utilizing convolutional neural networks (CNNs) and open-source libraries like TensorFlow and PyTorch, the platform recognized and classified products from real-time images, demonstrating significant improvements, including a 45% reduction in inventory counting time and a 9% increase in accuracy. Despite challenges such as staff resistance and technical limitations, the study highlighted the potential of computer vision technology to transform warehouse operations, offering a practical and adaptable solution for inventory management. 

Djenouri et al. [46] proposed a novel parallel evolutionary ARM algorithm which adopted hybrid cluster/GPU computing architecture. It was a genetic algorithm that ran on clusters of GPUs to efficiently discover diversified association rules. Since the task of association rule mining was very time consuming, the designed algorithm relied on the massively parallel GPU threads. A novel partition operation was applied by the leader to partition the big association rule space into sub-spaces that workers explored independently. In order to avoid redundant work, the proposed approach generated rules for each worker using a genetic algorithm. Each worker then returned the rules found to the leader, which selected the final set of rules to be presented to the user. The results revealed that CGPUGA was 600 times faster than the sequential version of the algorithm for big datasets. In terms of rule quality, the results showed that the CGPUGA algorithm provided rules of higher quality compared to the state-of-theart NIGGAR, MSP-MPSO and MPGA algorithms. 

Hyperparameter optimization is one of the most challenging tasks in machine learning. The work of Newcomer et al. [47] aimed to improve the performance and accuracy of groundwater flow models using hyperparameter optimization approaches. Tree of Parzen Estimators (TPE) and Random Search algorithms were applied to optimize MODFLOW-NWT’s solver settings. To quantify the performance of candidate solver settings, a loss function was calculated from the time elapsed and mass balance error of the MODFLOW-NWT forward run. When optimization was adopted, running time and error were reduced. The experimental results yielded a faster running time and fewer errors compared to a Random Search algorithm. The time to complete the optimization trials was also shorter with the TPE algorithm. However, additional attempts of other advanced hyperparameter optimization techniques could be achieved. Similarly, the work of Ma et al. [48] presented an intelligent model for classifying the quality of tunnel surrounding rocks in real-time, crucial for efficient tunneling and geological hazard prevention. The model employed a high-resolution neural network (HRNet) optimized with Bayesian optimization to enhance its robustness and accuracy. Key operational parameters from tunnel boring machines (TBMs) such as advance rate, total thrust, cutterhead torque, rotational speed, and pitch and roll angles were used as inputs. The model outperformed traditional methods and other neural network models like VGG and ResNet in terms of accuracy, precision, recall, and F1 scores, demonstrating its effectiveness in supporting TBM operations and ensuring construction safety. 

The research of Lye et al. [49] adopted deep neural networks integrated with an optimization algorithm, namely iterative surrogate model optimization. The proposed algorithm was a robust and efficient numerical approximation of partial differential equations (PDEs) constrained optimization problems. This algorithm was based on deep neural networks and its key feature was the iterative selection of training data through a feedback loop between deep neural networks and any underlying standard optimization algorithm. The proposed algorithm significantly outperformed a standard deep neural network based on a surrogate optimization algorithm as well as standard optimization algorithms.In terms of PDE constrained optimization, the crucial issue was optimization under uncertainty, which should be accomplished by the adaptation of the proposed algorithm. 

The optimization model regarding material structure was applied in the research of Tauzowski et al. [50] The objective of this study was to propose a relatively simple and efficient method for reliability based topology optimization for structures made of elasto-plastic material. In order to determine the optimal topology of elasto-perfectly plastic structures, the removal of material from the structure was considered. The mentioned process led to the weakening of the structural strength and stiffness, which increased the likelihood of structural failure. The methodology consisted of two nested optimization problems called the outer and 

6690 

VOLUME 13, 2025 

P. Chaipornkaew, T. Banditwattanawong: Novel Method for News Recommendation on Websites 


![](prepared/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm/images/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm.pdf-0007-01.png)


inner loop. The outer loop allowed for reducing volume of the optimized structure. The inner loop applied the well-known FORM method to calculate the reliability index. The results obtained by employing the proposed methodology were in good agreement with analytical solutions in the case of a twobar structure. In terms of the L-shape bracket, it provided optimal typologies comparable with those obtain by other methods. 

In addressing the critical issue of time efficiency in optimization processes, the acceleration of optimization algorithms is essential for practical applications. The investigation conducted by Chen et al. [51]. explored the advancement of gradient descent methodologies for convex optimization challenges by incorporating fixed-time and reset strategies derived from control theory principles. These strategies were designed to augment the speed of convergence and ensure system stability. The research presented a novel adaptive fixed-time gradient descent approach characterized by a reduced number of tuning parameters and enhanced robustness. Additionally, a reset mechanism was implemented to mitigate problems such as overshoot and instability that arose in the discrete variants of the algorithm. The findings of the study indicated that the integration of fixed-time and reset strategies significantly improved the optimization algorithms’ performance, particularly in terms of convergence rate and system stability. The paper advocated further exploration in this domain, suggesting the expansion of these algorithms to stochastic scenarios and their amalgamation with existing machine learning and artificial intelligence algorithms. 

## **III. PROPOSED CLUSTERED-VECTORS OPTIMIZATION ALGORITHM** 

The main concept of the proposed CVO algorithm is to determine the optimal vectors for clustering which give the highest accuracy in terms of prediction. This section describes the conceptual framework of the proposed CVO algorithm, as shown in Fig.1. The proposed CVO consists of three phases: Phase-I data pre-processing, Phase-II clustering optimization and Phase-III news title suggestion. As mentioned earlier, data were collected from the private company and the Kaggle database. The data pre-processing phase was only applied to the private dataset. In regard to the clustering optimization phase and the news title suggestion phase, both the private dataset and the public datasets were processed. 

## _A. NOTATIONS_ 

Table.1 lists the notations used in Fig.7, along with their definitions and functionalities. 

## _B. PHASE-I DATA PRE-PROCESSING_ 

The data pre-processing steps consist of data verification, feature selection, and data aggregation. 

- 1) Data verification: Since data were collected from backend websites, some data were not applicable. For example, some news titles shown in the dataset were 

**TABLE 1.** Details of notations. 


![](prepared/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm/images/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm.pdf-0007-12.png)


not published on the website. Therefore, these news titles were discarded from the visitor logs. This step was completed by consulting with a data owner from the company. 

6691 

VOLUME 13, 2025 

P. Chaipornkaew, T. Banditwattanawong: Novel Method for News Recommendation on Websites 


![](prepared/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm/images/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm.pdf-0008-01.png)



![](prepared/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm/images/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm.pdf-0008-02.png)


**FIGURE 1.** Conceptual framework for proposed CVO. 

- 2) Feature selection: Hugh data were gathered, but only the relevant features were considered. In addition, some attributes were redundant; therefore, such attributes were removed to reduce the computational time and over feature weighting. For example, there were published date and created date for each news record; therefore, only published date was selected. 

- 3) Data aggregation: Since the data which are visit logs and news information were derived from several sources, a data aggregation process was needed to map all information together. For example, the visit log and news ID were recorded in one table while the news titles and news ID were recorded in another table. 

The output of the data pre-processing phase included the auto-generated IDs of visitors and their news titles histories. 

## _C. PHASE-II CLUSTERING OPTIMIZATION_ 

For an effective news title recommendation system, accurate news title clustering is crucial. This study employed the optimization technique to reach the optimal vectors for clustering. The objective of this phase is to cluster news based on news titles. 

## 1) FEATURE REPRESENTATION 

This step aims to represent each word with its vector. There are six datasets in this experiment. The main dataset was in the Thai language while the others were in English. 

Therefore, news titles from the main dataset were separated into words using the word tokenization method specially designed for Thai, but for the others, the common python library was employed. Subsequently, five commonly used word embedding algorithms, namely TF-IDF, Word2Vec, Doc2Vec, Bag-of-Words, and Transformer (BERT), were employed across all datasets to generate vector representations of the words. The formula to compute the tf-idf is as follows [52]: 


![](prepared/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm/images/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm.pdf-0008-12.png)


where _t_ is the term, _d_ is the document, and _tft,d_ is the number of occurrences of _t_ in document _d_ . The _idft_ is computed as follows [52]: 


![](prepared/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm/images/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm.pdf-0008-14.png)


where _N_ is the total number of documents in the document set and _dft_ is the document frequency of _t_ . The document frequency is the number of documents in the document set that contain the term _t_ . 

The Word2Vec model is designed to create vector representations of words. It employs two primary algorithms: Continuous Bag of Words (CBOW) and Skip-gram. In the CBOW algorithm, the surrounding context words are utilized to predict the target word, whereas in the Skip-gram algorithm, the target word is used to predict the surrounding context words. The training objective of Word2Vec is to 

6692 

VOLUME 13, 2025 

P. Chaipornkaew, T. Banditwattanawong: Novel Method for News Recommendation on Websites 


![](prepared/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm/images/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm.pdf-0009-01.png)


maximize the average log probability of the context words given the target word, which is mathematically expressed as follows [53]: 


![](prepared/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm/images/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm.pdf-0009-03.png)


where _T_ is the total number of words in the corpus, _c_ is the size of the context window, _wt_ is the target word, and _wt_ + _j_ are the context words. The probability _p_ ( _wt_ + _j_ | _wt_ ) is computed using the softmax function: 


![](prepared/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm/images/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm.pdf-0009-05.png)


where _vwO_ and _vwI_ are the vector representations of the output and input words, respectively, and _W_ is the vocabulary size. 

The Doc2Vec model is a widely-used algorithm for generating vector representations of documents. It builds upon the Word2Vec model by incorporating a unique vector for each document. There are two primary architectures: Distributed Memory (DM) and Distributed Bag of Words (DBOW). In the DM model, both the context words and the document vector are utilized to predict the target word. The training objective is to maximize the average log probability of the target word given the context words and the document vector. The formula is as follows [54]: 


![](prepared/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm/images/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm.pdf-0009-08.png)


**FIGURE 2.** The result of the elbow method to the Thai news dataset. 


![](prepared/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm/images/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm.pdf-0009-10.png)


**FIGURE 3.** The result of the elbow method to the fake news dataset. 


![](prepared/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm/images/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm.pdf-0009-12.png)


where _T_ is the total number of words in the corpus, _c_ is the size of the context window, _wt_ is the target word, _wt_ + _j_ are the context words, and _D_ is the document vector. 

The probability _p_ ( _wt_ + _j_ | _D, wt_ ) is computed using the softmax function: 


![](prepared/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm/images/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm.pdf-0009-15.png)


where _vwO_ , _vwI_ , and _vD_ are the vector representations of the output word, input word, and document, respectively, and _W_ is the vocabulary size. 

The Bag-of-Words (BoW) model is a method for representing text data by transforming it into a vector of word frequencies. In this approach, each document is depicted as a vector, where each element corresponds to a unique word in the vocabulary, and the value of each element indicates the frequency of that word in the document [54]. To compute the BoW representation, follow these steps: First, split the text into individual words, a process known as tokenization. Next, compile a list of all unique words in the document set. Finally, count the occurrences of each word in the vocabulary and create a vector based on these counts. 

The resulting vector for a document can be represented as: 


![](prepared/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm/images/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm.pdf-0009-19.png)


where _f_ ( _wi, d_ ) is the frequency of word _wi_ in document _d_ , and _N_ is the total number of unique words in the vocabulary. The BoW model is simple and effective for many text processing tasks, but it does not take the order of words into account. 

## 2) CLUSTERING 

Since a news recommendation list is generated from news in the same cluster, the best clustering algorithm is needed to achieve the best recommendation performance. In this step, word vectors from the previous step were clustered using k-means. Given that the Thai news dataset was supplied by a private company, their domain expert was consulted to determine the optimal number of clusters. Considering that other websites categorize news into approximately 5 to 30 sections, the data owner advised that the number of clusters should not exceed 30. Thus, the elbow method was utilized to investigate the optimal number of clusters between 5 and 30 for Thai news. The elbow method was used to determine the optimal number of clusters for all datasets except for Variation news, which already had a predefined number of clusters. The results of the elbow method experiments for all datasets are illustrated in Fig.2 to Fig.6. These figures indicate that the optimal numbers of clusters are 14 for Thai news, 7 for Fake news, 10 for Article news, 8 for Indian news, and 13 for Reuters news. For Variation news, the predefined number of clusters is 10. 

6693 

VOLUME 13, 2025 

P. Chaipornkaew, T. Banditwattanawong: Novel Method for News Recommendation on Websites 


![](prepared/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm/images/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm.pdf-0010-01.png)



![](prepared/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm/images/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm.pdf-0010-02.png)


**FIGURE 4.** The result of the elbow method to the article news dataset. 


![](prepared/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm/images/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm.pdf-0010-04.png)


**FIGURE 5.** The result of the elbow method to the indian news dataset. 


![](prepared/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm/images/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm.pdf-0010-06.png)


**FIGURE 6.** The result of the elbow method to the Reuters news dataset. 

## 3) OPTIMIZATION 

The objective of this phase is to determine the optimal word vectors that maximize classification accuracy. Initially, word vectors derived from news titles and their clustering labels were evaluated using the RandomForest algorithm. To identify the best word vectors, an iterative process was used, generating new sets of word vectors and re-evaluating them with RandomForest. The Tree-structured Parzen Estimator (TPE), a form of Bayesian optimization, was employed for hyperparameter optimization, efficiently searching the hyperparameter space to find the best parameters for the 

model. The TPE algorithm is highly efficient for optimizing expensive and noisy objective functions. It adapts dynamically to the objective function, quickly focusing on promising regions of the hyperparameter space. Additionally, TPE can handle complex and high-dimensional hyperparameter spaces, making it a versatile and powerful tool for hyperparameter tuning [60]. The function to be minimized was the negative value of accuracy, with the initial parameter guess being the word vectors from the clustering process. Experiments showed that six iterations of the optimization process yielded the best results, as no significant changes were observed beyond this point. Therefore, the optimization process was limited to a maximum of six iterations. This method was particularly advantageous for optimizing noisy or discontinuous functions, as it did not require gradient calculations. The process of generating and evaluating word vectors was repeated until the highest classification accuracy was achieved. The primary equation in the Tree-structured Parzen Estimator (TPE) focuses on the density ratio, which is crucial for directing the choice of hyperparameters. This ratio is defined as: 


![](prepared/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm/images/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm.pdf-0010-11.png)


In this context, _p_ ( _x_ | _D_[(] _[l]_[)] ) represents the probability density of the promising hyperparameter configurations, and _p_ ( _x_ | _D_[(] _[g]_[)] ) represents the probability density of the less promising configurations. By maximizing this ratio, TPE focuses the search on the most promising regions of the hyperparameter space, improving the efficiency of the optimization process [61]. Once the new set of word vectors was generated, the RandomForest model was employed to reassess the accuracy. Such repetition of the processes was terminated when the highest accuracy score of classification model was reached. The optimal set of word vectors occurred when the highest accuracy score of classification was presented. When the optimization algorithm was completed, it yielded optimal word vectors, the target classes of news titles, and the accuracy of the model. The output of the clustering optimization phase were the class labels of news titles and the view histories of visitors. These data were ingested to phase-III to generate the recommendation list. The results from the proposed model were then compared with the baseline models, namely TF-IDF, Doc2Vec, Word2Vec, and BoW. 

Fig.7 presents the process of the Clustered-Vectors Optimization algorithm. The algorithm processes a collection of sentences that represent news headlines as its input, where _S_ denotes the set of sentences. The output is an optimal feature vector matrix ( _M_ ), where _d_ represents the number of news titles and _b_ represents the number of words in each news headline. Lines 1-6 describe the process of splitting a set of texts into individual words. _Si_ denotes each sentence, _Wi_ denotes the set of words within each sentence, and _wi,j_ denotes each individual word. Line 7 illustrates the process of combining all words into a single document, denoted as _D_ . 

6694 

VOLUME 13, 2025 

P. Chaipornkaew, T. Banditwattanawong: Novel Method for News Recommendation on Websites 


![](prepared/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm/images/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm.pdf-0011-01.png)



![](prepared/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm/images/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm.pdf-0011-02.png)


**FIGURE 7.** Algorithm of Clustered-Vectors optimization. 

Lines 8-14 detail the process of counting the frequency of each word, with _f_ representing the set of word frequencies. Lines 15 computes the vector for each word by analyzing its frequency within the document, with _VD_ representing the 

set of word vectors for the document. Line 16 defines the variables in _VD_ , where _v_ 1, _v_ 2, ..., _vm_ denote each word vector and _m_ is the number of unique words. Line 17 assigns _k_ as the number of clusters, as specified by the news owner. 

6695 

VOLUME 13, 2025 

P. Chaipornkaew, T. Banditwattanawong: Novel Method for News Recommendation on Websites 


![](prepared/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm/images/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm.pdf-0012-01.png)


Line 20 randomly initializes centroids as _c_ 1, _c_ 2, ..., _ck_ and the number of centroids is based on the value of _k_ . Line 21 stores the current centroids in the temporary centroids, denoted as _tci_ . Lines 23 to 27 describe the process of finding the shortest distance between each word vector and the centroids, then assigning each word vector to the nearest centroid, marking it with that centroid’s label, where _l_ represents the label for each centroid. Lines 28 to 30 describe the process of finding the new centroid by averaging all word vectors with the same label, where _ci_ denotes the new centroid, _Vli_ denotes the word vectors with the same label, and _li_ denotes the label for that centroid. Line 32 assigns each label to a set of labels, denoted as _L_ . Line 37 evaluates the classification performance using the RandomForest model, and then considers the accuracy. Line 40 adjusts each word vector using an incremental model. Line 41 sets the condition to repeat three main processes: employ the classification model, calculate the maximum accuracy, and apply the incremental model to word vectors. Line 42 assigns the optimal vectors to _M_ . 

To detail the computational complexity of the proposed algorithm, each line in Fig.7 is examined: 

Lines 1 to 6: The outer loop runs from _i_ = 1 to _d_ , iterating _d_ times, where _d_ is the number of news titles. Inside this loop, the string _Si_ is split into a list _Wi_ , which takes _O_ ( _b_ ) time where _b_ is the number of words in each news title. The inner loop runs from _j_ = 1 to _b_ , iterating _b_ times for each _i_ . Therefore, the inner loop’s time complexity is _O_ ( _b_ ). Since the inner loop is nested within the outer loop, the total time complexity is _O_ ( _d_ · _b_ ). The research found that the average number of words per news title for each dataset was 9, 12, 14, 7, 11, and 12 for Thai news, Fake news, Article news, Indian news, Reuters news, and Variation news, respectively. Given these results, the number of words in any news title ( _b_ ) can typically be considered constant. Thus, the time complexity simplifies to 

_O_ ( _d_ ) (a) 

Line 7: This line processes all words in the set. The outer summation iterates from _i_ = 1 to _d_ , resulting in _d_ iterations. For each iteration of the outer summation, the inner summation iterates from _j_ = 1 to _b_ , resulting in _b_ iterations. Each element _wi,j_ is accessed in constant time, _O_ (1). Consequently, the time complexity is _O_ ( _d_ · _b_ ). Given that _b_ represents the number of words in each news title and is considered a constant, the time complexity simplifies to 

_O_ ( _d_ ) (b) 

Lines 8 to 14: Line 8 initializes an empty set _f_ to store the frequency of each word, which is an _O_ (1) operation. Line 9 involves scanning through all the documents to identify unique words. Given _G_ documents, each with an average of _T_ words, this step has a time complexity of _O_ ( _G_ · _T_ ). Within the loop, the code checks if the word _w_ is already in the set _f_ , which has an average time complexity of _O_ (1). If the word is found, the code increments its count by 1, an _O_ (1) operation. If the word is not found, the code adds it to the set with an initial count of 1, also an _O_ (1) operation. Therefore, the overall time complexity is 

_O_ ( _G_ · _T_ ) (c) 

Lines 15 and 16: This process involves converting each document into a vector that reflects the occurrences of each word from the established vocabulary. To create these word count vectors, each word must be examined and counted to ensure the representation accurately reflects the document’s content. The time complexity for this process is _O_ ( _G_ · _T_ ) (d) 

Lines 17 to 31: This section involves the clustering process. The code starts by initializing _k_ clusters. In lines 19-22, _k_ centroids are randomly chosen from the set of vectors { _v_ 1 _, v_ 2 _, v_ 3 _, . . . , vd_ }, which takes _O_ ( _k_ ) time. In lines 23-27, each of the _v_ vector is assigned to the nearest cluster, resulting in a nested loop where the outer loop runs _d_ times and the inner loop runs _k_ times, leading to a time complexity of _O_ ( _d_ · _k_ ). In lines 28-30, the centroids are updated by calculating the mean of the vectors in each cluster, which takes _O_ ( _d_ ) time for each of the _k_ clusters, resulting in a time complexity of _O_ ( _d_ · _k_ ). This entire process is repeated until the centroids no longer change, which can take up to _t_ iterations. Therefore, the overall time complexity is _O_ ( _t_ · ( _k_ + _d_ · _k_ + _d_ · _k_ )), which simplifies to _O_ ( _t_ · _d_ · _k_ ). Given that _k_ is considered constant and _t_ is proportional to _d_ , the time complexity can be expressed as 

_O_ ( _t_ · _d_ ) (e) 

Lines 32 to 34: The code begins by initializing a set of labels _L_ , an operation with a time complexity of _O_ (1). Following this, it sets _accuracymax_ to 0 and count to 0, both of which are also _O_ (1) operations. Since these initializations are independent of the input size _n_ , their time complexity remains constant. Consequently, the overall time complexity is _O_ (1) (f) 

Lines 35 to 41: The do-while loop starts by incrementing count by 1, which is an _O_ (1) operation. The RandomForest function is then called with the set of vector _v_ and labels _L_ . The time complexity involves both training and prediction phases. During training, the complexity is _O_ ( _r_ · _d_ log _d_ · _p_ ), where _r_ is the number of trees, _d_ is the number of samples, and _p_ is the number of features. For prediction, the complexity is _O_ ( _r_ · _a_ ), with _a_ being the maximum depth of the trees. Assuming _r_ , _p_ , and _a_ are constant; therefore, the overall process of random forest is _O_ ( _d_ log _d_ ). The if condition checks if the current accuracy is greater than _accuracymax_ , an _O_ (1) operation. If true, _accuracymax_ is updated, and the incremental function is called, which modifies the set of vectors. The loop continues until either the accuracy no longer improves or count reaches 6. In the worst case, the loop runs 6 times. Therefore, the overall time complexity of the code is _O_ (6 · (1 + _d_ log _d_ + 1)), which simplifies to 

_O_ ( _d_ log _d_ ) (g) 

Line 42: This line involves copying or referencing the set of vectors. Assuming there are _d_ vectors in the set, the time complexity of this operation is _O_ ( _d_ ) (h) The overall complexity of the proposed algorithm is the sum of all these complexities: (a) + (b) + (c) + (d) + (e) + (f) + (g) + (h), which simplifies to _O_ (( _G_ · _T_ ) + ( _t_ · _d_ ) + ( _d_ log _d_ )) (i) 

6696 

VOLUME 13, 2025 

P. Chaipornkaew, T. Banditwattanawong: Novel Method for News Recommendation on Websites 


![](prepared/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm/images/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm.pdf-0013-01.png)


**TABLE 2.** Details of the news titles of six datasets. 


![](prepared/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm/images/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm.pdf-0013-03.png)


## _D. PHASE-III NEWS TITLE SUGGESTION_ 

This phase provides a recommendation list for each visitor. Firstly, visitor mapping was performed by aggregating the visitor log and the target classes of news titles. When this step was finished, every visitor was assigned to one group of news clusters. The next step was to rearrange the news titles in each group based on the created date. In order to generate the recommendation list, the top five news titles were selected from the same cluster to which visitors belonged. 

## **IV. EXPERIMENTS** 

In this section, all experimental settings are presented. 

## _A. DATASETS AND DATA PRE-PROCESSING_ 

In this study, the proposed approach is evaluated by utilizing six news title datasets. The first dataset is a set of Thai news titles which was provided by a private digital television company in Thailand. For confidentiality reasons, the name of the company has not been disclosed. This dataset, called ‘‘Thai news’’, is aggregated from three sources which are 103,860 news titles, 53,054 visits, and 4,997 actions. In this step, missing values and invalid data were excluded. In addition, the pre-processing process for text was applied, such as deleting stop words, spaces, symbols, numbers, and empty strings. After the data cleansing process was finished, only 2,496 news titles remained for the next step. 

The remaining five datasets used to evaluate the proposed approach were from public datasets provided by Kaggle. In order to refer to each dataset, their assigned names were ‘‘Fake news’’, ‘‘Article news’’, ‘‘Indian news’’, ‘‘Reuters news’’, and ‘‘Variation news’’. All pre-processing processes applied for Thai news were also employed with these five datasets. In order to reduce bias, the size of feature matrix of each public dataset should be similar to the size of feature matrix of Thai news. The size of feature matrix was generated based on the variations of words in news title. Since there were many variations of words in each public dataset, the number of news titles of public datasets was different from one another. Each news title was then separated into words and converted using feature representation. The feature matrix of each dataset was then generated. Table. 2 presents the source and number of instances for each dataset, while Table. 3 illustrates the feature matrix of news titles corresponding to each word embedding algorithm. 

**TABLE 3.** Feature matrix of news titles for each word embedding algorithm. 


![](prepared/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm/images/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm.pdf-0013-12.png)


**TABLE 4.** Details of the clusters based on TF-IDF. 


![](prepared/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm/images/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm.pdf-0013-14.png)


Variation news already provided the categories of news titles while the other five datasets did not define the categories of news titles. Therefore, the elbow method was applied to find the optimal number of clusters. The number of clusters was investigated between 2 and 30. According to the experiment, the optimal numbers of clusters of Thai news, Fake news, Article news, Indian news, and Reuters news should be 14, 7, 10, 8, and 13, respectively. The cluster details for each algorithm are shown in Tables. 4 through VIII. 

## _B. EXPERIMENTAL SETUP_ 

The experiment was conducted on a system running Windows 10, equipped with an Intel(R) Core(TM) i5-8365U CPU and 16 GB of RAM. Python version 3.7.6 was used to implement the proposed algorithm. For Thai language word segmentation, Pythainlp version 2.3.2 was utilized. The nltk library, version 3.8.1, handled word tokenization, while the gensim library was used for word embedding. Contextual embeddings were generated using the Transformer library, version 4.46.2. Torch version 2.5.1 was employed for word embeddings. The scikit-learn library, version 0.24.2, was used to apply several well-known algorithms, including k-means, TF-IDF, Cross Validation, Bag-of-Words, 

6697 

VOLUME 13, 2025 

P. Chaipornkaew, T. Banditwattanawong: Novel Method for News Recommendation on Websites 


![](prepared/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm/images/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm.pdf-0014-01.png)


**TABLE 5.** Details of the clusters based on Word2Vec. 


![](prepared/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm/images/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm.pdf-0014-03.png)


**TABLE 7.** Details of the clusters based on Bag-of-Words. 


![](prepared/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm/images/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm.pdf-0014-05.png)


**TABLE 6.** Details of the clusters based on Doc2Vec. 

**TABLE 8.** Details of the clusters based on transformer. 


![](prepared/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm/images/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm.pdf-0014-08.png)


and Random Forest. Hyperopt version 0.2.7 was used to determine the optimal hyperparameters. The same hyperparameter settings were applied to the remaining five public datasets as those used for the Thai news dataset. The hyperparameter settings for the experiment are detailed in Table. 9. 

## _C. PERFORMANCE MEASUREMENTS_ 

In the research, classification performance was measured using four metrics which were accuracy, precision, recall, and f1-score. Since all datasets are regarded as imbalanced data, the accuracy value alone cannot indicate model performance. Thus, the other metrics are also applied to ensure the performance of the classification models. 


![](prepared/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm/images/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm.pdf-0014-12.png)


## **V. EXPERIMENTAL RESULTS** 

In this study, a private news dataset and five public news datasets were used. Although all data sets were imbalanced as the nature of news and to be handled in our future work, the results show that CVO yields outstanding performance in several cases. This section is divided into three parts: A) the results for the private dataset (Thai news), B) the results for the five public datasets (Fake news, Article news, Indian news, Reuters news, and Variation news), and C) discussion of the results. 

## _A. RESULTS ON THE THAI NEWS DATASET_ 

The proposed Clustered-Vectors Optimization (CVO) was compared with other models. To mediate bias due to the 

6698 

VOLUME 13, 2025 

P. Chaipornkaew, T. Banditwattanawong: Novel Method for News Recommendation on Websites 


![](prepared/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm/images/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm.pdf-0015-01.png)


**TABLE 9.** Hyperparameter settings for each algorithm. 


![](prepared/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm/images/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm.pdf-0015-03.png)


**TABLE 10.** Performance comparison of the proposed CVO with other word embedding algorithms for Thai news. 


![](prepared/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm/images/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm.pdf-0015-05.png)


random sampling of the training and test sets, a ten-fold crossvalidation was applied for both the training and test sets. The average of four metrics, namely accuracy, precision, recall, and f1-score, was presented in this section based on ten-fold cross-validation. Table. 10 provides a detailed comparison of the proposed CVO model and other word embedding models. The results, evaluated using the Random Forest algorithm, indicate that the CVO model outperformed the five word embedding algorithms—TF-IDF, Word2Vec, Doc2Vec, Bagof-Words, and Transformer—across all metrics. Among the word embedding algorithms, Bag-of-Words, Transformer, and Doc2Vec performed better than TF-IDF and Word2Vec. Notably, Word2Vec had the lowest performance, with an accuracy of only 55.21%. 

## _B. RESULTS ON THE PUBLIC DATASETS_ 

This section compares the results of CVO with the other word embedding models on five publicly available datasets, which are Fake news, Article news, Indian news, Reuters news, and Variation news. The performance of the different models was evaluated by employing ten-fold cross-validation and the Random Forest model. Table. 11 demonstrates that the proposed CVO model performed exceptionally well on Indian news across all metrics. The results show an accuracy of 99.90%, precision of 99.41%, recall of 99.62%, and an F1-Score of 99.53%. When focusing on accuracy, the CVO algorithm also outperformed in Article news and Variation news, achieving 99.44% and 99.32%, respectively. Although the CVO could not surpass Word2Vec for Reuters news and Fake news, it still provided high accuracy compared to TF-IDF, Doc2Vec, and Bag-of-Words. Additionally, the accuracy differences between CVO and Word2Vec for Fake news and Reuters news were only 0.30 and 0.42, respectively. Although Word2Vec outperformed the CVO model for Fake news and Reuters news, it performed poorly on Indian news, with an accuracy of 79.40%, precision of 89.94%, recall of 76.23%, and an F1-Score of 79.68%. Among the six algorithms evaluated, Doc2Vec and Transformer exhibited the lowest performance. In summary, the CVO outperformed all other word embedding algorithms, except Word2Vec for Fake news and Reuters news, and maintained high accuracy across all datasets. Using the CVO model, organizations are able to perform better news clustering than before, especially when the dataset is imbalanced. Once news titles are categorized better, the news title recommendation system is likely to be more effective. Organizations can thus get higher customer engagement rates. Finally, it is possible to obtain more revenue when customers stay with the organization. 

## _C. DISCUSSION_ 

The proposed model shows superior performance for both Thai and Indian news compared to Article news, Variation news, and Fake news. A common characteristic of both Thai and Indian news is their focus on domestic topics. For instance, most Thai news covers events within Thailand, with only a few articles mentioning events outside the country. Similarly, Indian news predominantly focuses on domestic issues, with only a few titles addressing international events. Consequently, the news titles within Thai news are related to each other, as are the titles within Indian news. In contrast, Article news, Variation news, and Fake news can cover topics from around the world, resulting in a diverse range of terms that may not be related to each other. For Article news and Variation news, the CVO algorithm competes well with TFIDF, Word2Vec, Doc2Vec, Bag-of-Words, and Transformer in terms of accuracy. Therefore, when accuracy is the primary concern, the CVO algorithm is the best alternative. 

Although the CVO model does not outperform other word embedding algorithms for Fake news and Reuters news, it still achieves high performance, exceeding 98.5%. 

6699 

VOLUME 13, 2025 

P. Chaipornkaew, T. Banditwattanawong: Novel Method for News Recommendation on Websites 


![](prepared/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm/images/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm.pdf-0016-01.png)


**TABLE 11.** Performance comparison of the Clustered-Vectors Optimization (CVO) with other embedding algorithms for public news. 


![](prepared/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm/images/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm.pdf-0016-03.png)


In contrast, other methods like Word2Vec performs well on some datasets but poorly on others. For example, Word2Vec excels on Fake news and Reuters news but performs poorly on Indian news, with only 79.40% accuracy, 89.94% precision, 76.23% recall, and 79.68% F1-Score. Consequently, baseline methods such as TF-IDF, Word2Vec, Doc2Vec, and Transformer, may underperform on unseen datasets. Among the six algorithms evaluated, Doc2Vec and Transformer underperform compared to the others. Despite the advanced nature of the Transformer algorithm, its performance was inadequate. This is likely because the pretrained model used in the research wasn’t suitable for all datasets. Additionally, the Transformer may have struggled due to the brevity of the news titles, which were often phrases or slang rather than complete sentences, making them difficult to summarize effectively. 

When comparing the CVO model’s performance across Fake news, Article news, Reuters news, and Variation news, it does not consistently outperform other baseline algorithms. This inconsistency may be due to the diverse global topics covered by these news categories, making the CVO less suitable for such varied content. Given the numerous popular algorithms available for classification, this research experimented with several and found RandomForest to be the best fit for the experimental datasets. Consequently, RandomForest was chosen to evaluate the model. Although the CVO model shows only slight improvements over other baseline algorithms, even minor enhancements in news 

clustering performance can significantly boost revenue for organizations providing news to their customers. 

The key distinction between the proposed model and the baseline models lies in the use of a recurring process to determine optimal vectors, a feature absent in the baseline models. To further enhance the performance of the proposed CVO model, future research could focus on addressing data imbalance and reducing computational time. Although the model shows high accuracy, it has low recall on some datasets; for instance, in the Article news dataset, the model achieves 99.44% accuracy but only 93.66% recall. Since all datasets were imbalanced, applying data pre-processing techniques to address this imbalance could improve the CVO model’s performance. Additionally, while the optimization algorithm did not perform too slowly in this research due to the relatively small number of instances, applying the CVO model to real business scenarios with large datasets may result in slower running times. Future research could explore methods to reduce the computational time of the CVO model. 

In summary, the proposed CVO model can significantly enhance the performance of news clustering for both Thai and Indian news. Despite the absence of data pre-processing to manage imbalanced data, the model achieves a higher recall rate compared to other baseline methods. This superior performance is attributed to the model’s ability to determine optimal word vectors for clustering. Consequently, the proposed approach holds great potential for improving news recommendation systems. 

6700 

VOLUME 13, 2025 

P. Chaipornkaew, T. Banditwattanawong: Novel Method for News Recommendation on Websites 


![](prepared/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm/images/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm.pdf-0017-01.png)


The proposed model shows promise for improving clustering performance but faces several potential challenges. Unexpected characters in input sentences might cause the splitting operation to fail or produce incorrect tokens. Additionally, improper tokenization of words in the document can lead to inaccurate frequency counts. Initialization issues with the word frequency vector can disrupt subsequent steps. Randomly initializing centroids might result in poor clustering, especially if the initial centroids do not represent the data distribution well. Using an inappropriate distance metric to find the nearest centroid can assign words to incorrect clusters, degrading clustering performance. Incorrect implementation of the convergence condition might cause the algorithm to enter an infinite loop or terminate prematurely. Lastly, improper implementation of the incremental update of vectors might prevent the algorithm from improving accuracy as expected. 

Moreover, while the model tends to perform efficiently with small to moderately sized datasets, computational demands may increase with larger datasets, especially in high-dimensional spaces. According to the time complexity of the proposed model, the number of records _d_ affect the efficiency of the model, which is considered as _O_ ( _t_ · _d_ ) and _O_ ( _d_ log _d_ ). Scalability could be enhanced by employing simpler or more advanced clustering algorithms, optimizing hyperparameters for faster convergence, or by integrating parallel processing techniques to manage the increased computational load. However, these aspects are not the primary focus of this work. 

K-means was selected for its numerous advantages. Firstly, the well-known elbow method can be used to determine the optimal number of clusters when choosing k-means. Additionally, k-means is easy to understand and implement, and it guarantees convergence to a local minimum, ensuring a solution. It also adapts well to new data, which is beneficial in dynamic environments with constantly updated information. The results are straightforward to interpret, with each cluster represented by its centroid. The research primarily focused on vector optimization rather than clustering algorithms. Consequently, any clustering algorithm could be used to group news titles. However, k-means has some limitations, such as sensitivity to the initial placement of centroids and inefficiency in handling clusters of varying shapes and densities. 

## _D. FUTURE WORK_ 

The model is effective for small to medium-sized datasets, but larger datasets, particularly those in high-dimensional spaces, increase computational demands. Future research should aim to improve scalability by using simpler or more advanced clustering algorithms, tuning hyperparameters for faster convergence, or by employing parallel processing techniques to handle the increased computational load. The study also highlighted the importance of optimizing vectors rather than focusing solely on specific clustering algorithms, allowing flexibility in choosing methods for grouping news headlines. While k-means was selected for specific reasons, exploring 

other clustering algorithms could provide interesting results. The research did not address the issue of imbalanced data, as it is common for most news titles to belong to one category while fewer titles fall into another. News agencies often provide popular types of news to engage their audience, resulting in one group of news titles being significantly larger than others. However, it would be interesting for future work to explore algorithms that handle imbalanced data to evaluate their performance. Well-known methods include resampling techniques, cost-sensitive learning, and data augmentation, as studied by Baek et al., Hasib et al., and Jaiswal et al. Suitable metrics for evaluating performance on imbalanced datasets include the ROC Curve, PR Curve, Detection Rate (DR), Balanced Accuracy (BAcc), and Balanced Error Rate (BER). Future research could also explore other datasets, such as national and international news, to assess whether the model’s performance remains consistent or varies. Additionally, investigating the sequence of news titles that a user has clicked on or read over time, including news titles, content, and timestamps, could be valuable. 

## **VI. CONCLUSION** 

Recommendation systems are vital in the business world, as the recommendation list is generated from the clustering process results. Therefore, the clustering performance of the recommendation model is crucial to providing a list that aligns with customer preferences. This research introduces a novel method for news recommendation on websites using the Clustered-Vectors Optimization (CVO) algorithm. Text pre-processing techniques are employed to prepare the data for clustering. K-means and Incremental algorithms are integrated with the optimization technique to cluster and determine the optimal sets of word vectors. The clustering performance is then evaluated using the RandomForest algorithm. 

The proposed model can enhance customer engagement on websites, potentially increasing revenue for organizations. To verify the efficiency of the CVO model, five benchmark models which are TF-IDF, Word2Vec, Doc2Vec, Bag-ofWords, and Transformer were considered. The experiment utilized one real-world Thai news dataset, provided by a private digital television company in Thailand, and five public news datasets that had been widely-used in previous studies. The experimental results demonstrated that the proposed CVO model outperformed the five benchmark models when applied to Thai and Indian news. Additionally, the model achieved a higher recall rate despite the absence of data pre-processing for imbalanced data. For Article news and Variation news, the CVO model also excelled in terms of accuracy. Therefore, the proposed model is well-suited for clustering in recommendation systems and other applications requiring a clustering process. 

## **ACKNOWLEDGMENT** 

The authors extend their gratitude to an unnamed company, whose identity remains confidential. They acknowledge the 

6701 

VOLUME 13, 2025 

P. Chaipornkaew, T. Banditwattanawong: Novel Method for News Recommendation on Websites 


![](prepared/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm/images/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm.pdf-0018-01.png)


sensitivity of the business data provided by this company and assure that it will be used solely for research purposes and not otherwise disclosed. 

## **REFERENCES** 

- [1] G. Adomavicius and A. Tuzhilin, ‘‘Toward the next generation of recommender systems: A survey of the state-of-the-art and possible extensions,’’ _IEEE Trans. Knowl. Data Eng._ , vol. 17, no. 6, pp. 734–749, Jun. 2005. 

- [2] Statista, Inc., New York, NY, USA. _Daily Time Spent on Social Networking By Internet Users Worldwide From 2012 To 2022_ . Accessed: Dec. 4, 2022. [Online]. Available: https://www.statista. com/statistics/433871/dailysocial-media-usage-worldwide/ 

- [3] P. Chaipornkaew and T. Banditwattanawong, ‘‘A recommendation model based on visitor preferences on commercial websites using the TKD-NM algorithm,’’ in _Proc. Lect. Notes Netw. Syst._ , Aug. 2021, pp. 123–133. 

- [4] P. Chaipornkaew and T. Banditwattanawong, ‘‘A recommendation model based on user behaviors on commercial websites using TF-IDF, KMeans, and apriori algorithms,’’ in _Proc. Recent Adv. Inf. Commun. Technol._ , Jan. 2021, pp. 55–65. 

- [5] U. Erra, S. Senatore, F. Minnella, and G. Caggianese, ‘‘Approximate TF– IDF based on topic extraction from massive message stream using the GPU,’’ _Inf. Sci._ , vol. 292, pp. 143–161, Jan. 2015. 

- [6] C. Padurariu and M. E. Breaban, ‘‘Dealing with data imbalance in text classification,’’ _Proc. Comput. Sci._ , vol. 159, pp. 736–745, Jan. 2019. 

- [7] D. Kim, D. Seo, S. Cho, and P. Kang, ‘‘Multi-co-training for document classification using various document representations: TF-IDF, LDA, and Doc2 Vec,’’ _Inf. Sci._ , vol. 477, pp. 15–29, Mar. 2019. 

- [8] N. Alami, M. Meknassi, N. En-Nahnahi, Y. El Adlouni, and O. Ammor, ‘‘Unsupervised neural networks for automatic Arabic text summarization using document clustering and topic modeling,’’ _Expert Syst. Appl._ , vol. 172, Jun. 2021, Art. no. 114652. 

- [9] Y. Wang, ‘‘Research on the TF–IDF algorithm combined with semantics for automatic extraction of keywords from network news texts,’’ _J. Intell. Syst._ , vol. 33, no. 1, Jul. 2024, Art. no. 20230300. 

- [10] D. S. Asudani, N. K. Nagwani, and P. Singh, ‘‘Impact of word embedding models on text analytics in deep learning environment: A review,’’ _Artif. Intell. Rev._ , vol. 56, no. 9, pp. 10345–10425, Sep. 2023. 

- [11] F. Wang, Q. Wang, F. Nie, Z. Li, W. Yu, and F. Ren, ‘‘A linear multivariate binary decision tree classifier based on K-means splitting,’’ _Pattern Recognit._ , vol. 107, Nov. 2020, Art. no. 107521. 

- [12] Y. Zhang, J. Lu, F. Liu, Q. Liu, A. Porter, H. Chen, and G. Zhang, ‘‘Does deep learning help topic extraction? A kernel K-means clustering method with word embedding,’’ _J. Informetrics_ , vol. 12, no. 4, pp. 1099–1117, Nov. 2018. 

- [13] K. Wang, T. Zhang, T. Xue, Y. Lu, and S.-G. Na, ‘‘E-commerce personalized recommendation analysis by deeply-learned clustering,’’ _J. Vis. Commun. Image Represent._ , vol. 71, Aug. 2020, Art. no. 102735. 

- [14] S. Xiong and D. Ji, ‘‘Exploiting flexible-constrained K-means clustering with word embedding for aspect-phrase grouping,’’ _Inf. Sci._ , vols. 367–368, pp. 689–699, Nov. 2016. 

- [15] M. Mhiri, S. Abuelwafa, C. Desrosiers, and M. Cheriet, ‘‘Hierarchical representation learning using spherical k-means for segmentation-free word spotting,’’ _Pattern Recognit. Lett._ , vol. 101, pp. 52–59, Jan. 2018. 

- [16] A. P. Muniyandi, R. Rajeswari, and R. Rajaram, ‘‘Network anomaly detection by cascading K-means clustering and C4.5 decision tree algorithm,’’ _Proc. Eng._ , vol. 30, pp. 174–182, Jan. 2012. 

- [17] Y. T. Song and S. Wu, ‘‘Slope one recommendation algorithm based on user clustering and scoring preferences,’’ _Proc. Comput. Sci._ , vol. 166, pp. 539–545, Jan. 2020. 

- [18] S. A. Curiskis, B. Drake, T. R. Osborn, and P. J. Kennedy, ‘‘An evaluation of document clustering and topic modelling in two online social networks: Twitter and Reddit,’’ _Inf. Process. Manage._ , vol. 57, no. 2, Mar. 2020, Art. no. 102034. 

- [19] I. M. Tianda, M. N. Ubadah, M. F. F. Mardianto, S. A. A. Munawwarah, N. Ishak, D. Amelia, and E. Ana, ‘‘Clustering fake news with K-means and agglomerative clustering based on Word2 Vec,’’ _Int. J. Math. Comput. Res._ , vol. 12, no. 2, pp. 3999–4007, Feb. 2024. 

- [20] A. Razia Sulthana and S. Ramasamy, ‘‘Ontology and context based recommendation system using neuro-fuzzy classification,’’ _Comput. Electr. Eng._ , vol. 74, pp. 498–510, Mar. 2019. 

- [21] A. Anaissi and M. Goyal, ‘‘SVM-based association rules for knowledge discovery and classification,’’ in _Proc. 2nd Asia–Pacific World Congr. Comput. Sci. Eng. (APWC CSE)_ , Dec. 2015, pp. 1–5. 

- [22] Statista, Inc., New York, NY, USA. _Share of Individuals Reading or Downloading Online News, Newspapers or Magazines in Great Britain From 2007 to 2020_ . Accessed: Dec. 10, 2022. [Online]. Available: https://www.statista.com/statistics/286210/online-news-newspapersand-magazine-consumption-in-great-britain/ 

- [23] C. Wu, F. Wu, X. Wang, Y. Huang, and X. Xie, ‘‘FairRec: Fairness-aware news recommendation with decomposed adversarial learning,’’ in _Proc. 35th Int. Conf. Artif. Intell._ , Jan. 2020. 

- [24] Y. Chen, W. Ye, C. Lin, and Y. Chen, ‘‘Unbiased news recommendation model combining time and content,’’ _Expert Syst. Appl._ , vol. 256, Dec. 2024, Art. no. 124864. 

- [25] M. An, F. Wu, C. Wu, K. Zhang, Z. Liu, and X. Xie, ‘‘Neural news recommendation with long- and short-term user representations,’’ in _Proc. 57th Annu. Meeting Assoc. Comput. Linguistics_ , Florence, Italy, Jul. 2019. 

- [26] C. Wu, F. Wu, M. An, Y. Huang, and X. Xie, ‘‘Neural news recommendation with topic-aware news representation,’’ in _Proc. 57th Annu. Meeting Assoc. Comput. Linguistics_ , Florence, Italy, Aug. 2019. 

- [27] S. Raza and C. Ding, ‘‘News recommender system: A review of recent progress, challenges, and opportunities,’’ _Artif. Intell. Rev._ , vol. 55, no. 1, pp. 749–800, Jan. 2022. 

- [28] L. Heitz, J. A. Lischka, A. Birrer, B. Paudel, S. Tolmeijer, L. Laugwitz, and A. Bernstein, ‘‘Benefits of diverse news recommendations for democracy: A user study, challenges, and opportunities,’’ _Digit. Journalism_ , vol. 10, no. 10, pp. 1–21, 2022. 

- [29] C. Wu, F. Wu, Y. Huang, and X. Xie, ‘‘Personalized news recommendation: Methods and challenges,’’ _ACM Trans. Inf. Syst._ , vol. 41, no. 1, pp. 1–50, Jan. 2023. 

- [30] Z. Mao, X. Zeng, and K.-F. Wong, ‘‘Neural news recommendation with collaborative news encoding and structural user encoding,’’ in _Proc. Findings Assoc. Comput. Linguistics, EMNLP_ , 2021, pp. 46–55. 

- [31] C. Panagiotakis, H. Papadakis, A. Papagrigoriou, and P. Fragopoulou, ‘‘Improving recommender systems via a dual training error based correction approach,’’ _Expert Syst. Appl._ , vol. 183, Nov. 2021, Art. no. 115386. 

- [32] Z. Su, X. Zheng, J. Ai, Y. Shen, and X. Zhang, ‘‘Link prediction in recommender systems based on vector similarity,’’ _Phys. A, Stat. Mech. Appl._ , vol. 560, Dec. 2020, Art. no. 125154. 

- [33] Y. Xiao, ‘‘News recommendation system based on user interest and deep network,’’ _Proc. Comput. Sci._ , vol. 243, pp. 1105–1114, Jan. 2024. 

- [34] L. Zhang, T. Luo, F. Zhang, and Y. Wu, ‘‘A recommendation model based on deep neural network,’’ _IEEE Access_ , vol. 6, pp. 9454–9463, 2018. 

- [35] N. Li and Y. Xia, ‘‘Movie recommendation based on ALS collaborative filtering recommendation algorithm with deep learning model,’’ _Entertainment Comput._ , vol. 51, Sep. 2024, Art. no. 100715. 

- [36] R. Mishra, P. Kumar, and B. Bhasker, ‘‘A web recommendation system considering sequential information,’’ _Decis. Support Syst._ , vol. 75, pp. 1–10, Jul. 2015. 

- [37] Z. Sun, J. Zhang, H. Sun, and X. Zhu, ‘‘Collaborative filtering based recommendation of sampling methods for software defect prediction,’’ _Appl. Soft Comput._ , vol. 90, May 2020, Art. no. 106163. 

- [38] K. Taneja, J. Vashishtha, and S. Ratnoo, ‘‘Transformer based unsupervised learning approach for imbalanced text sentiment analysis of e-commerce reviews,’’ _Proc. Comput. Sci._ , vol. 235, pp. 2318–2331, Jan. 2024. 

- [39] R. Arreerard and T. Senivongse, ‘‘Thai defamatory text classification on social media,’’ in _Proc. IEEE Int. Conf. Big Data, Cloud Comput., Data Sci. Eng. (BCD)_ , Jul. 2018, pp. 73–78. 

- [40] P. Boonyarat, D. J. Liew, and Y.-C. Chang, ‘‘Leveraging enhanced BERT models for detecting suicidal ideation in Thai social media content amidst COVID-19,’’ _Inf. Process. Manage._ , vol. 61, no. 4, Jul. 2024, Art. no. 103706. 

- [41] I. Arroyo-Fernández, C.-F. Méndez-Cruz, G. Sierra, J.-M. TorresMoreno, and G. Sidorov, ‘‘Unsupervised sentence representations as word information series: Revisiting TF–IDF,’’ _Comput. Speech Lang._ , vol. 56, pp. 107–129, Jul. 2019. 

- [42] H. Li and J. Wang, ‘‘Collaborative annealing power K-means++ clustering,’’ _Knowl.-Based Syst._ , vol. 255, Nov. 2022, Art. no. 109593. 

- [43] H. Lu, Z. Cheng, R. Huang, Y. Qin, Y. Chen, C. Lin, and J. Xue, ‘‘DEDCIMAE: A deep evolutionary document clustering model with inherited mixed autoencoder,’’ _Inf. Sci._ , vol. 678, Sep. 2024, Art. no. 120880. 

6702 

VOLUME 13, 2025 

P. Chaipornkaew, T. Banditwattanawong: Novel Method for News Recommendation on Websites 


![](prepared/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm/images/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm.pdf-0019-01.png)


- [44] C.-K. Chen, T.-W. Hung, and T.-C. Weng, ‘‘Optimal replenishment policies with allowable shortages for a product life cycle,’’ _Comput. Math. Appl._ , vol. 53, no. 10, pp. 1582–1594, May 2007. 

- [45] W. Villegas-Ch, A. M. Navarro, and S. Sanchez-Viteri, ‘‘Optimization of inventory management through computer vision and machine learning technologies,’’ _Intell. Syst. Appl._ , vol. 24, Dec. 2024, Art. no. 200438. 

- [46] Y. Djenouri, A. Belhadi, P. Fournier-Viger, and H. Fujita, ‘‘Mining diversified association rules in big datasets: A cluster/GPU/genetic approach,’’ _Inf. Sci._ , vol. 459, pp. 117–134, Aug. 2018. 

- [47] M. W. Newcomer and R. J. Hunt, ‘‘NWTOPT—A hyperparameter optimization approach for selection of environmental model solver settings,’’ _Environ. Model. Softw._ , vol. 147, Nov. 2021, Art. no. 105250. 

   - [59] A. Jaiswal, P. Dwivedi, and R. K. Dewang, ‘‘Handling imbalance dataset issue in insider threat detection using machine learning methods,’’ _Comput. Electr. Eng._ , vol. 120, Dec. 2024, Art. no. 109726. 

   - [60] D. Shakya, V. Deshpande, M. J. S. Safari, and M. Agarwal, ‘‘Performance evaluation of machine learning algorithms for the prediction of particle Froude number F _rn_ using hyper-parameter optimizations techniques,’’ _Expert Syst. Appl._ , pp. 1–16, 2024. 

   - [61] J. Bergstra, R. Bardenet, Y. Bengio, and B. Kégl, ‘‘Algorithms for hyperparameter optimization,’’ in _Proc. 25th Annu. Conf. Neural Inf. Process. Syst._ , Dec. 2011, pp. 1–10. 

- [48] J. Ma, C. Ma, T. Li, W. Yan, R. S. Faradonbeh, H. Long, and K. Dai, ‘‘Real-time classification model for tunnel surrounding rocks based on high-resolution neural network and structure–optimizer hyperparameter optimization,’’ _Comput. Geotechnics_ , vol. 168, Feb. 2024, Art. no. 106155. 

- [49] K. O. Lye, S. Mishra, D. Ray, and P. Chandrashekar, ‘‘Iterative surrogate model optimization (ISMO): An active learning algorithm for PDE constrained optimization with deep neural networks,’’ _Comput. Methods Appl. Mech. Eng._ , vol. 374, Feb. 2021, Art. no. 113575. 

- [50] P. Tauzowski, B. Blachowski, and J. Lógó, ‘‘Topology optimization of elasto-plastic structures under reliability constraints: A first order approach,’’ _Comput. Struct._ , vol. 243, Jan. 2021, Art. no. 106406. 

- [51] Y. Chen, Y. Sun, and B. Wang, ‘‘Improving the performance of optimization algorithms using the adaptive fixed-time scheme and reset scheme,’’ _Mathematics_ , vol. 11, no. 22, p. 4704, Nov. 2023. 

- [52] C. D. Manning, P. Raghavan, and H. Schüze, ‘‘Term frequency and weighting,’’ in _Introduction To Information Retrieval_ . Cambridge, U.K.: Cambridge Univ. Press, 2009, pp. 117–119. [Online]. Available: https://nlp.stanford.edu/IR-book/html/htmledition/irbook.html 


![](prepared/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm/images/A_Novel_Method_for_News_Recommendation_on_Websites_Using_the_Clustered-Vectors_Optimization_Algorithm.pdf-0019-14.png)


PIYANUCH CHAIPORNKAEW was born in Bangkok, Thailand, in 1977. She received the bachelor’s degree in chemical engineering from Mahidol University, in 1999, and the Master of Science degree in information systems from Hawaii Pacific University, USA, in 2001. Currently, she is pursuing the Ph.D. degree in computer science with Kasetsart University, Thailand. Her research interests include text mining, machine learning, and computer vision. 

- [53] T. Mikolov, I. Sutskever, K. Chen, G. S. Corrado, and J. Dean, ‘‘Distributed representations of words and phrases and their compositionality,’’ in _Proc. Adv. Neural Inf. Process. Syst._ , vol. 26, Dec. 2013, pp. 3111–3119. 

- [54] Q. V. Le and T. Mikolov, ‘‘Distributed representations of sentences and documents,’’ in _Proc. 31st Int. Conf. Mach. Learn._ , vol. 4, Jun. 2014, pp. 1188–1196. 

- [55] S. Yuan, N. Liu, B. Sun, and C. Zhao, ‘‘A domain-knowledge based reconstruction framework for out-of-domain news title classification,’’ _Expert Syst. Appl._ , vol. 237, Mar. 2024, Art. no. 121483. 

- [56] F. Sufi, ‘‘Advanced computational methods for news classification: A study in neural networks and CNN integrated with GPT,’’ _J. Economy Technol._ , 2024, doi: 10.1016/j.ject.2024.09.001. 

- [57] H. Baek, S. Lee, and S. Kim, ‘‘Are female users equally active? An empirical study of the gender imbalance in Korean online news commenting,’’ _Telematics Informat._ , vol. 62, Sep. 2021, Art. no. 101635. 

- [58] K. M. Hasib, N. A. Towhid, K. O. Faruk, J. Al Mahmud, and M. F. Mridha, ‘‘Strategies for enhancing the performance of news article classification in bangla: Handling imbalance and interpretation,’’ _Eng. Appl. Artif. Intell._ , vol. 125, Oct. 2023, Art. no. 106688. 

THEPPARIT BANDITWATTANAWONG was 

born in Bangkok, Thailand. He received the B.Eng. degree (Hons.) in computer engineering from the King Mongkut’s Institute of Technology Ladkrabang, Thailand, the M.Eng. degree from the Asian Institute of Technology, Thailand, and the Ph.D. degree in informatics from the National Institute of Informatics (NII), The Graduate University for Advanced Studies, Tokyo, Japan. He is currently an Associate Professor with the Department of Computer Science, Kasetsart University, Bangkok. His main areas of research interests include intelligent optimization and networked data optimization. 

6703 

VOLUME 13, 2025 

