
![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0001-00.png)


Received 27 April 2025, accepted 28 May 2025, date of publication 3 June 2025, date of current version 11 June 2025. _Digital Object Identifier 10.1109/ACCESS.2025.3576253_ 

## Spatio-Temporal Aware Collaborative Service Ranking Prediction in IoT-Enabled Edge Computing 

## YUZE HUANG 1, (Member, IEEE), XIAO CHEN1, WENHUI ZHANG1, QIANXI LI1, AND HE LI2 

1School of Information Science and Engineering, Chongqing Jiaotong University, Chongqing 400074, China 

2School of Artifact Intelligent and Software, Nanyang Normal University, Nanyang 473061, China 

Corresponding author: He Li (lihe@nynu.edu.cn) 

This work was supported in part by the Natural Science Foundation of Chongqing, China, under Grant CSTB2022NSCQ-MSX0368; and in part by the Young Project of Science and Technology Research Program of Chongqing Education Commission of China under Grant KJQN202200702. 

- **ABSTRACT** With the rapid proliferation of services deployed on edge servers, selecting high quality services from a multitude of functionally similar offerings based on their rankings has become a critical issue. Service ranking is an effective approach to solve this problem. Traditional QoS aware service ranking approaches encounter new challenges in edge computing enabled Internet of Things (IoT) systems. On one hand, the geographical characteristics of services introduce heterogeneity into the evaluation criteria for service ranking. On the other hand, analyzing the multi-dimensional temporal characteristics of QoS poses a significant challenge. To address these challenges, we propose a spatio-temporal aware collaborative service ranking prediction approach, named ST-CRank, to achieve accurate service ranking results. Specifically, a spatial-aware service partial ranking model is introduced to generate partial rankings. In this model, a silhouette coefficient based clustering algorithm is utilized to partition edge domains, and services deployed on the same edge server are compared using the partial ranking model. The QoS comparisons are forecasted using a deep time series model to obtain partial rankings for each edge server, thereby capturing the multi-dimensional temporal characteristics of QoS. With the partial rankings obtained, the global ranking is achieved by aggregating the partial rankings within the same edge domain. Finally, the effectiveness of ST-CRank is evaluated through large scale real world dataset based experiments. The results demonstrate that our approach achieves higher accuracy in prediction compared to other baseline algorithms. 

**INDEX TERMS** Edge computing, Internet of Things (IoT), spatio-temporal aware, quality of service (QoS), service ranking prediction. 

## **I. INTRODUCTION** 

Internet of things (IoT) is an innovation network which interconnects geographically distributed devices [1]. In an IoT network, numerous services should process the data collected from sensors and devices [2]. With the development of IoT technology, sensors and devices are connected with each other though a network, and generate massive data to transmit to services for processing. In traditional cloud computing, transmitting massive data to 

The associate editor coordinating the review of this manuscript and approving it for publication was Leimin Wang . 

a remote cloud server is time-consuming and resourceconsuming [3], which cannot provide the low latency services to users. In order to fill this gap, a new computing paradigm named edge computing has been produced accordingly [4]. 

In edge computing paradigm, massive data are processed on edge devices near the users, and thus the services are deployed on the edge servers rather than on the remote centralized cloud [5]. Therefore, the services deployed on the edge servers can perform actions locally, and thus the network overhead and the latency are reduced accordingly [6]. Obviously, the edge computing can easily integrate with 

2025 The Authors. This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License. For more information, see https://creativecommons.org/licenses/by-nc-nd/4.0/ 

97930 

VOLUME 13, 2025 

Y. Huang et al.: Spatio-Temporal Aware Collaborative Service Ranking Prediction in IoT-Enabled Edge Computing 


![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0002-01.png)


IoT systems or intelligent transport systems to mitigate the computation-related problems [7], [8]. 

In IoT based edge computing, how to select the high quality IoT services according to Quality of Service (QoS) is an important issue. Thus, service ranking is the critical step for selecting the high quality services. In service ranking, how to rate the candidate services and order them according to the observed QoS values is the most crucial problem [9]. **We notice that it is difficult to evaluate all services with the same criterion due to the geographically distributed of services in edge environment. Therefore, service ranking prediction is a typical approach to obtain the order of similar functionality services [10].** 

Based on the existing service ranking prediction researches [11], [12], [13], we found that these approaches cannot address new challenges of spatial and temporal characteristics produced by edge computing. More specifically, the challenges can be introduced in detail as follows: 

- 1) **The geographical distributions of edge servers may affect the accuracy of service ranking prediction.** In edge computing environment, services are deployed on the edge servers geographically, and users can invoke the services seamlessly. Due to the coverage limitation of edge servers, a single edge server cannot cover all areas around users [14]. With the mobility of users, edge server handoffs occur. Therefore, it is impractical to rate all services by a single server in edge computing [15]. The heterogeneity of rating environment may lead the large errors for service ranking, thus, how to obtain the accuracy service ranking results by investigating the spatial characteristics of edge computing is a urgent problem for service ranking prediction. 

- 2) **Multi-dimensional temporal characteristics of QoS may affect the accuracy of service ranking prediction.** The temporality of QoS is another non-negligible factor for service ranking or QoS forecasting [16], [17]. We also noticed that the behaviors of mobile users can significantly influence the volatility of QoS across various temporal dimensions [18]. Therefore, how to investigate the multi-dimensional temporal characteristics of QoS is another urgent problem for service ranking prediction. 

In our previous work [17], we proposed a time-aware service ranking prediction approach to achieve the global ranking. In this approach, the partial rankings are obtained by an ARIMA based time series forecasting algorithm. Although this contribution can decrease the impact of different environments, this approach mainly focuses on how to obtain the service ranking by investigating the temporal characteristics of QoS, and ignore the effect of geographical distributions of edge servers. Another defect of previous work is that traditional approaches cannot fit the multi-dimensional temporal characteristics of QoS [19]. **Therefore, how to achieve service rankings by investigating the spatial and** 

## **multi-dimensional temporal characteristics of QoS is a critical issue for service ranking prediction in edge environments.** 

To address these challenges, we produced a spatio-temporal aware service collaborative ranking prediction approach named ST-CRank to obtain the service ranking with high accuracy. First, we present a spatial aware partial service ranking model to achieve the partial service rankings. In this model, all edge servers are divided into several edge domains according to their geographical locations, and then the service pairwise model is constructed to obtain the comparison values of the services on each server. Second, the partial rankings of each edge servers are obtained by a deep time series model named ST-ResNet to fit the temporal QoS attributes from multi-dimensions. Finally, the accuracy global ranking are achieved by aggregating the partial rankings within the same edge domain. More specifically, the contributions of this paper are threefold as follows. 

- 1) A spatio-temporal aware collaborative service ranking prediction approach is introduced to achieve the service ranking, which can achieve the service ranking by investigating the spatial and temporal dynamic characteristics of QoS. 

- 2) A spatial-aware partial service ranking model is presented to obtain the service partial ranking, in this model, the edge domains are divided by a silhouette coefficient based clustering algorithm, and then a deep time series model named ST-ResNet is presented to investigate the multi-dimensional temporal characteristics of QoS, facilitating the prediction of QoS attributes. 

- 3) A collaborative service ranking prediction model is constructed to achieve the accurate global ranking by aggregating the partial rankings within the same edge domain, which can eliminate the impact of different environments caused by the limitation of coverage of edge servers. 

The remainder of this paper is organized as follows. We first present the basic definitions of this paper in Section II. Then Section III proposes the overall framework of our proposed service ranking prediction approach. The details of the spatio-temporal aware collaborative service ranking approach can be found in Section IV. Furthermore, the efficacy of our approach is evaluated in Section V. Finally, we introduce the related works of this paper in Section VI and conclude our work in Section VII. 

## **II. PRELIMINARIES** 

