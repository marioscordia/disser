_**sustainability**_ 


![](prepared/sustainability-13-08141/images/sustainability-13-08141.pdf-0001-01.png)



![](prepared/sustainability-13-08141/images/sustainability-13-08141.pdf-0001-02.png)


## _Article_ 

## **Systematic Review of Contextual Suggestion and Recommendation Systems for Sustainable e-Tourism** 

**Haseeb Ur Rehman Khan[1] , Chen Kim Lim[2,] *, Minhaz Farid Ahmed[2,] * , Kian Lam Tan[3] and Mazlin Bin Mokhtar[2]** 

- 1 Faculty of Art, Computing & Creative Industry, Sultan Idris Education University, Tanjong Malim 35900, Perak, Malaysia; haseebrkhan6@gmail.com 

- 2 Institute for Environment & Development (LESTARI), Universiti Kebangsaan Malaysia (UKM), Bangi 43600, Selangor, Malaysia; mazlin@ukm.my 

- 3 School of Digital Technology, Wawasan Open University, George Town 10050, Penang, Malaysia; andrewtan@wou.edu.my 

- Correspondence: kim@ukm.edu.my (C.K.L.); minhaz@ukm.edu.my (M.F.A.) 

## ��������� **�������** 

**Citation:** Rehman Khan, H.U.; Lim, C.K.; Ahmed, M.F.; Tan, K.L.; Bin Mokhtar, M. Systematic Review of Contextual Suggestion and Recommendation Systems for Sustainable e-Tourism. _Sustainability_ **2021** , _13_ , 8141. https://doi.org/ 10.3390/su13158141 

Academic Editor: Nicoletta Santangelo 

Received: 26 May 2021 Accepted: 17 July 2021 Published: 21 July 2021 

**Publisher’s Note:** MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations. 


![](prepared/sustainability-13-08141/images/sustainability-13-08141.pdf-0001-15.png)


**Copyright:** © 2021 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ 4.0/). 

**Abstract:** Agenda 2030 of Sustainable Development Goals (SDGs) 9 and 11 recognizes tourism as one of the central industries to global development to tackle global challenges. With the transformation of information and communication technologies (ICT), e-tourism has evolved globally to establish commercial relationships using the Internet for offering tourism-related products, including giving personalised suggestions. The contextual suggestion has emerged as a modified recommendation system that is integrated with information-retrieval techniques within large databases to provide tourists with a list of suggestions based on contexts, such as location, time of day, or day of the week (weekdays or weekends). This study surveyed literature in the field of contextual suggestion and recommendation systems with a focus on e-tourism. The concerns linked with approaches used in contextual suggestion and recommendation systems are highlighted in this systematic review, while motivations, recommendations, and practical implications in e-tourism are also discussed in this paper. A query search using the keywords “contextual suggestion system”, “recommendation system”, and “tourism” identified 143 relevant articles published from 2012 to 2020. Four major repositories are considered for searching, namely, (i) Science Direct, (ii) Scopus, (iii) IEEE, and (iv) Web of Science. This review was carried out under the protocols of four phases, namely, (i) query searching in major article repositories, (ii) removal of duplicates, (iii) scan of title and abstract, and (iv) complete reading of articles. To identify the gaps in current research, a taxonomy analysis was exemplified into categories and subcategories. The main categories were highlighted as (i) review articles, (ii) model/framework, and (iii) applications. Critical analysis was carried out on the basis of the available literature on the limitations of approaches used in contextual suggestion and recommendation systems. In conclusion, the approaches used are mainly based on content-based filtering, collaborative filtering, preference-based product ranking, and language modelling. The evaluation measures for the contextual suggestion system include precision, normalized discounted cumulative, and mean reciprocal rank, while test collections comprise Internet resources. Given that the tourism industry contributed to the environmental and social-economic development, contextual suggestion and recommendation systems have presented themselves to be relevant in integrating and achieving SDG 9 and SDG 11 in many ways such as web-based e-services by the government sector and smart gadgets based on reliable and real-time data and information for city planners as well as law enforcement personnel in a sustainable city. 

**Keywords:** sustainable e-tourism; contextual suggestion system; recommendation system; personalisation; SDGs 

_Sustainability_ **2021** , _13_ , 8141. https://doi.org/10.3390/su13158141 

https://www.mdpi.com/journal/sustainability 

_Sustainability_ **2021** , _13_ , 8141 

2 of 27 

## **1. Introduction** 

Beginning in the 1980s, tourism in recent times has been evolving with technology, bringing major restructuring to both the industry and our view on tourism. Gradually, information and communication technologies (ICT) play an increasingly critical role in offering competitiveness to the tourism industry, and thus evolve the behaviour of tourists and the tourism industry, in which it is called e-tourism [1]. Facebook, Twitter, YouTube, and other social media platforms are used widely in e-tourism, and it is supported by tourists’ use of social media platforms with its exponential growth. Google survey (2012) has also reported that approximately 40% of tourists are influenced through the social network in the trip-planning phase, while 50% of tourists plan their trip based on public reviews and experiences about the specific destination and the ITB World Travel Trends (2012–2013). In short, e-tourism is the digitalisation of all processes and value chains in the tourism, travel, hospitality, and catering industries that enable organisations to maximise their efficiency and effectiveness [2]. 

Gretzel et al. [3] proposed six additional pillars to transform e-tourism via critically evaluating those pillars. The pillars are ontological and epistemological basics in history, reflexivity, equity, transparency, plurality, and creativity. Moreover, e-tourism spots ought to be a creative, interactive, and improve the travel experience for all guests. Similarly, the system should improve the quality of life and personal satisfaction of the residents [4]. However, various challenges emerge in the development of e-tourism, including the personalised content suggested to a tourist [5,6]. If the repositories of datasets are appropriate for dataset extraction and have implicit or explicit feedback, then system accuracy increases and concerns related to privacy decrease. Simultaneously, established ICT infrastructures can likewise have an essential role in developing e-tourism applications, such as cloud computing, Wi-Fi, RFID, smartphones, and sensors [7]. At present, a few e-tourism services are available, such as a recommendation system that proposes the prime pertinent vacation spot or POI relevant to personal preferences [8] to predict and assume the behaviour of tourists. Location-based tracking systems were introduced to accomplish area-based marketing [9], as well as sensor-based applications such as social sensors (e.g., social media), physical sensors (e.g., CCTV cameras), and weather sensors to aid a tourist with limited time to explore a city [10]. 

ICT is further evolving with the Internet of Things. Similarly, cities with sound technologies facilitate the modification of search engines in terms of capacity and speed because of the need to extract data from millions of documents. While technologies are continuously evolving, it may benefit e-tourism if the system can automatically help planning a tour or recommend a list of places based on a tourist’s personal preferences. This system can facilitate millions of tourists worldwide to utilize the technology based on tour planning and automatic suggestions of places they can visit to enhance their travel experience. 

Hence, a system to provide services to the tourist at the right time is necessary and can be achieved by understanding the tourist behaviour and their personal preferences to improve the travel experience. These scenarios have led to the evolution of traditional e-tourism, which has further evolved into sustainable e-tourism [5]. 

Contextual suggestions and recommendation systems are defined as those with the ability to respond and present suggestions with appropriate information based on tourist’s needs. The approaches in these systems fall in the area of information retrieval (IR) and artificial intelligence (AI). Based on these concepts, these systems can facilitate the tourists via providing a list of venues based on their context and personal preferences [11]. Tourists depend heavily on their cell phones when searching for events to participate in and finding fascinating nearby places or activities [12]. Figure 1 shows the categories of repositories in contextual suggestion and recommendation systems for a sustainable e-tourism. 

_Sustainability_ **2021** , _13_ , 8141 

3 of 27 


![](prepared/sustainability-13-08141/images/sustainability-13-08141.pdf-0003-02.png)


**Figure 1.** Categories of repositories in contextual suggestion and recommendation systems for sustainable e-tourism. 

The repositories include the contexts, social and physical sensors, tourist’s profile, and green contextual suggestion list. With improved systems, sustainable e-tourism utilizes the technology to maximize efficiency and effectiveness while applying sustainable principles in tourism. The sustainability principles refer to the environmental, economic, and sociocultural aspects of tourism development and a suitable balance must be established between these three dimensions to guarantee its long-term sustainability [13–15]. Four clusters serve as the criteria to achieve a sustainable e-tourism, namely, they are communities’ wellbeing, natural and cultural environment, tourism product quality and tourists’ satisfaction, and management and monitoring. Through the mediation of ICT, contextual suggestion and recommendation systems will significantly contribute to SDG 11 for the smarter and greener cities from which not only residents, but also tourists can benefit [16]. This will also facilitate further sustainable industrialization, necessary for economic growth, development, and innovation. Therefore, innovation and green infrastructure development in the e-tourism industry will significantly contribute towards SDG 9 for sustainable e- tourism [6] that can provide tourists with smart experiences enriched by real-time data that smart cities offer, with context awareness and personalization. 

In contextual suggestion and recommendation systems, the improvement on the recommendations can be made by utilizing various resources of data available in the repositories of smart cities to provide relevant suggestions. Contexts such as popularity (location rating, sentiment scores, wish list, number of likes), environment (seasons, weather, temperature, humidity), distance (shortest path, nearby places, geography), time (weekday, weekend), and atmosphere risks (health, environment, pandemic) are mostly considered in a suggestion system. This would strive for the improvement in communities’ well-being in achieving sustainable e-tourism. As the government starts to involve local control and participation in decision-making, the community gets a sense of belonging about the place 

_Sustainability_ **2021** , _13_ , 8141 

4 of 27 

in which they are living. It would also help in preserving and strengthening the protection of their cultural and natural touristic spots for sustainable e-tourism. Besides, with the e-tourism industry sustaining for a long term owing to tourist’s satisfaction, improvement in living conditions such as better facilities, Internet hot spot, and public transportations could be seen. Smart living is also promoted via a sustainable e-tourism through the use of electronic tools. 

In addition, data representation combined with green contexts such as green hotels, green products, and cultural and natural heritage might be an ideal fit to create a list of suggestions within the context of sustainable e-tourism in comparison with other conventional recommender systems. Suggestions that include consideration about green contexts and how to reduce trash during travel provide value-added services to improve both tourists’ and the community’s quality of life. In a sustainable e-tourism, tourism product quality and tourists’ satisfaction are viral for long-term economic viability. The contextual suggestions systems are not adapted to the tourism supply chain, but also solve the major problem of information search and decision-making process faced by tourists. Thus, the quality of services and experiences in a sustainable e-tourism is tremendously improved. 

Currently, in tourism, venue recommendations [17–19] heavily rely on data captured from location-based social networks (LBSNs) [20]. Through the social and physical sensors such as global position system (GPS) coordinates, social networking sites (SNSchares), and dialogues and messages posted and shared about travelling, these sensors can significantly improve the quality of recommendations. The latter provides essential data and the former can provide additional information for a query in a particular context [21]. When the quality of recommendations is upgraded, the natural and cultural environment in a sustainable e-tourism could be achieved. Zero mistakes on revisiting the same place or visiting the wrong place support pollution reduction. Moreover, dissemination, education, awareness, and communication about the heritages could also enhance environmental awareness. 

In contextual suggestion and recommendation systems, the profile of tourists can be made by collecting data from the travel history of the tourist; past checked-in places [22]; personal preferences such as likes and dislikes for a place; and contextual aspects such as current location, time of day, and any day of the week, as well as utilizing various resources of data available in the repositories of smart cities to provide relevant suggestions. Sustainable e-tourism also incorporates the advancement in technology [23], e.g., the travel bloggers develop trust through interaction with followers and readers via social media, provide recommendations based on their personal experiences about a place, and request tour recommendations for places and personal experiences from public international IPK (2012). Besides, the recommendations can be further improved through travellergenerated content (UGC) from travelogues and online travel reviews [24]. Moreover, location-based social networks such as TripAdvisor, Yelp, and Foursquare have emerged to fill the need for sustainable e-tourism. These applications may also assist a tourist in finding accommodations, restaurants, and points of interest (POI) based on activities, and cultural heritage by considering ratings, reviews, and tourists’ interest to generate a list of suggestions [25]. 

Another criterion for achieving sustainable e-tourism is the management and monitoring of touristic places. Proper management of the city and monitoring of the tourist destinations would guarantee safety and privacy to ensure tourist satisfaction and travel without disturbances. The recommendation system also considers carrying capacity as a context to allow tourists to avoid over-crowded places and places with environmental risks and pandemics. Hence, e-tourism contributes to reducing the negative effects in the tourism industry. Therefore, the tourist observes good experiences using electronic tools that lead to sustainable e-tourism. 

IT and e-tourism are still the hot topics over the past 30 years; and have developed technically, economically, and societally along with the development of the web, machine learning, and artificial intelligence [26]. However, recently, sustainability in tourism has also gained much attention. The author of [27] has also revealed a lack of theoretical 

_Sustainability_ **2021** , _13_ , 8141 

5 of 27 

