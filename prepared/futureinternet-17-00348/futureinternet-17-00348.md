
![](prepared/futureinternet-17-00348/images/futureinternet-17-00348.pdf-0001-00.png)


## _Article_ 

## **A Trusted Multi-Cloud Brokerage System for Validating Cloud Services Using Ranking Heuristics** 

**Rajganesh Nagarajan[1] , Vinothiyalakshmi Palanichamy[1] , Ramkumar Thirunavukarasu[2] and J. Arun Pandian[2,] *** 

- 1 Department of Computer Science and Engineering, Sri Venkateswara College of Engineering, Sriperumbudur 602117, India; rajganeshn@svce.ac.in (R.N.); vlakshmi@svce.ac.in (V.P.) 

- 2 School of Computer Science Engineering and Information Systems, Vellore Institute of Technology, Vellore 632014, India; ramkumar.thirunavukarasu@vit.ac.in 

- Correspondence: arunpandian.j@vit.ac.in 

## **Abstract** 

Academic Editor: Gianluigi Ferrari 

Received: 16 June 2025 Revised: 12 July 2025 Accepted: 30 July 2025 Published: 31 July 2025 

**Citation:** Nagarajan, R.; Palanichamy, V.; Thirunavukarasu, R.; Arun Pandian, J. A Trusted Multi-Cloud Brokerage System for Validating Cloud Services Using Ranking Heuristics. _Future Internet_ **2025** , _17_ , 348. https://doi.org/10.3390/fi17080348 

**Copyright:** © 2025 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https://creativecommons.org/ licenses/by/4.0/). 

Cloud computing offers a broad spectrum of services to users, particularly in multi-cloud environments where service-centric features are introduced to support users from multiple endpoints. To improve service availability and optimize the utilization of required services, cloud brokerage has been integrated into multi-cloud systems. The primary objective of a cloud broker is to ensure the quality and outcomes of services offered to customers. However, traditional cloud brokers face limitations in measuring service trust, ensuring validity, and anticipating future enhancements of services across different cloud platforms. To address these challenges, the proposed intelligent cloud broker integrates an intelligence mechanism that enhances decision-making within a multi-cloud environment. This broker performs a comprehensive validation and verification of service trustworthiness by analyzing various trust factors, including service response time, sustainability, suitability, accuracy, transparency, interoperability, availability, reliability, stability, cost, throughput, efficiency, and scalability. Customer feedback is also incorporated to assess these trust factors prior to service recommendation. The proposed model calculates service ranking (SR) values for available cloud services and dynamically includes newly introduced services during the validation process by mapping them with existing entries in the Service Collection Repository (SCR). Performance evaluation using the Google cluster-usage traces dataset demonstrates that the ICB outperforms existing approaches such as the Clustering-Based Trust Degree Computation (CBTDC) algorithm and the Service Context-Aware QoS Prediction and Recommendation (SCAQPR) model. Results confirm that the ICB significantly enhances the effectiveness and reliability of cloud service recommendations for users. 

**Keywords:** cloud broker; cloud service; service registry; service ranking; service recommendation 

## **1. Introduction** 

Cloud computing enables users to access services such as infrastructure, applications, and platforms on an on-demand basis [1]. Typically, users interact with cloud services through a single cloud service provider’s interface. However, in today’s dynamic and open digital ecosystem, relying solely on a single vendor often fails to meet diverse user requirements, particularly in terms of service quality. As a solution, multi-cloud computing has emerged, offering a broader range of services with greater flexibility. This paradigm supports the development of highly scalable and reliable service environments, allowing 

https://doi.org/10.3390/fi17080348 

_Future Internet_ **2025** , _17_ , 348 

_Future Internet_ **2025** , _17_ , 348 

2 of 15 

users to access best-in-class services across multiple providers. Moreover, multi-cloud computing addresses critical concerns such as vendor lock-in, cost–performance optimization, data privacy, and regulatory compliance. To further streamline service selection and delivery, intelligent cloud brokers [2] have been introduced. These brokers operate at both the producer and consumer levels, facilitating the provisioning of high-quality, validated services from multi-cloud environments. In this context, the intelligent cloud broker, as proposed in this work, is responsible for validating and verifying cloud services, thereby enhancing trust and efficiency in service recommendations. 

In general, the validation and verification of a cloud services are intended to provide the most reliable, robust, and secure services in accordance with customer expectations. This also assumes an ability to continuously offer cloud services even during uncertain interferences. In addition, the validation and verification of a service is usually determined using a number of multifaceted indicators which can be performed by the intelligent cloud brokers. The existing brokers perform the service selection based on either considering the Service Level Agreements (SLA) or Quality of Services (QoS’s) factors. In addition to that, the users’ feedback and ratings of the services can also be used for the identification of the right services by applying a number of techniques. All these processes are carried out for the single cloud provider only. No such attempts have been found with respect to multicloud computing. In this paper, an intelligent cloud broker with self-healing properties is proposed to perform the task of service validation and verification for a multi-cloud environment. 

In summary, the key contributions of this paper are as follows: 

- (1) Proposal of an Intelligent Cloud Broker—Introduces a novel intelligent cloud broker that extracts trust factors from a multi-cloud environment to enhance service selection processes; 

- (2) Trust Prediction and Clustering—Implements a trust prediction mechanism by validating and verifying extracted trust factors, followed by clustering services using a service ranking algorithm; 

- (3) Service Recommendation Framework—Provides a robust service recommendation system that incorporates validation reports to ensure reliability and accuracy. 

The rest of this paper is organized as follows: In Section 2, we recount the related work in multi-cloud service recommendation system. Section 3 explores the proposed system, which performs the validation and verification process by considering the thirteen service trust factors. The experimental works with the results and discussion are presented in Section 4. Finally, Section 5 concludes our proposal with future directions. 