In this section, we present the foundational concepts and definitions that underpin our paper in this paper, which focuses on delineating the essential components of QoS as the principal input for our methodology. 

Edge computing is a new computing paradigm, which can be regarded as the supplement and optimization of cloud computing [20]. In edge computing environments, the numerous sensor devices generate the massive data and 

97931 

VOLUME 13, 2025 

Y. Huang et al.: Spatio-Temporal Aware Collaborative Service Ranking Prediction in IoT-Enabled Edge Computing 


![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0003-01.png)


transmit them to the edge servers, which are responsible for processing the data and providing the low latency services to users [21]. To reduce the service invoking latency and avoiding the network congestion, the services with high computational requirements are offloaded on the edge servers, and users invoke the services from nearby edge servers [22]. As the number of services deployed on edge servers increases, it becomes important to select the high quality services from a large pool of functionally similar services based on QoS values. Thus, service ranking is a common method for service selection. We note that each edge server often considers the limitation of coverage areas, and the invoked edge server may handed off due to user mobility. Therefore, the location of the users may lead to heterogeneity in QoS evaluation criterion, and user mobility may introduce spatio-temporal characteristics into QoS. 

Before introducing the basic concept of QoS observed by user, we list the important symbols in this paper, which can be found in Table 1. 

**TABLE 1.** List of important symbols. 


![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0003-05.png)


In edge computing enabled IoT network, we delineate a series of services as _S_ = { _s_ 1 _, s_ 2 _, . . . , si_ }, and each service _si_ is associated with user _uj_ . After gathering all QoS values within time frame _t_ , a QoS matrix is established. As shown in Fig. 1, in the QoS matrix, each QoS attribute is indicated as _v_ = { _v[ij]_ 1 _[,][ v][ij]_ 2 _[, . . . ,][ v] t[ij]_[}][, which denotes the QoS value of service] _si_ invoked by user _uj_ . 


![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0003-07.png)



![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0003-08.png)



![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0003-09.png)



![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0003-10.png)



![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0003-11.png)


**FIGURE 1.** QoS matrix. 

Our research delves into the dynamic fluctuations of QoS attributes over time by analyzing the QoS datasets invoked 

by users. We employed a methodological framework by deep time series model to forecast the QoS comparison values. In sight of the literatures on time series forecasting models, it is commonly found that some models, including the ANN model, the LSTM model, and the ARIMA model, can achieve prediction results [23]. However, these traditional approaches mainly focus on single trends of time series, and cannot well fit multi-dimensional temporal characteristics of time series data, which may lead to large errors in forecasting. Compared with existing methods, we present a deep time series model based approach to analyze the dynamic changes in QoS from multi-dimensions spatio-temporal characteristics and capture the regularity characteristics of user service invocation in edge environments, which can effectively remedy the shortcomings of existing approaches. 

## **III. FRAMEWORK OF ST-CRANK** 

In the real world, numerous edge servers are deployed in geographical regions. Thus, the heterogeneity of the environments may lead to the heterogeneity of evaluation criteria, which means the traditional QoS forecasting algorithm cannot be suitable for edge computing. In our previous work [17], we presented a service ranking prediction algorithm in IoT environments, but the ARIMA based time series forecasting algorithm cannot involve the multi-dimensional temporal characteristic. On the other hand, the method aggregates all partial rankings, which is impractical in edge environments and may lead to large errors for service ranking prediction. 

In sight of previous works, we propose a method named ST-CRank to obtain global service rankings based on partial service rankings. The proposed ST-CRank can be divided into three stages: a spatial-aware partial service ranking model, deep time series model based QoS comparison forecasting, and the global ranking aggregation algorithm. The details can be found in Fig. 2. 

In this framework, various edge servers are first divided into different edge domains according to their locations. For each edge domain, the services are cached in the edge servers and the users invoke them near the edge servers. With the mobility of users, the QoS datasets exhibit temporal dynamic characteristics. In order to investigate the multi-dimensional temporal characteristics of the QoS, the service partial ranking model is introduced to obtain the QoS comparison values of the services deployed on an edge server, and then the deep neural network based time series forecasting algorithm is presented to forecast the service partial ranking results. Finally, the global ranking is obtained by aggregating the partial rankings within the same edge domain by obtaining the steady state probability, thus achieving service ranking for each entire edge domain. 

## **IV. COLLABORATIVE SERVICE RANKING PREDICTION MODEL** 

## _A. SPATIAL AWARE SERVICE PARTIAL RANKING MODEL_ 

As Fig. 3 shows, the services are deployed on edge servers, and the users invoke the low-latency services seamlessly. 

97932 

VOLUME 13, 2025 

Y. Huang et al.: Spatio-Temporal Aware Collaborative Service Ranking Prediction in IoT-Enabled Edge Computing 


![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0004-01.png)



![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0004-02.png)


**FIGURE 2.** Framework of ST-CRank. 

In edge environment, each edge server has its limited coverage. When the edge server cannot cover the location of mobile user, handed off to another edge server occurs. Thus, the spatial characteristics of QoS values is an non-negligible factor. In this paper, we present a spatial-aware service partial ranking model. In this model, the edge domains are first partitioned by the silhouette coefficient based clustering algorithm, and then a service pairwise model is presented to obtain the QoS comparison values of services for each edge server. 

To our best knowledge, the traditional k-means clustering algorithm often sets the k value with a subjective approach, which is a crucial factor for clustering algorithm. Here we present the silhouette coefficient based k-means clustering algorithm for dividing the edge domains. The silhouette coefficient is an efficient evaluation metric that indicates the degree of cohesion and separation of clusters. The detailed procedure of edge domain partitioning algorithm can be expressed as follows. 

First, the average distance between edge server _i_ and other servers in a same cluster denoted as _ai_ , which can be calculated as follows. 


![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0004-07.png)


where the _Ci_ denotes the _i_ - _th_ cluster. From the above equation, we know the smaller the _ai_ , the more likely the sample should be clustered into this cluster, which is called the intra-cluster dissimilarity. 

Second, we use _bi_ denotes the distance between edge server _i_ and cluster _Cj_ , which can be calculated as follows. 


![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0004-10.png)


From the equation, we know the larger the _bi_ , the small probability that the sample belongs to other clusters, which can be called the inter-cluster dissimilarity. 

With _ai_ and _bi_ calculated, the silhouette coefficient can be represented as: 


![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0004-13.png)


Considering the relationship between _ai_ and _bi_ . The silhouette coefficient also can be represented as follows. 


![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0004-15.png)


From the above equation, we know the range of silhouette coefficient value is from -1 to 1. A larger silhouette coefficient value indicates the object is more similar to other objects in its own cluster and less similar to objects in neighboring clusters. We notice that when the silhouette coefficient reaches its largest value, the value of _k_ will be determined. The details of edge domain partitioning algorithm can be found in Algorithm 1. 

During the process of partitioning the edge domains, we employ the silhouette coefficient to determine the optimal value of k, which is mathematically rigorous. The computation of the silhouette coefficient considers both intra-cluster dissimilarity and inter-cluster dissimilarity, denoted as _ai_ and _bi_ , respectively. We argue that this measurement mechanism effectively evaluates clustering quality under various geographical distribution models. We observed that when datasets exhibit the differences in geographical distributions, the equation for computing the silhouette coefficient can adapt its evaluation criteria accordingly. For instance, in densely distributed regions, _ai_ tends to be smaller, indicating higher intra-cluster cohesion. Conversely, in sparsely distributed regions, the value of _bi_ increases, ensuring the rationality of clustering boundaries. Our algorithm employs a normalized distance measure to calculate the silhouette coefficient, making it robust enough to handle diverse geographical distributions within the dataset. 

97933 

VOLUME 13, 2025 

Y. Huang et al.: Spatio-Temporal Aware Collaborative Service Ranking Prediction in IoT-Enabled Edge Computing 


![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0005-01.png)



![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0005-02.png)