advancement in conceptualizing travel information search to accommodate current technology advances owing to the complexity of the e-tourism information landscape. Here, data suffer from sparsity and the need to access tourists’ personal information to recommend a venue, which raises privacy concerns. The digital infrastructure provided by smart cities can facilitate overcoming data sparsity and privacy issues [21]. Therefore, the next generation of recommendation systems in sustainable e-tourism is highly required, and it must be effective not only in providing recommendations based on social sensors, but also in utilizing other contextual information. Additional information can be gathered through physical sensors to provide precise recommendations to tourists to enhance tourism services [28]. In this regard, this systematic review aimed to survey literature and previous work on contextual suggestion and recommendation systems in e-tourism to identify, evaluate, and summarize the findings of all relevant studies. Thus, the available evidence becomes more accessible to deliver the meticulous summary of all the research on contextual suggestion system, a recommendation system for sustainable e-tourism. 

## **2. Background of Contextual Suggestion System** 

Several studies focus on a suggestion system based on contextual factors and personal interests. An application creates a list of suggestions for venues within a city using explicit feedback query related to tourist’s interests and responses [29]. A different collaborative filtering approach incorporated contextual factors such as location, weather, time of day, and any days of the week (weekdays or weekends) [30]. Tourists’ budget and familiarity within a city are also used as contextual information [31]. The contextual suggestion system falls somewhere between traditional information retrieval and traditional recommendation. Unlike traditional information retrieval, the query is fixed, with the search results vary only to reflect the traveller’s profile and the geo-temporal context. Unlike traditional recommendation, the range of suggestions is completely open, with the quality of the description forming an important aspect of the tourist experience. Ideally, the description from the contextual suggestion system would be tailored to reflect the preferences of the individual traveller. Regardless of these studies, finding gaps between the existing approaches for contextual suggestion and recommendation systems considering contextual factors are always challenging. Moreover, these researchers considered their evaluations and methods owing to the lack of standard test collection and evaluation protocols available for testing approaches and the robustness of experiments. 

Therefore, to standardize the work based on the contextual suggestion system, the text retrieval conference (TREC) provides a test collection to run experiments and standard evaluation protocols for comparison [32]. In TREC, participants perform a given task, basically to consider the description of venues and contexts, anticipate suggestions for each blend of profile and context, and then create a list of places a tourist might wish to visit [33]. Most of the participants gathered the dataset from public websites and other resources that were later declared as standard test collection. The purpose of the TREC contextual suggestion track was to ease the process for future research by providing standard datasets for testing the approaches and standard evaluation measures for comparison. Various approaches were used based on positive ratings integrated with the textual similarity between the venue and the tourists’ profiles [34]. Other approaches were based on reviews, ratings, categories of venues, and contextual factors [34,35]. 

## **3. Systematic Review Protocol** 

Systematic reviews are planned to choose and assess the findings on a particular field of interest, and in this context, several pre-defined phases were followed. Therefore, we have completed this systematic review following the previously established method [36]. The systematic review started with a deep query searching of online articles to compile all papers related to the field. The principal keywords utilized to represent the main areas for this review are “contextual suggestion system” and “recommendation system”. The query is restricted to articles written in English. 

_Sustainability_ **2021** , _13_ , 8141 

6 of 27 

## _3.1. Information Resources_ 

In this review, source articles are derived from four major digital databases, namely, Science Direct, Web of Science (WoS), Scopus, and the Institute of Electrical and Electronics Engineers (IEEE). The rationale for selecting these source databases is that it provides access to science, social sciences, humanities, engineering, and technology in terms of the technical, theoretical, and disciplinary efforts by researchers around the world. Thus, these databases are reliable for this field of knowledge. The selection process consisted of the literature review followed by screening and filtering. The first phase is to scan the titles and abstracts to exclude duplicate resources and unrelated research. The second phase is to complete the reading of these articles. The rest of the phases in this review are summarized below under review protocol and taxonomy analysis. All insights are summarized under systematic review discussions. 

## _3.2. Inclusion Criteria_ 

The following criteria are utilized to choose the possibly relevant articles for screening purposes. The reason for inclusion criteria is to find more relevant papers connected to the contextual suggestion system. 

- i. Contextual suggestion system is a specific stream for research in e-tourism [11,29–50]; therefore, articles published from 2012 to May 2020 are used in this review. 

- ii. Articles based on contextual suggestion and recommendation systems with a focus on e-tourism are included. 

- iii. Articles that are related to e-tourism application domains are considered. 

- iv. Reviews and original articles that propose contextual suggestion and recommendation system “approaches” or “techniques” are screened for this review. 

## _3.3. Exclusion Criteria_ 

The following criteria are utilized to exclude the articles/papers from this review owing to unverified sources. 

- i. Unpublished works, doctoral thesis, blogs, articles on electronic media, and nonEnglish studies are excluded from this review. 

- ii. Papers with a focus on recommendation systems based on subscription-based services recommendations, health, news, education, social relation, job/vacancy, and paid services based recommendations are excluded from this review. 

- iii. Papers published before 2012 are also excluded because the papers are too old as the trend of technology evolves rapidly. 

A multi-level evaluation method was applied based on review protocols to choose the articles for this review. First, a query search on four online databases, namely, Science Direct, Web of Science, IEEE, and Scopus, revealed 1006 records after limiting the search engine to meet the inclusion criteria. Figure 2 shows the systematic review used for further screening. Keywords, titles, and abstracts were examined in the initial step to minimize the irrelevancy of articles, resulting in the exclusion of 738 records in this step. Subsequently, only 5 duplicates were found from the remaining 268 records. Next, after full-text reading, 143 articles were deemed to meet the inclusion criteria. In the end, only articles that focus on the contextual suggestion and recommendations systems in e-tourism were considered for this review. 

_Sustainability_ **2021** , _13_ , 8141 

7 of 27 


![](prepared/sustainability-13-08141/images/sustainability-13-08141.pdf-0007-02.png)



![](prepared/sustainability-13-08141/images/sustainability-13-08141.pdf-0007-03.png)


**Figure 2.** Flowchart of study selection, counting the search query and inclusion criteria. 

## **4. Taxonomy Analysis** 

The 1006 articles obtained from the four databases through separate query search were classified as follows: 711 from Science Direct, 25 from IEEE Explore, 10 from Web of Science (WoS), and 313 from Scopus. Figure 3 shows the bar chart based on the number of articles in different categories in the digital databases. These articles were categorized according to the field of study. Figure 4 shows the number of articles based on sub-categories of the model/framework. Figure 5 shows the yearly development and increasing trend for this field of research from 2012 to 2020. After skimming the titles and abstracts, 268 articles and 5 records were removed owing to duplication. Full-text reading omitted 120 articles, leaving 143 articles as the ultimate set. The 120 articles are eliminated based on the exclusion criteria if the recommendation system is concerned with e-commerce and subscriptionbased services as these criteria are out of the scope of this paper. These selected 143 articles were read carefully to discover a general gap leading to the recommendation and contextual suggestion systems in e-tourism. These outlines captured the common classifications of research articles and then refined the literature classification. Figure 6 shows that several 

_Sustainability_ **2021** , _13_ , 8141 

8 of 27 

subclasses could be distinguished in the main layers. The following sections list the determined classifications, constructing simple indicators throughout the discussion. 

As shown in Figure 6, the results show a pattern of article categories according to the taxonomic literature. The main focus of this review was the contextual suggestion and recommendation systems. The categories of articles were decomposed into several categories from the three main classes, namely, review articles [40,43–49], model/framework, and application. Under the second category of model/framework, it is sub-categorised into ~~time-based [50–53], activity-based [17,54–66], location-based [1,11,12,17,20,30,42,48,67–88],~~ social-based [9,89–106], and multi-dimension [107–133], while under the third category ~~of application, it is also sub-categorised into travelling and POI [1,4,8,49,50,73,134–~~ 155], shopping and e-commerce [156,157], and finally events and activities [22,158–167]. 


![](prepared/sustainability-13-08141/images/sustainability-13-08141.pdf-0008-04.png)


**----- Start of picture text -----**<br>
Distribution of Articles by Categories<br>in Digital Databases<br>22<br>SCOPUS 37<br>5<br>2<br>IEEE 4<br>1<br>WEB OF SCIENCE 4<br>16<br>SCIENCE DIRECT 49<br>3<br>0 10 20 30 40 50 60<br>Applications Model/Framework Review<br>Figure 3. Bar chart of summarization number of articles by different categories.<br>Categories by Models/Framework:<br>Total 94 Articles<br>TIME BASED 4<br>ACTIVITY BASED 14<br>LOCATION BASED 30<br>SOCIAL BASED 19<br>MULTI-DIMENSIONAL 27<br>0 5 10 15 20 25 30 35<br>Number of Articles<br>**----- End of picture text -----**<br>


**Figure 3.** Bar chart of summarization number of articles by different categories. 

**Figure 4.** Number of articles by model/framework. 

_Sustainability_ **2021** , _13_ , 8141 

9 of 27 


![](prepared/sustainability-13-08141/images/sustainability-13-08141.pdf-0009-02.png)


**----- Start of picture text -----**<br>
Categories by Years of Publication<br>2012 2013 2014 2015 2016 2017 2018 2019 2020<br>14<br>12 13 13<br>12<br>10 11 11<br>8 9<br>8<br>6 7 7<br>6 6 6<br>4 5 5<br>4 4<br>2 3 3<br>2 2<br>1 1 1 1 1 1<br>0<br>SCIENCEDIRECT WEB OF SCIENCE  IEEE SCOPUS<br>**----- End of picture text -----**<br>


**Figure 5.** Bar chart of summarization number of articles by publishing year. 

## _4.1. Review Articles_ 

Review articles summarized the current understanding or formulation of previously published studies related to the subject of this review. Through review articles, new findings, progress, research gaps, the people involved, debates on certain issues, and new ideas that can be highlighted for future research are identified. Several researchers have concentrated on the security and privacy related to the smart city. The authors of [51] also highlighted trust and safety issues, [52] raised issues related to the factors that are considered as context. The author of [48] focuses on capturing the activities of the user and reflects them on recommendation systems. The authors of [53] suggested sensors to capture such data. The authors of [54] highlighted the importance of recommendation system in e-learning, social network, smartphone, radio networks recommender system, smart tourism [55], TV [56], and context-aware vehicle networks [57]. 

## _4.2. Model/Framework_ 

Model/framework is one of the methods of effective research that consists of real or abstract forms such as mathematical models. The combinations of mathematical models are called approaches in previous studies. The model/framework in the present review is further divided into five categories. Time-based frameworks [58–61] were incorporated with temporal information. Activity-based [12,62–66,168–175] and location-based ones utilized the tourists’ geographic position via GPS to facilitate the tourists’ travel in an unfamiliar area. Social-based considered social-based constructs and effectiveness, and multi-dimension is a combination of all the approaches. 

_Sustainability_ **2021** , _13_ , 8141 

10 of 27 


![](prepared/sustainability-13-08141/images/sustainability-13-08141.pdf-0010-02.png)


**Figure 6.** A Taxonomy of research literature on the contextual suggestion system and recommendation system. 

## 4.2.1. Time-Based 

Recommendations systems have merged multiple times with various granularities to improve decision mechanism and make accurate recommendations. In comparison with traditional recommendation system, time is easy to capture owing to the recent development of smartphones, such as time of day (morning, night or evening), day of the week (workday, day off or weekend), the season (summer, winter, spring), or even semester (first or second semi-year) in an academic setting. It is not difficult to describe a contextual model that includes time information. Timestamp data are consistent and frequent at the same time [58–60]. Besides, the authors of [61] developed a time-based recommendation system based on events and activities with the context were the day and week, such as concert, music, and movie recommendation systems. 

## 4.2.2. Activity-Based 

Several papers have been published to identify various kinds of human activities, i.e., low-level activities, for instance, eating, reading, music, and movies [62–65], and high- 

_Sustainability_ **2021** , _13_ , 8141 

11 of 27 

level activities, or indoor activities (home or work tasks) [66], social activities [168], and outdoor and travelling activities [61,169–174]. The author of [175] has proposed methods for a recommendation that automatically identify everyday user activities by choosing the objects to be recommended in conjunction with the essence of user routine activities. 

## 4.2.3. Location-Based 

Location-based applications use a range of means to estimate the location of the user, such as global positioning system (GPS), which is the most well-known technology offering global coverage with precision, based on location; The authors of [12,67–69] proposed an adaptive personalization system for location-aware recommendations. The author of [70] has proposed an approach to find distant neighbours using location. However, users should not expect to obtain locations from related users or sites [71–76]. In reality, other users are also searching for POIs that are near enough to their current location [77,78]. Only those users that are located close to GPS trajectories form their travel experiences pattern [11,17,20,79–81]. The authors of [82] utilized the POIs’ popularity to optimize the probability estimate of the relative distance between the recipient and the POI, taken from semantic tags. In another aspect, POIs [48,83–85] have varying influence such as context and distances, e.g., users generally choose local stores, although many of them do not have any preference to see an attraction location [1,42,86]. Therefore, POI recommendation systems [30,87,88] must separate POIs from their categories when choosing the threshold of distance (тKilometers) to decide whether or not a POI constitutes a successful recommendation. 

## 4.2.4. Social-Based 

