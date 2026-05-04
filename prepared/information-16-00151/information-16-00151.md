
![](prepared/information-16-00151/images/information-16-00151.pdf-0001-00.png)


## _Review_ 

## **Popularity Bias in Recommender Systems: The Search for Fairness in the Long Tail** 

**Filippo Carnovalini[1,†] , Antonio Rodà[2,] *[,†] and Geraint A. Wiggins[1,3]** 

- 1 Computational Creativity Lab, Artificial Intelligence Research Group, Vrije Universiteit Brussel, Pleinlaan 2, 1050 Brussels, Belgium; geraint@ai.vub.ac.be (G.A.W.) 

- 2 Department of Information Engineering, University of Padova, Via Gradenigo 6a, 35131 Padova, Italy 

- 3 Cognitive Science Research Group, School of Electronic Engineering and Computer Science, Queen Mary University of London, Mile End Road, London E1 4NS, UK 

- Correspondence: antonio.roda@unipd.it; Tel.: +39-049-827-7581 

- These authors contributed equally to this work. 

**Abstract:** The importance of recommender systems has grown in recent years, as these systems are becoming one of the primary ways in which we access content on the Internet. Along with their use, concerns about the fairness of the recommendations they propose have rightfully risen. Recommender systems are known to be affected by popularity bias, the disproportionate preference towards popular items. While this bias stems from human tendencies, algorithms used in recommender systems can amplify it, resulting in unfair treatment of end-users and/or content creators. This article proposes a narrative review of the relevant literature to characterize and understand this phenomenon, both in human and algorithmic terms. The analysis of the literature highlighted the main themes and underscored the need for a multi-disciplinary approach that examines the interplay between human cognition, algorithms, and socio-economic factors. In particular, the article discusses how the overall fairness of recommender systems is impacted by popularity bias. We then describe the approaches that have been used to mitigate the harmful effects of this bias and discuss their effectiveness in addressing the issue, finding that some of the current approaches fail to face the problem in its entirety. Finally, we identify some open problems and research opportunities to help the advancement of research in the fairness of recommender systems. 

Academic Editor: Wei Zhang 

Received: 1 December 2024 Revised: 6 February 2025 Accepted: 14 February 2025 Published: 19 February 2025 

**Citation:** Carnovalini, F.; Rodà, A.; Wiggins, G.A. Popularity Bias in Recommender Systems: The Search for Fairness in the Long Tail. _Information_ **2025** , _16_ , 151. https://doi.org/ 10.3390/info16020151 

**Copyright:** © 2025 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https://creativecommons.org/ licenses/by/4.0/). 

**Keywords:** diversity; fairness; popularity bias; recommender systems; serendipity 

## **1. Introduction** 

Recommender systems have become pervasive in everyday life, and they shape the way we interact with the Internet. Social networks employ personalized recommendations to suggest posts and articles, on-demand entertainment websites suggest movies, songs, and other pieces of media that we might like based on our past preferences, and e-commerce websites leverage recommendations as a marketing tool [1]. In a world where a virtually infinite amount of information is at our disposal, personalized recommendations are the only tool that make it possible to explore these data in a meaningful manner, allowing us to find what we did not even know we were searching for. 

The societal need for a guide in this vast sea of information has pushed technological innovators to design recommender systems, but technology can shape a society just as much as a society can direct technology [2]. Artificial intelligence has posed novel ethical questions about the biases that affect human cognition, and that can be negatively impacted 

_Information_ **2025** , _16_ , 151 

https://doi.org/10.3390/info16020151 

_Information_ **2025** , _16_ , 151 

2 of 26 

by the use of intelligent computing systems [3,4]. Since recommender systems are becoming more and more influential in the way that we obtain and interact with new information, it is of paramount importance to ensure that potential biases that can arise from the use of these systems are known and, if possible, mitigated. 

Popularity bias, the disproportionate preference for popular items, is one such bias that is known to affect both humans and algorithms [5,6]. In the case of recommender systems, popularity bias can mean that users are more likely to be exposed to popular items, worsening the pre-existing human behavioral bias. Researchers, software developers, and other recommendation platform stakeholders need to be aware of this fact and address this limit of recommender systems that can negatively impact the user experience in the long term, as well as being harmful to some of the users involved. This bias is strongly related to other problems of recommender systems that leverage collaborative filtering algorithms. These algorithms are based on a matrix of ratings, saving how users evaluate the items they encounter. However, this matrix is generally extremely sparse, with more than 95% of user–item associations left empty [7,8]. The sparse distribution is also not uniform: there are few popular items that have many ratings and many items that have little to no ratings. We will refer to the set of these non-popular items as the long tail due to the shape of its distribution [9]. 

In this article, we wish to offer a survey on popularity bias, detailing how it can come into play in recommender systems and how it can affect their fairness towards different categories of users. Our goal is not to provide another systematic review of recent algorithms aimed at this issue (several systematic reviews have been published in recent years [10–14]) but rather a literature-informed, in-depth discussion on the topic, attempting to understand the nature of this bias and its roots in human behavior, which makes it harder to address it in computational contexts. Similarly, we will exemplify approaches that have been used to address the problem, critically discuss their adequacy to mitigate this bias, and try to provide tools and suggestions to those who face this issue in their systems. 

## _1.1. Research Questions_ 

The present article attempts to describe popularity bias, especially in the context of recommender systems, to understand how it can affect the fairness of these systems and what has been conducted in the research to address these issues. The literature review, as well as the structure of this paper, was driven by the following two research questions: 

- **RQ1** How does popularity bias affect the functioning and fairness of recommender systems towards users and stakeholders? 

- **RQ2** What can be carried out to mitigate the effects of popularity bias and showcase more of the long tail in recommendations? 

## _1.2. Methodology_ 

The present article attempts to survey the literature to identify insights and help answer the above questions. Given the broad nature of the above questions, we chose to perform a narrative review, as opposed to the growingly popular systematic review approach [15]. This means that we followed an iterative process to expand on the body of knowledge necessary for the writing of this review. Starting from some seed papers [1,16–19], we started taking notes on all relevant information related to our research questions. By considering both the papers that were cited in the seed papers and those that were later cited those papers, we expanded our pool of articles, further expanding it by directly considering search engine keywords related to aspects that we considered under-documented in seed papers. Once we reached a level of coverage of the literature that we considered sufficient to form a meaningful narration of the topic, we stopped adding sources and organized them per theme, leading to a 

_Information_ **2025** , _16_ , 151 

3 of 26 

general description of the themes we considered important to address the research questions (see Table 1). 

**Table 1.** Main topics identified in the literature on popularity bias in recommender systems. 

|**Main Topic**|**Subtopic/Method**|**References**|
|---|---|---|
|Human Popularity Bias|psychological heuristic|[20–22]|
||herd behavior|[5,23–27]|
||mere exposure effect|[28,29]|
||powerfulpersuasion mechanism|[30–36]|
|Algorithmic Popularity Bias|ranking|[37–39]|
||collaborative fltering|[9,40,41]|
||benign or harmfulpopularitybias|[42–46]|
|Fairness|related to objects/items to be<br>recommended|[16,44,45,47–51]|
||related to subjects/users that receive<br>the recommendation|[18,49,52–58]|
||related to news/contents of the<br>recommendation|[59–62]|
|Metrics|intra-list diversity|[63]|
||novelty|[64]|
||aggregate diversity|[65]|
||coverage|[66–69]|
||Gini index|[70]|
||Shannon entropy|[71]|
||serendipity|[72–75]|
||conformity|[44]|
||popularity-stratifed recall|[76]|
|Mitigation Algorithms|re-ranking|[77–81]|
||random approach|[64]|
||K-furthest neighbors|[82]|
||relatedness approach|[83]|
||transposed recommendation matrix|[84]|
||item clustering approach|[85]|
||content-based|[86]|
||innovators-based approach|[87,88]|
||NN-based approach|[89,90]|
||DL-based approach|[91]|
||graph-based approach|[75]|
||tags-based approach|[92]|
||emotional analysis|[93]|
||TIDE (TIme-Aware DisEntagled<br>Framework)|[44]|
||causal inference graph|[94]|



The three main sections of the paper reflect the main themes that were identified: the definition of popularity bias, fairness in recommender systems, and practical approaches to address popularity bias in recommender systems. The article is thus structured as follows: 

- Section 2 will review definitions of the concept of popularity bias, a term which can be used for human behavior as well as for the characteristics of algorithms. We will describe the process of attempting to understand how the two aspects are related, describing how this problem affects recommender systems specifically. 

- Section 3 will dive deeper into how the fairness of recommender systems is affected by this bias in order to answer RQ1. Since recommender systems have multiple 

_Information_ **2025** , _16_ , 151 

4 of 26 

stakeholders and can be used for a variety of applications, we will review how fairness is impacted from multiple viewpoints. 

- Section 4 mostly concerns answering RQ2 by reviewing the methods that are proposed in the literature to expose more of the long tail to users, grouping these algorithms by their general approaches and describing useful metrics to evaluate the effectiveness of these algorithms. Some additional considerations on the open challenges related to these approaches will be included in this section. 

- Sections 5 and 6 summarize the findings of this article, comment on the state of the art, and provide suggestions for future research directions. 

## **2. Understanding Popularity Bias** 

Before directly trying to answer the research questions, we understood from the literature that a unified view of what constitutes popularity bias and its roots in human behavior is often not adequately discussed. The concept of popularity bias is indeed multi-faceted and predates recommender systems. While this article focuses specifically on these algorithms, it is useful to showcase definitions that are related to other fields as well, including both human behavior and other artificial intelligence systems. 

## _2.1. Human Popularity Bias_ 

When making decisions, people tend to look at what other people are choosing. This behavior is part of the natural process of social learning that is observed in humans and other animal species, which allows us to quickly acquire knowledge without the need for first-person experience. The advanced use of social learning in humans has enabled our species to achieve great cultural progress [95] despite the fact that biases can hinder this process [20]. 

However, this mechanism leads to making decisions based on heuristic principles rather than considering all available information. In particular, when numeric and statistical data are involved, research shows that people often make decisions based on simplified processes that lead to the introduction of errors [21,22]. When social information is available, these simplified processes often involve doing what other people are doing instead of directly using the available information to make choices. This kind of behavior is known as “herd behavior” [5], and it has especially been studied within the context of financial markets [23–25]. This behavior is motivated by the belief that if many people are choosing differently from what one would do based on the information available to them, they assume that other people must have access to better information and thus disregard the choice they would make on their own. 

Along with other biases that can influence people towards preferring items that are frequently chosen, such as peer pressure [27] or the mere exposure effect [28,29] and other social phenomena, such as the institutional role of the persons making the decisions [26], herd behavior leads to the emergence of what we will call here “Human Popularity Bias”, to distinguish it from the algorithmic biases we will discuss later. In short, this bias leads people to believe that a popular item must have intrinsically higher quality because of its popularity. 

For these reasons, it is frequently observed that popular goods are preferred over non-popular ones. People prefer to buy best-seller books [30], download apps with high download counts on digital markets [31], buy more popular video games [32], and participate in online auctions that have more bids [33]. This is a powerful persuasion mechanism for marketers [34,35], who will often explicitly advertise the popularity of the goods they are selling [36]. 

_Information_ **2025** , _16_ , 151 

5 of 26 