**FIGURE 3.** Spatial aware partial ranking model based on clustering. 

With the edge domains partitioned, we present the service pairwise model to obtain the QoS comparison values of the services. As discussed in our previous work [17], the services deployed on a same edge server are compared with each other, indicating the relationship between different services. 

Here, we use _O[n] ij_[to][represent][the][outcome][of] _[n]_[-th] comparison for service _si_ and _sj_ , which can be denoted as follows. 


![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0005-06.png)


Thus, _O[n] ij_[=][1][indicates][service] _[s][j]_[is][ranked][higher][than] service _si_ . Consequently, a directed graph _G_ = ( _V , E_ ) is constructed to denote the ranked services. Therefore, the transmission from service _si_ to _sj_ can be expressed as ( _si, sj, qij_ ), Based on the deductions in [17], we can calculate the comparison value _cpij_ of service _si_ and _sj_ as follows. 


![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0005-08.png)


where _qij_ denotes the probability of service _si_ is ranked higher than _sj_ . Thus the comparison value _cpij_ can be denoted as the following form. 


![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0005-10.png)


As described in [24], the QoS comparisons between different services can be modeled as a random walk on a directed graph _G_ . In this a graph, the transition probability from service _si_ to _sj_ , denoted as _pij_ , is given by Equation 8, as shown at the bottom of the next page. 

As shown in Equation 8, _dmax_ denotes the node with the maximum out degree. To ensure the stability of the random walk process, we normalize the transition probabilities such that[�] _j[p][ij]_[=][1,][and][incorporate][self-loops] into the graph. With the transition probabilities between states established, the objective of service ranking can be transformed into forecasting the comparison values of QoS. Consequently, we aim to forecast the comparison value _cpij_ with deep time series model. In the following section, we elaborate on the details of this deep time series model. 

## _B. DEEP NEURAL NETWORK BASED TIME SERIES FORECASTING_ 

With the service partial ranking model constructed, we can obtain the pairwise compared values of services deployed on the same edge server. We observed that, due to the mobility of users, the measured QoS values exhibit the temporal dynamic characteristics over time. Additionally, because of the heterogeneity of the environments and the geographically distributed nature of services deployment, it is impractical to evaluate all services by a single user. Therefore, forecasting the comparison values becomes an essential task. While existing studies have proposed efficient approaches to forecast univariate time series data of QoS, they rarely address the multi-dimensional temporal data of QoS. To this end, we employ a deep neural network model to analyze time series data and investigate the multi-dimensional temporal characteristics of QoS. 

Through analyzing the QoS values in depth, we found this data typically exhibit three attributes: closeness, periodicity, and tendency. Subsequently, we describe these attributes in detail below. 

97934 

VOLUME 13, 2025 

Y. Huang et al.: Spatio-Temporal Aware Collaborative Service Ranking Prediction in IoT-Enabled Edge Computing 


![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0006-01.png)


## **Algorithm 1** Edge Domain Partitioning Algorithm 

**Input:** Location Data of Edge Server 

- **Output:** Edge Domains _R_ = { _r_ 1 _, r_ 2 _, . . . , rk_ } 

- 1: **for** k=1,2,...,n **do** 

- 2: **for** i=1,2,...,n **do** 

- 3: Calculate the _ai_ and _bi_ , and obtain the silhouette coefficient of _i_ 

- 4: **end for** 

- 5: Obtain the average silhouette coefficient of the whole dataset with _k_ value, denoted as ¯ _s_ ( _k_ ) 

- 6: Select the _k_ value with the largest silhouette coefficient 

## 3) TENDENCY 

With the evolution of service demands, QoS may exhibit a tendency toward either increasing or decreasing over an extended period. 

As is known, traditional time series forecasting methods may not effectively capture the complex multi-dimension characteristics of QoS. To address this challenge, we adopt the ST-ResNet [25] model to forecast the future QoS value. Through such a deep time series network, we can not only capture the multi-dimensional temporal characteristics in time series data effectively, but also investigate the spatial characteristics simultaneously [25], [26], [27]. 

- 7: **end for** 

- 8: Select the _k_ samples as the initial center { _ui, u_ 2 _, . . . , uk_ } 

- 9: **while** True **do** 

- 10: _num_ = 0 

- 11: **for** i=0,1,...,k **do** 12: _Ci_ = _�_ 13: **end for** 14: **for** j=1,2,...,n **do** 15: Calculate the every distance between _vj_ and _ui_ 16: Determine the cluster according to the nearest set, and let _τj_ = arg min _dij i_ ∈{1 _,_ 2 _,...,k_ } 

- 17: _rτi_ = _rτi_ ∪ _uj_ 18: **end for** 19: **for** i=1,2,...,k **do** 20: _u_[′] _i_[=] _C_[1] _i_ � _x_[∈] _[C][i][x]_ 21: **if** _u_[′] _i_[̸=] _[ u][i]_ **[then]** 22: _u_[′] _i_[=] _[ u][i]_ 

- 23: **else** 24: _num_ + + 25: **end if** 26: **end for** 27: **if** _num_ = _k_ **then** 28: break 29: **end if** 30: **end while** 

31: **return** _R_ = { _ri, r_ 2 _, . . . , rk_ } 

## 1) CLOSENESS 

Service invoking data over adjacent time intervals usually exhibit a strong correlation, indicating that changes in QoS values are continuous in the short term. 

## 2) PERIODICITY 

Due to the behavior patterns of user other non-negligible factors, the QoS may clearly present periodic characteristics. 


![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0006-23.png)



![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0006-24.png)



![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0006-25.png)



![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0006-26.png)



![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0006-27.png)


**FIGURE 4.** ST-ResNet architecture. 

As Fig. 4 illustrates, the ST-ResNet employs the residual learning architecture, which captures both local and global spatial dependencies by constructing a multi-layered feature extraction network. Compared with other models, ST-ResNet can adaptively adjust feature weights during the processing of geographical location information for edge servers, thereby accommodating spatial distribution differences. 

In addition to capturing spatial characteristics, ST-ResNet investigates the multi-dimensional temporal characteristics through a multi-branched fusion mechanism. In this model, parallel residual units respectively capture the closeness, periodicity, and tendency characteristics of time series data, 


![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0006-31.png)


97935 

VOLUME 13, 2025 

Y. Huang et al.: Spatio-Temporal Aware Collaborative Service Ranking Prediction in IoT-Enabled Edge Computing 


![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0007-01.png)


a capability rarely found in other traditional time series models. Next, we will elaborate on the details of forecasting QoS comparison values through the ST-ResNet model. 

As described in above content, ST-ResNet model can analyze the closeness, periodicity, and tendency characteristics of time series data through three parallel residual units. Here, we use _cp[ij] t_[=][(] _[cp][ij]_ 1 _[,][ cp][ij]_ 2 _[, . . .][ cp] t[ij]_[)][to][denote][the][QoS] comparison values between service _i_ and service _j_ over _t_ times, which have been calculated as Equation 7. 

Next we divided the time series QoS comparison data into three parts. Here we use _M[(][c][)]_ = _(M_ 1 _. . . Mx)_ , _M[(][p][)]_ = � _M_ 1 _. . . My_ � and _M[(][t][)]_ = _(M_ 1 _. . . Mz)_ to represent the closeness, periodicity and tendency, respectively. Those dimensions are explored by a same network structure. Here we use closeness data as an example to introduce the analysis progress. First, the input data are processed through the convolutional layer _C_ 1 according to the following formula. 


![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0007-05.png)


where _W(_ 1 _)_ and _b(_ 1 _)_ represent the weight and bias of the convolutional layer _C_ 1, respectively. 

Subsequently, the data are processed through _L_ residual units, and the method in _n_ -th unit can be express as follows. 


![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0007-08.png)


where _Res_ denotes the residual unit, which can be defined as _Res (x)_ = _g (x)_ , and _g (x)_ is represented as the following form. 