The social knowledge of the user, including individual preferences; overt (friends) and implied (similarity with users) social connections; tags; and social descriptions, e.g., clicks, likes, dislikes, and so on, is derived from websites, wikis, social bookmarking, file sharing, online forums, social networks for enterprises, and tagging applications. With the inclusion of data from social networks, recommendation systems also included a vast amount of personal knowledge from users [89–92]. To protect information, privacy and confidence concerns are thus crucial issues [9,93–95]. Several experiments have studied social network users’ activities to extract trustable individuals and benefit from their confident recommendations. Social ties-based strategies have been used for the first group of techniques to consider those actual friends are trustworthy than desired as a source of recommendations [96]. The author of [97] focuses heavily on the premise that individuals prefer others who identify with them to suggest similarity in taste. The definition of ‘family strangers’ has been proposed by the third group of research studies to describe a new degree of confidence between individuals based on different variables such as similarity of interest, geographical neighbourhood, and time meeting. The authors of [98] focused on the leader methods, and mined the social networks of all users to produce the most influential person who can craft their views on recommendations. To meet the needs of all users, several studies have recognized specific categories of users that need logical reasoning. The authors of [99] have suggested three types of “special users”, including (i) cold-start users who have recently joined the system and have a minimum activity record, (ii) grey sheep users who have unusual behaviour not similar to other users, and (iii) users who do not have any attitude in the current scenario. The first two groups of users i.e., “cold-start” and “grey sheep”, were defined on similarity-based usual context-aware behaviour. However, the third type of users has specified the similarity of users’ role set, which describes the similarity of shared context-aware interest between groups of users. Social-based recommendation can also be utilized in the context of smart cities; several studies have been carried out in the field of recommendation systems and their integration with other domains such as Smart Cities, [100] as well as in their implementations. The recommended approaches utilized the available information to offer a recommendation [101]. The author of [102] has developed a graphic recommendation system with comprehensive data on book contents, users’ history, and demographic information. The authors of [103] utilized 

_Sustainability_ **2021** , _13_ , 8141 

12 of 27 

the user’s personal and social information and integrated this information to increase the consistency of the relevant items recommendation. The authors of [104] have developed a technique based on probabilistic reasoning for personalizing a recommendation system. The recommendation system can also develop a schedule to visit fascinating places and events on the trip based on the profile and interest provided by the tourists. In Smart Cities and tourism, several forms of RS can be used, and numerous systems have been built with a range of interfaces, recommender, and functionalities [105]. The author of [106] has developed a recommendation system for personalized city transportation. Personalized route recommendations were provided using knowledge-based recommendation technologies, and suggestions were determined for each individual according to their choice for travel. 

## 4.2.5. Multi-Dimension 

In certain scenarios, a contextual information recommendation system combines various kinds of information to model a context [107–113] because of the correlation between contextual variables, e.g., the weather situations or the atmosphere surrounding the user may influence his/her mood [114]. The viewer will then look for different types of films than such user commonly watches [115–117] or listen to music according to the mood [118–120] or photos in which a user may be interested [121,122]. However, a complicated recommendation algorithm will conclude with the creation of a recommendation method that considers multiple contextual details [123–130]. Consequently, before using multi-dimensional information to personalize recommendations, it is important to research the importance of contextual elements in specific domains, for instance, a user is looking to think like a potential group [131,132]. The authors of [133] utilized an artificial neural network system to forecast the scores with which this approach brings together content (user and business) and metadata (review and rating) that deliver better prediction outcomes. A substantial increase in the overall efficacy of the recommendation system was reported in this study. 

## _4.3. Application_ 

In this taxonomy, the application domain category was defined as the initial prototype of the existing approaches in different application domains. This category was further divided into travelling and POI, shopping/e-commerce, and events/activities. Given the focus on travelling, travel and POI-based studies were especially examined in the development context of these systems. Cities are still changing, dynamic cyber-physical structures covering several areas. The model of smart city started by cities adopting communications technologies to supply services to their residents. The original idea of a smart city became smarter and more effective with the usage of information technology. In the beginning, resources were restricted to tangible fields, particularly energy and mobility systems. However, recent development not only dramatically improved what can be achieved for IT, but the capabilities and the area smart city covered have broadened significantly. 

## 4.3.1. Traveling and POI 

The authors of [134] proposed that contextual awareness in the tourism industry seeks to make smartphone applications more aware of travellers and allows travellers to do several visiting activities. One of the drawbacks of this approach is that travellers cannot obtain a decent SA for a tourist destination. This research has shown that multiple contextually aware mobile applications only help particular travelling activities and travellers will often move between different mobile applications to obtain optimum situation awareness. Thus, the interface design of mobile application does not support the cognitive functions of travellers, particularly in their perception, understanding, and prediction. Therefore, situation awareness enhances mobile interfaces and helps travellers to make a smarter decision based on different scenarios in the tourist destination. The authors of [135] proposed an approach that offers a generic model for users to navigate the patrimony tourism system by modelling their preference, profiles, and contexts to tailor services in line with their 

_Sustainability_ **2021** , _13_ , 8141 

13 of 27 

preferences. This method saves users’ history for continuously optimizing the recommendation services, and uses a collaborative filtering recommender system to calculate the most appropriate services based on their interest. An example of a scenario for saving time, costs, finding the relevant places, avoiding bad service, and so on illustrated the potential of the proposed framework to offer better service for tourists [136]. Researchers also suggested developing a prototype of the proposed framework and recommended improvement in an approach by using other intelligent approaches for future studies in e-tourism [8], such as micro-service architecture-based recommender services [4] and knowledge graph-based recommender services [137] based on data mining [138–140]. The authors of [141] proposed a route planning recommendation system that generates persuasive messages to highlight environmentally friendly options for users in the smart city. The authors of [50] suggested a context-aware web services recommendation for modelling impact on the user’s expectations on user location updates and location similarity mining based on the user location in the smart city context. The authors of [142–146] proposed a context-aware recommendation system using smartphone sensors integrated with smart city applications and e-tourism, another recommendation system based on tourist context [147,148]. The authors of [49,73,149,150] proposed a system of travel recommendations that mines appropriate locations, context, user preferences [151–153] users’ reviews [154], sentiments analysis [1], and users’ physical and psychological functionality levels [155]. 

## 4.3.2. Shopping and e-Commerce 

The authors of [156] proposed a general service recommendation system following telecommunication service distribution features of Ubiquitous Consumer Wireless World that match their complex, contextual, and customized preferences. This system can empower individual consumers to make decisions, and thus have a positive effect on the whole society, promoting and encouraging direct interactions between consumers and service providers. Such forms of direct relationships are very desirable for “Smart City Services” in that their directness makes it easier to adapt more dynamically and grow user-driven services. The authors of [157] proposed a context-aware recommendation system to predict reviews and ratings’ helpfulness for products having online reviews as reviews provide social proof of quality when shopping online. 

## 4.3.3. Events and Activities 

The authors of [158] suggested an approach to contextualize query internet-scale IoT data and illustrate a method for smart cities using recommendation applications of smart parking space. The authors of [159] suggested a smartphone application for event recommendation such as restaurants [160], cultural heritage [161,162], museums tours [22] monuments [163] route recommendations [164], concerts and events [165], and seminars [166] with the context-aware and tag-based recommendations. This initializes users’ accounts with minimal user intervention and the features of the items provide recommendations using a tag-based context-aware recommender algorithm. The authors of [167] presented a menu generation system to suggest menus according to user expectations that use the recipe dataset and annotations. Their method is appropriate to provide consumers with customized and healthy menus compared with the recent research on the food recommendation system. 

## **5. Critical Review** 

The limitations of approaches used in contextual suggestion and recommendation systems are explored through this systematic review. Numerous studies focus on the field of recommendation systems, but not on the contextual suggestions. In terms of approaches, most of the studies based on recommendation system use explicit feedback and crawl data from internet resources to test the approaches and contextual suggestions system based on both explicit and implicit feedbacks incorporated with contextual factors. Moreover, in the contextual suggestion system, studies used the test collections provided by TREC 

_Sustainability_ **2021** , _13_ , 8141 

14 of 27 

Contextual Suggestion Track. In addition, a crawler is at times used to extract information from Internet sources for further enhancements. 

Out of 143 articles, only 30 focus on location-based recommendation and contextual suggestion systems. Most of the studies used the content-based filtering approach, but are considered unfit given their lack of venue ratings, whether negative or positive, which is one of the limitations [37]. Rating-based collaborative filtering based on the factorization machine is also used to process the tourist’s feedback and contextual information to improve the accuracy of suggestions. However, data display a sparsity problem where the suggestion lacks accuracy [79,85,176]. 

Several studies used preference-based product ranking technique and weighted and unweighted combination of tourist’s attributes, such as prices and reviews of venues. These attributes signified how likely the tourist’s behaviour is influenced and how likely a tourist is to visit the particular suggested venue. However, this technique has inadequate feedback, and there are no such parameters to evaluate the tourist’s behaviour. Therefore, such approaches lack data and they could not be useful for venue recommendations and contextual suggestion systems [38,39]. Other studies used review-based approaches, but also suffer from a lack of reviews available for several venues [37–41,177–179]. 

## _5.1. Recommendations_ 

From the literature review, recommended works in various research fields are summarized to improve approaches used in contextual suggestion and recommendation systems, which can be undertaken by future system developers, scholars, industries, e-governments, health providers, web services, and restaurants in achieving sustainable e-tourism. 

## 5.1.1. Recommendations for System Developers 

As the complex subjectivity of the term “context” increases, this should be carefully analyzed in the application to provide consistent suggestions. In most of the reviewed studies, contextual factors are chosen based on past studies lacking validation of such contexts in similar application domains [25,39,42,84,133,152,177–180]. Hence, before developing contextual-based suggestion and recommendation systems, exploring relevant contexts in each application domain would be ideal [19]. After compiling the context, its relevancy and tourists’ preferences are required to assess the likelihood of the suggestion influencing the tourist [40,44,89,141,177,181]. The correlation between context and tourist preferences can be analyzed using techniques such as similarity measures and multi-regression [48,77,182,183]. Moreover, data in the mobile environment are typically multifarious, suffer from generalization, and can add on further complexity. More studies are needed in context-aware suggestions and recommendation systems based on the mobile environment that can be a significant contribution. 

Data distribution varies over time, including product features and tourists’ personal preferences. Therefore, using obsolete data to predict tourist’s present-day preferences can affect the performance of the recommendation system [54]. Thus, real-time data sharing, location-based filters, and context-aware recommendations are considered necessities in e-shopping and sustainable e-tourism. For instance, a tourist visiting a shopping mall would prefer real-time feeds based on location with precise recommendations of products and stores available in his/her current context. Besides, acknowledging the tourists’ carrying capacity for a touristic place would improve the tourists’ satisfaction, quality of services, and experience in the management and monitoring of a sustainable e-tourism. Furthermore, the development of electronic tools for tourism and designing strategies for economic growth is one of the smart city dimensions. Developing such applications needs a thorough examination of real-time data, current location, and contextual factors. Thus, modelling tourists’ preference with real-time data and the location-based context in recommendation systems can be an exciting research topic. 

_Sustainability_ **2021** , _13_ , 8141 

15 of 27 

## 5.1.2. Recommendations for Scholars 

Previous studies [30,83,86,87,110,184] thoroughly investigate approaches to overcome the data sparsity problem. However, the issue is yet to be well applied in numerous fields such as the contextual suggestion system. Therefore, cognitive computing-based adaptive-learning techniques for linking related information from one application domain to another to fill the information gap offer a good chance to solve the data sparsity problem. Thus, adaptive-learning based recommendation systems are a noteworthy direction [54]. 

Owing to the lack of datasets available in all respective domains, applications based on mobile recommendation system in other application domains such as social relations, events and activities, and businesses are unbalanced. Only 23% of studies in the travel recommendation domain use datasets extracted from publicly available repositories, such as the Geolife GPS trajectory dataset and LBSN [11,17,18,38,42,43,45,48,62,71,72,79,81,83,85–87,179,185–189]. Hence, ensuring that datasets are publicly available in other fields of the domain is needed for the research community to carry out experiments, evaluation, and comparison for best working approaches [48]. Moreover, communication of sustainability towards the tourist through public data would help in educating and enhancing their environmental awareness to achieve and improve sustainable e-tourism. In addition, collaborations between knowledge centers, social networks, and telecommunication providers in adding the context in the recommendation system contribute to the development of a smart people and smart city. 

## 5.1.3. Recommendations for Industries 

In recent years, an increasing volume of research on recommendation services has been deployed in various industries and applications. In several fields, contextual information is adopted in recommendation services by an enormous number of organizations. Therefore, a more enhanced software development service based on the reusability of industrial datasets for recommendations and contextual suggestion systems is necessary [190]. For instance, in movie recommendations [56,64,67,177], the production, tourists with different tastes or genres, and the services to watch online are increasing at enormous speed. Thus, the proposal for movie recommendations based on tourist models incorporates reviews of movie experts and movie synopsis to analyze the relevancy of the recommended movies to an appropriate tourist [177]. Moreover, a music recommendation system [69,175] can work with the same concept by classifying a list of songs into mood, activity, and health to recommend a list of songs to a tourist. With the same concept, music recommendation services are introduced by the last.fm, which utilizes tourists’ location and taste to recommend songs according to tourist personal preferences. By improving the recommendation rate and accuracy that satisfies the tourist, it would lead to an improvement in tourism product quality and economic viability in a sustainable e-tourism and smart economy. 