It must be noted that the mere heuristic of choosing popular items is not necessarily negative in itself, as high popularity is generally correlated with high quality (we already noted before how this social learning heuristic is favored by the human species). However, this is not always the case [96]. Because of human popularity bias, people often ignore other aspects that can influence the popularity and success of items that are not directly related to quality [97] and, more importantly, assign a disproportionate assessment of quality to popular items. For example, Powell et al. [98] studied the preference toward popular items in the context of e-commerce. In such a context, it has become common to allow users to leave ratings for items they bought on a scale from one through five. Users who wish to buy an item can see the average rating and the amount of users who rated the item. When choosing between an item that received few ratings and one that received many ratings, participants preferred items with more reviews, even if those reviews would indicate more certainty of low quality. A subsequent study that replicated this setting shows that sometimes, even if the more-rated product has a lower rating, it can be preferred [99]. 

In the rest of this article, we will focus on algorithmic biases rather than the human ones described here, but it is necessary to keep in mind the existence of these human behaviors when discussing their computational counterparts, as human popularity bias can influence how we design algorithms and evaluate their outcomes. Moreover, noting that the preference for popular items can be an effective heuristic for humans already gives us an insight into why algorithms that show popularity bias could become as successful as they are now. 

## _2.2. Algorithmic Popularity Bias_ 

Human popularity bias can influence how we perceive quality and how we make decisions based on social context rather than intrinsic information. Computational systems do not suffer from such implicit biases and have the potential to make decisions that do not depend on any extrinsic aspect. However, it is also possible for algorithms to incorporate biases, either because these are explicitly implemented [37,38] or because these arise from the interaction with biased data, for example, by learning from human-made decisions that incorporate biases [39]. 

When it comes to popularity bias, it can be the case that it is deliberately implemented in a system since, as already mentioned in the previous section, it is a known marketing and persuasion tool. For this reason, information retrieval systems might explicitly favor popular items by highlighting them or by giving them the first position in the results ranking. For example, Amazon adds a badge on best seller items on any search results page, or academic search engines, such as Google Scholar, rank results by the number of citations by default, which can be seen as a proxy for the popularity of the research items. Despite the fact that these practices disproportionately favor popular items, the final choice is left to the (human) user of the system, thus making this a case of human popularity bias, although they are encouraged by the way the system is built. As such, it is not different from a bookstore having a shelf for best-selling books or a website showcasing best-selling products on the homepage: these systems leverage human behavior, but their algorithms do not directly suffer from popularity bias. 

Instead, we suggest that it would be more appropriate to label a system as suffering from algorithmic popularity bias only when it must make an automated decision and choose between two items, choosing the most popular one when all the other features are equal. Given this definition, popularity bias can derive from unbalanced datasets: when a certain category is overrepresented in a dataset, a decision algorithm that was trained on that dataset without correcting for over-representation will favor the prediction of that category [42,43]. However, there are more subtle ways in which algorithms can lead to 

_Information_ **2025** , _16_ , 151 

6 of 26 

popularity bias. Recommender systems, in particular, are known to be strongly affected by algorithmic popularity bias [17]. 

This derives from the popularity of collaborative filtering algorithms within recommender systems [40]. These algorithms are based on suggesting items that are likely to be of interest to a certain user based on the similarity between items and the similarity between users. In this context, similarity is often computed based on the preference matrix of the system, a data structure that encodes how each user rated each item and if the user did rate that item. When explicit ratings from users are not available, we can use as proxy any data available to the system that indicates that the user appreciates the item, such as clicks or interaction time (but we will refer to both explicit and implicit data as “ratings” in the rest of the paper). Because of the large number of available items, each user will have provided (explicitly or implicitly) no rating whatsoever for most of the items. The opposite is also true: most items will not be rated by any user except for those items that are particularly popular. This phenomenon is known as the long tail [9] because, for any of these systems, there will be a small number of items that have many ratings and a large number of items that have very few ratings. However, since only items with ratings can be effectively recommended, the most basic forms of collaborative filtering fail to suggest items that have only a few ratings and, therefore, disproportionately favor items that are already popular. Cañamares and Castellis [41] provide a more precise mathematical formulation of this intuitive process. 

As already mentioned for human popularity bias, it holds true that some degree of algorithmic popularity bias can be expected and even be beneficial, as popular items can become popular because of their quality [44]. However, an excessive degree of algorithmic popularity bias does not always favor quality [45] and can be detrimental to the overall user appreciation of the system [46]. 

The discussion so far has described algorithmic popularity bias as a limit of a computational system hindering its robustness in making appropriate decisions. However, this fundamental bias is also linked to a variety of fairness shortcomings that we will describe in the next section. 

## **3. Fairness Perspectives** 

This section addresses our first research question: “How does popularity bias affect the functioning and fairness of recommender systems towards users and stakeholders ?” 

Fairness, or the lack thereof, is a widely studied phenomenon in AI and recommender systems, and it would be impossible to cover the entirety of the related literature in one paper. Here, we focus more specifically on the fairness aspects that are related to and/or impacted by the imbalance between popular and non-popular recommendations. We will, however, need to describe some general aspects of fairness to be able to discuss it. In particular, it is necessary to understand that recommender systems are always, by definition, multi-sided markets and thus involve different stakeholders that can be affected by the fairness of the systems in a variety of ways [16]. While some systems require more detailed descriptions, in general, recommender systems involve _subjects_ and _objects_ , where the subjects are the users of the system that receive recommendations, and objects are the items that are recommended to them. When dealing with the concept of fairness, we are primarily interested in being fair towards humans; therefore, one might think that subjects will be the main focus of this discussion. On the contrary, despite what the terminology suggests, objects can be humans (or at least their profile/account) or can be directly connected to humans. For example, in a music streaming service, the objects would be the songs that can be recommended by the system, but these are directly linked to the artists who wrote, performed, and/or produced those songs. For these artists, being or not 

_Information_ **2025** , _16_ , 151 

7 of 26 

being recommended by the system can imply economic (dis)advantages, thus becoming the ground for potential unfairness. Despite the limits of this nomenclature, we will use the terms subjects and objects to describe these two viewpoints in the following discussion, as these are the terms that are most used in literature. 

## _3.1. Popularity and Fairness for Objects_ 

Fairness is, by definition, the application of equal treatment to persons who differ only because of protected demographic characteristics [100]. In the context of recommender systems, the treatment is the recommendation itself. More precisely, if we consider the perspective of the items that can be recommended, the treatment is represented by the system’s decision to recommend or not recommend the item to the users of the system. These items can represent persons either directly (for example, in a recruiting system [101]) or indirectly if we consider the owners/authors of recommended objects and media. However, recommender systems are designed around the subjects: recommendations are geared towards them and are optimized to increase the likelihood that the subject will appreciate the suggested items. 

As already largely discussed above, this makes it so that popular items are far more likely to be recommended to users when compared with less popular items. While this is partially justified by the high quality that makes those items popular in the first place [44], it is also true that this bias can obfuscate the quality of less popular items that cannot emerge [45]. 

To further characterize the influence of popularity bias on the objects of recommender systems, it is useful to consider the concept of calibration. Calibration is used as a tool to evaluate the fairness of the recommender system by describing the characteristics of a user’s interaction history and comparing it with the recommendations they receive. This is usually used to describe unfairness towards subjects, but the two-sided nature of this method can provide us with information about the objects as well. An interesting finding by Abdollahpouri et al. [47] is that non-popular items are less likely to be suggested even to those users who are mostly interested in niche items and genres. 

From the perspective of fairness, which we introduced as being based on demographic characteristics, it might be possible to argue that favoring popular items is not unfair per se since popularity is not a protected demographic characteristic. However, two considerations should be remembered here: since the objects (or their owners) are stakeholders in recommender systems [16], it is in the economic interest of the recommender system administrators to ensure that they are treated fairly and given equal opportunities of being recommended, even if they belong to the long tail. For example, it was estimated in 2006 that niche books that could not be found in physical stores accounted for 30–40% of Amazon book sales [48]. Secondly, popularity can derive from historical and structural inequalities [49], which means that favoring popular items can be unfair towards protected groups. For example, female music artists are historically under-represented, which means that they are often not part of the most popular classes in recommender systems and, therefore, are less likely to be recommended [50,51]. 

## _3.2. Popularity and Fairness for Subjects_ 

On the receiving end of recommender systems, subjects should receive recommendations based on their personal taste. Ideally, since these systems want to maximize the accuracy of recommendations and user satisfaction, systems should be fair towards them since their demographic data are not (at least in general) used for recommendations. However, different demographic groups interact differently with recommender systems, and this can make it so that treatment is unequal despite the fact that the same algorithms are 

_Information_ **2025** , _16_ , 151 

8 of 26 

being used and the algorithms are unaware of demographic details [49,52]. For example, older users are more likely to interact with more of the recommended items in a given list of recommendations [53]. If the accuracy of these systems is different for different (groups of) users, we can infer that there is unequal treatment [54]. 

To go beyond the simple accuracy metric, we can once again use calibration to describe how different users are treated by recommender systems. We already discussed that users interested in niche items will still receive popular recommendations (as noted in the study by Abdollahpouri et al. [47], but this effect was also observed in other studies [55,56]). Calibration offers the possibility to further describe users’ preferences. For example, in a movie recommendation system, if a user has liked seven horror movies and three action movies in their interaction history, we can expect the system to suggest 70% horror movies and 30% action movies. Kullback–Liebler divergence (KL-divergence) can be used to estimate the difference in the user’s history distribution and that of the recommendations. Lin et al. show that a variety of factors can lead to an increase in miscalibration, including the user’s preference for a small number of genres and, once again, the presence of popularity bias in the system’s data [57]. 

Popularity bias itself can be unbalanced across different classes, expanding and worsening pre-existing biases [58]. Lesota et al. [18] explored the effect of popularity bias on female and male users of a music recommender system, finding that many collaborative filtering algorithms intensified the popularity bias towards female users. 

All the reported results should be sufficient to convince the reader that it would be naive to believe that demographic groups are not susceptible to recommendation algorithms, and this sufficiently ensures fairness in recommender systems, as popularity bias is linked to other unfair effects that should be given proper consideration. 

## _3.3. Popularity Bias Effect in Different Systems_ 

One additional consideration related to recommender systems is that the effects of popularity bias, as well as their interaction with other biases, may vary according to the _type_ of items that are recommended. 

The number of items that can be consumed by a user with a single recommendation is one of the main factors impacting fairness. For example, a user is likely to choose only one movie to watch when given a list of recommendations by streaming services such as Netflix but is also likely to listen to tens of songs when using a service like Spotify. Popularity bias can be worsened by the fact that the user can only interact with one or a few items, making it more probable that the user will select popular items. On the contrary, when a user consumes multiple items, it is possible to leverage this for the mitigation of popularity bias by including, for example, less popular songs within a playlist of many popular ones. However, music recommendation has its own downsides: given the sequential nature of music recommendation, it is often the case that recommendation is made on a song-to-song basis (sometimes without any user interaction, since the user may be inattentive to the systems), where the diversity of songs may be perceived by the user as a non-satisfactory continuation of the listening experience, and popularity can play a big role in this kind of recommendation [102]. 

Another interesting aspect to be considered is that sometimes media that is recommended by these systems can be consumed by groups of people [103], for example, friends watching a movie together or listening to the same playlist [104]. In this case, popularity bias is mixed with other group dynamics that can make the preference for popular items even more impactful [105]. 

Finally, popularity bias can have a very serious effect on other biases when dealing with certain kinds of items, like news articles or social media posts [59]. For example, it 

_Information_ **2025** , _16_ , 151 