![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0007-10.png)


where _W_ and _b_ are trainable parameters, and _ReLU_ is the activation function, _BN_ represents the Batch Normalization layer. After processing through residual units, the output data are processed by the one dimensional convolutional layer _C_ 2 according to the Equation 12, as shown at the bottom of the page. 

The processing of periodicity and tendency data is similar with the proximity data. With three parts are processed by the ST-ResNet model, the model integrates the outputs of three parts data, and then the final result is output through a hyperbolic tangent activation layer, which can be calculated according to the Equation 13, as shown at the bottom of the page. 

Finally, the model employs the Mean Square Error (MSE) function as the loss function to calculate the error as follows. 


![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0007-14.png)


As discussed above, ST-ResNet adopts an innovative residual learning architecture which captures the spatial dependencies by constructing a multi-leveled feature extraction network. In contrast to traditional models, ST-ResNet can adaptively adjust feature weights when handling the geographical locations of edge servers, thereby accommodating variations in spatial distribution. Moreover, the multi-branched fusion mechanism in ST-ResNet is especially well suited for addressing the multi-dimensional temporal characteristics of QoS. Specifically, the ST-ResNet model represents the closeness, periodicity, and tendency characteristics through parallel residual units, a capability not found in other models. 

Besides these considerations, the design of ST-ResNet incorporates the practical constraints of edge computing and is well suited for deployment on resource constrained edge servers. Additionally, the implementation of residual connections can mitigate the vanishing gradient problem during deep network training, thereby ensuring the stability of the model in long term forecasting tasks. 

In summary, compared with other models, ST-ResNet demonstrates significant advantages in handling spatial heterogeneity. Specifically, the ST-ResNet model exhibits superior performance in capturing spatial dependencies compared to the LSTM model. In contrast to traditional CNN and GNN models, the residual structure of ST-ResNet can provide stronger feature extraction capabilities, leading to higher computational efficiency when handling dynamic changes of QoS. Consequently, these advantages render ST-ResNet especially well suited for QoS forecasting tasks in edge computing environments. 

## _C. PARTIAL RANKINGS AGGREGATION ALGORITHM_ 

In the previous section, we have forecasted the comparison values of services by the deep time series model, thus obtaining the partial rankings for the same edge server. In order to obtain the global service ranking, we construct a Markov model to calculate the steady-state probabilities, which indicate the global service ranking. We found that due to the limitation of edge server coverage, aggregating partial rankings of all edge servers may introduce large errors for service ranking, and it is impractical for edge computing. To address this challenge, we aggregate the partial rankings within the same edge domain. 

As mentioned in our previous work [17], the transition probability _Prij_ of discrete time markov chain (DTMC) can 


![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0007-21.png)



![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0007-22.png)


97936 

VOLUME 13, 2025 

Y. Huang et al.: Spatio-Temporal Aware Collaborative Service Ranking Prediction in IoT-Enabled Edge Computing 


![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0008-01.png)


be expressed as follows. 


![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0008-03.png)


where _pij_ is the transition probability calculated from Equation 8. 

We use [ _π_ 1 _, π_ 2 _, . . . , πn_ ] to denote the steady-state probabilities of the DTMC, and we notice that[�] _[n] i_ =1 _[π][i]_[=][ 1.] Therefore, the steady state probabilities can be calculated using the following formula: 


![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0008-06.png)


With the steady state probabilities of the DTMC calculated, we can directly obtain the ranking of services in the same edge domain by ranking these probabilities. Next, we will describe the details of algorithm for determining the global ranking, which can achieve the global ranking and eliminate the differences in evaluation criteria caused by varied metrics and heterogeneous environments in edge computing. The process for obtaining the global ranking is described as follows. 

- Step 1. The edge domains are divided by a clustering based algorithm according to their geographical locations of the edge servers in edge computing environment, and then the pairwise comparison value of QoS deployed on the same edge server are obtained according to the Equation 7. 

- Step 2. The future comparison values are forecasted by the ST-ResNet model, and then the partial rankings for each edge server are obtained by the time series forecasting approach. 

- Step 3. The partial rankings in a same edge domain are aggregated, and the transition matrix _P_ is derived according to Equation 8. 

- Step 4. The steady-state probabilities of the transition matrix _P_ for DTMC are solved according to the Equation 16, and then the global ranking in each edge domain is obtained by ranking the steady state probabilities. 

The algorithm to achieve global ranking within edge domains is presented in Algorithm 2. 

## **V. EVALUATION** 

## _A. THEORETICAL ANALYSIS_ 

In this paper, we assume that there are _m_ edge servers in the edge computing environment, and _n_ IoT services are deployed on these edge servers. In our approach, we first divide the edge domains by the clustering based algorithm. In this clustering algorithm, the optimal silhouette coefficient must be determined, which has a time complexity of _O_ ( _lm_ ), where _l_ denotes the number of loops. During the clustering process, we let _t_ represent the number of iterations, thus the time complexity is _O_ ( _tlm_[2] ). In practice, both _l_ and _t_ are smaller than _m_ . So the time complexity for the edge domain partitioning algorithm can be approximated as _O_ ( _m_[2] ). 

**Algorithm 2** Service Ranking Prediction Algorithm 

- **Input:** QoS data **Output:** Service ranking within edge domains 

- 1: Initialize all learnable parameters _θ_ in the ST-ResNet 2: Construct training instances by combining the available time intervals into [ _M_[(] _[c]_[)] _, M_[(] _[p]_[)] _, M_[(] _[t]_[)] ] inputs based on closeness, periodicity, and tendency. 

- 3: **for** episode = 1 _,_ 2 _, . . . , E_ **do** 4: Select a minimal batch _Db_ of instances from the training set 

- 5: Update the model parameters _θ_ using the loss function with _Db_ 

- 6: **if** stop criteria are met **then** 7: end the training process 8: **end if** 9: **end for** 

- 10: Use the trained model to perform _X_ -step predictions with inputs _M_[(] _[c]_[)] _, M_[(] _[p]_[)] _, M_[(] _[t]_[)] 

- 11: Return [ _Mn_ +1 _, Mn_ +2 _, . . . , Mn_ + _x_ ] 12: Aggregate all predicted comparison values and compute the transition matrix _P_ 

- 13: Solve the DTMC using the transition matrix _P_ to obtain the steady state probabilities _π_ 

- 14: Rank the services based on their steady state probabilities _π_ 

With the edge domain divided, the services deployed on the same edge servers are compared by pairwise comparison model, and the future QoS comparison values are forecasted by deep time series model. Consequently, the time complexity 2 for pairwise comparison is _O_ (�� _Sj_ �� ), where �� _Sj_ �� represents the number of ranked services on each edge server. Therefore, the 2 overall computational complexity is _O_ (max _j_ �� _Sj_ �� ). 

With the partial rankings obtained, the transition matrix is calculated, and the steady-state probabilities are sorted to derive the global ranking. As described in our previous work [17], the overall computational complexity is _O_ ( _n_[2] ). We notice that the partial rankings within the same edge domain are aggregated. Assuming there are _p_ domains in the environment, and the number of services in the edge domain _i_ can be expressed as _Ki_ . So the time complexity is _O_ ( _ki_[2][),] where _ki_ ≪ _n_ . Notably,[�] _[p] i_ =1 _[k][i]_[=] _[n]_[. Therefore, the overall] computational complexity can be expressed as _O_ ( _[n] p_[2][).] 

In summary, the overall computational complexity of ST-CRank is _O_ ( _m_[2] + _[n] p_[2][).][Given][that] _[p]_[≪] _[m]_[≪] _[n]_[,][so][the] computational complexity of our approach is significant reduced to our previous work [17]. 

## _B. EXPERIMENTAL EVALUATION_ 

## 1) DATASETS AND EVALUATION METRICS 