## **2. Literature Review** 

Aldawsari et al. [3] proposed a review work on cloud brokers in a multi-cloud environment. The authors put forth a valid argument, that the available cloud brokers were not suited to the heterogeneous environment. In addition to that, energy consumption has been accounted for and highlighted in their work. However, the paper failed to address the possible techniques to overcome the identified issues. Chauhan et al. [4] highlighted the usages of a cloud broker in an interconnected cloud computing environment. Through this study, the authors have analyzed the strengths and weaknesses of the cloud broker in the areas such as pricing, optimization, trust, and QoS. Since the paper is a survey, deeper discussion only focused on better understanding of cloud broker in the multi-cloud environment. Yao et al. [5] mentioned the various roles of cloud service brokers such as intermediation, aggregation, arbitration, integration, and customization. Hence, the service delivery process is entirely coordinated by cloud service providers, the cloud service broker, and the customers. Supposing that there is an issue in any one of the involved parties, it 

_Future Internet_ **2025** , _17_ , 348 

3 of 15 

will certainly affect the performance of the broker. Petcu [6] addressed the need for interoperability between the clouds, since the clouds are locked in by vendors and need to be combined to fulfill the cloud user’s requirements. Though we currently have hybrid-type clouds, it is mandatory to interlink the multiple clouds for the better performance and user satisfaction. Hence, the authors proposed an approach to provide features such as portability and interoperability among multiple cloud providers. But this proposal does not highlight the practical approach to resolving the issues of the interoperability between the cloud service providers. 

Similarly, the authors in [7] also addressed the problem of service composition in multi-cloud environments. They also focused specifically on interoperability issues while performing multi-cloud service composition. In some situations, the reasoning is more difficult due to the nature of complex user requirements and the heterogeneity of cloud services. Hence, it is necessary to upgrade the entire system using parallel programming models. In another work [8], the authors addressed the interoperability and portability problems of cloud architectures. Cloud ontology-based service discovery and selection has been carried out to resolve the interoperability and portability problems in a cloud environment. In addition, Nagarajan et al. [9] performed the service selection with the support of constructed cloud ontology. A semantic network-based approach with the intersection search concept is advocated to perform the service selection. Calheiros et al. [10] discussed the limitations of the single cloud provider in the process of service offering. According to the increase in the demand of services, the existing approaches suffered in two aspects, such as SLA and QoS. Hence, the authors proposed an inter-cloud framework with the support of agents. The agents are responsible for publishing, discovering, and providing the services to the cloud user with agreed SLA. However, the decision-making policies for buying and selling services are not addressed in this paper. Grozev and Buyya [11] presented a review to emphasize the necessity of an inter-cloud architecture to accomplish reliability, Quality of Service (QoS), and cost efficiency by exploiting multiple clouds. The authors proposed the classifications for inter-cloud architectures and brokering apparatuses. The cloud environments that facilitate the brokering of distributed applications were also discussed. 

Mostajeran et al. [12] presented a review on the use of SLA-based brokering for inter-cloud computing which focused on QoS. In this work, the authors have elaborated on some of the SLA-based brokers and their workflow. All kinds of basic information on the aspects of the broker are explained theoretically. However, the solutions for the identified issues were not addressed well. Wagle [13] proposed an optimized method for the cloud service process. In order to provide more controlled services to the cloud users, the authors introduced a cloud auditor module and verified the entire process. So, the SLA violation is avoided and the user’s satisfaction level is increased. The functionalities of the cloud auditor and its decision-making ability in relation to fulfilling SLAs were not addressed well. Fowley et al. [14] introduced the idea of service brokerage for clouds which relies on interoperability and quality-of-service principles. The authors imparted the need for management support and interoperability in the context of cloud service brokerage. However, the trustworthiness of the services was not addressed in their work. Pang et al. [15] presented an approach for multi-cloud service composition using formal concept analysis and social network. Factors such as cost, energy consumption, and trustworthiness of the services are considered here. Though the authors highlighted the potential of context-based service representation for multi-cloud service composition, the practical difficulty with respect to the retrieval of context from multiple clouds was not successfully addressed. Haytamy and Omara [16] proposed an enhanced QoS-based service composition approach in a multi-cloud environment. In their work, the authors used the 

_Future Internet_ **2025** , _17_ , 348 

4 of 15 

PSO algorithm to propose the solution for the service composition problem. The wellknown customers only take part in the ranking process and hence the solution to the problem of cold-start is not yet considered in this paper. 

Effective service provisioning and the consumption of required services among the providers and consumers are the major bottlenecks in the existing cloud computing models. Hence, the authors in [17] proposed a cloud resource orchestration framework specifically focusing on multi-cloud competences. Through this study, the open research issues and the future scope for the cloud services composition have been accounted for. In a multi-cloud environment, the identification of trustworthy services has been a challenging problem. Missed QoS values leads to the improper selection of cloud services, resulting in a timeconsuming process. So, the authors in [18] proposed a clustering-based cloud service recommendation for achieving reliability with less time consumption. Al-Tarawneh and AlMousa [19] proposed an algorithm to employ an adaptive fuzzy-based engine to select the most appropriate data canter for user cloud service requests by considering user preferences in terms of cost and performance. However, the factors such as security capabilities of the service provider and security requirements of user applications have to be implemented. In addition, using a multi-objective optimization approach to balance both user cost and the provider’s revenue can also be considered. 