9 of 26 

is possible that the use of personalized recommendations may deepen the effect of “Filter Bubble” bias, exposing only views that the user already agrees with [60,61]. Such bubbles can become even harder to escape if an item of news becomes popular due to popularity bias, even if the news is fake, regardless of its popularity [62]. 

In the remainder of this paper, we will describe strategies to assess and mitigate the issues we described above. 

## **4. Mitigation Approaches** 

This section addresses the second of our research questions: “What can be carried out to mitigate the effects of popularity bias and showcase more of the long tail in recommendations?” Given the importance of the problem at hand, there have been many efforts to mitigate popularity bias in recommender systems. However, these efforts stem from different viewpoints. Namely, the main approach is to increase the diversity of recommendations, which is to say the variety of recommended items. Similarly, some researchers tried to increase the novelty of recommendations. Other researchers focused on the idea of serendipitous recommendations, plus other lesser-applied approaches emerged as well. Here, we attempt to cover all of these and discuss the limitations of each approach. 

## _4.1. Novelty and Diversity_ 

Accuracy was the main interest of early recommender systems and the main evaluation metric used until the early 2000s [64]. In those years, studies that focused on “beyondaccuracy” metrics began to emerge, also leading to the concepts of _novelty_ and _diversity_ becoming more and more popular for the evaluation of recommender systems. These concepts are not always directly meant to address popularity bias but aim to improve the user experience by taking into account more diverse recommendations. This, in turn, leads to a larger degree of exploration of the long tail and to the mitigation of popularity bias. 

Both novelty and diversity are terms that can have multiple meanings and that are used in diverse fields to describe different things. Within the context of recommender systems, they are both qualities of recommendations. Novelty describes the fact that recommended items are different from the ones that were already experienced by the user, and diversity describes the fact that recommended items show differences within themselves. This means that novelty does not imply that the recommended items should be new, recent, or novel in themselves. Similarly, diversity does not imply that the items (or the artists/authors linked to the items) are diverse when considering their cultural classifications or demographic groups. 

Since these metrics are strongly related and deal with differences between items, here we will jointly describe metrics for the evaluation of both, as well as algorithms for improving recommender systems according to these metrics. 

## 4.1.1. Metrics 

The general idea underlined above for the concepts of diversity and novelty translates to quantitative metrics that can be used to evaluate the effectiveness of recommender systems in recommending items that are not popular. Some metrics directly evaluate entire system, while other metrics deal with a single recommendation or a list of items that are recommended at one time. 

## Metrics over (Lists of) Recommendations 

We defined diversity as the fact that recommended items show differences between themselves, and as such, it makes sense to design a metric that computes the average difference between recommended items. Given a set of recommended items _R_ , it is possible 

_Information_ **2025** , _16_ , 151 

10 of 26 

to compute the diversity as what some researchers call intra-list diversity (or average intra-list distance [63]): 


![](prepared/information-16-00151/images/information-16-00151.pdf-0010-03.png)


This metric requires a distance metric _d_ ( _i_ , _j_ ), which can be the inverse of the similarity metrics already used for recommendation. If the recommender system is based on a similarity measure (as in the case of collaborative filtering), one might think it would be redundant to evaluate the system on the opposite measure. However, this metric tries to evaluate the differences between proposed recommendations and not between the recommendation and the user’s history (upon which the similarity measure was applied). 

While this is not explicitly encoded in the above formula, it is also possible to limit the evaluation to the top _N_ results obtaining _Diversity_ @ _N_ , taking inspiration from many common metrics used in information retrieval. This can be useful to do so because, depending on the system, users might have access to or only consider the first few recommendations from a list [106,107]. 

To compute the novelty of a set of recommendations, we can modify the same equation to account for the average difference between recommended items and items that are already known to a user (this can mean items that the user has consumed, rated, or simply visualized, depending on the system). Let _Iu_ be the set of items known to a user _u_ . We can define novelty (also called unexpectedness [64]) as follows: 


![](prepared/information-16-00151/images/information-16-00151.pdf-0010-07.png)


This definition relies on the same need for a distance metric, but this time, the risk of using a metric that is in direct opposition to what the algorithm tries to optimize is higher since the comparison is carried out with the user’s history. However, this definition can be easily adapted to consider the novelty of a single recommended item or to use a different aggregation function. Considering the maximum novelty of the recommended items instead of the average, for example, could provide an indication of how well the system is capable of suggesting novel items among other more expected ones without masking this information because of the presence of non-novel items. Similar to the above diversity, it is possible to adapt the equation to only consider _Novelty_ @ _N_ . 

Another interesting property of this metric is that it explicitly considers the user in its definition, making it a valuable candidate for measuring how fair the system is in suggesting the same number of novel items to different classes of users. Sometimes, this useful feature is undesirable when it is preferred to evaluate the novelty of a list of recommendations without disregarding the user. Our definition of novelty is related to the history of a certain user, but to make it user-agnostic, we can use a probabilistic approach. Supposing that an estimate _p_ ( _i_ ) of the probability of an item being known is available, it is possible to write novelty as follows: 


![](prepared/information-16-00151/images/information-16-00151.pdf-0010-10.png)


An estimate for _p_ ( _i_ ) can be obtained by using the ratio of users that have interacted with item _i_ over the total number of users. By doing so, we consider all the items that fall into the long tail as novel [66,84,108]. 

The above metrics are relative to single sets of recommendations and, in the case of the first definition of novelty, to a specific user. This makes these metrics quite useful for 

_Information_ **2025** , _16_ , 151 

11 of 26 

the internal evaluation of the system in an online setting: using them, the system may decide to change the recommendations to include more novel/diverse items or to re-rank the results (see Section 4.1.2). These metrics can also be used for offline evaluation to provide an indication of how diverse or novel the system’s recommendations are. To do so, one can compute the average values over a set of test recommendations, similar to how information retrieval systems are evaluated [109,110]. However, there are additional metrics that directly assess the system as a whole, considering all its recommendations over time to describe how capable it is to suggest novel and diverse items to its users. 

## Global Metrics 

A relatively simple metric to describe the capability of the system to suggest diverse items is the aggregate diversity [65]: 


![](prepared/information-16-00151/images/information-16-00151.pdf-0011-05.png)


Given that _U_ is the set of all users, this is the number of distinct items that the system has recommended to at least one user. To make the metric more informative, it can be changed to describe the fraction (or percentage) of items that have been recommended at least once. This metric is often referred to as _coverage_ [66–69]: 


![](prepared/information-16-00151/images/information-16-00151.pdf-0011-07.png)


Here, _I_ represents the set of all items available to the system that can be recommended. Coverage can provide an indication of how severe the popularity bias is in a recommender system: low coverage means that there are many non-popular items that are never recommended. However, its descriptive power is very limited as it cannot describe the different distribution of recommendations between popular and non-popular items: if every item is recommended exactly once except for a few items that are recommended thousands of times, the system would still suffer from severe popularity bias despite coverage being equal to 1. Some more powerful statistical metrics can be used for this goal, such as the _Gini_ index [70], 


![](prepared/information-16-00151/images/information-16-00151.pdf-0011-09.png)


or the Shannon entropy [71], 

Both require an estimate of the probability _p_ ( _i_ ) of an item being recommended by the system. In the Gini formulation, _k_ refers to the ranking of the item, and _ik_ is the item in position _k_ . This probability can be estimated by computing the number of times the item has been recommended over the total amount of times any item has been recommended. In this way, these metrics naturally incorporate the distribution of the recommendations. 

4.1.2. Algorithms Re-Ranking 

One popular approach to the improvement of diversity and novelty is that of reranking: given a list of recommendations ordered according to likelihood of being appreciated by the user, it is possible to change the ordering in order to feature more diverse recommendations in the first positions. Depending on the system, only the first few ele- 

_Information_ **2025** , _16_ , 151 

12 of 26 

ments of the list will actually be presented to the user, or more generally, the user is likely to only interact with the first few items on the recommendation list [107]. 

In order to effectively re-rank a list, it is necessary to employ one of the metrics listed above that apply to a list of recommendations, using a set cutoff _N_ to only consider the first positions. Given the metric, there are two possible approaches: either modifying the pre-existing list until the minimum objective value for the metric is met [77] or creating a list order that attempts to maximize the metric [78]. In the latter case, a greedy heuristic can be used to iteratively add the item that maximizes the diversity metric to the recommendation list, or it is possible to maximize a formula by balancing accuracy and diversity using the marginal relevance (MR) [79]: 


![](prepared/information-16-00151/images/information-16-00151.pdf-0012-04.png)


Here, _relevance_ ( _i_ ) is the relevance score assigned to item _i_ according to the recommendation algorithm, and _λ_ is a parameter used to tune the importance of diversity. Basically, this equation sums the diversity and the average relevance of the suggested items, and _λ_ is used to set the trade-off between the two elements of this metric. The greedy algorithm that maximizes this metric is referred to as the maximum marginal relevance (MMR). It is also possible to use novelty instead of diversity, as we will discuss in Section 4.2.2. 

## Algorithm Modification 

Instead of using pre-existing recommendation algorithms and modifying their results, it is also sometimes possible to directly alter the recommendation algorithm. 

One effective but rather naive way to improve novelty and diversity is the inclusion of random items in the recommendation list. Being selected at random, these items will statistically belong to the long tail and show a higher degree of novelty and diversity than those that would normally be suggested via collaborative filtering [64]. A slightly more advanced approach is the use of K-furthest neighbors (kFN) [82], a collaborative filtering algorithm that makes suggestions based on the _least_ similar users instead of using the most similar ones. The obvious downside of both these approaches is that the accuracy of the system decreases, and the recommendations are not really personalized to the user. Following a similar idea but with a more refined implementation, Nakatsuji et al. [83] propose a modified kNN based not on similarity between users but on _relatedness_ , i.e., a more relaxed definition of neighborhood constructed using a random walk with restart on a user similarity graph [111]. This method includes more dissimilar users than a standard kNN, allowing for more diversity in the recommendations. 

One interesting finding is that diversity can be improved using a transposed recommendation matrix, i.e., swapping the roles of users and items in a collaborative filtering system [84]. Other ways in which diversity can be improved (but that do not immediately also improve novelty) are the use of clustering and hybrid algorithms. Clustering refers to the idea of dividing items liked by the user into clusters and making suggestions based on each of the clusters [85]. This technique should ensure that the degree of diversity that is present in the user’s history is also reflected in the recommendations they receive. Instead, hybrid (or fusion) algorithms use the differences between different recommendation algorithms to improve diversity by selecting recommendations that were computed in different manners, for example, using both content-based recommendations and collaborative filtering. 

Content-based recommendations themselves are, arguably, a way to improve diversity. Because of their nature, these kinds of recommendations are less prone to popularity bias than those obtained through collaborative filtering since the only data they use are intrinsic 

_Information_ **2025** , _16_ , 151 

13 of 26 

item information and not user interaction [112]. However, it can be argued that suggesting items based on their content means that suggestions will be perceived as similar by users, not allowing for a greater perceived sense of diversity despite the fact that novel items from the long tail are selected [80]. This theoretic reasoning is not necessarily confirmed by real measurements [64] because the similarity in the metadata available to content-based recommendation may or may not correlate to user-perceived similarity [86], but even if this effect were found to be true, a hybrid approach could be used to mitigate it. 

## 4.1.3. Challenges 

Despite being a relatively new concept, most research in recent literature is aware of the importance of beyond-accuracy metrics and often considers novelty and diversity. However, there is still much research that can be carried out on these aspects. 