Computing technologies have been on continuous change from desktop to laptop platforms, to mobile, and most recently into wearable technology. Given the feature of being vital in daily lives, ABI research (2015) forecasts that the use of wearable devices (i.e., smart TVs, smart shoes, smart glasses, and smartwatches) would increase at enormous rates with the ability to connect and manage via smartphones wirelessly. Wearable computing offers various characteristics [78] to fulfil the concept of smart gadgets. For instance, different sensors can be utilized and integrated into clothing and or even the human body [191] to analyze behaviour, and at the same time, output can be presented on smartphones. Similarly, these sensors are easy to work with and operate, fulfilling versatile individual needs [107]. For instance, in travel itinerary recommendations [192], smart glasses can be used to provide the vision of the surrounding areas, integrated with augmented reality that provides details and recommends services related to the itinerary as well as activities and places to visit based on the tourist’s personal preferences [48]. 

In the mobile environment, wearable devices suffer from privacy problems owing to access and control through smartphones, where untrusted apps can unnoticeably capture pictures and videos without the tourist’s permission [95]. Hence, a balance mechanism is 

_Sustainability_ **2021** , _13_ , 8141 

16 of 27 

necessary for security and privacy issues to manage, secure, and set permissions that allow access to personal data and control the information sharing to any third party or untrusted app [5,52]. Nevertheless, the precision of recommendations can be compromised with the tourist’s interference [11,175]. Thus, the effects of the tourist’s permission and control on recommendations require thorough study [193]. 

## 5.1.4. Recommendations for e-Government 

The current e-government (e-Gov) environment aims to provide vital information and services to citizens online. Given that the tourism industry is considered as the foremost profitable, the e-Gov significantly develops applications to improve services related to e-tourism with the participation and control from the local community in decision-making, and providing natural and cultural information about the touristic spots would be a way to achieve sustainable tourism and a guarantee of income and revenue generation for the well-being of the community as well as the country. With the encouragement of citizen participation in protecting the place to which they belong, both sustainable e-tourism and smart governance can be achieved. Nevertheless, existing e-Gov services are generally restricted to visualization and information on tourist spots, where AI-based recommender services that can provide precise information in e-Gov are greatly required [194]. Tourists particularly prefer e-Gov services as a trusted trademark. Therefore, developers should construct applications and services based on personalization techniques and services related to the security of tourist and residents. Thus, recommendation services can play a huge role in e-Gov applications to deliver personalised services in e-tourism. Considering these factors in future research on e-Gov services recommendation systems presents a particular interest [54]. 

## 5.1.5. Recommendations for Health Providers 

Data limit the recommendation and contextual suggestion systems in providing appropriate information to a tourist. The data are restricted by the methods of information extracted from the sources, which are limited to sensors that feed and store data, and thus lack numerous dimensions. In a big data environment, various information dimensions can be acquired to assess tourist modelling based on personal preferences and provide comprehensive and precise recommendations. The approaches of [49,68,195] are examined to develop recommendation systems using big data. However, numerous directions remain to be explored in this regard. For instance, sensors in ubiquitous computing devices can extract more data from tourists, which can be utilized by health and medical application domains. Therefore, a health recommender system can emerge with appropriate information on health and precise personal preferences-based recommendations. Tourists’ satisfaction with medical tourism, employment, local economy, and long-term economic viability would improve the living conditions of the local community and achieve a sustainable e-tourism in the country. Besides, a contextual suggestion system that can provide emergency response facilities for tourists who like hiking and jungle tracking, for instance, would also contribute to smart living and give the tourist a sense of security when they are travelling in a foreign country. 

## 5.1.6. Recommendations for Web Services 

Context-aware web services provide recommendations based on the highest scores rated for an item and contextual tourist information, combined in the recommendation process to increase accuracy [196]. Despite recent development in context-aware web services recommendation, the works of [49,75,197] separately adopt contextual, spatial, and temporal constructs. However, the correlations between temporal and spatial constructs are not fully addressed [50]. Moreover, introducing other contextual factors such as social effects to increase the accuracy of recommendations is a significant direction. The social effects of a sustainable e-tourism include recommending the sustainable use of natural and cultural resources during travel, supporting pollution reduction, and selecting green hotels 

_Sustainability_ **2021** , _13_ , 8141 

17 of 27 

and products to strengthen the tourism product quality and tourists’ satisfaction. Another context-awareness in a smart environment that could be considered is suggestions on activities that provide tourists’ involvement in environmental protection such as recycling and reducing waste while travelling. 

## 5.1.7. Recommendations for Restaurants 

Contextual factors such as location, dining time, check-in time, and the operating hours of restaurants can be incorporated with the tourist’s personal preferences in recommending systems to improve accuracy. Similar preferences can be extracted from tourists’ friends and family and other social media. All this information can then be combined to recommend a restaurant to tourists and their group of friends [198,199]. Moreover, the application for recommending restaurants can be connected with not only social media (e.g., Facebook, Twitter), but also with LBSNs (e.g., Yelp, Trip advisor) to observe any changes regarding restaurant location, ratings, and reviews to provide tourist recommendations with updated information. Food is one of the most potential cultural exchanges as a driving force for peace when it comes to promoting one country’s culture. Therefore, accurate recommendations about the restaurants would yield tourists’ satisfaction and later achieve sustainable e-tourism. 

## _5.2. Practical Implications_ 

The benefits of contextual suggestion and recommendation systems in various areas of the study clearly show its importance in considering potential opportunities based on certain indicators. In the last decade, Internet tourists have seen an enormous increase in inaccessible online data. Such data are certainly valuable for tourists who intend to visit an obscure place [42,185]. To plan a trip, tourists frequently search associated information about the place such as transportation, restaurants, accommodations, and cultural and social activities around the area [7–9,134,200]. However, the never-ending list of choices available online, even only on tourism-based websites, can be overwhelming and thus confusing to tourists owing to its complexity. Evaluation can be time-consuming for tourists to choose the best fit for their respective needs [104,105,186,201,202]. 

To provide tailor-made information to a tourist, techniques such as personalization can be utilized to analyze tourists’ personal preferences, tastes, and limitations [6,8,11,69,71,135]. These techniques are specifically appropriate in recommendation systems [40,178] that aim to provide tourists with relevant information based on personalization by screening out irrelevant choices [67]. In tourism, contextual suggestion and recommendation systems are specifically designed to coordinate with the attributes of the travel industry, suggest appropriate attractions to a tourist, and provide visibility support to leisure resources [6,8,35,104]. If provided with explicit/implicit feedback, these systems can assist a tourist with spontaneously learning tourist preferences to provide precise recommendations [30,42,96,159,187]. Explicit feedback can be obtained by asking a tourist to fill out a form based on the travel experience and interest. Implicit feedback can be derived by accessing personal information and activity logs to analyze personal interests. 

Moreover, these contextual suggestion systems may not only take the preferences into account, but also process several contexts of the trip (i.e., weather, trip type, location, and more) that can benefit a tourist in a new city. A change in circumstances can also customize an entire trip in a limited time using mobile devices. The context can include locations by default, and a slight change in context can alter activities from a business trip to the relief of rest days and variations in weather conditions. Approaches based on context can proactively notify tourists with suggestions regarding their current contexts, such as plan changes, current weather, location, and appropriate time to visit the specific place [203]. For instance, on a business trip in a location planned for an office meeting, a tourist can prefer to spend time in nearby places if the meeting is postponed. As such, the contextual suggestion system can provide a list of places according to the tourist needs in that particular context. In general, tourists heavily rely on mobile devices for travel. This 

_Sustainability_ **2021** , _13_ , 8141 

18 of 27 

behaviour recently shows massive increases. Therefore, e-tourism applications provide a good opportunity for mobile services that help tourists by offering recommendations based on their preferences and current context [8,204]. Consequently, the SDGs have become major focal points for the study of tourism’s contribution towards SDGs 9 and 11 [205,206]. Tourism research also ensures economic, socio-cultural, and environmental sustainability in many contexts such as continuous tourism revenue, employment rates, energy efficiency, the usage and availability of clean potable water, biodiversity conservation, or crime rates for both local communities and tourists [207,208]. 

Sustainable e-tourism can be increased via using handphone-based reliable and realtime data and information for low carbon footprint in the tourism industry. The handphonebased convenient system can reduce carbon emissions via reducing the physical movement of tourists of the irrelevant searches for restaurants, accommodations, and so on. Therefore, this handphone-based convenient e-tourism can significantly contribute towards sustainable cities, i.e., SDG 11, as well as sustainable consumption, i.e., SDG 9. In addition, the contextual suggestions via cognitive computing-based adaptive-learning techniques have been instrumental for scholars such as city planners as well as for law enforcement personals to contribute towards developing a sustainable city for promoting tourism, i.e., SDG 11. Smart gadgets including wearable gadgets can also contribute significantly towards sustainable tourism [209–212], while linking entire industries related to tourism as well as ensuring privacy and security of tourists in sustainable cities, i.e., SDG 11. In this regard, the government sector can take on leadership roles for sustainable tourism via promoting internet app-based e-tourism services, because the government sector is well equipped with legal, institutional, and financial capabilities. Therefore, e-tourism services and information disseminations such as healthcare, transport, accommodation, restaurant, and so on by the government sector in collaboration with the private sector can also contribute significantly towards sustainable tourism owing to the trust in the government services including web-based ratings for specific services by tourists. 

## **6. Conclusions** 

Contextual suggestion and recommendation systems are widely used in various fields such as shopping and e-commerce, events and activities, social media, and e-tourism. In the latter, location-based context and travellers’ personal preferences are mainly considered. This systematic review of literary studies reveals that 30 out of 143 articles are on location-based contextual approaches, 4 are on time-based, and 27 are on the use of multidimensional approaches. In addition, out of 143 articles, 19 articles focused on social-based recommendations and contextual suggestions, 14 discussed activity-based approaches, and the remaining 8 articles were based on reviews. Furthermore, 94 articles were based on the analysis or evaluation study of model/framework, 41 were on applications, and 8 were on reviews. This review finds that the widely used approaches are content-based filtering, collaborative filtering, and matrix factorization. Normalized discounted cumulative gain (NDCG) and precision, as well as reciprocal rank (RR), are also widely adopted tools for evaluation. 

The contextual suggestion and recommendation systems have become a phenomenon in certain information retrieval (IR) and artificial intelligence (AI) areas to help travellers in strategic planning based on factors such as their interests and contexts that can influence their decision. This trend shows that several approaches in e-tourism are used in the development of contextual suggestion and recommendation systems, providing a list of venues to a traveller based on the context in line with the current technological development as well as data resources available in smart cities. Using these systems in e-tourism, they do not just offer the tourist efficient services by identifying personalised preference and buying touristic products in the most convenient way after eliminating the non-preferred items, further, it has also born as a way for sustainable travel and lifestyle. Besides, these systems are also among the top technologies in cutting down the travelling time and cost, ensuring more sustainable tourism. To have sustainability in e-tourism, the use of ICT and electronic 

_Sustainability_ **2021** , _13_ , 8141 

19 of 27 

tools in the environment, economy, and socio-culture have to be considered. The contextual suggestion system remains sustainable in e-tourism, as it is undeniable that it improved the tourist’s satisfaction and interests while maintaining the integrity of sustainability in the recommendation context. Future research can include the diversity of the tourism service blueprint for better touristic experiences, as well as how they enable the tourism industry to track and communicate with visitors in a more meaningful way and more effectively manage visitors’ experiences. Continuous collection and expansion on tourist contexts such as the data range of complex emotional responses and moment-to-moment traveller-related analysis might yield a more personally relevant search. Thus, the entire work process on contextual suggestion and recommendation systems has enhanced sustainable e-tourism in achieving SDG 9 and 11. 

**Author Contributions:** Conceptualization, H.U.R.K.; methodology, C.K.L., K.L.T.; validation, K.L.T. and M.B.M.; formal analysis, K.L.T.; investigation, H.U.R.K. and K.L.T.; resources, C.K.L. and K.L.T.; data curation, H.U.R.K.; writing—original draft preparation, H.U.R.K., C.K.L. and M.F.A.; writing—review and editing, C.K.L., K.L.T., M.F.A. and M.B.M.; supervision, C.K.L. and K.L.T.; project administration, M.B.M.; funding acquisition, M.F.A. and M.B.M. All authors have read and agreed to the published version of the manuscript. 

**Funding:** The publication of this article is supported by Universiti Kebangsaan Malaysia (UKM) grant MI-2019-013. 

**Institutional Review Board Statement:** Not applicable. 

**Informed Consent Statement:** Not applicable. 

**Data Availability Statement:** Not applicable. 

**Acknowledgments:** The authors are grateful to the reviewers for their constructive comments. 

## **References** 

1. Shafqat, W.; Byun, Y.C. A recommendation mechanism for under-emphasized tourist spots using topic modeling and sentiment analysis. _Sustainability_ **2020** , _12_ , 320. [CrossRef] 

2. Buhalis, D. Technology in tourism-from information communication technologies to eTourism and smart tourism towards ambient intelligence tourism: A perspective article. _Tour. Rev._ **2019** , _75_ , 267–272. [CrossRef] 

3. Gretzel, U.; Fuchs, M.; Baggio, R.; Hoepken, W.; Law, R.; Neidhardt, J.; Pesonen, J.; Markus, Z.; Xiang, Z. e-Tourism beyond COVID-19: A call for transformative research. _Inf. Technol. Tour._ **2020** , _22_ , 187–203. [CrossRef] 

4. Garcia, L.M.; Aciar, S.; Mendoza, R.; Puello, J.J. Smart Tourism Platform Based on Microservice Architecture and Recommender Services. In _Lecture Notes in Computer Science (Including Subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)_ ; Springer: Berlin/Heidelberg, Germany, 2018; Volume 10995, pp. 167–180. 