In order to evaluate the efficiency of the proposed algorithm, we use WS-DREAM dataset to evaluate the efficiency [28], [29], which is a widely used dataset in real world. This dataset 

97937 

VOLUME 13, 2025 

Y. Huang et al.: Spatio-Temporal Aware Collaborative Service Ranking Prediction in IoT-Enabled Edge Computing 


![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0009-01.png)


provides detailed location information, including latitude and longitude, as well as application servers for 339 users and 5,825 web services. The distribution of services across different countries is summarized in Table 2. 

**TABLE 2.** Distribution of services. 

where, _wi_ represents the weight of _i_ -th edge domain, which can be calculate by the number of edge servers in the corresponding edge domain. _KRCC i_ denotes the KRCC value of the _i_ -th edge domain. 

## 2) EXPERIMENTAL RESULTS 

In this section, we first determine the parameters, such as silhouette coefficient and learning rate of ST-ResNet model. 

In WS-DREAM, the QoS attributes also encompass the throughput and response time values collected from 4,500 services distributed across 57 countries. These services are invoked by 142 users over 16 hour period with each measurement session lasting 15 minutes. By analyzing these observations, we found that all response times values range from 0 to 20 seconds, with an average value of about 3.165 seconds. The throughput values range from 0 to 6726.833 kbps, with an average value of about 9.509 kbps. The statistical characteristics are summarized in Table 3. 

In order to select the suitable parameters of ST-ResNet model, we utilized Root Mean Square Error (RMSE) and Mean Absolute Error (MAE) as the performance metrics to assess the efficiency of the forecasting model. These metrics enable a comprehensive evaluation of the performance for ST-ResNet model, and ensure the model delivers precise predictions. 

Considering the ST-ResNet model is a deep neural network, we computed the FLOPs of ST-ResNet and compared them with LSTM model. 

Finally, we use the Kendall Rank Correlation Coefficient (KRCC) to evaluate the accuracy of ranking results. It can measure the statistical dependency between two variables by calculating the correlation coefficient. The value of the Kendall ranking correlation coefficient ranges between -1 and 1. A coefficient value of 1 indicates a perfectly consistent rank, and a value of -1 indicates completely opposite ranking. If the coefficient value is 0, it indicates that there is no rank correlation between the variables. The equation for calculating the correlation coefficient is provided as follows, 


![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0009-11.png)


where _n_ represents the total number of services in _i_ -th edge domain, while _C_ and _D_ represent the number of concordant and discordant pairs in the rankings respectively. 

In this paper, we divided the global system into different edge domains and conducted cluster analysis for each domain. we employed the weighted average method to evaluate the service quality of each domain comprehensively. Here, the weights are determined based on the percentage of edge servers contained in each edge domain. Specifically, the final results are calculated by Equation 18. 


![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0009-14.png)


In order to divides the edge domains, we first determine the optimal silhouette coefficient. We noticed that when the edge servers are divides into three different domains, the silhouette coefficient reaches the maximum value of 0.791, therefore, we select this value as the basis to divide the edge servers, and the clustering results can be found in Fig. 5. 

To evaluate the convergence of the ST-RseNet in our proposed ST-Crank approach, we set the learning rates during the training process of ST-RseNet to four different levels, which are 0.00001, 0.00005, 0.0001, and 0.001. The results are shown in Fig. 6 and Fig. 7. 

From these figures, it is evident that at a learning rate of 0.00001, the model achieves convergence but gets trapped in a local optimum. This behavior stems from the excessively small learning rate, which leads to overly gradual updates of the model parameters, thereby hindering its ability to escape the local optimum. When the learning rate is increased to 0.00005, the model’s performance improves; however, it still fails to achieve an optimal state. This indicates that a higher learning rate is required for the model to adequately explore the parameter space. At a learning rate of 0.0001, the model demonstrates the best convergence characteristics, achieving rapid convergence and a relatively low training error. This improvement can be attributed to the balanced nature of this learning rate, which effectively reconciles training speed with optimization accuracy. Conversely, when the learning rate is further increased to 0.001, although the model converges more quickly, the final training error increases. This phenomenon arises because an excessively large learning rate may cause the model to overlook the optimal solution or skip over critical fine-grained features during the optimization process. Based on these considerations, we have selected a learning rate of 0.0001. 

Furthermore, we investigated the impact on performance for ST-ResNet with varying numbers of residual unit. Table 4 presents the RMSE and MAE metrics of the model with different numbers of residual units. The results indicate that when the number of residual units is set to 8, the model achieves optimal performance, with RMSE and MAE values of 0.0715 and 0.0409, respectively. Upon analysis, we found that when the number of residual units is fewer than 8, the model’s feature extraction capability is insufficient, preventing it from fully capturing the spatio-temporal features of QoS data. Conversely, when the number of units exceeds 8, the additional parameters do not improve performance and instead increase the risk of overfitting. 

With the parameters determined, we evaluate the efficiency of the proposed approach compared with the following 

97938 

VOLUME 13, 2025 

Y. Huang et al.: Spatio-Temporal Aware Collaborative Service Ranking Prediction in IoT-Enabled Edge Computing 


![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0010-01.png)


**TABLE 3.** QoS dataset characteristics. 


![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0010-03.png)


**FIGURE 5.** Clustering results. 


![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0010-05.png)


**FIGURE 6.** Training error convergence of ST-ResNet at different learning rates. 


![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0010-07.png)


**FIGURE 7.** Testing error convergence of ST-ResNet at different learning rates. 

**TABLE 4.** Experimental results for determining residual unit. 


![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0010-10.png)


baseline algorithms. It should be noticed that only the time series forecasting approaches are different in our 

experiments, while the same approach for aggregating the partial rankings is adopted to obtain the final global rankings. 

- **ARIMA** [19]: Forecasting the comparison values by the ARIMA model, which is a typical statistic based time series approach. 

- **LSTM** [30]: Forecasting the comparison value by the Long Short-Time Memory algorithm (LSTM), which is a classical time series model based on the Recurrent Neural Network (RNN). 

97939 

VOLUME 13, 2025 

Y. Huang et al.: Spatio-Temporal Aware Collaborative Service Ranking Prediction in IoT-Enabled Edge Computing 


![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0011-01.png)


- **PSO** : The Particle Swarm Optimization (PSO) based approach is adopted to search for the minimum RMSE values to obtain the forecasting values. 

- **SVD** : The Singular Value Decomposition (SVD) based approach is adopted to decompose the Hankel matrix, and then the comparison values of QoS are forecasted by a linear forecasting model based on the decomposed results. 

First, since both the ST-ResNet model and LSTM model are deep time series model, we compare their FLOPs to reflect the computation requirements of these deep neural network. As shown in Table 5, The FLOPs of LSTM are larger than those of the ST-ResNet model. By analyzing the reasons, we find that the FLOPs of each LSTM layer are approximately 9.453 MFLOPs, while the FLOPs of each residual unit are approximately 2.359 MFLOPs. The results indicate that in the LSTM model, adding an LSTM layer has a more significant impact on computational demand compared to adding a residual unit in the ResNet structure. 

**TABLE 5.** FLOPs of deep time series models. 

We noticed that it is difficult to calculate the FLOPs of other forecasting approach, such as ARIMA, PSO, and SVD. Therefore, we also evaluate all algorithms on response time data by conducting experiments and measuring the efficiency using RMSE and MAE metrics. The results are presented below. 

**TABLE 6.** The efficiency of different forecasting algorithms. 


![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0011-08.png)


From Table 6, it can be observed that the ST-CRank achieves the lowest values for both RMSE and MAE with values are 0.07595 and 0.05895 respectively. The LSTM and ARIMA algorithms exhibit similar levels of accuracy, with RMSE values of 0.07925 and 0.0814, respectively, and MAE values of 0.06215 and 0.06225, respectively. In contrast, the SVD and PSO result in significantly larger forecasting errors. As shown in Table 6, the RMSE values for SVD and PSO are 0.09765 and 0.54145, while their respective MAE values are 0.0769 and 0.46065. This discrepancy arises because SVD and PSO are not conventional time series forecasting algorithms, which inherently leads to greater forecasting errors. Furthermore, ST-ResNet demonstrates superior performance in capturing fine grained spatio-temporal features compared to LSTM and ARIMA. 