In our previous works [20,21], the trust level of services is evaluated with a Fuzzybased MapReduce framework. The concept of Map-Reducer is employed to envisage the trust level of services. As an extension [22], a fuzzy-based intelligent cloud broker (ICB) is proposed to facilitate the service requirements for an inexperienced cloud user. The fuzzy inferencing and decision-making model are employed to perform the effective service recommendation. However, the appropriate evidence regarding the services has not been focused on during the generation of the recommendation. Alyas et al. [23] investigated resource allocation in decentralized multi-cloud environments, focusing on ensuring Quality of Service (QoS). It addresses challenges in estimating and dynamically adjusting resources based on workload and parallelism. Given the diversity of service and resource providers, a cooperative strategy is essential for sustainable QoS. The study aims to identify key parameters for developing an effective and rational resource allocation mechanism. Decentralized multi-cloud resource allocation faces several challenges, including interoperability issues, increased system complexity, and inconsistent QoS across providers. Security risks, latency due to distributed coordination, and lack of a global resource view further complicate management. Additionally, dynamic scaling can lead to unpredictable costs, while resource contention may affect fairness and performance. 

Key obstacles to service provisioning include heterogeneous devices, varying QoS needs, and the expanding availability of cloud and fog resources. Using fog infrastructure is essential for overcoming cloud providers’ latency restrictions. The growing number of fog infrastructure providers (FIPs) necessitates assessing pricing, location, quality of service, and resources in order to choose the best one. In order to solve this, the authors [24] suggested a scalable, adaptable platform for service placement in multi-cloud and multi-fog scenarios. Each resource manager (RM) of the available providers is given the opportunity to implement their own placement policy after the proposal broadcasts service requirements to them. An optimization task is used to represent the placement problem in order to minimize the overall weighted delay and cost. However, the proposal may face inconsistent decisions due to decentralized RMs and increased network overhead from broadcasting. Its heuristic (MCD1) may not always find optimal solutions. Scalability could be challenged as the number of providers grows. Tang et al. [25] suggested a workflow scheduling technique for Multi-Cloud Environments (MCEs) based on the Asynchronous Advantage Actor– Critic (A3C) method. An agent that adjusts local parameters and adjusts to changes in the 

_Future Internet_ **2025** , _17_ , 348 

5 of 15 

environment is used to model each cloud provider. An initialization policy determines which tasks are allocated to virtual machines. To accommodate data from actual scientific workflows, a customized critic network is created. This improves the agents’ ability to adapt and make decisions. According to simulation data, the suggested MCWS-A3C performs better than three benchmark approaches in terms of cost, makespan, and resource usage. Nevertheless, in extremely dynamic cloud environments, the A3C algorithm may experience problems with convergence. The difficulty and computational overhead of training numerous agents rise. Deployment in the real world could need a lot of tweaking to accommodate different workflow patterns. 

Pandi et al. [26] compare and contrast Kubernetes and Terraform as orchestration technologies for cloud cost minimization. The study simulates real-time workloads across several clouds to assess their cost-reduction capabilities. Jenkins-integrated Kubernetes is evaluated for its autoscaling capabilities and resource allocation effectiveness. In order to reduce cloud expenses, the study also looks at how machine learning and predictive analytics may be incorporated into the orchestration process. This gives enterprises a way to manage many clouds at a lower cost. New users may find the learning curve for Terraform and Kubernetes to be quite severe. Cost optimization is constrained by the intricacy of integration and multi-cloud settings. Performance and dependability can change according to workload, necessitating adjustment for best outcomes. By combining services from several cloud providers, a multi-cloud environment enables enterprises to create a single, diverse platform. Depending on business requirements, it provides the freedom to execute tasks on either private or public clouds. In multi-cloud systems, efficient load balancing enhances throughput, minimizes makespan, improves resource efficiency, and provides fault tolerance by rerouting traffic in the event of cloud outages. This study [27] compares the performance of several optimization techniques and presents an optimized fault-tolerant load balancing technique utilizing the multi-objective cat swarm optimization algorithm (MCSOFLB). Managing heterogeneous settings might become more challenging when multi-cloud load balancing is used. Mechanisms for fault tolerance may result in higher overhead and longer traffic rerouting times. For different cloud service circumstances and workloads, optimized load balancing techniques need to be fine-tuned. 

## **3. Proposed System Architecture—Validation and Verification of Cloud Services in Multi-Cloud Environment** 

Identification of a right and valid cloud service is still a highly challenging problem, which leads to an untrusted service with massive time consumption. To overcome these issues, the proposed work aimed to validate the services by considering thirteen different potential trust metrics of the service such as response time, sustainability, suitability, accuracy, transparency, interoperability, availability, reliability, stability, cost, throughput, efficiency, and scalability. This section describes the proposed system with an overview which includes the relevant work modules for performing the validation and verification of cloud services in the multi-cloud environment. The overall architecture of the proposed work is shown in Figure 1. The primary objective of this work is attained by incorporating a special entity called ‘intelligent cloud broker (ICB)’, which is responsible for the overall processing of the proposed architecture. 

The ICB involves four major processes such as extraction of service trust factors from multi-cloud environment, service trust factors prediction process, clustering of services, and recommending of services. The very first phase in this proposed work is to collect and manage the service details with the service registry. The second phase is the heart of the proposed work, which involves the primary process such as the validation and verification of the service details. Following that, the ICB performs the service clustering and maintains 

_Future Internet_ **2025** , _17_ , 348 

6 of 15 

the services according to the types. Finally, the ICB prepares the recommended service list and publishes its details in the registry and to the cloud users. A detailed working explanation of the proposed modules is presented in the subsequent sections. 


![](prepared/futureinternet-17-00348/images/futureinternet-17-00348.pdf-0006-03.png)


**Figure 1.** Proposed work for validation and verification of multi-cloud services. 

## _3.1. Extraction of Service Trust Factors from Multi-Cloud Environment_ 