5. Kontogianni, A.; Alepis, E. Smart tourism: State of the art and literature review for the last six years. _Array_ **2020** , _6_ , 1–12. [CrossRef] 

6. Buhalis, D.; Amaranggana, A. Smart Tourism Destinations Enhancing Tourism Experience through Personalisation of Services. _Inf. Commun. Technol. Tour._ **2015** , _2015_ , 377–389. 

7. Masseno, M.D.; Santos, C. Privacy and Data Protection Issues on Smart Tourism Destinations—A First Approach. _Intell. Environ._ **2018** , _23_ , 298–307. 

8. Gavalas, D.; Konstantopoulos, C.; Mastakas, K.; Pantziou, G. Mobile recommender systems in tourism. _J. Netw. Comput. Appl._ **2014** , _39_ , 319–333. [CrossRef] 

9. Masseno, M.D.; Santos, C. Smart Tourısm Destınatıons Prıvacy Risks on Data Protectıon—A Fırst Approach, from an European Perspectıve. _Rev. Eletrônica Sapere Aude_ **2019** , _1_ , 125–149. 

10. Nitti, M.; Pilloni, V.; Giusto, D.; Popescu, V. IoT Architecture for a sustainable tourism application in a smart city environment. _Mob. Inf. Syst._ **2017** , _2017_ , 92101640. [CrossRef] 

11. Efraimidis, P.; Drosatos, G.; Arampatzis, A.; Stamatelatos, G.; Athanasiadis, I. A Privacy-by-Design Contextual Suggestion System for Tourism. _J. Sens. Actuator Netw._ **2016** , _5_ , 10. [CrossRef] 

12. Ravi, L.; Subramaniyaswamy, V.; Vijayakumar, V.; Chen, S.; Karmel, A.; Devarajan, M. Hybrid Location-based Recommender System for Mobility and Travel Planning. _Mob. Netw. Appl._ **2019** , _24_ , 1226–1239. [CrossRef] 

13. Bayrak, G.Ö. Sustainable Tourism. In _Encyclopedia of Corporate Social Responsibility_ ; Idowu, S.O., Capaldi, N., Zu, L., Gupta, A.D., Eds.; Springer: Berlin/Heidelberg, Germany, 2013. 

_Sustainability_ **2021** , _13_ , 8141 

20 of 27 

14. Amerta, I.M.S.; Sara, I.M.; Bagiada, K. Sustainable tourism development. In _International Research Journal of Management, IT and Social Sciences_ ; Sloap: London, UK, 2018; Volume 5, pp. 248–254. 

15. Niedziółka, I. Sustainable tourism development. _Reg. Form. Dev. Stud._ **2014** , _8_ , 157–166. 

16. Wee, G.F.; Ahmad, A.M.A. Cultural heritage tourism: Determinants of behavioral intention to visit a historical city from experiential perspectives. _J. Tour. Hosp. Environ. Manag._ **2021** , _6_ , 1–10. 

17. Aliannejadi, M.; Rafailidis, D.; Crestani, F. A collaborative ranking model with multiple location-based similarities for venue suggestion. In Proceedings of the 2018 ACM SIGIR International Conference on Theory of Information Retrieval, Tianjin, China, 15–18 September 2018; pp. 19–26. 

18. Aliannejadi, M.; Rafailidis, D.; Crestani, F. Personalised Keyword Boosting for Venue Suggestion Based on Multiple LBSNs. In _Lecture Notes in Computer Science_ ; Springer: Berlin/Heidelberg, Germany, 2017; pp. 291–303. 

19. Aliannejadi, M.; Mele, I.; Crestani, F. User Model Enrichment for Venue Recommendation. In Proceedings of the Asia Information Retrieval Symposium, Beijing, China, 30 November–2 December 2016; pp. 212–223. 

20. Bao, J.; Zheng, Y.; Wilkie, D.; Mokbel, M. Recommendations in location-based social networks: A survey. _Geoinformatica_ **2015** , _19_ , 525–565. [CrossRef] 

21. Deveaud, R.; Albakour, M.; Macdonald, C.; Ounis, I. Challenges in Recommending Venues within Smart Cities. In _ECIR’14 Information Access in Smart Cities Workshop (i-ASC 2014)_ ; i-ACS: Amsterdam, The Netherlands, 2014; pp. 1–2. 

22. Su, X.; Sperli, G.; Moscato, V.; Picariello, A.; Esposito, C.; Choi, C. An Edge Intelligence Empowered Recommender System Enabling Cultural Heritage Applications. _IEEE Trans. Ind. Inform._ **2019** , _15_ , 4266–4275. [CrossRef] 

23. Azazi, N.A.N.; Shaed, M.M. Social Media and Decision-Making Process among Tourist: A Systematic Review. In _Jurnal Komunikasi: Malaysian Journal of Communication_ ; Universiti Kebangsaan Malaysia Press: Bangi, Malaysia, 2020; Volume 36. 

24. Xiang, Z.; Fesenmaier, D.R. _Analytics in Smart Tourism Design_ ; Springer: Vienna, Austria, 2017. 25. Figueredo, M. From photos to travel itinerary: A tourism recommender system for smart tourism destination. In Proceedings of the 4th International Conference Big Data Computing Service and Applications, Bamberg, Germany, 26–29 March 2018; pp. 85–92. 

26. Neidhardt, J.; Werthner, H. IT and tourism: Still a hot topic, but do not forget IT. _Inf. Technol. Tour._ **2018** , _20_ , 1–7. [CrossRef] 27. Gretzel, U.; Zarezadeh, Z.; Li, Y.; Xiang, Z. The evolution of travel information search research: A perspective article. _Tour. Rev._ **2019** , _75_ , 319–323. [CrossRef] 

28. Quijano-Sánchez, L.; Cantador, I.; Cortés-Cediel, M.E.; Gil, O. Recommender systems for smart cities. _Inf. Syst._ **2020** , _92_ , 101545. [CrossRef] 

29. Braunhofer, M.; Elahi, M.; Ricci, F.; Schievenin, T. Context-Aware Points of Interest Suggestion with Dynamic Weather Data Management. In _Information and Communication Technologies in Tourism_ ; Springer: Cham, Switzerland, 2014; pp. 87–100. 

30. Aliannejadi, M.; Crestani, F. Personalised Context-Aware Point of Interest Recommendation. _ACM Trans. Inf. Ssystems_ **2018** , _36_ , 1–28. [CrossRef] 

31. Baltrunas, L.; Ludwig, B.; Peer, S.; Ricci, F. Context relevance assessment and exploitation in mobile recommender systems. _Pers. Ubiquitous Comput._ **2012** , _16_ , 507–526. [CrossRef] 

32. Dean-hall, A.; Thomas, P.; Clarke, C.L.A.; Simone, N.; Voorhees, E. Overview of the TREC 2013 Contextual Suggestion Track. In Proceedings of the TREC, Gaithersburg, MD, USA, 19–22 November 2013; pp. 1–12. 

33. Dean-hall, A.; Clarke, C.L.; Kamps, J.; Thomas, P.; Voorhees, E. Overview of the TREC 2015 Contextual Suggestion Track. In Proceedings of the TREC, Gaithersburg, MD, USA, 17–20 November 2015; pp. 1–2. 

34. Dean-Hall, A.; Clarke, C.L.A. The Power of Contextual Suggestion. In _Advances in Information Retrieval_ ; Springer: Berlin/Heidelberg, Germany, 2015; pp. 352–357. 

35. Dean-hall, A.; Clarke, C.L.A.; Thomas, P.; Voorhees, E. Overview of the TREC 2014 Contextual Suggestion Track. In Proceedings of the TREC, Gaithersburg, MD, USA, 19–21 November 2014; pp. 1–11. 

36. Kitchenham, B.; Charters, S. _Guidelines for Performing Systematic Literature Reviews in Software Engineering_ ; Elsevier: Amsterdam, The Netherlands, 2007; pp. 1–44. 

37. Rikitianskii, A.; Harvey, M.; Crestani, F. A Personalised Recommendation System for Context-Aware Suggestions. In _Advances in Information Retrieval_ ; Springer: Berlin/Heidelberg, Germany, 2014; pp. 63–74. 

38. McCreadie, R.; Mackie, S.; Manotumruksa, J. _University of Glasgow at TREC 2015: Experiments with Terrier in Contextual Suggestion, Temporal Summarisation and Dynamic Domain Tracks_ ; University of Glasgow: Glasgow, UK, 2015. 

39. Hariri, N.; Mobasher, B.; Burke, R.; Zheng, Y. Context-aware recommendation based on review mining. In _ITWP@ IJCAI_ ; ITWP@ IJCAI: Barcelona, Spain, 2011. 

40. Chen, G.; Chen, L. Recommendation based on contextual opinions. In _International Conference on User Modeling, Adaptation, and Personalization_ ; Springer: Berlin/Heidelberg, Germany, 2014; pp. 61–73. 

41. Tan, K.L.; Khan, H.U.R.; Lim, C.K. Challenges in recommending venues by using contextual suggestion track. _Int. J. Eng. Technol._ **2018** , _7_ , 207–211. 

42. Chakraborty, A. Enhanced Contextual Recommendation using Social Media Data. In Proceedings of the 41st International ACM SIGIR Conference on Research & Development in Information Retrieval, Ann Arbor, MI, USA, 8–12 July 2018; p. 1455. 

43. Crestani, F. Personalised Recommendations for Context Aware Suggestions. In _SIMBig_ ; Springer: Regensburg, Germany, 2016; pp. 19–21. 

44. Hubert, G.; Cabanac, G. _Irit at Trec 2012 Contextual Suggestion Track_ ; University of Waterloo: Waterloo, ON, Canada, 2012. 

_Sustainability_ **2021** , _13_ , 8141 

21 of 27 

45. Manotumruksa, J.; Macdonald, C.; Ounis, I. A Contextual Recurrent Collaborative Filtering framework for modelling sequences of venue checkins. _Inf. Process. Manag._ **2020** , _57_ , 102092. [CrossRef] 

46. Seyler, D.; Chandar, P.; Davis, M. An information retrieval framework for contextual suggestion based on heterogeneous information network embeddings. In Proceedings of the 41st International ACM SIGIR Conference on Research & Development in Information Retrieval, Ann Arbor, MI, USA, 8–12 July 2018; pp. 953–956. 

47. Hoffmann, H.; Addala, P.; Clarke, C.L. WaterlooClarke: TREC 2015 Contextual Suggestion Track. In Proceedings of the TREC, Gaithersburg, MD, USA, 17–20 November 2015. 

48. Ben Sassi, I.; Mellouli, S.; Ben Yahia, S. Context-aware recommender systems in mobile environment: On the road of future research. _Inf. Syst._ **2017** , _72_ , 27–61. [CrossRef] 

49. Xu, Y.; Yin, J.; Deng, S.; Xiong, N.N.; Huang, J. Context-aware QoS prediction for web service recommendation and selection. _Expert Syst. Appl._ **2016** , _53_ , 75–86. [CrossRef] 

50. Fan, X.; Hu, Y.; Li, J.; Wang, C. Context-aware ubiquitous web services recommendation based on user location update. In Proceedings of the International Conference on Cloud Computing and Big Data (CCBD), Shanghai, China, 4–6 November 2015; pp. 111–118. 

51. Aznoli, F.; Navimipour, N.J. Cloud services recommendation: Reviewing the recent advances and suggesting the future research directions. _J. Netw. Comput. Appl._ **2016** , _2017_ , 73–86. [CrossRef] 

52. Dandekar, P.; Fawaz, N.; Ioannidis, S. Privacy auctions for recommender systems. _ACM Trans. Econ. Comput. (TEAC)_ **2014** , _2_ , 1–22. [CrossRef] 

53. Ilarri, S.; Delot, T.; Trillo-Lado, R. A Data Management Perspective on Vehicular Networks. _IEEE Commun. Surv. Tutor._ **2015** , _17_ , 2420–2460. [CrossRef] 

54. Lu, J.; Wu, D.; Mao, M.; Wang, W.; Zhang, G. Recommender system application developments: A survey. _Decis. Support Syst._ **2015** , _74_ , 12–32. [CrossRef] 

55. Kzaz, L.; Dakhchoune, D.; Dahab, D. Tourism Recommender Systems: An Overview of Recommendation Approaches. _Int. J. Comput. Appl._ **2018** , _180_ , 9–13. [CrossRef] 

56. Véras, D.; Prota, T.; Bispo, A.; Prudêncio, R.; Ferraz, C. A literature review of recommender systems in the television domain. _Expert Syst. Appl._ **2015** , _42_ , 9046–9076. [CrossRef] 

57. Vahdat-Nejad, H.; Ramazani, A.; Mohammadi, T.; Mansoor, W. A survey on context-aware vehicular network applications. _Veh. Commun._ **2016** , _3_ , 43–57. [CrossRef] 

58. Schaller, R.; Harvey, M.; Elsweiler, D. _Relating User Interaction to Experience during Festivals_ ; Springer: Regensburg, Germany, 2014; pp. 38–47. 

59. Wang, J.; Zhang, Y. _SIGIR’13 Opportunity Model for E-Commerce Recommendation Right Product_ ; ACM: Dublin, Ireland, 2013; pp. 303–312. 