Finally, considering the large errors of PSO and SVD, we only evaluate the efficiency of our proposed ST-CRank approach by KRCC, and then compare it with LSTM and ARIMA algorithms. In order to evaluate the capability to handle different scales of matrix densities, we vary the proportions of selected services in each edge server from 10% to 60% with the step of 10%. Here, 10% means that only 10% services are randomly selected to obtain the partial rankings in the edge servers. The experimental results can be found in Fig. 8 and Fig. 9. 


![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0011-11.png)


**FIGURE 8.** Accuracy of ranking prediction for response time. 


![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0011-13.png)


**FIGURE 9.** Accuracy of ranking prediction for throughput. 

From these two figures, we can find that the three algorithms demonstrate a gradual improvement in KRCC as the number of selected services increases. Moreover, the ST-CRank achieves higher accuracy compared to LSTM and ARIMA. 

97940 

VOLUME 13, 2025 

Y. Huang et al.: Spatio-Temporal Aware Collaborative Service Ranking Prediction in IoT-Enabled Edge Computing 


![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0012-01.png)


More specifically, as shown in Figure 8, it can be observed that as the proportion of selected services increases from 10% to 60%, the KRCC of ST-CRank increases form 0.764 to 0.833. Similarly, the KRCC values of LSTM and ARIMA increase from 0.761 to 0.832, and from 0.756 to 0.825, respectively. All experimental results demonstrate that the KRCC of ST-CRank is approximately 0.10% to 0.58% higher than that of LSTM across different scales of selected services, and the KRCC of ST-CRank is approximately 0.87% to 1.32% higher than that of ARIMA across different scales of selected services. 

In Figure 9, as the proportion of selected services increases from 10% to 60%, the KRCC of ST-CRank rises from 0.843 to 0.893, while the KRCC values of LSTM and ARIMA increase from 0.839 to 0.886, and from 0.838 to 0.887, respectively. All experimental results demonstrate that, across different scales of selected services, the KRCC of ST-CRank is approximately 0.50% to 0.78% higher than that of LSTM, and approximately 0.45% to 0.71% higher than that of ARIMA. 

All experimental results indicate that ST-CRank achieves higher accuracy compared to other baseline algorithms across different matrix densities. Specifically, it demonstrates superior prediction ability when handling high matrix density, suggesting that our proposed approach is more effective in addressing large scale service ranking prediction problems than other baseline algorithms. 

In light of these results, we observe that the response time is primarily influenced by network transmission and service processing capabilities, which exhibit stability and a relatively simple pattern. Whether using STCRank, LSTM, or ARIMA, all methods can effectively capture this simple time series pattern. Particularly when the matrix density reaches 60%, all models can obtain sufficient learning samples for modeling the relatively simple pattern accurately, leading to their performance converging. In contrast, throughput is a more complex attribute of QoS, which is more significantly influenced by user behavior patterns. The closeness, periodicity and tendency characteristics of this attribute are more pronounced. Our experiments also demonstrate that ST-Crank can effectively extract such characteristics and achieve higher accuracy. 

## **VI. RELATED WORKS** 

## _A. SERVICE RANKING_ 

Edge computing is the supplement and optimization of cloud computing, which can provide the low-latency services to users [20]. In an edge computing enabled IoT system, the massive data are generated by the devices and transmitted to the edge servers. The services deployed on the edge servers receive the data, process them, and provide the services to users with low latency and high quality [21], [22]. As the number of services deployed on the servers increased, how 

to select the high-quality services is an important issue, and service ranking is an effective approach to solve this problem. 

Service ranking is a significant research topic in services computing, which focuses on how to effectively rank services with similar functions according to specific rules. The most commonly used method is evaluating and ranking the services based on the QoS attributes. For instance, trust scores for all web services were determined using a confusion matrix, which can facilitate the ranking of services [31]. Wang et al. filtered services by assessing credibility of users and then implemented a global ranking [32]. Devi and Shanmugalakshmi proposed a linear programming based method to reorder existing QoS values [33]. Shi et al. also introduced a QoS model that can express user preferences to rank services based on a combination of multiple QoS attributes [34]. 

We notice that most traditional service ranking works mainly focus on how to rank services with known QoS values, which is impractical in the real world, and it is also impractical for a single client to rate all services. In our previous work [17], we presented a time-aware model to forecast the future QoS, and fill the gaps caused by the heterogeneity of rating criteria. However this work mainly focuses on the temporal aspect of QoS, neglecting the geographical factors of services in edge computing environments. 

In summary, the spatial and temporal are non-negligible factors for services rankings. To address this problem, we propose the spatio-temporal aware collaborative ranking prediction approach to obtain the accurate global rankings. 

## _B. QoS FORECASTING_ 

As discussed in the above content, most service ranking studies are based on the known QoS values, which is impractical in the real world. Therefore, some studies have been proposed to forecast the unknown QoS values [35], [36]. Chen et al. proposed a swarm intelligence-based PSO-USRec algorithm, which can accurately predict missing QoS records between users and services [37]. Another study utilized a Neural Collaborative Filtering (NCF) based model to recommend and select services [38]. Wu et al. explored an approach to enhance the accuracy of QoS predictions by sensing the QoS characteristics [39]. Li et al. proposed a topology-aware neural framework, which can comprehensively capture the contextual environment of service invocations, and achieve higher accuracy QoS prediction results [40]. Tang et al. proposes a biased non negative tucker factorization of 3D Tensors model, which can extract potential features from QoS values [41]. Literature [42] proposes a location-aware deep interaction forest approach for web service QoS prediction, which can improve the accuracy of prediction results. However, these studies cannot fully address the challenges produced by distributed environments. 

97941 

VOLUME 13, 2025 

Y. Huang et al.: Spatio-Temporal Aware Collaborative Service Ranking Prediction in IoT-Enabled Edge Computing 


![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0013-01.png)


To address the challenges of edge computing, some researchers proposed various efficient approaches [43], [44]. Yan et al. noticed the significant characteristics of dynamic edge computing environments, such as user mobility and the incompleteness of historical QoS data, thus introducing a method that combines the ARIMA model with the SVD technique to predict QoS values [44]. Some deep neural network based approaches have been presented to improve the accuracy for QoS forecasting, however we observed that these approaches either can fail to capture the multi-dimensional spatio-temporal characteristics of QoS or necessitate substantial computational resources [45], [46], which makes them unsuitable for edge computing. 

Although these studies provide efficient methods for prediction through time series analysis, they often neglect to investigate the multi-dimensional characteristics inherent in time series data. Furthermore, most research focuses on forecasting QoS values and does not extend this analysis to service ranking predictions. To address this gap, we propose a spatio-temporal aware service ranking prediction method designed to explore the spatial and multi-dimensional characteristics of QoS while enhancing the accuracy of service ranking. 

## **VII. CONCLUSION** 

In this paper, we propose a spatio-temporal aware ranking method that derives global rankings from partial rankings. This approach first proposes a clustering-based algorithm to partition the edge servers into several edge domains. Subsequently, the ST-ResNet model is adapted to forecast the partial rankings. Finally, the partial rankings of each edge server are aggregated to archive the global ranking within an edge domain. In order to validate the efficiency of our approach, the experiments were conducted on large scale datasets. The results demonstrate that our approach achieves higher accuracy in ranking results compared to other baseline algorithms by exploring the spatial and multi-dimensional temporal characteristics of QoS. 