First of all, while the distance-based metrics we described above have become the de-facto standard in the evaluation of diversity, it is not entirely clear how well they represent the users’ perception of diversity in the recommendations. Similarly, there is still little research on the actual impact of diverse recommendations on user satisfaction and, more generally, on the way in which users interact with systems that can provide diverse recommendations. 

From the viewpoint of popularity bias, it is also unclear how well these approaches can help expose items from the long tail to users and whether they can limit the overrecommendation of popular items. To this end, a long-term evaluation of the development over time of a system’s recommendations would be required to assess how effectively the current definitions of diversity and novelty can help flatten the recommendation distribution. 

The next section will address studies on serendipity, with one in particular providing a promising line of research that attempts to go beyond simply recommending novel items. As we will argue in Section 4.2.3, advancements in this sub-field may also require a redefinition of the concepts of novelty and diversity in light of unexpectedness and usefulness. 

## _4.2. Serendipity_ 

Research on novelty and diversity shows that it is possible to expose elements from the long tail to users, but this in itself does not suffice to ensure that the recommendations will better the user experience. Research is thus shifting towards recommendations that are diverse but also accurate, trying to strike a balance between accuracy and novelty by being more conscious about which elements from the long tail should be recommended. 

One approach in particular that is gaining traction is that of _serendipity_ , which implies suggesting items that are unexpected but appreciated by the user [72]. The term comes from the fairy tale “The Three Princes of Serendip”, written by Cristoforo Armeno. He adapted, along with other source material, the Persian poem “Hasht Bihisht” by Amir Khusrow, who first introduced the characters that give the title to the story. In this tale, the protagonists succeed in their travels by accidentally finding things they were not looking for. 

Within research on recommender systems, many definitions have been proposed to describe serendipity, but a consensus on a single shared definition has not been reached. Ziarani and Ravanmehr [73] surveyed a variety of proposed definitions and found out that the most common components to describe serendipity in recommender systems are usefulness and unexpectedness, sometimes also including novelty and relevance. In general, it is safe to describe a serendipitous recommendation as a recommendation that is useful/valuable to the user despite the fact that they did not expect it. 

_Information_ **2025** , _16_ , 151 

14 of 26 

## 4.2.1. Metrics 

Given the definition of serendipity as a combination of usefulness and unexpectedness, a simple metric for its evaluation over a list of recommended items _R_ is the following: 


![](prepared/information-16-00151/images/information-16-00151.pdf-0014-04.png)


which is simply the ratio of useful items among unexpected items. As usual, if we cut off _R_ to only consider the top _N_ recommendations, we can obtain _Serendipity_ @ _N_ ( _R_ ). Note that the equation formulated by Chantanurak et al. [74] and later reprised by others [73] is ambiguous as it suggests taking the ratio between useful (or positive) items and unexpected ones, which could be (wrongly) understood as also considering the items that are useful but not unexpected, which would lead to a metric that is not limited to one as we would expect from a ratio, and more importantly would not be informative to the concept of serendipity. This metric leaves a lot of room for interpretation as it does not describe how to tell if an item is useful and/or unexpected. The fact that the user interacts or provides a positive rating can be used as an indication of the usefulness, while a measure for novelty can be used as a proxy for unexpectedness. In the case of an online evaluation, it is also possible to directly ask users whether they found recommendations unexpected and/or serendipitous. 

One limit of the above formulation is that it only considers items that are unexpected, not giving an indication of how many of the recommended items are serendipitous. The following formulation addresses this: 


![](prepared/information-16-00151/images/information-16-00151.pdf-0014-07.png)


This formulation is equivalent to the one proposed by De Gemmis et al. [75] as long as we consider “is useful and unexpected” to be equivalent to “is serendipitous” (as we propose it should be). 

This second formulation might seem more intuitive to some, as it directly evaluates how many of the recommended items are serendipitous. The downside is that, in order to obtain a perfect score, this metric requires that all the suggested items be unexpected. Since this might be too strict of a requirement (and very unlikely in a real-world scenario), it can mean that the informative power of this metric is limited, and the previous may be preferred as it evaluates how appropriately the system decides to select unexpected items. 

There are other quantitative metrics that have been proposed for serendipity, and the reader may want to consult other reviews on the subject to discover alternative proposed formulations [72,73]. We do not report further metrics because the ones mentioned here are sufficient to show that, in general, unexpectedness/novelty and user interaction are used to assess the serendipity of the recommendation. Moreover, it is more interesting to shift the discussion towards the methods used for implementing serendipity rather than discussing metrics because while these metrics follow the evaluation tradition of information retrieval, we believe that serendipity should guide the _process_ used for the recommendation, rather than being a measurable feature of the output. Measuring accuracy and novelty and balancing the two should already provide a good indication of how well a system can extract recommendations from the long tail without forfeiting the appropriateness of recommendations. In Section 4.2.3, we will further argue that research should possibly follow a different direction in the evaluation of serendipity. 

_Information_ **2025** , _16_ , 151 

15 of 26 

## 4.2.2. Algorithms Re-Ranking 

Similar to what is often conduced regarding novelty and diversity, one approach to increase serendipity is that of taking the output of an accuracy-based recommendation algorithm and re-ranking its results. In Section 4.1.2, we presented the MMR algorithm that attempts to re-rank results to balance relevance and diversity. While that algorithm was proposed for the goal of diversity and not that of serendipity, using Formula (1) with novelty instead of diversity can be seen as a serendipity approach, as it balances relevance and novelty. Following the same basic idea of balancing accuracy and unexpectedness, Ito et al. [80] propose a more detailed approach for serendipity that depends on a parameter. This allows us to fine-tune the recommendation algorithm to give more or less importance to accuracy. This implementation is based on the concept of confidence, which is a probabilistic estimate for the user rating of a certain item based on users who are similar and dissimilar to the target user. 

An approach that further departs from metric-based re-ranking is the one used for song recommendation by Auralist [81], which, after obtaining a basic list of relevant recommendations, has a module to diversify the list by choosing artists that have a diverse listenership and a further module that identifies clusters of songs often listened by the user, favoring songs that are outside these clusters. 

## Algorithm Modification 

One strategy to obtain more serendipitous recommendations within a collaborative filtering framework is that of modifying the neighborhood upon which the suggestions are based. In particular, by leveraging users that are actively exploring content of the platform to find more novel items, it is possible to obtain ratings on items that generally have fewer ratings. These users are often referred to as “innovators”. Wang et al. [87] identified these innovators based on how quickly they explored long tail items and leveraged them for recommendations. Kawamae [88] also considered the temporal development of systems and found innovators that were similar to the user but that explored new items more quickly. An estimate for how likely the target user will like items that these innovators have recently explored was used for recommendations. The general idea is to give more visibility to items that are not yet popular, but the fact that similarity between users is still at the basis of this system means that instead of escaping popularity bias, it might force the user towards (soon-to-be) popular items more rapidly. 

Another way to modify collaborative filtering is to use more advanced and complex definitions of similarity between users, which may capture deeper connections between users. One promising approach is to use neural networks to model user-to-item relations instead of the classic kNN approach [89,90]. 

## Other Approaches 

Some researchers have proposed novel approaches that do not directly derive from collaborative filtering. De Gemmis et al. [75] used a graph representation of the similarity between items computed using their metadata and external knowledge extracted from WordNet and Wikipedia. A random walk was then employed to suggest items, starting from the nodes that represented items liked by the user and using the graph representation to explore related items. 

Lu and Chung [92] also used metadata in the form of tags. Inspired by creativity research, they combined tags using machine learning to determine unexpected recommendations. While the surprise of generated items increased significantly, accuracy suffered from this approach. 

_Information_ **2025** , _16_ , 151 

16 of 26 

One further approach that was applied to the recommendation of learning material was the use of emotional analysis on the content of items to be recommended [93], which can be seen as a case of a hybrid algorithm employing both collaborative filtering and content-based recommendation. The emotional analysis looked for positive sentiments and those related to surprise, perhaps interpreting too literally the concept of unexpectedness by proposing materials that are unexpected in their _content_ rather than unexpected in _being recommended_ . This approach employed re-ranking based on the results of the sentiment analysis, but we include it in this section because the analysis used is different enough from usual metric-based re-ranking to be considered a different approach. The system provided good results both in terms of classic measures in an online test where users were asked to rate, among other aspects, the novelty and unexpectedness of the proposed materials. One downside of this approach, beside the fact that it is unclear if it actually achieved Serendipity in the sense of serendipitous recommendations, is that textual items are needed to perform this kind of analysis in an efficient way. 

## 4.2.3. Challenges 

Research on serendipity has become more active in the last few years, but there is still no universal definition of this concept within the field of recommender systems. While the general consensus sees serendipity as a property of recommendations that are both unexpected and valuable, in practice, different researchers have a diverse understanding of the concept, which can lead to different implementations. This may derive from the word that was chosen for this concept: the term “Serendipity” has a long history both in literature and pop culture [113] and is sometimes seen to have an almost _magical_ quality [114]. It is important to avoid being influenced by the poetic aura of the word and instead be guided by the needs of recommender systems when dealing with serendipity; therefore, finding a more unifying definition should be one of the goals of researchers in this field. 

Another open challenge for serendipity is that of evaluation. As noted by prior reviews on serendipity [73], it is not easy to evaluate this specific aspect of a recommender system, and some researchers fail to do this to a satisfactory degree. Offline evaluation has become easier since the release of datasets specifically aimed at serendipity [115], but it is not entirely clear how well offline evaluation can capture the concept of serendipity since many of the metrics for serendipity require proxies for the concepts of unexpectedness. These are usually based on novelty and diversity or other concepts related to long tail exploration, but it might be necessary to define different approaches that better capture the user-based notion of unexpectedness. Online evaluation can be implemented by simply asking users to evaluate how serendipitous they find the recommended items (or how unexpected they found items they enjoyed) [116], but to have evaluations that can be compared across different systems, it is necessary to determine a reproducible evaluation processes and, before that, to have an agreed definition for serendipity. 