In a multi-cloud environment, a cloud user can use different types of services such as Software as a Service (SaaS), Platform as a Service (PaaS), Infrastructure as a Service (IaaS), and simply anything as a service, termed as ‘XaaS’. 

## 3.1.1. Identification of Trust Factors and Feedback 

In this paper, 13 service trust factors with respect to the available cloud services are considered for validation and verification process. From each cloud service provider’s side, we have attained the values for the trust factors. In addition to that, the ICB enables the cloud user to post feedback for the consumed services. The obtained feedback can be utilized for the determination of service trust factors. The service trust factors which are considered in the proposed model are presented below. 

## _**Service Response Time (p**_ **1** _**)**_ 

Service response time (SRT) indicates the service availability, which is measured from the response time of the service provider. In IaaS, it is measured as how quickly the service is available to the user. The service response time is calculated by 


![](prepared/futureinternet-17-00348/images/futureinternet-17-00348.pdf-0006-11.png)


where _x_ is user id, _tx_ is the time between user x’s request time and the time at which the service becomes available, and N is total number of service requests. 

The service response time failure (SRTF) is calculated by 

SRTF = _[ns]_ / _N_ 

(2) 

_Future Internet_ **2025** , _17_ , 348 

7 of 15 

where _ns_ is the number of times the service provider was not able to provide the service within the maximum response time. 

## _**Sustainability (p**_ **2** _**)**_ 

The environmental impact of cloud service provisioning is referenced by the term ‘sustainability’ and is measured by the average carbon footprint or energy efficiency of cloud services. The carbon footprint or energy efficiency is calculated by carbon calculators such as the PUE (Power Usage Efficiency) calculator. 

> _[essential][f][ eatures][p][rovided b][y][p][rovider][′][s services]_ Sustainability = _[Number o ][f]_ (3) _Number o f essential f eatures required by the customer_ 

## _**Suitability (p**_ **3** _**)**_ 

Suitability is the proportion of essential features required by the customer that are actually provided by the cloud service. It is defined as follows: 

> _[Features Provided][ ∩][Essential][Features Re][q][uired][|]_ Suitability = _[|][Essential]_ (4) _|Essential Features Required|_ 

## _**Accuracy (p**_ **4** _**)**_ 

Accuracy indicates the degree of proximity to the user’s actual values when using a service compared to the expected values. Also, the frequency of success in fulfilling the promised SLA in terms of storage, computing, and network is considered. The accuracy is calculated by 


![](prepared/futureinternet-17-00348/images/futureinternet-17-00348.pdf-0007-11.png)


where _n_ is the number of previous users and _sx_ is the number of times the cloud provider successfully satisfied the promised values for user _x_ over service time T. 

_**Transparency (p**_ **5** _**)**_ 

Transparency is an important feature in cloud services which directs the range to which users’ usability is not affected by any changes in services. The usability is measured by 


![](prepared/futureinternet-17-00348/images/futureinternet-17-00348.pdf-0007-15.png)


## _**Interoperability (p**_ **6** _**)**_ 

The ability of the services to interact with other services is denoted as interoperability and is calculated by 


![](prepared/futureinternet-17-00348/images/futureinternet-17-00348.pdf-0007-18.png)


## _**Availability (p**_ **7** _**)**_ 

Availability is measured by the percentage of time a customer accesses the services. It is calculated by 


![](prepared/futureinternet-17-00348/images/futureinternet-17-00348.pdf-0007-21.png)


## _**Reliability (p**_ **8** _**)**_ 

Reliability defines the successful service provisioning without failure, which is calculated by 

> _[success ][f][ ul][service][p][rovisionin][g]_ Reliability = _[Number o ][f]_ (9) _Number o f time service provisioning_ 

_**Stability (p**_ **9** _**)**_ 

_Future Internet_ **2025** , _17_ , 348 

8 of 15 

Stability measures the variations in the service performance, which is calculated by 

> _[times service was][p][rovisioned without deviations][f][ rom SLA terms]_ Stability = _[Number o ][f]_ (10) _Total number o f service provisioning_ 

This definition ensures that only consistent, SLA-compliant service deliveries are counted as stable, providing a realistic assessment of the provider’s reliability. _**Cost (p**_ **10** _**)**_ 

Cost is calculated based on volume-based metrics to show the difference in heterogeneous resources such as the cost of one unit of storage, processing unit, cache memory, and network bandwidth. Cost is calculated by 

_vm cost_ = ∑( _cost o f cpu_ + _cost o f storage_ + _cost o f network bandwidth_ ) (11) 

## _**Throughput (p**_ **11** _**)**_ 

Throughput is measured from number of tasks completed by the cloud service per unit of time, which is calculated by 

Throughput = 

_Number o f task completed_ 

(12) _Execution time o f n tasks on m number o f machines_ 

## _**Efficiency (p**_ **12** _**)**_ 

Efficiency defines the effective utilization of cloud services, which is measured by 

_Execution time o f n number o f tasks on m number o f machines_ Efficiency = (13) _Execution time o f n tasks on m number o f machines × Time overhead_ 

Here, time overheads are infrastructure initial delay, inter task communication delays, etc. _**Scalability (p**_ **13** _**)**_ 

Scalability defines the ability of a system which can handle a large number of application requests simultaneously. There are two types of scalabilities, such as horizontal scalability, which increases the same type of cloud resources in _vm_ , and vertical scalability which increases the ability of cloud resources in _vm_ . Based on Amdahl’s law 


![](prepared/futureinternet-17-00348/images/futureinternet-17-00348.pdf-0008-17.png)


here _p_ is the number of processors; _α_ is the fraction of calculation, which is sequential (vertical); and 1 _− α_ is the fraction of calculation which is parallel (horizontal). 

These 13 service trust factors consider the performance, transparency, cost, and user experience. Each factor is quantifiable, adaptable to IaaS, PaaS, and SaaS, and ensures objective, comparable rankings in the proposed model. 