The main thrust of this paper is to explore the spatio-temporal characteristics of QoS and achieve the high accuracy global rankings in edge environments. Although security and privacy are important factors in edge computing, which is out of the scope of this study. In future work, we plan to explore privacy problem of QoS for service ranking. Additionally, we will further optimize the efficiency of deep time series models to obtain the more accurate results while reducing the computational complexity of the algorithm. 

## **REFERENCES** 

- [1] I. U. Din, M. Guizani, S. Hassan, B. Kim, M. K. Khan, M. Atiquzzaman, and S. Ahmed, ‘‘The Internet of Things: A review of enabled technologies and future challenges,’’ _IEEE Access_ , vol. 7, pp. 7606–7640, 2019. 

- [2] A. I. Abdallaahmed, A. Gani, S. H. A. Hamid, A. Abdelmaboud, H. J. Syed, R. A. A. Habeeb, and I. Ali, ‘‘Service management for IoT: Requirements, taxonomy, recent advances and open research challenges,’’ _IEEE Access_ , vol. 7, pp. 155472–155488, 2019. 

- [3] W. Yu, F. Liang, X. He, W. G. Hatcher, C. Lu, J. Lin, and X. Yang, ‘‘A survey on the edge computing for the Internet of Things,’’ _IEEE_ , vol. 6, no. 11, pp. 6900–6919, Nov. 2017. 

- [4] S. Hu and G. Li, ‘‘Dynamic request scheduling optimization in mobile edge computing for IoT applications,’’ _IEEE Internet Things J._ , vol. 7, no. 2, pp. 1426–1437, Feb. 2020. 

- [5] I. Hadžic, Y. Abe, and H. C. Woithe, ‘‘Server placement and selection for edge computing in the ePC,’’ _IEEE Trans. Services Comput._ , vol. 12, no. 5, pp. 671–684, Sep. 2019. 

- [6] K. Zhang, S. Leng, Y. He, S. Maharjan, and Y. Zhang, ‘‘Mobile edge computing and networking for green and low-latency Internet of Things,’’ _IEEE Commun. Mag._ , vol. 56, no. 5, pp. 39–45, May 2018. 

- [7] B. Omoniwa, R. Hussain, M. A. Javed, S. H. Bouk, and S. A. Malik, ‘‘Fog/Edge computing-based IoT (FECIoT): Architecture, applications, and research issues,’’ _IEEE Internet Things J._ , vol. 6, no. 3, pp. 4118–4149, Jun. 2019. 

- [8] J. Zhang and K. B. Letaief, ‘‘Mobile edge intelligence and computing for the Internet of Vehicles,’’ _Proc. IEEE_ , vol. 108, no. 2, pp. 246–261, Feb. 2020. 

- [9] I. Toma, D. Roman, D. Fensel, B. Sapkota, and J. M. Gómez, ‘‘A multicriteria service ranking approach based on non-functional properties rules evaluation,’’ in _Proc. 5th Int. Conf. Service-Oriented Comput. (ICSOC)_ , Jan. 2007, pp. 435–441. 

- [10] Z. Zheng, X. Wu, Y. Zhang, M. R. Lyu, and J. Wang, ‘‘QoS ranking prediction for cloud services,’’ _IEEE Trans. Parallel Distrib. Syst._ , vol. 24, no. 6, pp. 1213–1222, Jun. 2013. 

- [11] C. Mao, J. Chen, D. Towey, J. Chen, and X. Xie, ‘‘Search-based QoS ranking prediction for Web services in cloud environments,’’ _Future Gener. Comput. Syst._ , vol. 50, pp. 111–126, Sep. 2015. 

- [12] H. Ma, H. Zhu, Z. Hu, K. Li, and W. Tang, ‘‘Time-aware trustworthiness ranking prediction for cloud services using interval neutrosophic set and ELECTRE,’’ _Knowledge-Based Syst._ , vol. 138, pp. 27–45, Dec. 2017. 

- [13] V. Mareeswari and E. Sathiyamoorthy, ‘‘LocPSORank-prediction of ranking of Web services using location-based clustering and PSO algorithm,’’ _Int. J. Web Services Res._ , vol. 15, no. 3, pp. 38–60, Jul. 2018. 

- [14] Z. Rejiba, X. Masip-Bruin, and E. Marín-Tordera, ‘‘A survey on mobilityinduced service migration in the fog, edge, and related computing paradigms,’’ _ACM Comput. Surveys_ , vol. 52, no. 5, pp. 1–33, Sep. 2020. 

- [15] S. Wang, Y. Zhao, L. Huang, J. Xu, and C.-H. Hsu, ‘‘QoS prediction for service recommendations in mobile edge computing,’’ _J. Parallel Distrib. Comput._ , vol. 127, pp. 134–144, May 2019. 

- [16] M. Abu-Elkheir, M. Hayajneh, and N. A. Ali, ‘‘Data management for the Internet of Things: Design primitives and solution,’’ _Sensors_ , vol. 13, no. 11, pp. 15582–15612, Nov. 2013. 

- [17] Y. Huang, J. Huang, B. Cheng, S. He, and J. Chen, ‘‘Time-aware service ranking prediction in the Internet of Things environment,’’ _Sensors_ , vol. 17, no. 5, p. 974, Apr. 2017. 

- [18] Z. Liu, Q. Z. Sheng, W. E. Zhang, D. Chu, and X. Xu, ‘‘Contextaware multi-QoS prediction for services in mobile edge computing,’’ in _Proc. IEEE Int. Conf. Services Comput. (SCC)_ , Jul. 2019, pp. 72–79. 

- [19] G. E. P. Box, G. M. Jenkins, G. C. Reinsel, and G. M. Ljung, _Time Series Analysis: Forecasting and Control_ , 5th ed., Hoboken, NJ, USA: Wiley, 2015. 

- [20] Z. Shah, U. Javed, M. Naeem, S. Zeadally, and W. Ejaz, ‘‘Mobile edge computing (MEC)-enabled UAV placement and computation efficiency maximization in disaster scenario,’’ _IEEE Trans. Veh. Technol._ , vol. 72, no. 10, pp. 13406–13416, Oct. 2023. 

- [21] Y. Chen, D. Pi, S. Yang, Y. Xu, B. Wang, and Y. Wang, ‘‘A multi-strategy optimizer for energy minimization of multi-UAV-assisted mobile edge computing,’’ _Swarm Evol. Comput._ , vol. 91, Dec. 2024, Art. no. 101748. 

- [22] Q. Liu, H. Zhang, X. Zhang, and D. Yuan, ‘‘Improved DDPG based two-timescale multi-dimensional resource allocation for multi-access edge computing networks,’’ _IEEE Trans. Veh. Technol._ , vol. 73, no. 6, pp. 9153–9158, Jun. 2024. 

- [23] Y. Syu and C.-M. Wang, ‘‘QoS time series modeling and forecasting for Web services: A comprehensive survey,’’ _IEEE Trans. Netw. Service Manage._ , vol. 18, no. 1, pp. 926–944, Mar. 2021. 

- [24] J. Huang, Y. Chen, C. Lin, and J. Chen, ‘‘Ranking Web services with limited and noisy information,’’ _Proc. IEEE Int. Conf. Web Services (ICWS), pp. 638–645, Jun. 2014._ , vol. 2014, pp. 638–645, Jun. 2014. 

97942 

VOLUME 13, 2025 

Y. Huang et al.: Spatio-Temporal Aware Collaborative Service Ranking Prediction in IoT-Enabled Edge Computing 


![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0014-01.png)


- [25] J. Zhang, Y. Zheng, and D. Qi, ‘‘Deep spatio-temporal residual networks for citywide crowd flows prediction,’’ in _Proc. 31st AAAI Conf. Artif. Intell. (AAAI)_ , vol. 31, Feb. 2017, pp. 1655–1661. 