Both the problem of providing clear definitions and that of evaluation are problems that are known in the field of computational creativity (http://computationalcreativity. net/ (accessed on 17 February 2025)), which attempts to obtain creative behaviors from computational systems. As noted by Lu and Chung [92], there is a strong relationship between the concepts of serendipity, which we describe as unexpectedness and usefulness, and that of creativity, which is usually described as novelty and value [117,118], although they are not the same (it must be noted that this concept of novelty is not the one used in recommender systems but rather describes the fact that creative artifacts are new). We propose that it is possible to learn from the past experience of computational creativity practitioners for some useful lessons regarding serendipity research. One such lesson is understanding _where_ and _when_ serendipity occurs. Is it a property of the system, capable of 

_Information_ **2025** , _16_ , 151 

17 of 26 

producing serendipitous recommendations, of the recommendations, that are serendipitous, of the _user’s perception_ of the recommendations when they find them serendipitous, or of the researchers/system owners that deem certain interactions serendipitous? These viewpoints roughly correspond to the four perspectives of creativity: process, product, person, and press [119]. Understanding these different perspectives can perhaps provide researchers with inspiration for different approaches to serendipity and to its evaluation. Creativity is understood as an _ex-post_ property [120]: a property that is attributed to something after its creation and, as such, cannot be imposed by construction. Arguably, serendipity is similarly a property that cannot be constructed but is found. For this reason, it is important to employ evaluation paradigms that go beyond the simple quantitative evaluation of the produced recommendations but rather evaluate the recommendation process itself and its capability of potentially producing serendipitous recommendations [121]. The literature on computational creativity offers many paradigms for evaluation [122] and for the description of how a conceptual space is explored [123,124], and we believe that it would be possible to employ many of those ideas in the context of serendipitous recommendations. 

## _4.3. Other Approaches_ 

The study of novelty, diversity, and serendipity are the main research lines within the field of recommender systems that address the problem of exposing more of the long tail to users of the system. However, there are further approaches that tackle popularity bias, but they do not fall precisely into one of these categories. 

## 4.3.1. Algorithms 

Arguing that it is necessary to distinguish “benign” and “harmful” popularity bias, Zhao et al. [44] propose a system called TIDE (TIme-Aware DisEntagled Framework). The authors observe that popular items tend to have high ratings on average, showing the positive effects of popularity, but that the ratings decrease when the item is most popular, meaning that because of popularity bias, the item was exposed to users who were not interested. Leveraging temporal information, their system uses disentangled learning to distinguish the effects of user data, item quality, and conformity. Conformity is the term the authors use to describe harmful popularity bias. Their system performs well according to classic metrics when compared to other systems, but was not evaluated via diversity-specific metrics. Because of this, it is hard to tell if the system managed to propose less popular items or if it only managed to suggest non-relevant popular ones. 

A similar approach, but one that does not leverage temporal information, was proposed by Wei et al. [94]. Using a causal inference graph, they proposed to use counterfactual reasoning to reduce the effect of popularity and only recommend based on item properties. 

Another approach was suggested by Steck [76] through a novel metric called popularity-stratified recall. This metric corrects the classic recall metric to consider item popularity (or an estimate of popularity). This allows us to both evaluate a system’s performance in recommending appropriate items that are not popular but also to train a system for recommendations that are not biased towards popular items. However, through a user study, Steck found that favoring the long tail in this way may lead to more variance in recommendation accuracy and reduce the trust of users in the system as a whole. Interestingly, he notes that this reduced trust makes it harder to suggest serendipitous items since the user will not expect to find useful items in the recommendations, even if the unexpectedness of items increases. 

Borges and Stefanidis [91] proposed the use of popularity-aware formulations of variational autoencoders within a collaborative filtering framework by applying a penalty to popular items in the decoder module. The system managed to reduce popularity bias, 

_Information_ **2025** , _16_ , 151 

18 of 26 

measured through the number of popular items in the first positions of the recommendation ranking but decreased the overall accuracy of the system. 

## 4.3.2. Challenges 

While the works that deal with novelty and serendipity aim at the exposure of the long tail in the recommendations, some of these works focused on popularity and followed the opposite approach of _not_ recommending popular items. Both offer valuable insights and future directions for research. On the one hand, it is necessary to limit the exposure of popular items without affecting users who wish to be exposed to these items. For this goal, further exploring causal inference methods is a viable option. On the other hand, exposure of the long tail requires providing the recommender system with further information that will allow it to make meaningful recommendations even without the safety of collaborative filtering. Content-based and contextual recommendations may allow for such meaningful inferences. 

However, we propose that the main direction forward should be the search for a unified view of the problem. Popularity bias has two sides: over-recommended popular items and under-recommended non-popular ones. A unified view requires the consideration of both. The hybridization of recommendation approaches could be a way to achieve this by having different models to consider the two sides of the problem. Metrics should also reflect this. Some metrics used in these works describe the presence (or absence) of popular items, while novelty metrics tend to describe the presence of non-popular ones. Some more unified views of the recommendation distribution are offered by the Gini index or Shannon’s entropy. Exploring further metrics to describe the general distribution of the recommendations could lead to advancements in the unified approaches to mitigate popularity bias. 

## **5. Discussion and Future Opportunities** 

Our research was driven by two fundamental questions, to which we try to provide an answer here, summarizing the findings of this literature review. 

- **RQ1** How does popularity bias affect the functioning and fairness of recommender systems towards users and stakeholders? 

In order to fully understand the question, we first discussed definitions of popularity bias in various contexts, showing how the preference for more popular items is rooted in human nature (see Section 2). In recommender systems, in particular, popular items are disproportionately likely to be recommended when compared with less popular items, as discussed in Section 3. While this is partly to be expected because items can become popular due to their inherent quality, it can also be detrimental to the quality of the system. Users who would like to see more niche items are still recommended popular items, and items that would deserve more recognition are not recommended due to this bias. Moreover, the literature shows that popularity biases can interact with pre-existing biases, worsening the effects of systematic biases, and can affect different demographic classes in different ways. All of these effects hinder the fairness of recommender systems and can worsen the overall user experience. 

- **RQ2** What can be carried out to mitigate the effects of popularity bias and showcase more of the long tail in recommendations? 

In Section 4, we attempted to cover the large amount of research that has been devoted to the diversification of recommendations, which is meant to expose more items from the long tail. Three key reoccurring concepts were found in the literature: diversity, the inclusion of dissimilar items in a set of recommendations, novelty, the inclusion 

_Information_ **2025** , _16_ , 151 

19 of 26 

of items different from the user’s history in recommendations, and serendipity, the recommendation of items that are unexpected but also valuable for the user. For each, researchers have tried to propose metrics to quantify the level of variety in the recommendations, as well as various algorithms that leverage those metrics. Some researchers also proposed novel algorithms for a recommendation that explicitly encode for popularity and learn to mitigate the preference towards these items. 

A critical review of the above-mentioned literature highlights some open problems that deserve more attention from research, as well as future opportunities to address popularity bias in recommender systems. 

## **Open Problem 1:** Evaluation Paradigms 

The evaluation of approaches to mitigate popularity bias and promote serendipitous recommendations has largely relied on metrics adapted from information retrieval, such as novelty, diversity, and their variants. However, these metrics have recognized limitations when applied to recommender systems [109,125], as they do not fully capture user experience and utility. For serendipity in particular, the current quantitative metrics based on unexpectedness and accuracy serve as proxies but may fail to evaluate the qualitative aspects that make a recommendation truly serendipitous from a user’s perspective. There is a need to move beyond just evaluating the recommendation outputs to more holistic paradigms that assess the capability of the recommendation process itself to potentially generate serendipitous results. Drawing inspiration from the field of computational creativity [126], which has long grappled with evaluating creative artifacts, could provide a fresh perspective [122,127]. Computational creativity emphasizes evaluating the process that gives rise to creative outcomes rather than just the outcomes themselves. It employs multi-faceted evaluation techniques, including human studies and analysis of the exploration of the conceptual space. Adapting such process-centric evaluation paradigms could enable a more insightful assessment of serendipity in recommender systems beyond what is currently possible with output-based metrics alone. 

## **Open Problem 2:** Leveraging Additional Information 

Most current approaches that address popularity bias primarily rely on user–item interaction data, such as explicit ratings or implicit interaction logs. However, these data are inherently skewed by the very popularity of the items themselves. To overcome this intrinsic limitation and enable more meaningful recommendations beyond popularity, recommender systems should leverage additional sources of information. Content metadata about the items, such as textual descriptions, tags, and multimedia attributes, can provide a semantic understanding of the items themselves, separate from their popularity. Similarly, contextual signals like the user’s recent activity, location, and the device used can enrich the user profile beyond just past interactions. Incorporating such additional information through hybrid or multi-signal approaches can help overcome the limitations of collaborative data alone. Content-based and context-aware recommendations, unbiased by popularity, can be combined with collaborative ones to mitigate bias. Furthermore, this additional information can feed more advanced learning models, such as neural networks or reasoning systems, to infer latent preferences and discover non-trivial connections between users and items. While acquiring and integrating these additional data presents operational challenges, it represents a promising direction to move beyond the intrinsic limitations of popularity data alone. 

## **Future Opportunity 1:** Unified View of Popularity 

_Information_ **2025** , _16_ , 151 

20 of 26 

The issue of popularity bias has two interconnected sides: the over-recommendation of already popular items and the under-recommendation of long tail, niche items. Current research efforts tend to tackle these as separate problems, with some approaches aimed at limiting exposure to popular items, while others try to boost the recommendation of novel and diverse items from the long tail. However, a siloed view fails to address the inherent skewness in the distribution of recommendations towards popularity. A unified perspective is needed that simultaneously accounts for both the head and the long tail. Hybrid recommendation approaches that combine different models and strategies could provide a path towards this unified treatment. Additionally, evaluation metrics should evolve to characterize the overall distribution rather than focusing on either extreme. Measures like the Gini index or Shannon’s entropy offer a more comprehensive view compared to metrics that only capture popular items or novel recommendations in isolation. Exploring unified metrics aligned with a hybrid recommendation framework could pave the way for more balanced and less popularity-skewed recommendations. 

## **Future Opportunity 2:** Personalized Levels of Popularity 

As described in Section 2.1, popularity bias is intrinsic to human nature and can sometimes even be seen as a positive feature of human psychology or of an information system. However, just accepting that a system can be biased towards popular items because humans are similarly biased does not consider the bigger picture, where some users desire to find more niche items and would not accept being exposed to many popular items [56]. Moreover, without explicit control over the popularity of recommendations, different categories of users could receive unbalanced treatment [18]. Therefore, in order to increase the holistic effectiveness of recommender systems as well as overall user satisfaction, the popularity of recommended items could be explicitly controlled by the recommender system, allowing for recommendations that are personalized both in the content of the recommendations and in this meta-feature of the recommendation that would match the level of explorativeness of the user. 

## **6. Conclusions** 

In this article, we reviewed the scientific literature related to popularity bias, a term that describes the disproportionate preference towards popular items. This bias affects, in different ways, both humans and algorithms and is known to be especially relevant in recommender systems, impacting the fairness of these systems. We described the phenomenon and the ways in which it can unfairly impact the users of recommender systems, considering the different perspectives of subjects and objects and how different systems are impacted. Several metrics related to different aspects of popularity bias (see Table 1) were identified and discussed. We later reviewed the main approaches that have been proposed for the mitigation of this bias by the recommender systems community, resulting in a list of 15 different approaches (see Table 1). The main directions that have been explored to address the long tail problem are the improvement of novelty, diversity, and serendipity. However, despite the large amount of recent research on these aspects, the reviewed approaches cannot fully address the problem of popularity bias, and a lot of the available research on these subjects was not directly meant to address this problem. Some further approaches are described that specifically try to address it, primarily by limiting the number of popular items that are recommended. 

Recommender systems are rapidly becoming the main tool for the exploration of unmeasurable amounts of data on the Internet. Addressing the fairness of these systems and their capability to actually represent all the available data in a less unbalanced way 

_Information_ **2025** , _16_ , 151 

21 of 26 

is of paramount importance. With this review, we have shown that researchers are aware of this problem and are actively proposing solutions to address these biases. While the issue is far from having a definitive solution, we are sure that we are going to see many improvements in the near future. 

**Author Contributions:** Conceptualization, F.C. and A.R.; methodology, F.C. and A.R.; investigation, F.C.; resources, A.R.; data curation, F.C. and A.R.; writing—original draft preparation, F.C.; writing— review and editing, F.C., G.A.W. and A.R.; supervision, A.R. and G.A.W.; funding acquisition, A.R. All authors have read and agreed to the published version of the manuscript. 

**Funding:** This research was partially funded by the Department of Information Engineering of the University of Padova under the project “Creative Recommendations to avoid Unfair Bottlenecks”. Research carried out within the project “SISSI” was funded by Regione Veneto for program POC 2014-2020 (application ID 10449164). 

**Conflicts of Interest:** The authors declare no conflicts of interest. The funders had no role in the design of the study; in the collection, analyses, or interpretation of data; in the writing of the manuscript; or in the decision to publish the results. 

## **References** 

1. Bobadilla, J.; Ortega, F.; Hernando, A.; Gutiérrez, A. Recommender systems survey. _Knowl.-Based Syst._ **2013** , _46_ , 109–132. [CrossRef] 

2. Vermaas, P.; Kroes, P.; Van de Poel, I.; Franssen, M.; Houkes, W. A philosophy of technology: From technical artefacts to sociotechnical systems. _Synth. Lect. Eng. Technol. Soc._ **2011** , _6_ , 1–134. 

3. Ntoutsi, E.; Fafalios, P.; Gadiraju, U.; Iosifidis, V.; Nejdl, W.; Vidal, M.E.; Ruggieri, S.; Turini, F.; Papadopoulos, S.; Krasanakis, E. Bias in data-driven artificial intelligence systems—An introductory survey. _Wiley Interdiscip. Rev. Data Min. Knowl. Discov._ **2020** , _10_ , e1356. [CrossRef] 

4. Osoba, O.A.; Welser, W., IV. _An Intelligence in Our Image: The Risks of Bias and Errors in Artificial Intelligence_ ; Rand Corporation: Santa Monica, CA, USA, 2017. 

5. Banerjee, A.V. A Simple Model of Herd Behavior. _Q. J. Econ._ **1992** , _107_ , 797–817. [CrossRef] 

6. Abdollahpouri, H.; Mansoury, M.; Burke, R.; Mobasher, B. The Unfairness of Popularity Bias in Recommendation. _arXiv_ **2019** , arXiv:1907.13286. 

7. Idrissi, N.; Zellou, A. A systematic literature review of sparsity issues in recommender systems. _Soc. Netw. Anal. Min._ **2020** , _10_ , 15. [CrossRef] 

8. Bobadilla, J.; Serradilla, F. The effect of sparsity on collaborative filtering metrics. In Proceedings of the Twentieth Australasian Conference on Australasian Database, Wellington, New Zealand, 20–23 January 2009; Volume 92, pp. 9–18. 

9. Park, Y.J.; Tuzhilin, A. The long tail of recommender systems and how to leverage it. In Proceedings of the 2008 ACM Conference on Recommender Systems, Lausanne, Switzerland, 23–25 October 2008; pp. 11–18. 

10. Wang, Y.; Ma, W.; Zhang, M.; Liu, Y.; Ma, S. A survey on the fairness of recommender systems. _Acm Trans. Inf. Syst._ **2023** , _41_ , 1–43. [CrossRef] 

11. Zhao, Y.; Wang, Y.; Liu, Y.; Cheng, X.; Aggarwal, C.C.; Derr, T. Fairness and diversity in recommender systems: A survey. _Acm Trans. Intell. Syst. Technol._ **2023** , _16_ , 1–28. [CrossRef] 

12. Jin, D.; Wang, L.; Zhang, H.; Zheng, Y.; Ding, W.; Xia, F.; Pan, S. A survey on fairness-aware recommender systems. _Inf. Fusion_ **2023** , _100_ , 101906. [CrossRef] 

13. Chen, J.; Dong, H.; Wang, X.; Feng, F.; Wang, M.; He, X. Bias and debias in recommender system: A survey and future directions. _Acm Trans. Inf. Syst._ **2023** , _41_ , 1–39. [CrossRef] 

14. Klimashevskaia, A.; Jannach, D.; Elahi, M.; Trattner, C. A survey on popularity bias in recommender systems. _User Model.-UserAdapt. Interact._ **2024** , _34_ , 1777–1834. [CrossRef] 

15. Greenhalgh, T.; Thorne, S.; Malterud, K. Time to challenge the spurious hierarchy of systematic over narrative reviews? _Eur. J. Clin. Investig._ **2018** , _48_ , e12931. [CrossRef] 

16. Abdollahpouri, H.; Burke, R. Multi-stakeholder recommendation and its connection to multi-sided fairness. _arXiv_ **2019** , arXiv:1907.13158. 

17. Abdollahpouri, H. Popularity Bias in Ranking and Recommendation. In Proceedings of the 2019 AAAI/ACM Conference on AI, Ethics, and Society, Honolulu, HI, USA, 27–28 January 2019; pp. 529–530. [CrossRef] 

_Information_ **2025** , _16_ , 151 

22 of 26 

18. Lesota, O.; Melchiorre, A.; Rekabsaz, N.; Brandl, S.; Kowald, D.; Lex, E.; Schedl, M. Analyzing Item Popularity Bias of Music Recommender Systems: Are Different Genders Equally Affected? In Proceedings of the Fifteenth ACM Conference on Recommender Systems, Amsterdam, The Netherlands, 27 September–1 October 2021; pp. 601–606. [CrossRef] 

19. Porcaro, L.; Castillo, C.; Gómez, E. Diversity by Design in Music Recommender Systems. _Trans. Int. Soc. Music. Inf. Retr._ **2021** , _4_ , 114–126. [CrossRef] 

20. Thompson, B.; Griffiths, T.L. Human biases limit cumulative innovation. _Proc. R. Soc. B Biol. Sci._ **2021** , _288_ , 20202752. [CrossRef] [PubMed] 

21. Kahneman, D.; Slovic, S.P.; Slovic, P.; Tversky, A. _Judgment Under Uncertainty: Heuristics and Biases_ ; Cambridge University Press: Cambridge, UK, 1982. 

22. Gilovich, T.; Griffin, D.; Kahneman, D. _Heuristics and Biases: The Psychology of Intuitive Judgment_ ; Cambridge University Press: Cambridge, UK, 2002. 

23. Bikhchandani, S.; Hirshleifer, D.; Welch, I. Learning from the behavior of others: Conformity, fads, and informational cascades. _J. Econ. Perspect._ **1998** , _12_ , 151–170. [CrossRef] 

24. Bikhchandani, S.; Sharma, S. Herd behavior in financial markets: A review. _IMF Work. Pap._ **2000** , _47_ , 279–310. [CrossRef] 

25. Choijil, E.; Méndez, C.E.; Wong, W.K.; Vieito, J.P.; Batmunkh, M.U. Thirty years of herd behavior in financial markets: A bibliometric analysis. _Res. Int. Bus. Financ._ **2022** , _59_ , 101506. [CrossRef] 

26. Rook, L. An Economic Psychological Approach to Herd Behavior. _J. Econ. Issues_ **2006** , _40_ , 75–95. [CrossRef] 27. Calvó-Armengol, A.; Jackson, M.O. Peer Pressure. _J. Eur. Econ. Assoc._ **2010** , _8_ , 62–89. [CrossRef] 

28. Bornstein, R.F.; Craver-Lemley, C. Mere exposure effect. In _Cognitive Illusions_ ; Psychology Press: Hove, UK, 2016; pp. 266–285. 29. Montoya, R.M.; Horton, R.S.; Vevea, J.L.; Citkowicz, M.; Lauber, E.A. A re-examination of the mere exposure effect: The influence of repeated exposure on recognition, familiarity, and liking. _Psychol. Bull._ **2017** , _143_ , 459–498. [CrossRef] 

30. Chen, Y.F. Herd behavior in purchasing books online. _Comput. Hum. Behav._ **2008** , _24_ , 1977–1992. [CrossRef] 31. Hanson, W.A.; Putler, D.S. Hits and misses: Herd behavior and online product popularity. _Mark. Lett._ **1996** , _7_ , 297–305. [CrossRef] 32. Zhu, F.; Zhang, X.M. Impact of Online Consumer Reviews on Sales: The Moderating Role of Product and Consumer Characteristics. _J. Mark._ **2010** , _74_ , 133–148. [CrossRef] 

33. Dholakia, U.M.; Basuroy, S.; Soltysinski, K. Auction or agent (or both)? A study of moderators of the herding bias in digital auctions. _Int. J. Res. Mark._ **2002** , _19_ , 115–130. [CrossRef] 

34. Griskevicius, V.; Goldstein, N.J.; Mortensen, C.R.; Sundie, J.M.; Cialdini, R.B.; Kenrick, D.T. Fear and Loving in Las Vegas: Evolution, Emotion, and Persuasion. _J. Mark. Res._ **2009** , _46_ , 384–395. [CrossRef] [PubMed] 

35. Nolan, J.M.; Schultz, P.W.; Cialdini, R.B.; Goldstein, N.J.; Griskevicius, V. Normative social influence is underdetected. _Personal. Soc. Psychol. Bull._ **2008** , _34_ , 913–923. [CrossRef] [PubMed] 

36. Bearden, W.O.; Etzel, M.J. Reference group influence on product and brand purchase decisions. _J. Consum. Res._ **1982** , _9_ , 183–194. [CrossRef] 

37. Letheren, K.; Russell-Bennett, R.; Whittaker, L. Black, white or grey magic? Our future with artificial intelligence. _J. Mark. Manag._ **2020** , _36_ , 216–232. [CrossRef] 

38. Biswas, M.; Murray, J. The effects of cognitive biases and imperfectness in long-term robot-human interactions: Case studies using five cognitive biases on three robots. _Cogn. Syst. Res._ **2017** , _43_ , 266–290. [CrossRef] 

39. Sengupta, E.; Garg, D.; Choudhury, T.; Aggarwal, A. Techniques to Elimenate Human Bias in Machine Learning. In Proceedings of the 2018 International Conference on System Modeling & Advancement in Research Trends (SMART), Moradabad, India, 23–24 November 2018; pp. 226–230. [CrossRef] 

40. Abdollahpouri, H.; Burke, R.; Mobasher, B. Controlling Popularity Bias in Learning-to-Rank Recommendation. In Proceedings of the Eleventh ACM Conference on Recommender Systems, Como, Italy, 27–31 August 2017; pp. 42–46. [CrossRef] 

41. Cañamares, R.; Castells, P. Should I follow the crowd? A probabilistic analysis of the effectiveness of popularity in recommender systems. In Proceedings of the the 41st International ACM SIGIR Conference on Research & Development in Information Retrieval, Ann Arbor, MI, USA, 8–12 July 2018; pp. 415–424. 

42. Weiss, G.M.; McCarthy, K.; Zabar, B. Cost-sensitive learning vs. sampling: Which is best for handling unbalanced classes with unequal error costs? _Dmin_ **2007** , _7_ , 24. 

43. Elkan, C. The foundations of cost-sensitive learning. In Proceedings of the International Joint Conference on Artificial Intelligence, Seattle, WA, USA, 4–10 August 2001; Lawrence Erlbaum Associates Ltd.: Mahwah, NJ, USA, 2001; Volume 17, pp. 973–978. 

44. Zhao, Z.; Chen, J.; Zhou, S.; He, X.; Cao, X.; Zhang, F.; Wu, W. Popularity Bias Is Not Always Evil: Disentangling Benign and Harmful Bias for Recommendation. _arXiv_ **2021** , arXiv:2109.07946. [CrossRef] 

45. Ciampaglia, G.L.; Nematzadeh, A.; Menczer, F.; Flammini, A. How algorithmic popularity bias hinders or promotes quality. _Sci. Rep._ **2018** , _8_ , 15951. [CrossRef] 

46. Anderson, A.; Maystre, L.; Anderson, I.; Mehrotra, R.; Lalmas, M. Algorithmic effects on the diversity of consumption on spotify. In Proceedings of the Web Conference, Taipei, Taiwan, 20–24 April 2020; pp. 2155–2165. 

_Information_ **2025** , _16_ , 151 

23 of 26 

47. Abdollahpouri, H.; Mansoury, M.; Burke, R.; Mobasher, B. The Connection Between Popularity Bias, Calibration, and Fairness in Recommendation. In Proceedings of the Fourteenth ACM Conference on Recommender Systems, Virtual, 22–26 September 2020; pp. 726–731. [CrossRef] 

48. Brynjolfsson, E.; Hu, Y.J.; Smith, M.D. From niches to riches: Anatomy of the long tail. _Sloan Manag. Rev._ **2006** , _47_ , 67–71. 49. Schelenz, L. Diversity-aware Recommendations for Social Justice? Exploring User Diversity and Fairness in Recommender Systems. In Proceedings of the UMAP 2021—Adjunct Publication of the 29th ACM Conference on User Modeling, Adaptation and Personalization, Utrecht, The Netherlands, 21–25 June 2021; pp. 404–410. [CrossRef] 

50. Ferraro, A.; Serra, X.; Bauer, C. Break the Loop: Gender Imbalance in Music Recommenders. In Proceedings of the 2021 Conference on Human Information Interaction and Retrieval, Canberra, Australia, 14–19 March 2021; pp. 249–254. [CrossRef] 

51. Shakespeare, D.; Porcaro, L.; Gómez, E.; Castillo, C. Exploring artist gender bias in music recommendation. _arXiv_ **2020** , arXiv:2009.01715. 

52. Park, M.; Weber, I.; Naaman, M.; Vieweg, S. Understanding musical diversity via online social media. In Proceedings of the International AAAI Conference on Web and Social Media, Oxford, UK, 26–29 May 2015; Volume 9, pp. 308–317. 

53. Beel, J.; Langer, S.; Nürnberger, A.; Genzmehr, M. The Impact of Demographics (Age and Gender) and Other User-Characteristics on Evaluating Recommender Systems. In _Research and Advanced Technology for Digital Libraries_ ; Lecture Notes in Computer Science; Hutchison, D., Kanade, T., Kittler, J., Kleinberg, J.M., Mattern, F., Mitchell, J.C., Naor, M., Nierstrasz, O., Pandu Rangan, C., Steffen, B., et al., Eds.; Springer: Berlin/Heidelberg, Germany, 2013; Volume 8092, pp. 396–400. [CrossRef] 

54. Mansoury, M.; Mobasher, B.; Burke, R.; Pechenizkiy, M. Bias disparity in collaborative recommendation: Algorithmic evaluation and comparison. _arXiv_ **2019** , arXiv:1908.00831. 

55. Abdollahpouri, H.; Mansoury, M.; Burke, R.; Mobasher, B.; Malthouse, E. User-centered Evaluation of Popularity Bias in Recommender Systems. In Proceedings of the 29th ACM Conference on User Modeling, Adaptation and Personalization, Utrecht, The Netherlands, 21–25 June 2021; pp. 119–129. [CrossRef] 

56. Kowald, D.; Schedl, M.; Lex, E. The Unfairness of Popularity Bias in Music Recommendation: A Reproducibility Study. In _Advances in Information Retrieval_ ; Lecture Notes in Computer Science; Jose, J.M., Yilmaz, E., Magalhães, J., Castells, P., Ferro, N., Silva, M.J., Martins, F., Eds.; Springer International Publishing: Cham, Switzerland, 2020; Volume 12036, pp. 35–42. [CrossRef] 

57. Lin, K.; Sonboli, N.; Mobasher, B.; Burke, R. Calibration in Collaborative Filtering Recommender Systems: A User-Centered Analysis. In Proceedings of the 31st ACM Conference on Hypertext and Social Media, Virtual Event, 13–15 July 2020; pp. 197–206. [CrossRef] 

58. Tsintzou, V.; Pitoura, E.; Tsaparas, P. Bias disparity in recommendation systems. _arXiv_ **2018** , arXiv:1811.01461. 

59. Yang, J. Effects of popularity-based news recommendations (“most-viewed”) on users’ exposure to online news. _Media Psychol._ **2016** , _19_ , 243–271. [CrossRef] 

60. Lunardi, G.M.; Machado, G.M.; Maran, V.; de Oliveira, J.P.M. A metric for Filter Bubble measurement in recommender algorithms considering the news domain. _Appl. Soft Comput._ **2020** , _97_ , 106771. [CrossRef] 

61. Nguyen, T.T.; Hui, P.M.; Harper, F.M.; Terveen, L.; Konstan, J.A. Exploring the filter bubble: The effect of using recommender systems on content diversity. In Proceedings of the 23rd International Conference on World Wide Web, Seoul, Republic of Korea, 7–11 April 2014; pp. 677–686. 

62. Akar, E.; Hakyemez, T.C.; Bozanta, A.; Akar, S. What Sells on the Fake News Market? Examining the Impact of Contextualized Rhetorical Features on the Popularity of Fake Tweets. _Online J. Commun. Media Technol._ **2021** , _12_ , e202201. [CrossRef] 

63. Smyth, B.; McClave, P. Similarity vs. diversity. In Proceedings of the International Conference on Case-Based Reasoning, Vancouver, BC, Canada, 30 July–2 August 2001; Springer: Berlin/Heidelberg, Germany, 2001; pp. 347–361. 

64. Castells, P.; Hurley, N.; Vargas, S. Novelty and diversity in recommender systems. In _Recommender Systems Handbook_ ; Springer: Berlin/Heidelberg, Germany, 2022; pp. 603–646. 

65. Adomavicius, G.; Kwon, Y. Improving aggregate recommendation diversity using ranking-based techniques. _IEEE Trans. Knowl. Data Eng._ **2012** , _24_ , 896–911. [CrossRef] 

66. Kaminskas, M.; Bridge, D. Diversity, Serendipity, Novelty, and Coverage: A Survey and Empirical Analysis of Beyond-Accuracy Objectives in Recommender Systems. _Acm Trans. Interact. Intell. Syst._ **2017** , _7_ , 1–42. [CrossRef] 

67. Bellogín, A.; Cantador, I.; Castells, P. A comparative study of heterogeneous item recommendations in social systems. _Inf. Sci._ **2013** , _221_ , 142–169. [CrossRef] 

68. Bellogín, A.; Cantador, I.; Díez, F.; Castells, P.; Chavarriaga, E. An empirical comparison of social, collaborative filtering, and hybrid recommenders. _Acm Trans. Intell. Syst. Technol. (TIST)_ **2013** , _4_ , 1–29. [CrossRef] 

69. Herlocker, J.L.; Konstan, J.A.; Terveen, L.G.; Riedl, J.T. Evaluating collaborative filtering recommender systems. _Acm Trans. Inf. Syst. (TOIS)_ **2004** , _22_ , 5–53. [CrossRef] 

70. Vargas, S.; Castells, P. Improving sales diversity by recommending users to items. In Proceedings of the 8th ACM Conference on Recommender Systems, Silicon Valley, CA, USA, 6–10 October 2014; pp. 145–152. 

_Information_ **2025** , _16_ , 151 

24 of 26 

71. Szlávik, Z.; Kowalczyk, W.; Schut, M. Diversity measurement of recommender systems under different user choice models. In Proceedings of the International AAAI Conference on Web and Social Media, Barcelona, Spain, 17–21 July 2011; Volume 5, pp. 369–376. 

72. Kotkov, D.; Wang, S.; Veijalainen, J. A survey of serendipity in recommender systems. _Knowl.-Based Syst._ **2016** , _111_ , 180–192. [CrossRef] 

73. Ziarani, R.J.; Ravanmehr, R. Serendipity in Recommender Systems: A Systematic Literature Review. _J. Comput. Sci. Technol._ **2021** , _36_ , 375–396. [CrossRef] 

74. Chantanurak, N.; Punyabukkana, P.; Suchato, A. Video recommender system using textual data: Its application on LMS and serendipity evaluation. In Proceedings of the 2016 IEEE International Conference on Teaching, Assessment, and Learning for Engineering (TALE), Bangkok, Thailand, 7–9 December 2016; IEEE: Piscataway, NJ, USA, 2016; pp. 289–295. 

75. De Gemmis, M.; Lops, P.; Semeraro, G.; Musto, C. An investigation on the serendipity problem in recommender systems. _Inf. Process. Manag._ **2015** , _51_ , 695–717. [CrossRef] 

76. Steck, H. Item popularity and recommendation accuracy. In Proceedings of the Fifth ACM Conference on Recommender Systems—RecSys ’11, Chicago, IL, USA, 23–27 October 2011; p. 125. [CrossRef] 

77. Yu, C.; Lakshmanan, L.; Amer-Yahia, S. It takes variety to make a world: Diversification in recommender systems. In Proceedings of the 12th International Conference on Extending DATABASE Technology: Advances in Database Technology, Saint-Petersburg, Russia, 24–26 March 2009; pp. 368–378. 

78. Deselaers, T.; Gass, T.; Dreuw, P.; Ney, H. Jointly optimising relevance and diversity in image retrieval. In Proceedings of the ACM International Conference on Image and VIDEO Retrieval, Santorini Island, Greece, 8–10 July 2009; pp. 1–8. 

79. Carbonell, J.; Goldstein, J. The use of MMR, diversity-based reranking for reordering documents and producing summaries. In Proceedings of the 21st Annual International ACM SIGIR Conference on Research and Development in Information Retrieval, Melbourne, Australia, 24–28 August 1998; pp. 335–336. 

80. Ito, H.; Yoshikawa, T.; Furuhashi, T. A study on improvement of serendipity in item-based collaborative filtering using association rule. In Proceedings of the 2014 IEEE International Conference on Fuzzy Systems (FUZZ-IEEE), Beijing, China, 6–11 July 2014; IEEE: Piscataway, NJ, USA, 2014; pp. 977–981. 

81. Zhang, Y.C.; Séaghdha, D.Ó.; Quercia, D.; Jambor, T. Auralist: Introducing serendipity into music recommendation. In Proceedings of the Fifth ACM International Conference on Web Search and Data Mining—WSDM ’12, Seattle, WA, USA, 8–12 February 2012; p. 13. [CrossRef] 

82. Said, A.; Fields, B.; Jain, B.J.; Albayrak, S. User-centric evaluation of a k-furthest neighbor collaborative filtering recommender algorithm. In Proceedings of the 2013 Conference on Computer Supported Cooperative Work, San Antonio, TX, USA, 23–27 February 2013; pp. 1399–1408. 

83. Nakatsuji, M.; Fujiwara, Y.; Tanaka, A.; Uchiyama, T.; Fujimura, K.; Ishida, T. Classical music for rock fans? Novel recommendations for expanding user interests. In Proceedings of the 19th ACM International Conference on Information and Knowledge Management, Toronto, ON, Canada, 26–30 October 2010; pp. 949–958. 

84. Vargas, S.; Castells, P. Rank and relevance in novelty and diversity metrics for recommender systems. In Proceedings of the Fifth ACM Conference on Recommender Systems—RecSys ’11, Chicago, IL, USA, 23–27 October 2011; p. 109. [CrossRef] 

85. Zhang, M.; Hurley, N. Novel item recommendation by user profile partitioning. In Proceedings of the 2009 IEEE/WIC/ACM International Joint Conference on Web Intelligence and Intelligent Agent Technology, Milan, Italy, 15–18 September 2009; IEEE: Piscataway, NJ, USA, 2009; Volume 1, pp. 508–515. 

86. Kito, N.; Oku, K.; Kawagoe, K. Correlation analysis among the metadata-based similarity, acoustic-based distance, and serendipity of music. In Proceedings of the 19th International Database Engineering & Applications Symposium, Yokohama, Japan, 13–15 July 2015; pp. 198–199. 

87. Wang, C.D.; Deng, Z.H.; Lai, J.H.; Philip, S.Y. Serendipitous recommendation in e-commerce using innovator-based collaborative filtering. _IEEE Trans. Cybern._ **2018** , _49_ , 2678–2692. [CrossRef] 

88. Kawamae, N. Serendipitous recommendations via innovators. In Proceedings of the 33rd International ACM SIGIR Conference on Research and Development in Information Retrieval, Geneva, Switzerland, 19–23 July 2010; pp. 218–225. 

89. Deng, Z.H.; Huang, L.; Wang, C.D.; Lai, J.H.; Philip, S.Y. Deepcf: A unified framework of representation learning and matching function learning in recommender system. In Proceedings of the AAAI Conference on Artificial Intelligence, Honolulu, HI, USA, 27 January–1 February 2019; Volume 33, pp. 61–68. 

90. He, X.; Liao, L.; Zhang, H.; Nie, L.; Hu, X.; Chua, T.S. Neural collaborative filtering. In Proceedings of the 26th International Conference on World Wide Web, Perth, Australia, 3–7 April 2017; pp. 173–182. 

91. Borges, R.; Stefanidis, K. On mitigating popularity bias in recommendations via variational autoencoders. In Proceedings of the 36th Annual ACM Symposium on Applied Computing, Virtual Event, 22–26 March 2021; pp. 1383–1389. [CrossRef] 

92. Lu, W.; Chung, F.L. Computational Creativity Based Video Recommendation. In Proceedings of the 39th International ACM SIGIR Conference on Research and Development in Information Retrieval, Pisa, Italy, 17–21 July 2016; pp. 793–796. [CrossRef] 

_Information_ **2025** , _16_ , 151 

25 of 26 

93. Sayahi, S.; Ghorbel, L.; Zayani, C.; Champagnat, R. Towards Serendipitous Learning Resource Recommendation. In Proceedings of the 15th International Conference on Computer Supported Education—Volume 1: EKM, Prague, Czech Republic, 21–23 April 2023; INSTICC, SciTePress: Setúbal, Portugal, 2023; pp. 454–462. [CrossRef] 

94. Wei, T.; Feng, F.; Chen, J.; Wu, Z.; Yi, J.; He, X. Model-Agnostic Counterfactual Reasoning for Eliminating Popularity Bias in Recommender System. In Proceedings of the 27th ACM SIGKDD Conference on Knowledge Discovery & Data Mining, Singapore, 14–18 August 2021; pp. 1791–1800. [CrossRef] 

95. Castro, L.; Toro, M.A. Cumulative cultural evolution: The role of teaching. _J. Theor. Biol._ **2014** , _347_ , 74–83. [CrossRef] [PubMed] 

96. Salganik, M.J.; Dodds, P.S.; Watts, D.J. Experimental Study of Inequality and Unpredictability in an Artificial Cultural Market. _Science_ **2006** , _311_ , 854–856. [CrossRef] 

97. Fraiberger, S.P.; Sinatra, R.; Resch, M.; Riedl, C.; Barabási, A.L. Quantifying reputation and success in art. _Science_ **2018** , _36_ 2, 825–829. [CrossRef] [PubMed] 

98. Powell, D.; Yu, J.; DeWolf, M.; Holyoak, K.J. The love of large numbers: A popularity bias in consumer choice. _Psychol. Sci._ **2017** , _28_ , 1432–1442. [CrossRef] [PubMed] 

99. Heck, D.W.; Seiling, L.; Bröder, A. The Love of Large Numbers Revisited: A Coherence Model of the Popularity Bias. _Cognition_ **2020** , _195_ , 104069. [CrossRef] [PubMed] 

100. Rescher, N. _Fairness_ ; Routledge: London, UK, 2017. 

101. Geyik, S.C.; Ambler, S.; Kenthapadi, K. Fairness-Aware Ranking in Search & Recommendation Systems with Application to LinkedIn Talent Search. In Proceedings of the 25th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining, Anchorage, AK, USA, 4–8 August 2019; pp. 2221–2231. [CrossRef] 

102. Vall, A.; Quadrana, M.; Schedl, M.; Widmer, G. Order, context and popularity bias in next-song recommendations. _Int. J. Multimed. Inf. Retr._ **2019** , _8_ , 101–113. [CrossRef] 

103. Xiao, L.; Min, Z.; Yongfeng, Z.; Zhaoquan, G.; Yiqun, L.; Shaoping, M. Fairness-aware group recommendation with paretoefficiency. In Proceedings of the Eleventh ACM Conference on Recommender Systems, Como, Italy, 27–31 August 2017; pp. 107–115. 

104. Htun, N.N.; Lecluse, E.; Verbert, K. Perception of fairness in group music recommender systems. In Proceedings of the 26th International Conference on Intelligent User Interfaces, College Station, TX, USA, 14–17 April 2021; pp. 302–306. 

105. Yalcin, E.; Bilge, A. Investigating and counteracting popularity bias in group recommendations. _Inf. Process. Manag._ **2021** , _58_ , 102608. [CrossRef] 

106. Deshpande, M.; Karypis, G. Item-based top- _N_ recommendation algorithms. _Acm Trans. Inf. Syst._ **2004** , _22_ , 143–177. [CrossRef] 

107. Karypis, G. Evaluation of Item-Based Top- _N_ Recommendation Algorithms. In Proceedings of the Tenth International Conference on Information and Knowledge Management—CIKM’01, Atlanta, GA, USA, 5–10 November 2001; p. 247. [CrossRef] 

108. Zhao, S.; Zhou, M.X.; Yuan, Q.; Zhang, X.; Zheng, W.; Fu, R. Who is talking about what: Social map-based recommendation for content-centric social websites. In Proceedings of the Fourth ACM Conference on Recommender Systems, Barcelona, Spain, 26–30 September 2010; pp. 143–150. 

109. Valcarce, D.; Bellogín, A.; Parapar, J.; Castells, P. On the robustness and discriminative power of information retrieval metrics for top-N recommendation. In Proceedings of the 12th ACM Conference on Recommender Systems, Vancouver, BC, Canada, 2–7 October 2018; pp. 260–268. [CrossRef] 

110. Cremonesi, P.; Koren, Y.; Turrin, R. Performance of recommender algorithms on top-n recommendation tasks. In Proceedings of the fourth ACM conference on Recommender systems—RecSys ’10, Barcelona, Spain, 26–30 September 2010; p. 39. [CrossRef] 

111. Tong, H.; Faloutsos, C.; Pan, J.Y. Fast random walk with restart and its applications. In Proceedings of the Sixth International Conference on Data Mining (ICDM’06), Hong Kong, China, 18–22 December 2006; IEEE: Piscataway, NJ, USA, 2006; pp. 613–622. 

112. Celma, Ò.; Herrera, P. A new approach to evaluating novel recommendations. In Proceedings of the 2008 ACM Conference on Recommender Systems, Lausanne, Switzerland, 23–25 October 2008; pp. 179–186. 

113. Merton, R.K.; Barber, E. The travels and adventures of serendipity. In _The Travels and Adventures of Serendipity_ ; Princeton University Press: Princeton, NJ, USA, 2011. 

114. Leong, T.W.; Vetere, F.; Howard, S. The serendipity shuffle. In Proceedings of the 17th Australia Conference on Computer-Human Interaction: Citizens Online: Considerations for Today and the Future, Canberra, Australia, 21–25 November 2005; pp. 1–4. 

115. Kotkov, D.; Konstan, J.A.; Zhao, Q.; Veijalainen, J. Investigating serendipity in recommender systems based on real user feedback. In Proceedings of the 33rd Annual ACM Symposium on Applied Computing, Pau, France, 9–13 April 2018; pp. 1341–1350. [CrossRef] 

116. Maccatrozzo, V.; Terstall, M.; Aroyo, L.; Schreiber, G. SIRUP: Serendipity In Recommendations via User Perceptions. In Proceedings of the 22nd International Conference on Intelligent User Interfaces, Limassol, Cyprus, 13–16 March 2017; pp. 35–44. [CrossRef] 

117. Sarkar, P.; Chakrabarti, A. Studying engineering design creativity-developing a common definition and associated measures. In Proceedings of the NSF Workshop on Studying Design Creativity, Aix-en-Provence, France, 10–11 March 2008; p. 20. 

_Information_ **2025** , _16_ , 151 

26 of 26 

118. Carnovalini, F.; Rodà, A. Computational Creativity and Music Generation Systems: An Introduction to the State of the Art. _Front. Artif. Intell._ **2020** , _3_ , 14. [CrossRef] [PubMed] 

119. Jordanous, A. Four PPPPerspectives on computational creativity in theory and in practice. _Connect. Sci._ **2016** , _28_ , 194–216. [CrossRef] 

120. Hodson, J. The Creative Machine. In Proceedings of the ICCC, Atlanta, GA, USA, 19–23 June 2017; pp. 143–150. 

121. Wiggins, G.A. Computational Creativity and Consciousness: Framing, Fiction and Fraud Paper type: Study Paper. In Proceedings of the 12th International Conference on Computational Creativity (ICCC ’21), México City, Mexico, 14–18 September 2021; p. 10. 

122. Jordanous, A. Evaluating Evaluation: Assessing Progress and Practices in Computational Creativity Research. In _Computational Creativity: The Philosophy and Engineering of Autonomously Creative Systems_ ; Veale, T., Cardoso, F.A., Eds.; Computational Synthesis and Creative Systems; Springer International Publishing: Cham, Switzerland, 2019; pp. 211–236. [CrossRef] 

123. Boden, M.A. _The Creative Mind: Myths and Mechanisms_ ; Routledge: London, UK, 2004. 

124. Wiggins, G.A. A Framework for Description, Analysis and Comparison of Creative Systems. In _Computational Creativity: The Philosophy and Engineering of Autonomously Creative Systems_ ; Veale, T., Cardoso, F.A., Eds.; Computational Synthesis and Creative Systems; Springer International Publishing: Cham, Switzerland, 2019; pp. 21–47. [CrossRef] 

125. Ferro, N.; Fuhr, N.; Grefenstette, G.; Konstan, J.A.; Castells, P.; Daly, E.M.; Declerck, T.; Ekstrand, M.D.; Geyer, W.; Gonzalo, J.; et al. The Dagstuhl Perspectives Workshop on Performance Modeling and Prediction. _Acm SIGIR Forum_ **2018** , _52_ , 91–101. [CrossRef] 

126. Colton, S.; Wiggins, G.A. Computational creativity: The final frontier? In Proceedings of the ECAI, Montpellier, France, 27–31 August 2012; Volume 2012, pp. 21–26. 

127. Jordanous, A. A standardised procedure for evaluating creative systems: Computational creativity evaluation based on what it is to be creative. _Cogn. Comput._ **2012** , _4_ , 246–279. [CrossRef] 

**Disclaimer/Publisher’s Note:** The statements, opinions and data contained in all publications are solely those of the individual author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to people or property resulting from any ideas, methods, instructions or products referred to in the content. 