## 3.1.2. Service Trust Prediction Process 

In Algorithm 1, the inputs are available services and newly arrived cloud services with the parameter set. The SR value for each cloud services with feedback from service set(ss) is calculated by 


![](prepared/futureinternet-17-00348/images/futureinternet-17-00348.pdf-0008-22.png)


where ‘n’ is the number of cloud services (cs). 

The newly arrived services represent a mix of IaaS, PaaS, and SaaS offerings, including compute and storage providers, email and collaboration tools, container-based platforms, helpdesk systems, and enterprise backup solutions. The SR value for newly arrived cloud services (without feedback) has been assigned by finding the equivalent available cloud 

_Future Internet_ **2025** , _17_ , 348 

9 of 15 

services from the Service Collection Repository (SCR). Finally, the cloud services from the service set (ss) are ordered based on their SR values and formed into clusters, namely the ‘Complete trustworthy cluster group’, ‘Trustworthy cluster group’, ‘Partially trustworthy cluster group’, and ‘Untrustworthy cluster group’. The validation and verification process of the proposed model is illustrated in Algorithm 1. 

**Algorithm 1:** Service ranking and cloud service cluster formation. 

Service Ranking (SR) algorithm 

**Inputs:** Service set (ss) = {cs1, cs2, . . ., csn} Parameter set (ps) = {p1, p2, . . ., p13} 

**Outputs:** Clusters with ordered services 

1. Compute the SR value for each cloud services(cs) for each cloud services from ss if (each cloud services with customer feedback) compute SRn = _[p]_[1][+] _[p]_[2] 13[+][...][+] _[p]_[13] else //Newly arrived cloud services without feedback Finding the equivalent cloud services which is existing for the newly arrived cloud services from Service Collection Repository (SCR). 

Assign the SR of matched services to the newly arrived services. 