60. Zhang, Y.; Zhang, M.; Zhang, Y.; Lai, G.; Liu, Y.; Zhang, H.; Ma, S. _Daily-Aware Personalized Recommendation Based on Feature-Level Time Series Analysis Categories and Subject Descriptors_ ; ACM: Florence, Italy, 2015; pp. 1373–1383. 

61. Rahimiaghdam, S.; Karagoz, P.; Mutlu, A. _Personalized Time-Aware Outdoor Activity Recommendation System_ ; ACM Digital Library: Pisa, Italy, 2016; pp. 1121–1126. 

62. Colombo-Mendoza, L.O.; Valencia-García, R.; Rodríguez-González, A.; Alor-Hernández, G.; Samper-Zapater, J.J. RecomMetz: A context-aware knowledge-based mobile recommender system for movie showtimes. _Expert Syst. Appl._ **2015** , _42_ , 1202–1222. [CrossRef] 

63. De Pessemier, T.; Dooms, S.; Martens, L. Context-aware recommendations through context and activity recognition in a mobile environment. _Multimed. Tools Appl._ **2014** , _72_ , 2925–2948. [CrossRef] 

64. Lee, S.; Choi, J. Enhancing user experience with conversational agent for movie recommendation: Effects of self-disclosure and reciprocity. _Int. J. Hum. Comput. Stud._ **2017** , _103_ , 95–105. [CrossRef] 

65. Wang, X.; Rosenblum, D.; Wang, Y. Context-aware mobile music recommendation for daily activities. In Proceedings of the 20th ACM International Conference on Multimedia, Nara, Japan, 29 October–2 November 2012; p. 99. 

66. Sáez-Martín, A.; Haro-de-Rosario, A.; Caba-Perez, C. A vision of social media in the Spanish smartest cities. _Transform. Gov. People Process. Policy_ **2014** , _8_ , 521–544. [CrossRef] 

67. Albakour, M.D.; Deveaud, R.; Macdonald, C.; Ounis, I. Diversifying contextual suggestions from location-based social networks. In Proceedings of the 5th Information Interaction in Context Symposium, Regensburg, Germany, 26–30 August 2014; pp. 125–134. 

68. Narayanan, M.; Cherukuri, A.K. A study and analysis of recommendation systems for location-based social network (LBSN) with big data. _IIMB Manag. Rev._ **2016** , _28_ , 25–30. [CrossRef] 

69. Cheng, Z.; Shen, J. Just-for-me: An adaptive personalization system for location-aware social music recommendation. In Proceedings of the International Conference on Multimedia Retrieval, Glasgow, UK, 1–4 April 2014; pp. 185–192. 

70. Kumar, V.; Jarratt, D.; Anand, R.; Konstan, J.A.; Hecht, B. Where far can be close: Finding distant neighbors in recommender systems. _CEUR Workshop Proc._ **2015** , _1405_ , 13–20. 

71. Li, M.; Sagl, G.; Mburu, L.; Fan, H. A contextualized and personalized model to predict user interest using location-based social networks. _Comput. Environ. Urban Syst._ **2016** , _58_ , 97–106. [CrossRef] 

_Sustainability_ **2021** , _13_ , 8141 

22 of 27 

|72.|Liu, B.; Fu, Y.; Yao, Z.; Xiong, H. Learning geographical preferences for point-of-interest recommendation. In Proceedings of the|
|---|---|
||19th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, Chicago, IL, USA, 11–14 August 2013;|
||pp. 1043–1051.|
|73.|Massai, L.; Nesi, P.; Pantaleo, G. PAVAL: A location-aware virtual personal assistant for retrieving geolocated points of interest|
||and location-based services. _Eng. Appl. Artif. Intell._ **2019**,_77_, 70–85. [CrossRef]|
|74.|Meng, S.; Qi, L.; Li, Q.; Lin, W.; Xu, X.; Wan, S. Privacy-preserving and sparsity-aware location-based prediction method for|
||collaborative recommender systems. _Future Gener. Comput. Syst._ **2019**,_96_, 324–335. [CrossRef]|
|75.|Ren, L.; Wang, W. An SVM-based collaborative fltering approach for Top-N web services recommendation. _Future Gener. Comput._|
||_Syst._ **2018**,_78_, 531–543. [CrossRef]|
|76.|Son, J.W.; Kim, A.Y.; Park, S.B. A location-based news article recommendation with explicit localized semantic analysis. In|
||Proceedings of the 36th International ACM SIGIR Conference on Research and Development in Information Retrieval, Dublin,|
||Ireland, 28 July–1 August 2013; pp. 293–302.|
|77.|Hu, B.; Ester, M. Spatial topic modeling in online social media for location recommendation. In Proceedings of the 7th ACM|
||Conference on Recommender Systems, Hong Kong, China, 12–16 October 2013; pp. 25–32.|
|78.|Mettouris, C.; Papadopoulos, G.A. Ubiquitous recommender systems. _Computing_**2014**,_96_, 223–257. [CrossRef]|
|79.|Cheng, C.; Yang, H.; King, I.; Lyu, M. Fused Matrix Factorization with Geographical and Social Infuence in Location-Based|
||Social Networks. In Proceedings of the 26th AAAI Conference on Artifcial Intelligence, Toronto, ON, Canada, 22–26 July 2012;|
||pp. 17–23.|
|80.|Davarpour, M.H.; Sohrabi, M.K.; Naderi, M. Toward a semantic-based location tagging news feed system: Constructing a|
||conceptual hierarchy on geographical hashtags. _Comput. Electr. Eng._ **2019**,_78_, 204–217. [CrossRef]|
|81.|Dombrowski, L.; Brubaker, J.R.; Hirano, S.H.; Mazmanian, M.; Hayes, G.R. It takes a network to get dinner: Designing location-|
||based systems to address local food needs. In Proceedings of the 2013 ACM International Joint Conference on Pervasive and|
||Ubiquitous Computing, Zurich, Switzerland, 8–12 September 2013; pp. 519–528.|
|82.|Tang, X.; Wan, X.; Zhang, X. _Cross-Language Context-Aware Citation Recommendation in Scientifc Articles_; SIGIR: Gold Coast,|
||Australia, 2014; pp. 817–826.|
|83.|Aliannejadi, M.; Crestani, F. Venue appropriateness prediction for personalized context-aware venue suggestion. In Proceed-|
||ings of the 40th International ACM SIGIR Conference on Research and Development in Information Retrieval, Tokyo, Japan,|
||7–11 August 2017; pp. 1177–1180.|
|84.|Aliannejadi, M.; Mele, I.; Crestani, F. Personalized ranking for context-aware venue suggestion. In Proceedings of the Symposium|
||on Applied Computing, Marrakech, Morocco, 3–7 April 2017; pp. 960–962.|
|85.|Griesner, J.; Paristech, T.; Naacke, H. POI Recommendation: Towards Fused Matrix Factorization with Geographical and|
||Temporal Infuences. In Proceedings of the 9th ACM Conference on Recommender System, Vienna, Austria, 16–20 September|
||2015; pp. 301–304.|
|86.|Lian, D.; Zhao, C.; Xie, X.; Sun, G.; Chen, E.; Rui, Y. GeoMF: Joint geographical modeling and matrix factorization for point-of-|
||interest recommendation. In Proceedings of the 20th ACM SIGKDD International Conference on Knowledge Discovery and Data|
||Mining, New York, NY, USA, 24–27 August 2014; pp. 831–840.|
|87.|Arampatzis, A.; Kalamatianos, G. Suggesting points-of-interest via content-based, collaborative, and hybrid fusion methods in|
||mobile devices. _ACM Trans. Inf. Syst._ **2017**,_36_, 1–28. [CrossRef]|
|88.|Montanelli, S.; Castano, S.; Genta, L. Urban information integration through smart city views. _Int. J. Knowl. Learn._ **2014**,_9_, 3.|
||[CrossRef]|
|89.|Ma, H. An experimental study on implicit social recommendation. In Proceedings of the 36th International Acm Sigir Conference|
||on Research and Development in Information Retrieval, Dublin, Ireland, 28 July–1 August 2013; pp. 73–82.|
|90.|Lu, W.; Ioannidis, S.; Bhagat, S.; Lakshmanan LV, S. Optimal recommendations under attraction, aversion, and social infuence. In|
||Proceedings of the 20th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, New York, NY,|
||USA, 24–27 August 2014; pp. 811–820.|
|91.|Natarajan, S.; Vairavasundaram, S.; Natarajan, S.; Gandomi, A.H. Resolving data sparsity and cold start problem in collaborative|
||fltering recommender system using Linked Open Data. _Expert Syst. Appl._ **2020**,_149_, 113248. [CrossRef]|
|92.|Shen, Y.; Jin, R. Learning personal + social latent factor model for social recommendation. In Proceedings of the ACM SIGKDD|
||International Conference on Knowledge Discovery and Data Mining, Beijing, China, 12–16 August 2012; pp. 1303–1311.|
|93.|Cheng, Y.; Liu, J.; Yu, X. Online social trust reinforced personalized recommendation. _Pers. Ubiquitous Comput._ **2016**,_20_, 457–467.|
||[CrossRef]|
|94.|He, K.; Mu, X. Differentially private and incentive compatible recommendation system for the adoption of network goods. In|
||Proceedings of the 15th ACM Conference on Economics and Computation, Palo Alto, CA, USA, 8–12 June 2014; pp. 949–966.|
|95.|Zhu, H.; Xiong, H.; Ge, Y.; Chen, E. Mobile app recommendations with security and privacy awareness. In Proceedings of the|
||20th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, New York, NY, USA, 24–27 August|
||2014; pp. 951–960.|
|96.|Sato, T.; Fujita, M.; Kobayashi, M.; Ito, K. Recommender system by grasping individual preference and infuence from other|
||users. In Proceedings of the 2013 IEEE/ACM International Conference on Advances in Social Networks Analysis and Mining|
||(ASONAM 2013), Niagara, ON, Canada, 25–28 August 2013; pp. 1345–1351.|



_Sustainability_ **2021** , _13_ , 8141 

23 of 27 

97. Perez, C.; Birregah, B.; Lemercier, M. _Familiar Strangers Detection in Online Social Networks_ ; IEEE: Niagara Falls, ON, Canada, 2014; pp. 1175–1182. 

98. Al-Sharawneh, J.; Sinnappan, S.; Williams, M.A. Credibility-based twitter social network analysis. In _Lecture Notes in Computer Science (Including Subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)_ ; 7808 LNCS; Springer: Berlin/Heidelberg, Germany, 2013; pp. 323–331. 

99. Hong, J.; Hwang, W.S.; Kim, J.H.; Kim, S.W. Context-aware music recommendation in mobile smart devices. In Proceedings of the ACM Symposium on Applied Computing, Gyeongju, Korea, 24–28 March 2014; pp. 1463–1468. 

100. Aisopos, F.; Litke, A.; Kardara, M.; Tserpes, K.; Campo, P.M.; Varvarigou, T. Social network services for innovative smart cities: The RADICAL platform approach. _J. Smart Cities_ **2016** , _2_ , 1–15. [CrossRef] 

101. Psomakelis, E.; Aisopos, F.; Litke, A.; Tserpes, K. Big Iot and Social Networking Data for Smart Cities: Algorithmic improvements on Big Data Analysis in the context of RADICAL city applications. _arXiv_ **2015** , arXiv:1607.00509. 

102. Yao, W.; He, J.; Huang, G.; Cao, J.; Zhang, Y. A graph-based model for context-aware recommendation using implicit feedback data. _World Wide Web_ **2015** , _18_ , 1351–1371. [CrossRef] 

103. Yao, W.; He, J.; Huang, G.; Zhang, Y. SoRank: Incorporating social information into learning to rank models for recommendation. In Proceedings of the 23rd International, Seoul, Korea, 7–11 April 2014; pp. 409–410. 

104. Luberg, A.; Tammet, T.; Järv, P. Smart city: A rule-based tourist recommendation system. In _Information and Communication Technologies in Tourism_ ; Springer: Berlin/Heidelberg, Germany, 2011; pp. 51–62. 

105. Borràs, J.; Moreno, A.; Valls, A. Intelligent tourism recommender systems: A survey. _Expert Syst. Appl._ **2014** , _41_ , 7370–7389. [CrossRef] 

106. Palaiokrassas, G.D.; Charlaftis, V.; Litke, A.; Varvarigou, T. Recommendation Service for Big Data Applications in Smart Cities. In Proceedings of the International Conference on High Performance Computing & Simulation (HPCS), Genoa, Italy, 17–21 July 2017; pp. 217–223. 

107. Castellanos, Á.; Luca, E.W.; De Cigarrán, J. Time, Place and Environment: Can Conceptual Modelling Improve Context-Aware Recommendation? In Proceedings of the Fifth Workshop on Context-awareness in Recommendation and Retrieval, Vienna, Austria, 29 March–2 April 2015. 

108. Kurihara, S.; Moriyama, K.; Numao, M. Context-Aware Application Prediction and Recommendation in Mobile Devices. _Int. Jt. Conf. Web Intell. Intell. Agent Technol._ **2013** , _1_ , 494–500. 

109. Mizzaro, S.; Pavan, M.; Scagnetto, I.; Zanello, I. A context-aware retrieval system for mobile applications. In Proceedings of the ACM International Conference Proceeding Series, Montreal, QC, Canada, 3–5 August 2014; pp. 18–25. 