- [26] D. Zhai, A. Liu, S. Chen, Z. Li, and X. Zhang, ‘‘SeqST-ResNet: A sequential spatial temporal ResNet for task prediction in spatial crowdsourcing,’’ in _Proc. 24th Int. Conf. Database Syst. Adv. Appl. (DASFAA)_ , Jan. 2019, pp. 260–275. 

- [27] H. Wang, J. Chen, Z. Fan, Z. Zhang, Z. Cai, and X. Song, ‘‘ST-ExpertNet: A deep expert framework for traffic prediction,’’ _IEEE Trans. Knowl. Data Eng._ , vol. 35, no. 7, pp. 7512–7525, Jul. 2023. 

- [28] Y. Zhang, Z. Zheng, and M. R. Lyu, ‘‘WSPred: A time-aware personalized QoS prediction framework for Web services,’’ in _Proc. IEEE 22nd Int. Symp. Softw. Rel. Eng._ , Nov. 2011, pp. 210–219. 

- [29] Z. Zheng, Y. Zhang, and M. R. Lyu, ‘‘Investigating QoS of real-world Web services,’’ _IEEE Trans. Services Comput._ , vol. 7, no. 1, pp. 32–39, Jan. 2014. 

YUZE HUANG (Member, IEEE) received the Ph.D. degree in computer science and technology from Beijing University of Posts and Telecommunications in 2018. He is currently an Assistant Professor with the School of Information Science and Engineering, Chongqing Jiaotong University. He has published some papers in international conference proceedings and journals, such as FGCS, MobiCom, SCC, and _Sensors_ . His research interests include services computing and edge computing. He is a member of ACM. He served as a Reviewer for international journals, such as IEEE IoT JOURNAL and IEEE TRANSACTIONS ON NETWORK AND SERVICE MANAGEMENT. 

- [30] B. Ghojogh and A. Ghodsi, ‘‘Recurrent neural networks and long shortterm memory networks: Tutorial and survey,’’ 2023, _arXiv:2304.11461_ . 

- [31] M. Hasnain, M. F. Pasha, I. Ghani, M. Imran, M. Y. Alzahrani, and R. Budiarto, ‘‘Evaluating trust prediction and confusion matrix measures for Web services ranking,’’ _IEEE Access_ , vol. 8, pp. 90847–90861, 2020. 

- [32] X. Wang, P. He, J. Zhang, and Z. Wang, ‘‘QoS prediction of Web services based on reputation-aware network embedding,’’ _IEEE Access_ , vol. 8, pp. 161498–161508, 2020. 

- [33] D. R. and S. R., ‘‘Cloud providers ranking and selection using quantitative and qualitative approach,’’ _Comput. Commun._ , vol. 154, pp. 370–379, Mar. 2020. 

- [34] L.-L. Shi, L. Liu, L. Jiang, R. Zhu, and J. Panneerselvam, ‘‘QoS prediction for smart service management and recommendation based on the location of mobile users,’’ _Neurocomputing_ , vol. 471, pp. 12–20, Jan. 2022. 

- [35] T. Jithendra, M. Z. Khan, S. S. Basha, R. Das, A. Divya, C. L. Chowdhary, A. Alahmadi, and A. H. Alahmadi, ‘‘A novel QoS prediction model for Web services based on an adaptive neuro-fuzzy inference system using COOT optimization,’’ _IEEE Access_ , vol. 12, pp. 6993–7008, 2024. 

- [36] G. Khababa, S. Bessou, F. Seghir, N. H. Harun, A. S. Almazyad, P. Jangir, and A. W. Mohamed, ‘‘Collaborative filtering techniques for predicting Web service QoS values in static and dynamic environments: A systematic and thorough analysis,’’ _IEEE Access_ , vol. 13, pp. 45350–45376, 2025. 

- [37] J. Chen, C. Mao, and W. W. Song, ‘‘QoS prediction for Web services in cloud environments based on swarm intelligence search,’’ _KnowledgeBased Syst._ , vol. 259, Jan. 2023, Art. no. 110081. 

- [38] H. Gao, Y. Xu, Y. Yin, W. Zhang, R. Li, and X. Wang, ‘‘Context-aware QoS prediction with neural collaborative filtering for Internet-of-Things services,’’ _IEEE Internet Things J._ , vol. 7, no. 5, pp. 4532–4542, May 2020. 

- [39] D. Wu, X. Luo, M. Shang, Y. He, G. Wang, and X. Wu, ‘‘A datacharacteristic-aware latent factor model for Web services QoS prediction,’’ _IEEE Trans. Knowl. Data Eng._ , vol. 34, no. 6, pp. 2525–2538, Jun. 2022. 

- [40] J. Li, H. Wu, J. Chen, Q. He, and C.-H. Hsu, ‘‘Topology-aware neural model for highly accurate QoS prediction,’’ _IEEE Trans. Parallel Distrib. Syst._ , vol. 33, no. 7, pp. 1538–1552, Jul. 2022. 

- [41] P. Tang, T. Ruan, H. Wu, and X. Luo, ‘‘Temporal pattern-aware QoS prediction by biased non-negative tucker factorization of tensors,’’ _Neurocomputing_ , vol. 582, May 2024, Art. no. 127447. 

- [42] S. Zhu, J. Ding, and J. Yang, ‘‘Location-aware deep interaction forest for Web service QoS prediction,’’ _Appl. Sci._ , vol. 14, no. 4, p. 1450, Feb. 2024. 

- [43] Y. Yin, Z. Cao, Y. Xu, H. Gao, R. Li, and Z. Mai, ‘‘QoS prediction for service recommendation with features learning in mobile edge computing environment,’’ _IEEE Trans. Cognit. Commun. Netw._ , vol. 6, no. 4, pp. 1136–1145, Dec. 2020. 

- [44] C. Yan, Y. Zhang, W. Zhong, C. Zhang, and B. Xin, ‘‘A truncated SVD-based ARIMA model for multiple QoS prediction in mobile edge computing,’’ _Tsinghua Sci. Technol._ , vol. 27, no. 2, pp. 315–324, Apr. 2022. 

- [45] A. Hameed, J. Violos, A. Leivadeas, N. Santi, R. Grünblatt, and N. Mitton, ‘‘Toward QoS prediction based on temporal transformers for IoT applications,’’ _IEEE Trans. Netw. Service Manage._ , vol. 19, no. 4, pp. 4010–4027, Dec. 2022. 

- [46] Y. Eljakani, A. Boulouz, and C. Thomson, ‘‘Predicting diverse QoS metrics in IoT: An adaptive deep learning cross-layer approach for performance balancing,’’ _Ad Hoc Netw._ , vol. 170, Apr. 2025, Art. no. 103769. 


![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0014-24.png)



![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0014-25.png)



![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0014-26.png)



![](prepared/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing/images/Spatio-Temporal_Aware_Collaborative_Service_Ranking_Prediction_in_IoT-Enabled_Edge_Computing.pdf-0014-27.png)


XIAO CHEN received the B.Sc. degree from Chongqing University of Education, in 2021. He is currently pursuing the master’s degree with the School of Information Science and Engineering, Chongqing Jiaotong University. His research interests include edge computing and services computing. 

WENHUI ZHANG received the B.Sc. degree from Guizhou University of Commerce, in 2023. She is currently pursuing the master’s degree with the School of Information Science and Engineering, Chongqing Jiaotong University. Her research interests include deep learning and multimodal learning. 

QIANXI LI received the B.Sc. degree from Henan Normal University, in 2022. She is currently pursuing the master’s degree with the School of Information Science and Engineering, Chongqing Jiaotong University. Her research interests include deep learning and edge intelligent. 

HE LI received the M.S. degree in computer science and technology from Henan Polytechnic University, in 2013, and the Ph.D. degree in communication and information systems from the Key Laboratory of Networking and Switching Technology, Beijing University of Posts and Telecommunications, in 2018. He is currently an Associate Professor at Nanyang Normal University. His research interests include ad hoc and sensor network management. 

97943 

VOLUME 13, 2025 