Mapping(csx,ncsy) = ∑ _[n] x_ =1[∑] _[m] y_ =1 _[max]_[(] _[cs] x[∩][ncs][y]_ � NSRy = SRx 

end if 

2. Clustering the cloud services based on SR values 

   - if (SR value between 0.750 and 1.0) 

Move cs to “Complete trust worthy cluster group” elseif (SR value between 0.500 and 0.749) Move cs to “Trust worthy cluster group” elseif (SR value between 0.300 and 0.499) Move cs to “Partially trust worthy cluster group” else (SR value less than 0.299) Move cs to “Untrustworthy cluster group” 

end if end for 

## 3.1.3. Service Registry 

The outcome of the Service Collection Repository (SCR) is projected as a service description and the same is published with the service registry. If any users’ requirements are matched with the service registry, then the intelligent cloud broker recommends the appropriate service collection from the SCR itself. In this case, if it is a new kind of request, then the intelligent broker initiates the regular process of the proposed work. 

## **4. Experimental Setup** 

In this section, the performance of the proposed model is analyzed by applying different cloud services with different service trust factors. The experiments were performed on a machine with an Intel Xeon E5 2620 v4processor @ 2.1 GHz and 16 GB of RAM using Windows 10 by using the Weka tool. The Weka tool includes a collection of machine learning algorithms to perform the data processing. In this work, the tool is used for analyzing and clustering the cloud services based on SR values. 

_Future Internet_ **2025** , _17_ , 348 

10 of 15 

## _4.1. Dataset Description_ 

The proposed service ranking algorithm is evaluated using the Google clusterusage traces dataset [28], which provides detailed information on resource utilization across a large-scale Google data center. The dataset contains over 700,000 task instances distributed across approximately 12,000 physical machines. The InstanceUsage table from the dataset was primarily utilized, focusing on the following seven key features: start_time, end_time, collection_ID, instance_index, average_usage, maximum_usage, and random_sampled_usage. These features provide essential insights into task-level resource usage, which are leveraged in our ranking algorithm to evaluate service performance. 

## _4.2. Results and Analysis_ 

The performance of the proposed model is compared with an existing cloud service recommendation system using a clustering-based trust degree computation algorithm (CBTDC) [18] and Service Context-Aware QoS Prediction and Recommendation of Cloud Infrastructure Services (SCAQPR) [29]. In the CBTDC algorithm, the limited-service trust measures are considered for the services ranking. The service trust measures are calculated for the available services based on customer feedback. Hence, the algorithm has not focused on the newly arrived services. In addition, the SCAQPR algorithm considered the newly arrived services while preparing the ranked list of services using matrix factorization approach. The services ranking is based on limited QoS factors after computing the missed values of newly arrived services. The proposed work concentrates on 13 service trust factors along with users’ feedback to prepare the ranked list of services through SR values as shown in Table 1. Here, the SR values are calculated for the newly arrived services by mapping these services (by referring service description) with the existing services. The performance comparison of the proposed work with the existing works for available and newly arrived services is depicted in Table 2. 

**Table 1.** Service trust factors value for the existing services. 

|**Parameters**||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Cloud Services**|**_p_1**|**_p_2**|**_p_3**|**_p_4**|**_p_5**|**_p_6**|**_p_7**|**_p_8**|**_p_9**|**_p_10**|**_p_11**|**_p_12**|**_p_13**|
|cs1|0.723|0.762|0.831|0.717|0.729|0.848|0.831|0.718|0.837|0.682|0.893|0.612|0.522|
|cs2|0.729|0.788|0.843|0.720|0.737|0.854|0.842|0.729|0.844|0.693|0.908|0.627|0.537|
|cs3|0.691|0.718|0.807|0.682|0.691|0.815|0.717|0.627|0.724|0.591|0.822|0.512|0.503|
|cs4|0.532|0.553|0.681|0.531|0.522|0.591|0.522|0.418|0.493|0.412|0.688|0.412|0.388|
|cs5|0.411|0.488|0.552|0.510|0.412|0.415|0.432|0.371|0.408|0.376|0.611|0.373|0.301|
|cs6|0.587|0.591|0.712|0.588|0.597|0.611|0.627|0.497|0.512|0.511|0.717|0.491|0.409|
|cs7|0.371|0.311|0.326|0.377|0.325|0.317|0.322|0.291|0.377|0.293|0.512|0.361|0.202|
|cs8|0.876|0.835|0.843|0.722|0.742|0.861|0.85|0.734|0.853|0.898|0.911|0.634|0.841|
|cs9|0.655|0.681|0.772|0.615|0.623|0.782|0.689|0.512|0.671|0.538|0.788|0.507|0.411|
|cs10|0.711|0.753|0.823|0.705|0.712|0.833|0.812|0.683|0.791|0.653|0.872|0.609|0.517|



By considering Table 2, the service trust factors such as service response time, sustainability, suitability, accuracy, transparency, interoperability, availability, reliability, stability, cost, throughput, efficiency, and scalability are calculated to order the various cloud services. For each cloud service, the parameter values are measured for the SR values, which are shown in Figure 2. 

_Future Internet_ **2025** , _17_ , 348 

11 of 15 

**Table 2.** Performance comparison of the proposed work with the existing works. 

|**Rank**|**Cloud**<br>**Services**|**Proposed**<br>**Model SR**<br>**Value**|**Existing**<br>**CBTDC—SR**<br>**Value**|**Existing**<br>**SCAQPR—SR**<br>**value**|**Diff (Proposed**<br>**Model—**<br>**CBTDC)**|**Diff**<br>**(Proposed—**<br>**SCAQPR)**|
|---|---|---|---|---|---|---|
|Cloud|Services with|Trust Factors and Feedback Values|||||
|1|cs8|0.815|0.892|0.887|_−_0.077|_−_0.072|
|2|cs2|0.758|0.812|0.795|_−_0.054|_−_0.037|
|3|cs1|0.747|0.853|0.761|_−_0.106|_−_0.014|
|4|cs10|0.729|0.762|0.737|_−_0.033|_−_0.008|
|5|cs3|0.685|0.731|0.712|_−_0.046|_−_0.027|
|6|cs9|0.634|0.676|0.643|_−_0.042|_−_0.009|
|7|cs6|0.573|0.543|0.581|+0.030|_−_0.008|
|8|cs4|0.519|0.407|0.492|+0.112|+0.027|
|9|cs5|0.435|0.407|0.437|+0.028|_−_0.002|
|10|cs7|0.293|0.322|0.376|_−_0.029|_−_0.083|
|Cloud|Services with|Trust Factors only(NewlyArrived Services)|||||
|11|ncs1|0.741 (cs1)|NA|0.738|NA|+0.003|
|12|ncs2|0.291 (cs7)|NA|0.304|NA|_−_0.013|
|13|ncs3|0.632 (cs9)|NA|0.629|NA|+0.003|
|14|ncs4|0.726 (cs10)|NA|0.719|NA|+0.007|
|15|ncs5|0.517 (cs4)|NA|0.521|NA|_−_0.004|



## **Cloud Services Vs ServiceTrust Factors** 


![](prepared/futureinternet-17-00348/images/futureinternet-17-00348.pdf-0011-05.png)


**----- Start of picture text -----**<br>
1<br>0.9 cs1<br>0.8 cs2<br>0.7<br>cs3<br>0.6<br>cs4<br>0.5<br>cs5<br>0.4<br>cs6<br>0.3<br>cs7<br>0.2<br>0.1 cs8<br>0 cs9<br>p1 p2 p3 p4 p5 p6 p7 p8 p9 p10 p11 p12 p13<br>cs10<br>Service Trust Factors (Parameters)<br>Cloud Service-Parameter values<br>**----- End of picture text -----**<br>


**Figure 2.** Service trust factors of cloud services. 

From Figure 3, it can be seen that the proposed model considers the newly arrived services along with the available services (than existing CBTDC) and the number of service trust factors considered for SR value calculation with respect to the existing SCAQPR is improvised towards to the betterment of an effective service clustering process. 

_Future Internet_ **2025** , _17_ , 348 

12 of 15 


![](prepared/futureinternet-17-00348/images/futureinternet-17-00348.pdf-0012-02.png)


**----- Start of picture text -----**<br>
Comparison of proposed work with existing works<br>1<br>0.9<br>0.8<br>0.7<br>0.6<br>0.5 Proposed Model<br>0.4 Existing CBTDC<br>0.3<br>Existing SCAQPR<br>0.2<br>0.1<br>0<br>cs8 cs2 cs1 cs10 cs3 cs9 cs6 cs4 cs5 cs7 ncs1 ncs2 ncs3 ncs4 ncs5<br>Cloud Services<br>SR Values<br>**----- End of picture text -----**<br>


**Figure 3.** Comparison of proposed work with existing works. 

The final results of the proposed work are categorized into the clusters, namely the ‘Complete trustworthy’ cluster group, ‘Trustworthy’ cluster group, ‘Partially trustworthy’ cluster group, and ‘Untrustworthy’ cluster group. Here, the proposed work considered the existing and newly arrived services for the formation of different clusters to prepare and update the Service Collection Repository (SCR), which is shown in Table 3. 

**Table 3.** Clusters with the cloud services of the proposed model. 

|**Clusters**|**Cloud Services**|
|---|---|
|Complete trustworthyclustergroup|cs8, cs2|
|Trustworthyclustergroup|cs1, cs10, cs3, cs9, cs6, cs4,_ncs_1,_ncs_3,_ncs_4,_ncs_5|
|Partiallytrustworthyclustergroup|cs5|
|Untrustworthy cluster group|cs7,_ncs_2|



## **5. Conclusions and Future Enhancements** 

In a multi-cloud environment, the validation and verification of cloud services play a crucial role in recommending appropriate services that meet user requirements and ensure service quality. The proposed work introduces an intelligent cloud broker (ICB) designed to address the dynamic needs of cloud users by calculating service ranking (SR) values based on multiple service trust factors derived from existing services. Additionally, the ICB efficiently accommodates newly arrived services by referencing the SR values of similar existing services, thereby ensuring adaptability and continuity in service recommendations. To enhance the accuracy of SR value calculation, the model incorporates thirteen distinct service trust factors, leading to improved performance compared to existing approaches. The experimental evaluation, conducted on a set of selected cloud services, demonstrates the model’s effectiveness in service ranking and recommendation. However, the current implementation is limited by the scope of the dataset and static evaluation parameters. As a direction for future work, the model can be enhanced by integrating advanced machine learning algorithms that can learn and adapt automatically to large-scale, real-time, and dynamic cloud service datasets. This integration will further enable the intelligent cloud 

_Future Internet_ **2025** , _17_ , 348 

13 of 15 

broker to scale effectively and maintain high recommendation accuracy in practical multicloud scenarios. 

**Author Contributions:** R.N.: conceptualization of the research framework; overall supervision; manuscript review and editing; ensured alignment with cloud computing standards and trust modeling principles. V.P.: system design and implementation; data collection and experimentation; preparation of graphs and tables; contributed to drafting the initial manuscript. R.T.: technical guidance on ranking heuristics and trust factor integration; contributed to methodology refinement and literature review; assisted in manuscript revisions. J.A.P.: formal analysis and validation of the proposed model; coordinated peer review responses and manuscript finalization; served as the corresponding author and provided academic supervision throughout the research. All authors have read and agreed to the published version of the manuscript. 

**Funding:** This research received no external funding. 

**Data Availability Statement:** The data that support the findings of this study are available from the corresponding author upon reasonable request. 

**Acknowledgments:** The authors would like to acknowledge the infrastructure support provided by Sri Venkateswara College of Engineering, Sriperumbudur, Tamil Nadu, India; Vellore Institute of Technology, Vellore, Tamil Nadu, India, which were essential for the successful completion of this research. 

**Conflicts of Interest:** The authors declare no conflicts of interest. 

## **Abbreviations** 

The following abbreviations are used in this manuscript: 

|**Notation**|**Description**|
|---|---|
|SRT|Service Response Time|
|SS|Service Set|
|PS|Parameter Set|
|SR|Service Ranking Value for Available Cloud Service|
|NSR|Service Ranking Value for Newly Arrived Cloud Service|
|p|Parameter (Service Trust Factor)|
|cs|Cloud Service|
|ncs|New Cloud Service|
|n|Number of Available Cloud Services|
|m|Number of Newly Arrived Cloud Services|
|SCR|Service Collection Repository|
|vm|Virtual Machine|
|IaaS|Infrastructure as a Service|
|PaaS|Platform as a Service|
|SaaS|Software as a Service|
|ICB|Intelligent Cloud Broker|



## **References** 

1. Rajganesh, N.; Ramkumar, T. A review on broker based cloud service model. _J. Comput. Inf. Technol._ **2016** , _24_ , 283–292. [CrossRef] 2. Nagarajan, R.; Thirunavukarasu, R. A review on intelligent cloud broker for effective service provisioning in cloud. In Proceedings of the 2018 Second International Conference on Intelligent Computing and Control Systems (ICICCS), Madurai, India, 14–15 June 2018; pp. 519–524. 

3. Aldawsari, B.; Baker, T.; England, D. Towards a holistic multi-cloud brokerage system: Taxonomy, survey, and future directions. In Proceedings of the 2015 IEEE International Conference on Computer and Information Technology; Ubiquitous Computing and Communications; Dependable, Autonomic and Secure Computing; Pervasive Intelligence and Computing, Liverpool, UK, 26–28 October 2015; pp. 1467–1472. 

_Future Internet_ **2025** , _17_ , 348 

14 of 15 

4. Chauhan, S.S.; Pilli, E.S.; Joshi, R.C.; Singh, G.; Govil, M.C. Brokering in interconnected cloud computing environments: A survey. _J. Parallel Distrib. Comput._ **2019** , _133_ , 193–209. [CrossRef] 

5. Yao, J.; Yang, M.; Deng, T.; Guan, H. The Cloud Service Broker in Multicloud Demand Response. _IEEE Cloud Comput._ **2018** , _5_ , 80–91. [CrossRef] 

6. Petcu, D. Portability and interoperability between clouds: Challenges and case study. In Proceedings of the European Conference on a Service-Based Internet, Poznan, Poland, 26–28 October 2011; Springer: Berlin/Heidelberg, Germany, 2011; pp. 62–74. 

7. Ghazouani, S.; Mezni, H.; Slimani, Y. Bringing semantics to multicloud service compositions. _Softw. Pract. Exp._ **2020** , _50_ , 447–469. [CrossRef] 

8. Abbas, G.; Mehmood, A.; Lloret, J.; Raza, M.S.; Ibrahim, M. FIPA-based reference architecture for efficient discovery and selection of appropriate cloud service using cloud ontology. _Int. J. Commun. Syst._ **2020** , _33_ , e4504. [CrossRef] 

9. Nagarajan, R.; Thirunavukarasu, R.; Shanmugam, S. A cloud broker framework for infrastructure service discovery using semantic network. _Int. J. Intell. Eng. Syst._ **2018** , _11_ , 11–19. [CrossRef] 

10. Calheiros, R.N.; Toosi, A.N.; Vecchiola, C.; Buyya, R. A coordinator for scaling elastic applications across multiple clouds. _Future Gener. Comput. Syst._ **2012** , _28_ , 1350–1362. [CrossRef] 

11. Grozev, N.; Buyya, R. Inter-Cloud architectures and application brokering: Taxonomy and survey. _Softw. Pract. Exp._ **2014** , _44_ , 369–390. [CrossRef] 

12. Mostajeran, E.; Ismail, B.I.; Khalid, M.F.; Ong, H. A survey on SLA-based brokering for inter-cloud computing. In Proceedings of the 2015 Second International Conference on Computing Technology and Information Management (ICCTIM), Johor, Malaysia, 21–23 April 2015; pp. 25–31. 

13. Wagle, S.S. Cloud service optimization method for multi-cloud brokering. In Proceedings of the 2015 IEEE International Conference on Cloud Computing in Emerging Markets (CCEM), Bangalore, India, 25–27 November 2015; pp. 132–139. 

14. Fowley, F.; Pahl, C.; Jamshidi, P.; Fang, D.; Liu, X. A classification and comparison framework for cloud service brokerage architectures. _IEEE Trans. Cloud Comput._ **2016** , _6_ , 358–371. [CrossRef] 

15. Pang, B.; Yang, Y.; Hao, F. A sustainable strategy for multi-cloud service composition based on formal concept analysis. In Proceedings of the 2019 IEEE 21st International Conference on High Performance Computing and Communications; IEEE 17th International Conference on Smart City; IEEE 5th International Conference on Data Science and Systems (HPCC/SmartCity/DSS), Zhangjiajie, China, 10–12 August 2019; pp. 2659–2665. 

16. Haytamy, S.; Omara, F. Enhanced qos-based service composition approach in multi-cloud environment. In Proceedings of the 2020 International Conference on Innovative Trends in Communication and Computer Engineering (ITCE), Aswan, Egypt, 8–9 February 2020; pp. 33–38. 

17. Tomarchio, O.; Calcaterra, D.; Modica, G.D. Cloud resource orchestration in the multi-cloud landscape: A systematic review of existing frameworks. _J. Cloud Comput._ **2020** , _9_ , 49. [CrossRef] 

18. Wang, Y.; Wen, J.; Zhou, W.; Tao, B.; Wu, Q.; Tao, Z. A cloud service selection method based on trust and user preference clustering. _IEEE Access_ **2019** , _7_ , 110279–110292. [CrossRef] 

19. Al-Tarawneh, M.; Al-Mousa, A. Adaptive user-oriented fuzzy-based service broker for cloud services. _J. King Saud Univ. Comput. Inf. Sci._ **2022** , _34_ , 354–364. [CrossRef] 

20. Nagarajan, R.; Thirunavukarasu, R.; Shanmugam, S. A fuzzy-based intelligent cloud broker with MapReduce framework to evaluate the trust level of cloud services using customer feedback. _Int. J. Fuzzy Syst._ **2018** , _20_ , 339–347. [CrossRef] 

21. Nagarajan, R.; Selvamuthukumaran, S.; Thirunavukarasu, R. A fuzzy logic based trust evaluation model for the selection of cloud services. In Proceedings of the 2017 International Conference on Computer Communication and Informatics (ICCCI), Coimbatore, India, 5–7 January 2017; pp. 1–5. 

22. Nagarajan, R.; Thirunavukarasu, R. A fuzzy-based decision-making broker for effective identification and selection of cloud infrastructure services. _Soft Comput._ **2019** , _23_ , 9669–9683. [CrossRef] 

23. Alyas, T.; Ghazal, T.M.; Alfurhood, B.S.; Issa, G.F.; Thawabeh, O.A.; Abbas, Q. Optimizing Resource Allocation Framework for Multi-Cloud Environment. _Comput. Mater. Contin._ **2023** , _75_ , 4119–4136. [CrossRef] 

24. Azizi, S.; Farzin, P.; Shojafar, M.; Rana, O. A scalable and flexible platform for service placement in multi-fog and multi-cloud environments. _J. Supercomput._ **2024** , _80_ , 1109–1136. [CrossRef] 

25. Tang, X.; Liu, F.; Wang, B.; Xu, D.; Jiang, J.; Wu, Q.; Chen, C.P. Workflow scheduling based on asynchronous advantage actor–critic algorithm in multi-cloud environment. _Expert Syst. Appl._ **2024** , _258_ , 125245. [CrossRef] 

26. Pandi, S.S.; Kumar, P.; Suchindhar, R.M. Integrating Jenkins for Efficient Deployment and Orchestration across Multi-Cloud Environments. In Proceedings of the 2023 International Conference on Innovative Computing, Intelligent Communication and Smart Electrical Systems (ICSES), Chennai, India, 14–15 December 2023; pp. 1–6. 

27. Suresh, P.; Keerthika, P.; Devi, R.M.; Kamalam, G.K.; Logeswaran, K.; Sadasivuni, K.K.; Devendran, K. Optimized task scheduling approach with fault tolerant load balancing using multi-objective cat swarm optimization for multi-cloud environment. _Appl. Soft Comput._ **2024** , _165_ , 112129. [CrossRef] 

_Future Internet_ **2025** , _17_ , 348 

15 of 15 

28. Available online: https://github.com/google/cluster-data/blob/master/ClusterData2019.md (accessed on 5 January 2025). 

29. Nagarajan, R.; Thirunavukarasu, R. A service context-aware QoS prediction and recommendation of cloud infrastructure services. _Arab. J. Sci. Eng._ **2020** , _45_ , 2929–2943. [CrossRef] 

**Disclaimer/Publisher’s Note:** The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content. 