110. Natarajasivan, D.; Govindarajan, M. Location based context aware user interface recommendation system. In Proceedings of the ACM International Conference Proceeding Series, San Francisco, CA, USA, 26 June–1 July 2016. 

111. Nguyen, T.V.; Karatzoglou, A.; Baltrunas, L. Gaussian Process Factorization Machines for context-aware recommendations. In Proceedings of the 37th International ACM SIGIR Conference on Research and Development in Information Retrieval, Gold Coast, Australia, 6–11 July 2014; pp. 63–72. 

112. Shih, N.J.; Diao, P.H.; Chen, Y. ARTS, an AR tourism system, for the integration of 3D scanning and smartphone AR in cultural heritage tourism and pedagogy. _Sensors_ **2019** , _19_ , 3725. [CrossRef] [PubMed] 

113. Sitkrongwong, P.; Maneeroj, S.; Samatthiyadikun, P.; Takasu, A. Bayesian probabilistic model for context-aware recommendations. In Proceedings of the 17th International Conference on Information Integration and Web-Based Applications and Services, Brussels, Belgium, 11–13 December 2015. 

114. Jiménez, O.; Salamó, M.; Boratto, L. Context-aware event recommendation in event-based social networks. _Front. Artif. Intell._ **2019** , _319_ , 235–244. 

115. Amatriain, X. Big & personal: Data and models behind Netflix recommendations. In _Workshop on Big Data, Streams and Heterogeneous Source Mining: Algorithms, Systems, Programming Models and Applications_ , 2nd ed.; Kdd BigMine 19: Chicago, IL, USA, 2013; pp. 1–6. 

116. Bielik, P.; Tomlein, M.; Krátky, P.; Mitrík, Š.; Barla, M.; Bieliková, M. Move2Play: An innovative approach to encouraging people to be more physically active. In Proceedings of the 2nd ACM SIGHIT International Health Informatics Symposium, Miami, FL, USA, 28–30 January 2012; pp. 61–70. 

117. Odi´c, A.; Tkalˇciˇc, M.; Tasiˇc, J.F.; Košir, A. Relevant context in a movie recommender system: Users’ opinion vs. _Stat. Detection. CEUR Workshop Proc._ **2012** , _12_ , 889. 

118. Aizenberg, N.; Koren, Y.; Somekh, O. Build your own music recommender by modeling internet radio streams. In Proceedings of the 21st Annual Conference on World Wide Web, Lyon, France, 16–20 April 2012; pp. 1–10. 

119. Chen, C.M.; Tsai, M.F.; Liu, J.Y.; Yang, Y.H. Music recommendation based on multiple contextual similarity information. _Int. Conf. Web Intell._ **2013** , _1_ , 65–72. 

120. Nirjon, S.; Dickerson, R.F.; Li, Q.; Asare, P.; Stankovic, J.A.; Hong, D.; Zhao, F. MusicalHeart: A hearty way of listening to music. In Proceedings of the 10th ACM Conference on Embedded Networked Sensor Systems, Toronto, ON, Canada, 6–9 November 2012; pp. 43–56. 

121. Chen, T.; He, X.; Kan, M.Y. Context-aware image tweet modelling and recommendation. In Proceedings of the ACM Multimedia Conference, Amsterdam, The Netherlands, 15–19 October 2016; pp. 1018–1027. 

_Sustainability_ **2021** , _13_ , 8141 

24 of 27 

122. Lemos, F.D.A.; Carmo, R.A.F.; Viana, W.; Andrade, R.M.C. Towards a context-aware photo recommender system. In Proceedings of the CEUR Workshop Proceedings, Buffalo, NY, USA, 26–30 July 2012; p. 889. 

123. Adomavicius, G.; Jannach, D. Preface to the special issue on context-aware recommender systems. _User Modeling User-Adapt. Interact._ **2014** , _24_ , 1–5. [CrossRef] 

124. Dumitrescu, D.A.; Santini, S. Improving novelty in streaming recommendation using a context model. In Proceedings of the CEUR Workshop Proceedings, Buffalo, NY, USA, 26–30 July 2012; p. 889. 

125. He, Q.; Agu, E.; Strong, D.; Tulu, B. RecFit: A context-aware system for recommending physical activities. In Proceedings of the 1st Workshop on Mobile Medical Applications, Memphis, TN, USA, 3–6 November 2014; pp. 34–39. 

126. Lin, J.; Sugiyama, K.; Kan, M.-Y.; Chua, T.-S. New and improved: Modeling versions to improve app recommendation. In Proceedings of the 37th International ACM SIGIR Conference on Research & Development in Information Retrieval, Gold Coast, Australia, 6–11 July 2014; pp. 647–656. 

127. Livne, A.; Gokuladas, V.; Teevan, J.; Dumais, S.T.; Adar, E. CiteSight: Supporting contextual citation recommendation using differential search. In Proceedings of the 37th International ACM SIGIR Conference on Research & Development in Information Retrieval, Gold Coast, Australia, 6–11 July 2014; pp. 807–816. 

128. Zhang, W.; Wang, J.; Feng, W. Combining latent factor model with location features for event-based group recommendation. In Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, Chicago, IL, USA, 11–14 August 2013; pp. 910–918. 

129. Beer, W.; Derwein, C.; Herramhof, S. Implementation of a Map-Reduce based Context-Aware Recommendation Engine for Social Music Events. _Int. J. Adv. Intell. Syst._ **2013** , _6_ , 367–375. 

130. Beer, W.; Derwein, C.; Herramhof, S. Implementation of context-aware item recommendation through MapReduce data aggregation. In Proceedings of the ACM International Conference Proceeding Series, St. Andrews, UK, 6–9 October 2013; pp. 26–32. 

131. Oh, J.M.; Moon, N.M. User-selectable interactive recommendation system in mobile environment. _Multimed. Tools Appl._ **2012** , _57_ , 295–313. [CrossRef] 

132. Zeng, C.; Jia, D.; Wang, J.; Hong, L.; Nie, W.; Li, Z.; Tian, J. Context-aware social media recommendation based on potential group. In Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, Beijing, China, 12–16 August 2012. 

133. Paradarami, T.K.; Bastian, N.D.; Wightman, J.L. A hybrid recommender system using artificial neural networks. _Expert Syst. Appl._ **2017** , _83_ , 300–313. [CrossRef] 

134. Lim, T.Y. Designing the next generation of mobile tourism application based on situation awareness. In Proceedings of the Southeast Asian network of Ergonomics Societies Conference, Langkawi, Malaysia, 9–12 July 2012; pp. 1–7. 

135. Benfares, C.; El Idrissi YE, B.; Amine, A. Smart city: Recommendation of personalized services in patrimony tourism. In Proceedings of the 4th IEEE International Colloquium on Information Science and Technology, Tangier, Morocco, 24–26 October 2016; pp. 835–840. 

136. Bao, J.; Zheng, Y.; Mokbel, M.F. Location-based and preference-aware recommendation using sparse geo-social networking data. In Proceedings of the ACM International Symposium on Advances in Geographic Information Systems, Redondo Beach, CA, USA, 6 November 2012; pp. 199–208. 

137. Yochum, P.; Chang, L.; Gu, T.; Zhu, M.; Zhang, W. Tourist attraction recommendation based on knowledge graph. In _IFIP Advances in Information and Communication Technology_ ; Springer: Berlin/Heidelberg, Germany, 2018; p. 538. 

138. Wang, Z.; Liu, B. Tourism recommendation system based on data mining. _J. Phys. Conf. Ser._ **2019** , _1345_ , 022027. [CrossRef] 

139. Ye, J.; Xiong, Q.; Li, Q.; Gao, M.; Xu, R. Tourism Service Recommendation Based on User Influence in Social Networks and Time Series. 2019 IEEE 21st International Conference on High Performance Computing and Communications. In Proceedings of the 17th International Conference on Smart City, Zhangjiajie, China, 10–12 August 2019; pp. 1445–1451. 

140. Ricci, F.; Shapira, B.; Rokach, L. _Recommender Systems Handbook_ , 2nd ed.; Springer: Regensburg, Germany, 2015. 

141. Bothos, E.; Apostolou, D.; Mentzas, G. A recommender for persuasive messages in route planning applications. In Proceedings of the 7th International Conference on Information, Intelligence, Systems & Applications, Chalkidiki, Greece, 13–15 July 2016; pp. 1–5. 

142. Braunhofer, M.; Ricci, F. Selective contextual information acquisition in travel recommender systems. _Inf. Technol. Tour._ **2017** , _17_ , 5–29. [CrossRef] 

143. Jorro-Aragoneses, J.L.; Diaz Agudo, M.B.; Recio Garcia, J.A. Madrid live: A context-aware recomendar system of leisure plans. In Proceedings of the International Conference on Tools with Artificial Intelligence, Boston, MA, USA, 6–8 November 2018; pp. 796–801. 

144. Khallouki, H.; Abatal, A.; Bahaj, M. An ontology-based context awareness for smart tourism recommendation system. In Proceedings of the ACM International Conference Proceeding Series, Chengdu, China, 25–27 August 2018; pp. 1–5. 

145. Zou, X.; Gonzales, M.; Saeedi, S. A Context-aware Recommendation System using smartphone sensors. In Proceedings of the 7th IEEE Annual Information Technology, Electronics and Mobile Communication Conference, Vancouver, BC, Canada, 13–15 October 2016. 

146. Mrazovic, P.; Larriba-Pey, J.L.; Matskin, M. Improving Mobility in Smart Cities with Intelligent Tourist Trip Planning. In Proceedings of the International Computer Software and Applications Conference, Turin, Italy, 4–8 July 2017; Volume 1, pp. 897–907. 

_Sustainability_ **2021** , _13_ , 8141 

25 of 27 

147. Cha, S.; Ruiz, M.P.; Wachowicz, M.; Tran, L.H.; Cao, H.; Maduako, I. The role of an IoT platform in the design of real-time recommender systems. In Proceedings of the 3rd World Forum on Internet of Things, Reston, VA, USA, 12–14 December 2017; pp. 448–453. 

148. Meehan, K.; Lunney, T.; Curran, K.; McCaughey, A. Context-aware intelligent recommendation system for tourism. In Proceedings of the International Conference on Pervasive Computing and Communications Workshops, San Diego, CA, USA, 18–22 March 2013; pp. 328–331. 

149. Smirnov, A.; Kashevnik, A.; Ponomarev, A.; Teslya, N.; Shchekotov, M.; Balandin, S.I. Smart Space-Based Tourist Recommendation System. In _Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)_ ; Springer: Berlin/Heidelberg, Germany, 2014; Volume 8638, pp. 40–51. 

150. Yoon, H.; Zheng, Y.; Xie, X.; Woo, W. Social itinerary recommendation from user-generated digital trails. _Pers. Ubiquitous Comput._ **2012** , _16_ , 469–484. [CrossRef] 

151. Feng, W.L.; Duan, Y.C.; Huang, M.X.; Dong, L.F.; Zhou, X.Y.; Hu, T. A Research on Smart Tourism Service Mechanism Based on Context Awareness. _Appl. Mech. Mater._ **2014** , _519–520_ , 752–758. [CrossRef] 

152. Tarantino, E.; Falco, D.I.; Scafuri, U. A mobile personalised tourist guide and its tourist evaluation. _Inf. Technol. Tour._ **2019** , _21_ , 413–455. [CrossRef] 

153. Wang, D.; Li, X.; Li, Y. China’s “smart tourism destination” initiative: A taste of the service-dominant logic. _J. Destin. Mark. Manag._ **2013** , _2_ , 59–61. [CrossRef] 

154. Alnogaithan, O.; Algazlan, S.; Aljuraiban, A.; Shargabi, A.A. Tourism Recommendation System Based on User Reviews. In Proceedings of the International Conference on Innovation and Intelligence for Informatics, Computing, and Technologies, Sakhier, Bahrain, 22–23 September 2019; Volume 1345, pp. 1–5. 

155. Santos, F.; Almeida, A.; Martins, C.; Oliveira, P.; Gonçalves, R. Tourism recommendation system based in user functionality and points-of-interest accessibility levels. _Adv. Intell. Syst. Comput._ **2017** , _537_ , 275–284. 

156. Zhang, Y.; Song, B.; Zhang, P. Social behavior study under pervasive social networking based on decentralized deep reinforcement learning. _J. Netw. Comput. Appl._ **2017** , _86_ , 72–81. [CrossRef] 

157. Tang, J.; Gao, H.; Hu, X.; Liu, H. Context-aware review helpfulness rating prediction. In Proceedings of the 7th ACM Conference on Recommender Systems, Hong Kong, China, 12–16 October 2013; pp. 1–8. 

158. Yavari, A. Contextualised Service Delivery in the Internet of Things. 2016, 1–6. Available online: papers3://publication/uuid/55 AE999C-48FA-45BC-A4EE-66EC033C1623 (accessed on 23 November 2020). 

159. Horowitz, D.; Contreras, D.; Salamó, M. EventAware: A mobile recommender system for events. _Pattern Recognit. Lett._ **2018** , _105_ , 121–134. [CrossRef] 

160. Hartanto, M.; Utama, D.N. Intelligent decision support model for recommending restaurant. _Cogent Eng._ **2020** , _7_ , 1763888. [CrossRef] 

161. Barile, F.; Calandra, D.M.; Caso, A.; Dauria, D.; Di Mauro, D.; Cutugno, F.; Rossi, S. ICT solutions for the OR.C.HE.S.T.R.A. project: From personalized selection to enhanced fruition of cultural heritage data. In Proceedings of the 10th International Conference on Signal-Image Technology and Internet-Based Systems, Marrakech, Morocco, 23–27 November 2014; pp. 501–507. 

162. Nguyen, T.T.; Camacho, D.; Jung, J.E. Identifying and ranking cultural heritage resources on geotagged social media for smart cultural tourism services. _Pers. Ubiquitous Comput._ **2017** , _21_ , 267–279. [CrossRef] 

163. Amorim, M.; Mar, A.; Monteiro, F.; Sylaiou, S.; Pereira, P.; Martins, J. Smart Tourism Routes Based on Real Time Data and Evolutionary Algorithms. In _Lecture Notes in Computer Science (Including Subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics)_ ; Springer: Berlin/Heidelberg, Germany, 2018; pp. 417–426. 

164. Su, H.; Zheng, K.; Huang, J.; Jeung, H.; Chen, L.; Zhou, X. CrowdPlanner: A crowd-based route recommendation system. In Proceedings of the International Conference on Data Engineering, Chicago, IL, USA, 31 March–4 April 2014; Volume 1, pp. 1144–1155. 

165. Cena, F.; Likavec, S.; Lombardi, I.; Picardi, C. Should i Stay or Should i Go? Improving Event Recommendation in the Social Web. _Interact. Comput._ **2016** , _28_ , 55–72. [CrossRef] 

166. Zanda, A.; Eibe, S.; Menasalvas, E. SOMAR: A social mobile activity recommender. _Expert Syst. Appl._ **2012** , _39_ , 8423–8429. [CrossRef] 

167. Bianchini, D.; Antonellis, D.V.; Franceschi, D.N.; Melchiori, M. PREFer: A prescription-based food recommender system. _Comput. Stand. Interfaces_ **2017** , _54_ , 64–75. [CrossRef] 

168. Pticek, M.; Podobnik, V.; Jezic, G. Beyond the Internet of Things: The Social Networking of Machines. _Int. J. Distrib. Sens. Netw._ **2016** , _12_ , 8178417. [CrossRef] 

169. Assem, H.; Buda, T.S.; O’sullivan, D. RCMC: Recognizing Crowd-Mobility Patterns in Cities Based on Location Based Social Network Data. _ACM Trans. Intell. Syst. Technol._ **2017** , _8_ , 1–30. [CrossRef] 

170. Badawi, H.F.; Dong, H.; El Saddik, A. Mobile cloud-based physical activity advisory system using biofeedback sensors. _Future Gener. Comput. Syst._ **2017** , _66_ , 59–70. [CrossRef] 

171. Badii, C.; Bellini, P.; Cenni, D.; Difino, A.; Nesi, P.; Paolucci, M. Analysis and assessment of a knowledge based smart city architecture providing service APIs. _Future Gener. Comput. Syst._ **2017** , _75_ , 14–29. [CrossRef] 

172. Lozano-Oyola, M.; Blancas, F.J.; González, M.; Caballero, R. Sustainable tourism tags to reward destination management. _J. Environ. Manag._ **2019** , _250_ , 109458. [CrossRef] 

_Sustainability_ **2021** , _13_ , 8141 

26 of 27 

173. Sawchuk, A.A. Motion Primitive-Based Human Activity Recognition Using a Bag-of-Features Approach Categories and Subject Descriptors. In _Proceedings of the 2nd ACM SIGHIT International Health Informatics Symposium_ ; ACM Digital Library: New York, NY, USA, 2013; Volume 10, pp. 631–640. 

174. Tang, L.; Zou, Q.; Zhang, X.; Ren, C.; Li, Q. Spatio-Temporal Behavior Analysis and Pheromone-Based Fusion Model for Big Trace Data. _ISPRS Int. J. Geo-Inf._ **2017** , _6_ , 151. [CrossRef] 

175. Okada, K.; Karlsson, B.F.; Sardinha, L.; Noleto, T. ContextPlayer: Learning contextual music preferences for situational recommendations. In _SIGGRAPH Asia 2013 Symposium on Mobile Graphics and Interactive Applications_ ; SIGGRAPH: New York, NY, USA, 2013. 

176. Katsumi, H.; Yamada, W.; Ochiai, K. Generic POI Recommendation. In _Adjunct Proceedings of the 2020 ACM International Joint Conference on Pervasive and Ubiquitous Computing and Proceedings of the 2020 ACM International Symposium on Wearable Computers_ ; ACM: Mexico City, Mexico, 2020; pp. 46–49. 

177. Garcia, E.S.; O’Mahony, M.P.; Smyth, B. On the real-time web as a source of recommendation knowledge. In Proceedings of the Fourth ACM Conference on Recommender Systems, Barcelona, Spain, 26–30 September 2010; pp. 305–308. 

178. Chen, L.; Chen, G.; Wang, F. Recommender systems based on tourist reviews: The state of the art. _User Modeling Adapt. Pers._ **2015** , _25_ , 99–154. [CrossRef] 

179. Yang, P.; Fang, H. Combining Opinion Profile Modeling with Complex Context Filtering for Contextual Suggestion. In Proceedings of the 24th Text REtrieval Conference, Gaithersburg, MD, USA, 17–20 November 2015; pp. 1–4. 

180. Angelidou, M. Smart city policies: A spatial approach. _Cities_ **2014** , _41_ , S3–S11. [CrossRef] 

181. Handte, M.; Foell, S.; Wagner, S.; Kortuem, G.; Marrón, P.J. An internet-of-things enabled connected navigation system for urban bus riders. _IEEE J. Internet Things_ **2016** , _3_ , 735–744. [CrossRef] 

182. Zhang, J.D.; Chow, C.Y. Geosoca: Exploiting geographical, social and categorical correlations for point-of-interest recommendations. In Proceedings of the 38th International ACM SIGIR Conference on Research and Development in Information Retrieval, Santiago, Chile, 9–13 August 2015; pp. 443–452. 

183. Bi, X.; Jin, W. An improved collaborative filtering similarity model based on neural networks. In Proceedings of the 2015 International Conference on Intelligent Transportation, Big Data and Smart City, Santiago, Chile, 9–13 August 2015; pp. 85–89. 

184. Yang, Z.; Chen, W.; Huang, J. Enhancing recommendation on extremely sparse data with blocks-coupled non-negative matrix factorization. _Neurocomputing_ **2018** , _278_ , 126–133. [CrossRef] 

185. Hashemi, S.H.; Kamps, J. On the Reusability of Personalized Test Collections. In Proceedings of the Adjunct Publication of the 25th Conference on User Modeling, Adaptation and Personalization, Bratislava, Slovakia, 9–12 July 2017; pp. 185–189. 

186. Brandt, T.; Bendler, J.; Neumann, D. Social media analytics and value creation in urban smart tourism ecosystems. _Inf. Manag._ **2017** , _54_ , 703–713. [CrossRef] 

187. Raza, S.; Ding, C. Progress in context-aware recommender systems—An overview. _Comput. Sci. Rev._ **2019** , _31_ , 84–97. [CrossRef] 

188. Yuan, Q.; Cong, G.; Ma, Z.; Sun, A.; Thalmann, N.M. Time-aware point-of-interest recommendation. In Proceedings of the 36th International ACM SIGIR Conference on Research and Development in Information Retrieval, Dublin, Ireland, 28 July–1 August 2013; pp. 363–372. 

189. Yuan, H.; Xu, H.; Qian, Y.; Li, Y. Make your travel smarter: Summarizing urban tourism information from massive blog data. _Int. J. Inf. Manag._ **2016** , _36_ , 1306–1319. [CrossRef] 

190. Benkaddour, F.Z.; Taghezout, N.; Kaddour-Ahmed, F.Z.; Hammadi, I.A. An Adapted Approach for User Profiling in a Recommendation System: Application to Industrial Diagnosis. _Int. J. Interact. Multimed. Artif. Intell._ **2018** , _5_ , 118–130. [CrossRef] 

191. Ayata, D.; Yaslan, Y.; Kamasak, M.E. Emotion based music recommendation system using wearable physiological sensors. _IEEE Trans. Consum. Electron._ **2018** , _64_ , 196–203. [CrossRef] 

192. Lim, K.H.; Chan, J.; Karunasekera, S.; Leckie, C. Personalized itinerary recommendation with queuing time awareness. In Proceedings of the 40th International ACM SIGIR Conference on Research and Development in Information Retrieval, Tokyo, Japan, 7–11 August 2017; pp. 325–334. 

193. Huang, C.D.; Goo, J.; Nam, K.; Yoo, C.W. Smart tourism technologies in travel planning: The role of exploration and exploitation. _Inf. Manag._ **2017** , _54_ , 757–770. [CrossRef] 

194. Al-Hassan, M.; Lu, H.; Lu, J. A semantic enhanced hybrid recommendation approach: A case study of e-Government tourism service recommendation system. _Decis. Support Syst._ **2015** , _72_ , 97–109. [CrossRef] 

195. Deebak, B.D.; Al-Turjman, F. A novel community-based trust aware recommender systems for big data cloud service networks. _Sustain. Cities Soc._ **2020** , _61_ , 102274. [CrossRef] 

196. Botangen, K.A.; Yu, J.; Sheng, Q.Z.; Han, Y.; Yongchareon, S. Geographic-aware collaborative filtering for web service recommendation. _Expert Syst. Appl._ **2020** , _151_ , 113347. [CrossRef] 

197. Su, K.; Xiao, B.; Liu, B.; Zhang, H.; Zhang, Z. TAP: A personalized trust-aware QoS prediction approach for web service recommendation. _Knowl. Based Syst._ **2017** , _115_ , 55–65. [CrossRef] 

198. Roy, A.; Banerjee, S.; Sarkar, M.; Darwish, A.; Elhoseny, M.; Hassanien, A.E. Exploring New Vista of intelligent collaborative filtering: A restaurant recommendation paradigm. _J. Comput. Sci._ **2018** , _27_ , 168–182. [CrossRef] 

199. Zhang, C.; Zhang, H.; Wang, J. Personalized restaurant recommendation method combining group correlations and customer preferences. _Inf. Sci._ **2018** , _454_ , 128–143. [CrossRef] 

_Sustainability_ **2021** , _13_ , 8141 

27 of 27 

200. Wang, X.; Li, X.R.; Zhen, F.; Zhang, J. How smart is your tourist attraction?: Measuring tourist preferences of smart tourism attractions via a FCEM-AHP and IPA approach. _Tour. Manag._ **2016** , _54_ , 309–320. [CrossRef] 

201. Gretzel, U.; Sigala, M.; Xiang, Z.; Koo, C. Smart tourism: Foundations and developments. _Electron. Mark._ **2015** , _25_ , 179–188. [CrossRef] 

202. Pashaei, J.B.; Yousefi, S.; Masoumi, B. Efficient service recommendation using ensemble learning in the internet of things (IoT). _J. Ambient. Intell. Humaniz. Comput._ **2020** , _11_ , 1339–1350. [CrossRef] 

203. Hashemi, S.H.; Kamps, J. Where to go next? Exploiting behavioral user models in smart environments. In Proceedings of the 25th Conference on User Modeling, Adaptation and Personalization, Bratislava, Slovakia, 9–12 July 2017; pp. 50–58. 

204. Ye, B.H.; Ye, H.; Law, R. Systematic review of smart tourism research. _Sustainability_ **2020** , _12_ , 3401. [CrossRef] 

205. United Nations World Tourism Organization & United Nations Development Programme. _Tourism and the Sustainable Development Goals—Journey to 2030_ ; UNWTO: Madrid, Spain, 2017. 

206. Hall, C.M. Constructing sustainable tourism development: The 2030 agenda and the managerial ecology of sustainable tourism. _J. Sustain. Tour._ **2019** , _27_ , 1044–1060. [CrossRef] 

207. Rasoolimanesh, S.M.; Ramakrishna, S.; Hall, C.M.; Esfandiar, K.; Seyfi, S. A systematic scoping review of sustainable tourism indicators in relation to the sustainable development goals. _J. Sustain. Tour._ **2020** , 1–21. [CrossRef] 

208. Weaver, D.B. _Sustainable Tourism_ ; Edward Elgar Publishing: Cheltenham, UK, 2006. 

209. Roly, M.R.; Siwar, C.; Ismail, S.M.; Salleh NH, M. Exploring the indicators for environmental protection in the context of green tourism. _Adv. Sci. Lett._ **2015** , _21_ , 1786–1790. [CrossRef] 

210. Jusoh, A.; Sauman, S.; Yunu, S.; Nayan, N.; Ramli, Z. Archaeotourism and its Attractiveness in the Context of Heritage Tourism in Malaysia. _Int. J. Acad. Res. Bus. Soc. Sci._ **2017** , _7_ , 1162–1174. [CrossRef] 

211. Azlan, A.; Kadaruddin, A.; Nor, A.I. Systematic review on ecosystem services (ES) of ecotourism in South-East Asia (ASEAN). _Probl. Ekorozw._ **2021** , _16_ , 113–122. 

212. Fesenmaier, D.R.; Xiang, Z. (Eds.) _Design Science in Tourism: Foundations of Destination Management_ ; Springer: Berlin/Heidelberg, Germany, 2016. 

