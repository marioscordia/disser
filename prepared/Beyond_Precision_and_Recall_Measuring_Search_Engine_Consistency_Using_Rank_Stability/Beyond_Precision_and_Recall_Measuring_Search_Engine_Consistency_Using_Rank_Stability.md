
![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0001-00.png)


Received 24 March 2025, accepted 10 May 2025, date of publication 19 May 2025, date of current version 2 June 2025. _Digital Object Identifier 10.1109/ACCESS.2025.3571184_ 

## Beyond Precision and Recall: Measuring Search Engine Consistency Using Rank Stability 

## KRISHNAN BATRI 1, RAJERMANI THINAKARAN 2, S. LAKSHMI 3, R. SOWRIRAJAN 4, AND SIVARAM MURUGAN 5 

1School of Computer Science and Engineering, Jain University, Bengaluru, Karnataka 560069, India 

2Faculty of Data Science and Information Technology, INTI International University, Nilai, Negeri Sembilan 71800, Malaysia 

3Department of Electronics and Communication Engineering, Jain University, Bengaluru, Karnataka 560069, India 

4Department of Mathematics, Dr. N. G. P. Arts and Science College, Coimbatore, Tamil Nadu 641035, India 

5Department of Computer Engineering, Faculty of Engineering and Natural Sciences, Sivas University of Science and Technology, 58000 Sivas, Türkiye 

Corresponding author: S. Lakshmi (lakshmi.s@jainuniversity.ac.in) 

**ABSTRACT** Traditional information retrieval metrics assess document relevance but neglect ranking stability—a critical factor in today’s dynamic web environments where search algorithms constantly evolve. We present _Rmeasure_ , a comprehensive framework that quantifies search engine consistency by analyzing both overlapping and non-overlapping results through the lens of psychophysical principles, particularly the Weber-Fechner Law. Our three-component approach ( _Roverlap_ , _Rnon-overlap_ , and _Rcomprehensive_ ) provides multidimensional insights into ranking variations. Experimental evaluation across Google and Bing using diverse query types reveals significant performance differences: Bing demonstrates superior ranking stability (minimum _Roverlap_ of 0.0527), while Google exhibits considerable fluctuation ( _Rnon-overlap_ reaching 0.3653), especially for high-volume queries. Statistical measures confirm Bing’s consistency advantage, with Google showing rank differences averaging up to 21.622 positions. Beyond technical contributions, _Rmeasure_ advances UN Sustainable Development Goals by enhancing information access equity (SDG 4), fostering innovation in search technology evaluation (SDG 9), and promoting consistent retrieval experiences across diverse user populations (SDG 10). By integrating perceptual modeling with rank-based analytics, _Rmeasure_ extends search engine evaluation beyond traditional relevance metrics, offering a robust methodology for assessing real-world search performance. 

- **INDEX TERMS** Search engine evaluation, rank correlation, rank stability, repeated queries, ranking consistency, overlapping results, non-overlapping results, psychophysical modeling, Weber-Fechner Law, information retrieval, Rmeasure framework, Google, Bing. 

## **I. INTRODUCTION** 

Search engine ranking inconsistency poses a significant challenge in the modern information ecosystem, undermining user experience and information retrieval effectiveness despite the revolutionary impact of the World Wide Web (WWW) on information access [1]. While multiple search engines compete for market share, users typically develop loyalty to a specific platform based on perceived reliability and result quality. However, this perceived reliability is continuously tested by dynamic ranking algorithms, real- 

The associate editor coordinating the review of this manuscript and approving it for publication was Mohamed Elhoseny . 

time indexing updates, and personalization mechanisms that produce inconsistent results across identical queries. Evaluating and quantifying this ranking stability represents a critical yet underexplored dimension of search engine performance assessment. 

Traditional Information Retrieval (IR) metrics, such as precision, recall, and F-measure, focus primarily on document relevance but fail to capture the temporal stability of search rankings [2]. These conventional metrics rely on predefined relevance judgments that are inherently subjective and context-dependent. Furthermore, they inadequately account for the ranked order of retrieved results—a factor that significantly influences user behavior, as research demonstrates 

2025 The Authors. This work is licensed under a Creative Commons Attribution 4.0 License. For more information, see https://creativecommons.org/licenses/by/4.0/ 

92242 

VOLUME 13, 2025 

K. Batri et al.: Beyond Precision and Recall: Measuring Search Engine Consistency 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0002-01.png)


that users predominantly interact with the top-ranked search results, often ignoring lower-ranked alternatives [3]. As a result, these established IR metrics provide an incomplete picture of search engine performance from a user-centric perspective. 

The variability in search results across repeated identical queries represents a fundamental limitation of current search technologies. When users submit the same query multiple times, they may encounter different rankings or entirely different result sets due to continuous indexing updates, personalization algorithms, and real-time ranking adjustments. These frequent fluctuations can erode user confidence and create frustration when attempting to relocate previously discovered information. Despite its significant impact on user experience and information accessibility, the dimension of search result stability remains inadequately addressed in contemporary evaluation frameworks. This research gap necessitates the development of robust metrics that can effectively quantify rank stability across temporally separated searches. 

Existing rank correlation measures, including Kendall’s Tau and Spearman’s Rho, offer mathematical frameworks for quantifying similarity between ranked lists [4]. However, these traditional measures operate under the assumption that both compared lists contain identical elements arranged in different orders—an assumption that rarely holds in web search scenarios. Modern search engines continuously index an expanding universe of documents, resulting in both overlapping and non-overlapping results across search instances [5]. Consequently, applying conventional rank correlation measures without appropriate modification can yield incomplete or potentially misleading insights into search result consistency. 

The phenomenon of ranking inconsistency can be understood through the lens of psychophysical principles, particularly the Weber-Fechner Law, which establishes that perceived intensity follows a logarithmic function of actual stimulus intensity [6]. When applied to search ranking behavior, this principle suggests that initial query repetitions produce noticeable ranking variations, but subsequent repetitions yield progressively smaller perceptible changes. This pattern indicates that search engines dynamically adjust their rankings over repeated queries before eventually stabilizing. Incorporating this psychological insight into search evaluation methodologies enables a more nuanced and realistic assessment of ranking stability across time. 

Recent empirical studies on search engine ranking dynamics further highlight the need for enhanced evaluation metrics [7]. For instance, Dean’s [8] comprehensive analysis of 11.8 million Google search results identified content quality, backlink profiles, and user engagement signals as key ranking factors that contribute to result variability. These findings align with our research focus on ranking stability and validate the need for specialized metrics. Additionally, advanced rank correlation coefficients such as AP correlation ( _τAP_ ) have emerged, offering probabilistic interpretations 

of ranking consistency that better reflect real-world user interactions [9]. These developments underscore the evolving nature of search evaluation methodologies and the critical need for novel measures that account for the complex, dynamic behaviors of modern search algorithms. 

To address these identified gaps, this study introduces a novel rank correlation measure specifically designed for evaluating web search engines. Unlike conventional correlation measures, our approach separately accounts for both overlapping and unique documents while incorporating the effects of query repetition over time. By capturing the systematic rank shifts introduced by search engines in response to repeated identical queries, our method provides a more comprehensive assessment of ranking stability. We validate our approach through empirical experiments on major search engines including Google and Bing, offering new insights into search consistency patterns across platforms. 

- The key contributions of this research are as follows: 

- 1) Identification and analysis of fundamental limitations in conventional IR metrics for evaluating search engine performance, with particular emphasis on the need for rank stability assessment. 

- 2) Integration of Weber-Fechner Law principles to explain and model ranking fluctuations resulting from query repetition effects. 

- 3) Development of a novel rank correlation measure that independently evaluates both overlapping and nonoverlapping search results to provide a more granular assessment of ranking stability. 

- 4) Comprehensive empirical evaluation of ranking consistency across major commercial search engines, revealing platform-specific patterns and providing actionable insights for search engine optimization and user experience enhancement. 

The remainder of this paper is structured as follows: Section II reviews related work on search engine evaluation and rank correlation measures. Section III presents the proposed rank correlation approach and its mathematical formulation. Section IV describes the experimental setup, datasets, and evaluation methodology. Section V discusses the results and key findings. Finally, Section VI concludes the paper and suggests potential directions for future research. 

## **II. RELATED WORK** 

The evaluation of search engine performance has traditionally centered around relevance-based metrics such as precision, recall, and F-measure. These metrics assess retrieval accuracy effectively but fail to capture the temporal or perceptual stability of ranking, a critical dimension of user experience in dynamic search environments. As search engines continuously evolve through real-time indexing, algorithmic experimentation, and personalization, ranking consistency needs more sophisticated evaluation frameworks. 

Correlation coefficients are widely used in statistical analysis to measure relationships between variables. Pearson’s correlation coefficient ( _r_ ) is suitable for linear relationships 

92243 

VOLUME 13, 2025 

K. Batri et al.: Beyond Precision and Recall: Measuring Search Engine Consistency 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0003-01.png)


between continuous variables [10]. For ranking similarity, Kendall’s Tau and Spearman’s Rho are popular nonparametric alternatives [9]. However, both assume full overlap between ranked lists—an assumption rarely satisfied in web search due to ongoing index changes and query contextualization. 

To mitigate these limitations, variations such as Weighted Kendall’s Tau [11] and adaptive correlation measures [12] were introduced, prioritizing top-ranked items and adapting to shifting rankings. Yet, they still underperform in settings with significant non-overlap between result sets. Moreover, their distance functions do not incorporate perceptual models of user sensitivity to changes in rank. 

Psychophysical principles, such as the Weber-Fechner Law [13], have been used to explain how perceived intensity varies logarithmically with stimulus changes. This model suggests that users are more sensitive to ranking differences at the top of a result list. Incorporating such principles into ranking evaluation—e.g., through attention-weighted or perception-aware metrics—offers a more user-aligned assessment framework [14]. 

Beyond traditional correlation metrics, more robust methods have emerged. _AP Correlation_ ( _τAP_ ) accounts for the average precision between ranked lists and reflects early-position sensitivity [15]. _Rank-Biased Overlap (RBO)_ supports incomplete and indefinite lists using a probabilistic decay model and has gained popularity for handling nonoverlapping ranks effectively [16]. Semantic similarity-based techniques [17] and probabilistic inference models [18] further enhance alignment across evolving results but typically require external knowledge bases or complex models. 

Table 1 summarizes key characteristics of major rank correlation techniques. 

Scalable frameworks have also been explored. Adaptive sampling methods extract representative subsets for evaluation [19], while progressive evaluation frameworks assess search rankings as results arrive incrementally [20]. Such techniques reduce computational cost while maintaining evaluation robustness in expanding web corpora. 

Modern research trends emphasize automation and context adaptation in search evaluation. Emerging methods include machine learning-based metric selection [21], real-time evaluation tools [22], and context-aware assessment [23], aligning ranking behavior with personalized user expectations. 

Despite these advances, no existing metric unifies: 

- Rank-based stability for both overlapping and nonoverlapping results, 

- Temporal sensitivity across repeated queries, 

- Perception-aware modeling of rank changes. 

To address these gaps, we introduce **Rmeasure** , a novel rank correlation framework comprising _Roverlap_ , _Rnonoverlap_ , and _Rcomprehensive_ components. Rmeasure uniquely integrates statistical variation and psychophysical modeling to evaluate the consistency of web search rankings 

across repeated queries, even when the result sets are only partially overlapping. 

## **III. MATHEMATICAL PROOF OF TRADITIONAL IR METRICS’ INADEQUACY USING INFORMATION GAIN/LOSS** 

Traditional Information Retrieval (IR) metrics such as precision, recall, and F1-score evaluate document relevance but fail to assess ranking stability. Users expect a reasonable level of consistency in search results over repeated queries. However, search engines dynamically update their rankings, leading to variations that conventional metrics fail to capture. This section establishes a formal mathematical proof demonstrating that traditional IR metrics remain unchanged despite search result instability. 

## _A. INFORMATION TURNOVER FRAMEWORK_ 

To measure ranking stability, we introduce an **Information Turnover Framework** , which quantifies document changes in retrieved results across repeated queries. 

_Definition 1 (Retrieved Result Set):_ Let _Q_ be a query executed at two time points _t_ 1 and _t_ 2, yielding result sets: 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0003-20.png)


where _R_ ( _Q, t_ ) denotes the top _n_ ranked documents retrieved at time _t_ . 

_Definition 2 (Information Gain and Loss):_ We define: 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0003-23.png)



![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0003-24.png)


where: - _Information Gain_ refers to newly introduced documents at _t_ 2 that were absent at _t_ 1. - _Information Loss_ refers to documents removed from _t_ 1 that no longer appear in _t_ 2. 

_Definition 3 (Information Turnover):_ Total instability in search results is computed as: 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0003-27.png)


_Definition 4 (Normalized Information Turnover):_ To facilitate comparisons across different queries, we define a normalized version: _IT_ ( _Q, t_ 1 _, t_ 2) _NIT_ ( _Q, t_ 1 _, t_ 2) = (5) | _R_ ( _Q, t_ 1) ∪ _R_ ( _Q, t_ 2)| _[.]_ 

where 0 ≤ _NIT_ ≤ 1 . A value of: - _NIT_ = 0 indicates perfect stability (identical result sets across queries). - _NIT_ = 1 represents complete turnover (entirely different result sets). 

## _B. THEOREM: FUNDAMENTAL LIMITATION OF TRADITIONAL IR METRICS_ 

_Theorem III-B (Invariance of Traditional Metrics to Result Turnover):_ For any query _Q_ and time points _t_ 1 and _t_ 2, there exist distinct result sets _R_ ( _Q, t_ 1) and _R_ ( _Q, t_ 2) such that all traditional IR metrics remain unchanged, while _IT_ ( _Q, t_ 1 _, t_ 2) can be arbitrarily large. 

92244 

VOLUME 13, 2025 

K. Batri et al.: Beyond Precision and Recall: Measuring Search Engine Consistency 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0004-01.png)


**TABLE 1.** Comparison of rank correlation metrics. 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0004-03.png)


_Proof:_ Let _k >_ 0 be the number of top results considered. Assume: 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0004-05.png)



![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0004-06.png)


where all documents are relevant. 

Since all retrieved documents remain relevant, the precision, recall, and F1-score are: 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0004-09.png)



![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0004-10.png)



![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0004-11.png)


However, the **Information Turnover** is: 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0004-13.png)



![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0004-14.png)



![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0004-15.png)


This proves that traditional IR metrics remain unchanged despite complete instability, contradicting their effectiveness in measuring ranking stability. 

Solving for | _O_ |: 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0004-18.png)


The number of changed documents is: 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0004-20.png)


Approximating to an integer: 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0004-22.png)


By adjusting | _D_ change|, we achieve any desired stability level while keeping IR metrics unchanged. 

## **IV.** _**R**_ **MEASURE: A POSITION-BASED PERFORMANCE METRIC FOR WEB SEARCH ENGINES** 

Web search evaluation faces a fundamental challenge when comparing different search engines: how do we assess ranking quality when search results don’t completely overlap? Traditional metrics work well when result sets are identical, but fall short when search engines return partially or entirely different web pages. _R_ measure addresses this critical gap by providing a comprehensive framework for evaluating search engine performance across both overlapping and nonoverlapping results. 

## _A. CORE PROBLEM IN SEARCH ENGINE EVALUATION_ 

## _C. COROLLARY: EXISTENCE OF CONTROLLED STABILITY LEVELS_ 

_Corollary III-C (Controllable Result Stability):_ For any stability level 0 ≤ _v_ ≤ 1 , there exist result sets with identical IR metrics that exhibit a normalized information turnover exactly equal to _v_ . 

_Proof:_ Given a result set size _k_ , let the overlap size be: 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0004-30.png)


We define: 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0004-32.png)


Substituting into (5): 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0004-34.png)


When two search engines return different sets of results for the same query, conventional metrics become insufficient because: 

- They typically assume result sets are identical or highly similar 

- They cannot meaningfully compare ranking quality across different document sets 

- They fail to capture the psychological impact of ranking variations on users 

_R_ measure resolves these limitations through a twocomponent approach that separately evaluates overlapping and non-overlapping results, followed by a comprehensive metric that combines these components. 

## _B. THE ROVERLAP COMPONENT_ 

The _R_ overlap metric quantifies ranking consistency for web pages that appear in both result sets. It measures how 

92245 

VOLUME 13, 2025 

K. Batri et al.: Beyond Precision and Recall: Measuring Search Engine Consistency 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0005-01.png)


similarly the common documents are positioned across different search engines. 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0005-03.png)


## where: 

- _A_ and _B_ represent the result sets from two different search engines 

- _rA_ ( _x_ ) and _rB_ ( _x_ ) denote the rank positions of web page _x_ in sets _A_ and _B_ 

- _n_ is the maximum number of results considered (e.g., top-10 or top-20) 

- | _A_ ∩ _B_ | is the number of common results between sets _A_ and _B_ 

- | _A_ ∪ _B_ | is the total number of unique results across both sets 

The first bracketed term calculates the average normalized rank difference for overlapping results. The second term ( | _A_ ∪ _nB_ |[)][applies][a][scaling][factor][that][accounts][for][the][degree] of overlap between result sets. 

The _R_ overlap metric produces values in the range [0 _,_ 1], where: 

- _R_ overlap = 0 _._ 0 indicates perfect ranking consistency (all common results maintain identical rank positions) 

- _R_ overlap = 1 _._ 0 represents maximum ranking inconsistency (common results appear at opposite ends of the rankings) 

Lower _R_ overlap values signify greater ranking stability across search engines. 

## _C. PSYCHOLOGICAL FOUNDATION: THE WEBER-FECHNER LAW_ 

The _R_ overlap metric is grounded in the Weber-Fechner Law from psychophysics, which models how humans perceive changes in stimulus intensity: 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0005-17.png)


## 1) PRACTICAL APPROACH TO TEMPORAL STABILITY ASSESSMENT 

To overcome this limitation, _R_ measure employs a pragmatic approach: instead of waiting for extended periods, we repeatedly submit identical queries within a short timeframe. This technique serves as a proxy for temporal stability assessment, as modern search engines typically exhibit variations in results even for identical queries executed in quick succession. These variations arise from: 

- Index updates that occur continuously rather than at fixed intervals 

- Load balancing across distributed server farms 

- Randomized elements in ranking algorithms 

- A/B testing of algorithm modifications 

- Personalization factors that may fluctuate even within short periods 

By analyzing these short-term variations, we can infer how the search engine might behave over longer time horizons without waiting for those periods to elapse. This approach provides a practical approximation of temporal stability while enabling timely evaluation. 

## 2) STATISTICAL REFINEMENTS FOR REPEATED QUERIES 

To quantify performance across repeated queries, _R_ measure introduces several statistical refinements: 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0005-28.png)



![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0005-29.png)


where _RO_ represents the set of all _R_ overlap values calculated across multiple query repetitions. The size of this set is determined by: 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0005-31.png)


With _rf_ representing the repetition factor (how many times each query is executed). 

where: 

- _S_ represents the perceived sensation intensity 

- _I_ is the actual stimulus intensity 

- _I_ 0 is the reference intensity level 

- _k_ is a scaling constant 

This logarithmic relationship explains why _R_ overlap doesn’t simply use linear rank differences. Human perception of ranking changes follows a similar logarithmic pattern—small changes in top positions (e.g., from rank 1 to rank 2) are perceived as more significant than the same absolute change further down the list (e.g., from rank 9 to rank 10). 

## _D. ACCOMMODATING QUERY REPETITION_ 

In an ideal evaluation scenario, we would measure search result stability over extended time periods (e.g., days or weeks) to capture how ranking algorithms evolve and affect user experience. However, waiting for such long intervals is impractical for timely evaluation. 

## 3) INTERPRETATION OF QUERY REPETITION METRICS 

These statistical measures provide valuable insights into search engine stability: 

- _RO_ minmin: The best-case scenario for ranking consistency 

- _RO_ minmax: The worst-case scenario for ranking consistency 

- _RO_ ave: The average ranking consistency across all query repetitions 

- _RO_ -Diff: The spread between these values, indicating overall stability 

A stable search engine will show minimal variation in 

_R_ overlap values across query repetitions, while an unstable one will exhibit significant fluctuations. These short-term fluctuations serve as a reasonable proxy for long-term stability, allowing evaluators to assess temporal consistency without the delays associated with extended time periods. 

92246 

VOLUME 13, 2025 

K. Batri et al.: Beyond Precision and Recall: Measuring Search Engine Consistency 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0006-01.png)


## _E. ALGORITHMIC IMPLEMENTATION FOR ROVERLAP_ 

The calculation of _RO_ variations follows this systematic procedure: 

## **Algorithm 1** Calculation of _RO_ Variations 

## **Require:** Repetition factor _rf_ , Query _q_ 

**Ensure:** _RO_ minmin, _RO_ minmax, _RO_ ave, and _RO_ -Diff 

- 1: Initialize _RO_ ←∅ 

- 2: **for** _i_ = 1 to _rf_ **do** 

- 3: Submit query _q_ and store returned web pages in _Ai_ 4: **for** _j_ = _i_ + 1 to _rf_ **do** 

- 5: Submit query _q_ again and store returned web pages in _A j_ 

- 6: Compute _R_ overlap between _Ai_ and _Aj_ using Equation (20) 

- 7: _RO_ ← _RO_ ∪{ _R_ overlap} 

- 8: **end for** 9: **end for** 

- 10: _RO_ minmin ← min( _RO_ ) 

- 11: _RO_ minmax ← max( _RO_ ) 1 

- 12: _RO_ ave ← | _RO_ | � _Y_ ∈ _RO[Y]_ 13: _RO_ -Diff ← max _Y_ ∈ _RO_ | _Y_ − _RO_ minmin| 

## **V. THE** _**R**_ **NON-OVERLAP COMPONENT** 

In web search engine evaluation, comparing result sets _A_ and _B_ often reveals varying degrees of overlap. When these sets are not identical or only partially overlap, traditional metrics like _R_ overlap become inadequate, as they can only analyze common elements between sets. This limitation becomes particularly problematic when evaluating the ranking behavior of non-common web pages. 

We introduce _R_ non-overlap, a comprehensive metric designed to analyze ranking patterns of unique web pages that appear exclusively in one result set. This metric requires at least one non-common web page between sets _A_ and _B_ to be applicable. When sets are completely identical, _R_ non-overlap is undefined and defaults to zero. 

## _A. FORMAL DESIGN OF RNON-OVERLAP_ 

For any query, a search engine retrieves _m_ relevant web pages, though typically only the first _n_ results are displayed due to pagination constraints. Our analysis focuses on these top _n_ results, effectively transforming an unbounded result set into a finite one through truncation. 

In the context of repeated queries, we consider a web page relevant if it appears in at least one of the retrieved result sets. The design of _R_ non-overlap specifically targets the analysis of unique web pages that exist in one set but not the other. 

1) RANK ASSIGNMENT AND MATHEMATICAL FORMULATION Let us consider a web page _X_ that exists in set _A_ but not in set _B_ . While _X_ has a well-defined rank _rA_ ( _X_ ) in set _A_ , its rank in set _B_ is undefined. We postulate that _X_ could have a rank in 

_B_ anywhere between _n_ + 1 and _m_ , represented as: 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0006-23.png)


This fundamental assumption leads to our formulation of _R_ non-overlap: 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0006-25.png)


where: 

- _A_ − _B_ represents the set of web pages that appear in set _A_ but not in set _B_ 

- _rA_ ( _X_ ) is the rank position of web page _X_ in set _A_ 

- _n_ is the maximum number of results considered 

- | _A_ ∩ _B_ | is the number of common results between sets _A_ and _B_ 

The first term quantifies the positional disparity of unique elements, while the second term weights this by the proportional overlap between sets. 

## _B. BOUNDARY ANALYSIS OF RNON-OVERLAP_ 

We analyze the range of _R_ non-overlap under two boundary conditions: 

## 1) LOWER BOUND 

When sets _A_ and _B_ share no common elements ( _A_ ∩ _B_ = ∅), then | _A_ ∩ _B_ | = 0. Substituting into Equation (27) yields _R_ non-overlap = 0 _._ 0. 

## 2) UPPER BOUND 

When set _A_ contains precisely one element not present in _B_ (| _A_ − _B_ | = 1) and this element appears at the highest rank ( _rA_ ( _X_ ) = 1), we can simplify Equation (27): 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0006-38.png)


As _n_ increases and | _A_ ∩ _B_ | approaches _n_ , _R_ non-overlap approaches 1.0. Therefore: 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0006-40.png)


An optimal ranking algorithm minimizes _R_ non-overlap, while a suboptimal algorithm produces higher values. This behavior aligns with the intuition that effective search engines should maintain consistent rankings across repeated queries. 

## _C. STATISTICAL VARIATION AND ALGORITHMIC COMPUTATION OF RNON-OVERLAP_ 

When queries are repeated multiple times with repetition factor _rf_ , we observe � _rf_ 2 � possible _R_ non-overlap values. To systematically analyze this variation, we first determine 

92247 

VOLUME 13, 2025 

K. Batri et al.: Beyond Precision and Recall: Measuring Search Engine Consistency 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0007-01.png)


_RN_ min, the minimum observed _R_ non-overlap value, and then compute the deviation set: 

_RN_ Diff = {| _RN_ min − _Y_ |; ∀ _Y_ ∈ _RN , Y_ ̸= _RN_ min} (30) 

From this set, we derive three key statistical measures: 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0007-05.png)


These metrics collectively quantify the stability and consistency of the ranking algorithm under repeated queries. 

_D. ALGORITHMIC IMPLEMENTATION FOR RNON-OVERLAP_ Algorithm 2 outlines the steps to determine _RN_ Diff and its derived statistics. 

**Algorithm 2** _RN_ Diff Calculation Procedure 

**Require:** Repetition factor _rf_ , Number of results _n_ 

**Ensure:** _RN_ min, _RN_ Diff, _RN_ minmin, _RN_ minmax, _RN_ ave 

- 1: Initialize _RN_ as a matrix of size _rf_ × _rf_ 

- 2: **for** _i_ = 1 to _rf_ **do** 

- 3: Execute query and retrieve the top _n_ web pages as set _Ai_ 

- 4: **for** _j_ = _i_ + 1 to _rf_ **do** 

- 5: Execute query again and retrieve the top _n_ web pages as set _Aj_ 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0007-16.png)


- 7: **end for** 

- 8: **end for** 

- 9: _RN_ min = min{ _RN_ [ _i_ ][ _j_ ] _>_ 0 : 1 ≤ _i < j_ ≤ _rf_ } 

- 10: _RN_ Diff = {| _RN_ min − _RN_ [ _i_ ][ _j_ ]| : _RN_ [ _i_ ][ _j_ ] ̸= _RN_ min _,_ 1 ≤ _i < j_ ≤ _rf_ } 

- 11: _RN_ minmin = min( _RN_ Diff) 

- 12: _RN_ minmax = max( _RN_ Diff) 

- 13: _RN_ ave = | _RN_ 1Diff| � _Z_ ∈ _RN_ Diff _[Z]_ 14: **return** _RN_ min, _RN_ Diff, _RN_ minmin, _RN_ minmax, _RN_ ave 

## _E. IMPLICATIONS FOR SEARCH ENGINE EVALUATION_ 

The _R_ non-overlap metric addresses a crucial evaluation gap by providing meaningful analysis of non-common search results. This approach offers several advantages for comprehensive search engine assessment: 

- It captures information about ranking behavior that traditional overlap-only metrics miss 

- It provides a mathematical framework for evaluating result consistency even when different pages are returned 

- It enables fair comparison between search engines with different retrieval strategies 

- It produces meaningful statistics that can identify unstable ranking algorithms 

By combining _R_ overlap with _R_ non-overlap, evaluators gain a more complete picture of search engine performance across both common and unique results. This holistic approach more accurately reflects the user experience, where both the consistency of familiar results and the relevance of unique discoveries matter. 

## **VI.** _**R**_ **COMPREHENSIVE: A UNIFIED APPROACH TO RANKING CONSISTENCY** 

When evaluating search engine performance across multiple queries, we need a holistic metric that considers both overlapping and non-overlapping results. While _R_ overlap quantifies consistency for common web pages and _R_ non-overlap measures behavior for unique results, these metrics in isolation provide only partial insights into overall ranking performance. To address this limitation, we introduce _R_ comprehensive, a unified framework that integrates both perspectives. 

## _A. FORMAL DEFINITION OF RCOMPREHENSIVE_ 

The _R_ metric combines _R_ and _R_ comprehensive overlap non-overlap using a weighted approach: 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0007-35.png)


where: 

- _α_ is a weighting factor in the range [0 _,_ 1] that determines the relative importance of each component 

- _R_ overlap quantifies ranking consistency for common results as defined in Equation (20) 

- _R_ non-overlap measures ranking behavior for unique results as defined in Equation (27) 

This formulation ensures that _R_ maintains the comprehensive same interpretable range as its component metrics: 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0007-41.png)


As with the individual metrics, lower values of _R_ comprehensive indicate greater ranking consistency, with 0 _._ 0 representing perfect stability and 1 _._ 0 indicating maximum inconsistency. _B. PARAMETER SELECTION AND ADAPTATION_ The weighting parameter _α_ provides flexibility in emphasizing different aspects of ranking behavior based on evaluation priorities: 

- _α_ = 0 _._ 5: Equal weighting between overlap and non-overlap components, suitable for general evaluation scenarios where both aspects are equally important 

- _α >_ 0 _._ 5: Greater emphasis on ranking consistency of common results, appropriate for contexts where users are likely to focus on familiar web pages 

- _α <_ 0 _._ 5: Greater emphasis on handling of unique results, beneficial when evaluating search engines’ ability to introduce diverse or novel content 

92248 

VOLUME 13, 2025 

K. Batri et al.: Beyond Precision and Recall: Measuring Search Engine Consistency 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0008-01.png)


## _C. JUSTIFICATION OF WEIGHTING STRATEGY AND HANDLING OF UNCERTAINTY_ 

The proposed _Rcomprehensive_ metric combines _Roverlap_ and _Rnon-overlap_ using a convex linear combination controlled by the weighting factor _α_ ∈ [0 _,_ 1]: 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0008-04.png)


In our current implementation, the value of _α_ is set to 0.5, implying an equal emphasis on overlapping and nonoverlapping ranking behavior. This default choice is intended as a balanced baseline to initiate comparison. However, we acknowledge that this selection lacks a formal theoretical justification. To evaluate the effect of the weighting factor, we conducted a sensitivity analysis by varying _α_ from 0.1 to 0.9 in increments of 0.1. The experiments were repeated across the complete set of Googlewhack and biographical queries for both Google and Bing. 

Our observations indicate that in high-overlap scenarios, such as those associated with Googlewhack queries, the value of _R_ comprehensive remains relatively stable across changes in _α_ . However, in lower-overlap cases—especially for high-volume queries on Google—the metric demonstrates significant sensitivity to the value of _α_ . This finding suggests that an adaptive or data-driven approach to determining the weighting factor may be more appropriate than a static assignment. As a future extension, we propose learning _α_ via query-specific optimization techniques, such as crossvalidation on user feedback, minimization of empirical rank deviation, or entropy-based heuristics that reflect the relative information certainty in overlapping versus non-overlapping result segments. 

Additionally, the current formulation treats all ranking observations as deterministic and does not explicitly incorporate uncertainty, despite the stochastic nature of web search outputs caused by personalization, load balancing, and algorithm experimentation. To enhance robustness, the incorporation of uncertainty-aware fusion strategies is a promising direction. This may involve the use of fuzzy integrals, such as the Choquet or Sugeno integrals, which allow interaction modeling under vagueness, or evidencebased methods such as Dempster-Shafer theory to express confidence levels in rank agreement. Interval-based or probabilistic ranking formulations could also be employed, allowing each ranked position to be represented as a range or distribution rather than a fixed value. These extensions would enable Rmeasure to model not only structural rank variation but also the degree of certainty associated with each ranking instance, thereby strengthening its applicability in real-world, noisy search environments. 

## component parts: 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0008-09.png)



![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0008-10.png)


where: 

- _RO_ minmin, _RO_ minmax, _RO_ ave represent the statistical metrics derived from _R_ overlap values 

- _RN_ minmin, _RN_ minmax, _RN_ ave represent the corresponding metrics from _R_ non-overlap values 

These combined measures provide a comprehensive view of ranking consistency across both overlapping and nonoverlapping results. To further quantify the stability of _R_ comprehensive across repeated queries, we define the deviation measure: 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0008-15.png)


where _RC_ represents the set of all _R_ comprehensive values calculated across multiple query repetitions, and _RC_ min is the minimum value in this set. 

_E. ALGORITHMIC IMPLEMENTATION FOR RCOMPREHENSIVE_ Algorithm 3 outlines the systematic procedure for calculating _R_ comprehensive and its statistical variations: 

|**Algorithm 3**Calculation of_R_comprehensiveVariations|**Algorithm 3**Calculation of_R_comprehensiveVariations|**Algorithm 3**Calculation of_R_comprehensiveVariations||
|---|---|---|---|
|**Require:** Repetition factor_rf_, Query_q_, Weight_α_||||
|**Ensure:** _RC_minmin,_RC_minmax,_RC_ave, and_RC_-Diff||||
|1:|Initialize_RC_ ←∅|||
|2:|**for**_i_=1 to_rf_ **do**|||
|3:|Submit query_q_and store returned web pages in||_Ai_|
|4:|**for**_j_=_i_+1 to_rf_ **do**|||
|5:|Submit query_q_again and store returned web||pages|
||in_Aj_|||
|6:|Compute<br>_R_overlap<br>between<br>_Ai_<br>and|_Aj_|using|
||Equation(20)|||
|7:|Compute _R_non-overlap between _Ai_ and|_Aj_|using|
||Equation(27)|||
|8:|_R_comprehensive ←_α_×_R_overlap+(1−_α_)×_R_non-overlap|||
|9:|_RC_ ←_RC_ ∪{_R_comprehensive}|||
|10:|**end for**|||
|11:|**end for**|||
|12:|_RC_min ←min(_RC_)|||
|13:|_RC_minmin ←min{|_RC_min−_Y_| |_Y_ ∈_RC, Y_ =_RC_min}|||
|14:|_RC_minmax ←max{|_RC_min−_Y_| |_Y_ ∈_RC, Y_ =_RC_min}|||
|15:|_RC_ave ←<br>1<br>|_RC_|<br>�<br>_Y_∈_RC Y_|||
|16:|_RC_-Diff←{|_RC_min−_Y_| |_Y_ ∈_RC, Y_ =_RC_min}|||
|17:|**return** _RC_minmin,_RC_minmax,_RC_ave, and_RC_-Diff|||



## _D. STATISTICAL EXTENSIONS FOR REPEATED QUERIES_ 

When evaluating search engine performance across repeated queries with repetition factor _rf_ , we extend _R_ comprehensive to capture statistical variations. The combined statistical measures are derived from the corresponding metrics of the 

## _F. PRACTICAL APPLICATIONS AND SIGNIFICANCE_ 

The _R_ comprehensive framework offers several practical advantages for search engine evaluation: 

92249 

VOLUME 13, 2025 

K. Batri et al.: Beyond Precision and Recall: Measuring Search Engine Consistency 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0009-01.png)


- **Holistic Assessment** : By considering both overlapping and non-overlapping results, it provides a more complete picture of search engine performance than traditional metrics. 

- **Flexible Evaluation** : The weighting parameter allows evaluators to customize the metric according to specific evaluation objectives or search contexts. 

- **User-Centered Approach** : The adaptive weighting mechanism naturally aligns with user experiences, where the relative importance of common versus unique results varies based on the query context. 

- **Statistical Robustness** : The extended statistical measures enable evaluators to quantify not only average performance but also best-case and worst-case scenarios, providing insights into ranking stability. 

When applied to comparative search engine evaluation, _R_ comprehensive can reveal subtle differences in ranking behavior that might be overlooked by more traditional metrics. For instance, two search engines might exhibit similar performance on overlapping results but differ significantly in how they handle unique web pages. The comprehensive framework captures these nuances, enabling more informed decisions about search engine quality and appropriate use cases. 

Furthermore, the metric can guide algorithm development by highlighting specific areas for improvement—whether in maintaining consistency for common results or in optimizing the ranking of unique content. This targeted feedback mechanism can accelerate the refinement of ranking algorithms and ultimately enhance the user search experience. 

## **VII. RESULTS AND DISCUSSIONS** 

The detail of the experimental setup, the experiments, and the results of the experiments are discussed in this section. 

then these two query repetition methods become the same. Hence, a query should contain at least two words. 

## 3) QUERIES 

As the queries are repeated, and the performance analysis is depending on the number of relevant web-pages returned by the repeated queries, the type and nature of the queries play an important role. Hence, two sets of queries are used in the experiments. 

The queries which will fetch a minimum number of hits from the web-search engines form the first set. A Google search query that only returns a single entry in the search has become known as a Googlewhack [24]. As the experiment needs a query with a low number of results, the use of a Googlewhack is a useful option. Five queries from the Googlewhack list are selected. The selected queries are: 1) ambidextrous scallywags, 2) anxiousness scheduler, 3) assonant octosyllable, 4) bamboozle guzzler, and 5) illuminatus ombudsman [25]. 

The second set consists of high-volume search queries that consistently generate substantial search results. These wellestablished biographical queries represent notable public figures with significant digital footprints, providing an effective contrast to the minimal-result Googlewhack queries. The selected queries are: 1) anthony bourdain, 2) kate spade, 3) meghan markle, 4) stan lee, and 5) stephen hawking [26]. 

## 4) QUERY REPETITION FACTOR (RF) 

Trial experiments were conducted, and the overlap between the successive repetition factors was analyzed. Based on the results, it is confirmed that the overlap is maximum when a query is repeated for ’4’, and ’5’ times. Hence ’5’ is selected as the maximum value for the repetition factor. 

## 5) NUMBER OF RELEVANT WEB-PAGES (N) 

## _A. EXPERIMENTAL SETUP_ 

The experiments entirely depend on the web-search engines, query, query repetition factor (rf), and query repetition method. 

## 1) WEB-SEARCH ENGINES 

The alphametic.com application was used to analyze the market share of web search engines in the top 15 GDP countries. According to this analysis, Google is in the top spot in 14 countries. Bing is in the next spot after Google, in 13 countries. Due to their prevalence of use in these countries, the experiments were conducted on the search engines Google and Bing. 

## 2) QUERY REPETITION METHOD 

In our experiments, the queries are repeated in two possible ways. The methods are: 1) Repeating the query as a whole (phrase-based repetition method), and 2) Split the query into tokens, and repeat the query as tokens (token-based repetition method). If a given query is a single word query, 

We restricted the number of relevant web-pages (n) to 120, as the users are interested only in the first few result pages. The number of relevant web-pages (n) is varied in a step of 10. Hence, there are 12 possible levels of relevant web-pages (10, 20, ..., 120), and the experiments are conducted at all these levels. 

## _B. RESULTS, AND ANALYSIS OF ROVERLAP_ 

Table 2 shows the Roverlap values of Bing and Google for the two sets of queries. In the table, _n_ represents the document levels which we increased in steps of 10. The labels ‘Tokens’ and ‘Phrase’ represent the token-based and phrasebased repetition methods respectively. 

From Table 2, it is identified that the phrase and tokenbased repetition methods in Googlewhack and high-volume biographical queries produce almost the same level of performance in Bing. Whereas in Google, there is a significant difference between the phrase and token-based repetition methods in high-volume biographical queries. There are no such differences in Googlewhack queries. 

92250 

VOLUME 13, 2025 

K. Batri et al.: Beyond Precision and Recall: Measuring Search Engine Consistency 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0010-01.png)


From the above discussion, it is identified that irrespective of the type of repetition methods, Bing gives almost the same rank or position to the common or overlapping web-pages. Google, however, gives a different rank or position to the overlapping web-pages when the number of hits to a query is maximum. Interestingly, Google gives almost the same position for phrase and token-based repetition method when the number of hits of a query is minimum. An average search engine user can use either phrase or token-based repetition methods to receive a better performance in Bing. In Google, however, the user has to use both token and phrase-based methods for getting better performance if the number of hits of a query is not known. 

## _C. AVERAGE RANK DIFFERENCE ANALYSIS_ 

The _Roverlap_ metric introduced in Section IV-B serves as an indirect indicator of rank differences among relevant or overlapping web pages returned by search engines for repeated queries. Since _Roverlap_ depends on _A_ ∩ _B_ , _A_ ∪ _B_ , and rank differences—with rank difference being the most critical factor and directly proportional to _Roverlap_ —we conducted a separate analysis of rank difference values. 

The formula used for calculating _Roverlap_ in Equation (20) can be rearranged to calculate the average rank difference value: 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0010-06.png)


where _x_ = | _A_ ∩ _B_ | represents the cardinality of the intersection between result sets. This formulation reveals an inverse relationship between | _A_ ∩ _B_ | and the average rank difference—as the intersection of results increases, the average rank difference decreases. This demonstrates a fundamental trade-off between result overlap and ranking consistency. 

Table 3 presents the average rank difference values for both Googlewhack queries and High-volume biographical queries across Bing and Google search engines. 

Our analysis reveals that the patterns in average rank difference values closely align with those observed in the _Roverlap_ analysis. For Google, High-volume Biographical queries exhibit significantly higher average rank differences compared to Googlewhack queries. Notably, for queries with minimal hits, the variation in average rank difference becomes negligible across different query repetition methods. In contrast, Bing demonstrates more consistent rankings for relevant web pages regardless of the query repetition approach employed. 

This analysis provides quantitative evidence of the ranking consistency characteristics of these major search engines. Google shows greater sensitivity to query volume, while Bing exhibits more stable ranking behavior across repeated queries. These findings have important implications for search engine evaluation and optimization, particularly in 

understanding how ranking algorithms respond to different types of queries and repetition methods. 

## _D. RESULTS AND ANALYSIS OF ROMINMIN , ROMINMAX , AND ROAVE_ 

The _Roverlap_ values are calculated at various repetition factor levels. The variation of _Roverlap_ values against repetition factor ( _rf_ ) variations cannot be easily correlated. When correlated, this produces a set of values which we have condensed into single metrics for clearer analysis. We use _ROminmin_ , _ROminmax_ , and _ROave_ for this purpose. The _ROminmin_ gives the minimum range of _Roverlap_ value when the _rf_ value is varied. Similarly, _ROminmax_ gives the maximum range, and _ROave_ gives the average range of _Roverlap_ variation when the _rf_ value is varied. 

Tables 4 and 5 present the _ROminmin_ , _ROminmax_ , and _ROave_ values for Bing and Google, respectively, for both Googlewhack and High-volume biographical queries. 

The formula used to calculate _Roverlap_ was previously discussed in Equation (20). The numerator of this formula contains two terms: i) _n_ , and ii) rank difference of the common or overlapping ( _A_ ∩ _B_ ) web pages. The denominator also contains two terms: i) _A_ ∩ _B_ , and ii) _A_ ∪ _B_ . 

From the results presented in Tables 4 and 5, we can observe several patterns in the search engine behavior. For both Bing and Google, the maximum values of _ROminmax_ occur at lower values of _N_ (typically _N_ = 10 or _N_ = 20), indicating greater variability in overlap metrics at smaller result set sizes. As _N_ increases, both _ROminmax_ and _ROave_ generally decrease, suggesting more stable overlap patterns with larger result sets. 

When comparing search engines, Google shows higher _ROave_ values than Bing for Googlewhack queries, indicating greater variation in result rankings when queries have minimal hits. For High-volume biographical queries, the pattern becomes more complex, with Google maintaining more consistent _ROminmin_ values across different values of _N_ compared to Bing. 

These metrics provide valuable insight into the stability and consistency of search engine results when queries are repeated under varying conditions, revealing fundamental differences in the ranking algorithms employed by Bing and Google. 

Assume that at a particular level of ‘n’ and ‘rf’, the value of _A_ ∩ _B_ for a query is _x_ times higher when compared to another query repetition factor. As a result, the numerator value gets increased by a factor of _y_ , provided that the common webpages don’t occupy the same position. As | _A_ ∩ _B_ | increases, | _A_ ∪ _B_ | automatically decreases. Consequently, the product of | _A_ ∪ _B_ | and | _A_ ∩ _B_ | is also increased by a factor of _z_ . However, the value of _y_ is greater than the value of _z_ . 

Hence, at a particular level of ‘n’ and ‘rf’, if the value of | _A_ ∩ _B_ | is high for a particular query, it leads to the _Roverlap_ value’s variation. As _Roverlap_ value varies, the minimum, maximum, and average range ( _ROminmin_ , _ROminmax_ , and _ROave_ ) also vary. We represented this variation graphically 

92251 

VOLUME 13, 2025 

K. Batri et al.: Beyond Precision and Recall: Measuring Search Engine Consistency 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0011-01.png)


**TABLE 2.** Roverlap Values of bing and Google Search engines using different query types and repetition methods. 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0011-03.png)


**TABLE 3.** Average rank difference values of Bing and Google. 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0011-05.png)


**TABLE 4.** _ROminmin_ , _ROminmax_ , and _ROave_ Values of Bing. 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0011-07.png)


as a minmax graph. Figures 1 and 2 show the variation of _ROminmin_ , _ROminmax_ , and _ROave_ of Bing and Google for both types of repetition methods. 

The range variation illustrates the variation in the _Roverlap_ values. The exact range variation and its values are analyzed using the area under the curve analysis. The phrase-based repetition method in Bing has 9.309, and the token-based method has 10.515 as the area under the curve values. In Google, the phrase-based method has 9.629, and the tokenbased method has 10.45 as the area under the curve value. 

From the area under the curve analysis, it is confirmed that the variation of the overlapping web-page’s rank is almost similar in both token and phrase-based repetition methods for both Bing and Google. 

## _E. RESULT AND ANALYSIS OF RNON_ **−** _OVERLAP_ 

The number of overlapping web-pages and their rank variations are analyzed in _Smeasure_ and _Roverlap_ . When a query is repeated and submitted to a web-search engine, the engine typically returns both overlapping and non-overlapping 

92252 

VOLUME 13, 2025 

K. Batri et al.: Beyond Precision and Recall: Measuring Search Engine Consistency 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0012-01.png)


**TABLE 5.** _ROminmin_ , _ROminmax_ , and _ROave_ values of Google. 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0012-03.png)


web-pages. While _Smeasure_ directly analyzes the number of overlapping web-pages and indirectly addresses nonoverlapping web-pages, the rank of non-overlapping webpages requires further examination. The _Rnon_ − _overlap_ metric addresses this gap by analyzing the rank of non-common or non-overlapping web-pages. 

The formula used to calculate _Rnon_ − _overlap_ was previously discussed in equation (27). Two sets of queries were repeatedly submitted to Bing and Google at various ‘rf’ levels, and the _Rnon_ − _overlap_ value was calculated for these repeated queries. Table 6 presents the _Rnon_ − _overlap_ values of Bing and Google at various ‘n’ levels. 

Analysis of Table 6 reveals that the query repetition method significantly impacts _Rnon_ − _overlap_ values in both Bing and Google. However, for High-volume Biographical Queries in Bing, the difference in _Rnon_ − _overlap_ values between phrasebased and token-based repetition methods is minimal. These findings confirm that repeating queries using both phrasebased and token-based repetition methods can enhance the performance of web-search engines’ ranking mechanisms. 

The _Rnon_ − _overlap_ values for both Bing and Google show a decreasing trend as the ‘n’ value increases in both Googlewhack and High-volume Biographical Queries. Interestingly, when ‘n’ reaches 50 or 60, the _Rnon_ − _overlap_ value begins to increase. This minimum value indicates a significant presence of non-overlapping web-pages at these particular ‘n’ values. Therefore, when ‘n‘ equals 50 or 60, repeating queries yields the maximum number of previously undiscovered web-pages. 

## 1) IMPACT OF THE NON-OVERLAPPING WEB-PAGE’S RANK 

The rank of non-overlapping web-pages directly influences _Rnon_ − _overlap_ values. When non-overlapping web-pages have lower ranks (appearing higher in search results), the _Rnon_ − _overlap_ value increases. Conversely, when these pages have higher ranks (appearing lower in search results), the _Rnon_ − _overlap_ value decreases. To verify and analyze this relationship between non-common web-page ranks and _Rnon_ − _overlap_ values, we conducted further investigation. 

The total number of web-pages ‘n’ was divided into three segments: i) first thirty percent (0-30%), ii) middle forty 

percent (31)-70%), and iii) last thirty percent (71-100%). For example, with an ‘n’ value of 10, these segments correspond to positions 1-3, 4-7, and 8-10, respectively. After dividing the web-pages into these segments, we calculated the percentage of non-overlapping web-pages within each segment. This calculation was performed for both phrase-based and tokenbased repetition methods in Bing and Google. Figures 3 and 4 illustrate the results of this analysis. 

Figures 3 and 4 demonstrate that as the ‘n’ value increases, the percentage of non-overlapping web-pages in the first thirty percent gradually increases for both phrase-based and token-based repetition methods in Bing and Google. The proportion of non-overlapping web-pages in the middle forty percent is lower compared to the last thirty percent at small values of ‘n’, but this relationship reverses at higher ‘n’ values. 

Having calculated the percentage distribution of nonoverlapping web-pages across these three segments at various ‘n’ values, we analyzed the correlation between these percentages and the corresponding _Rnon_ − _overlap_ values. 

Our analysis revealed a negative correlation between the percentage of non-overlapping web-pages in the first thirty percent and _Rnon_ − _overlap_ values, confirming our earlier hypothesis. Non-common web-pages appearing at the top of search results tend to reduce _Rnon_ − _overlap_ values. For a highperforming search engine, the _Rnon_ − _overlap_ value should be minimal. Therefore, an effective search engine should have a high percentage of non-overlapping web-pages in the first thirty percent of results. In other words, non-overlapping web-pages should ideally occupy prominent positions in websearch engine results. 

## _F. RESULTS AND ANALYSIS OF RNMINMIN , RNMINMAX , AND RNAVE_ 

The _Rnon_ − _overlap_ value’s variation is directly related to the rank or position of the non-overlapping webpages. As the rank of the non-overlapping web-pages varies from a query to another, and from the phrase-based to the token-based repetition methods, we analyzed the range of the nonoverlapping web-pages’ rank variation. It can be indirectly analyzed by using the _Rnon_ − _overlap_ value. The minimum of 

92253 

VOLUME 13, 2025 

K. Batri et al.: Beyond Precision and Recall: Measuring Search Engine Consistency 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0013-01.png)



![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0013-02.png)



![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0013-03.png)


**FIGURE 1.** _Roverlap_ range of Bing. 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0013-05.png)



![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0013-06.png)


**FIGURE 2.** _Roverlap_ range of Google. 

**TABLE 6.** _Rnon_ **−** _overlap_ values of Bing and Google. 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0013-09.png)


the _Rnon_ − _overlap_ at various ‘n’ level is calculated, and based on the minimum value, the range of the _Rnon_ − _overlap_ value is calculated. The minimum deviation is called _RNminmin_ , the maximum deviation is called _RNminmax_ , and the average deviation is termed _RNave_ . Tables 7 and 8 show the _RNminmin_ , _RNminmax_ , and _RNave_ values for Googlewhack 

and High-volume Biographical Queries for both Bing and Google. 

The _RNminmin_ , _RNminmax_ , and _RNave_ variations are almost the same for both phrase and token-based repetition methods in Bing and Google. Using the Googlewhack queries category in Google, the value of _RNminmin_ in token-based and 

92254 

VOLUME 13, 2025 

K. Batri et al.: Beyond Precision and Recall: Measuring Search Engine Consistency 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0014-01.png)



![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0014-02.png)



![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0014-03.png)


**FIGURE 3.** Percentage of non-overlapping web pages at various ‘n’ levels in Bing. 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0014-05.png)



![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0014-06.png)


**FIGURE 4.** Percentage of non-overlapping web pages at various ‘n’ levels in Google. 

**TABLE 7.** _RNminmin_ , _RNminmax_ , and _RNave_ values of Bing. 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0014-09.png)


phrase-based repetition methods has a significant variation. From the above analysis, it is confirmed that Google places the non-overlapping web-pages in a slightly different manner 

at the bottom of the results when the number of hits for those queries is minimum. Apart from that, both Bing and Google place the non-overlapping web-pages in the same manner. 

92255 

VOLUME 13, 2025 

K. Batri et al.: Beyond Precision and Recall: Measuring Search Engine Consistency 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0015-01.png)


**TABLE 8.** _RNminmin_ , _RNminmax_ , and _RNave_ values of Google. 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0015-03.png)


## _G. RESULTS AND ANALYSIS OF RCOMPREHENSIVE_ 

The stability of search engine result rankings can be comprehensively evaluated by combining the non-overlap measurements with their range variations. We propose a new metric, _Rcomprehensive_ , which is calculated by taking 50% of the _Rnon_ − _overlap_ values and 50% of the range values previously analyzed. This comprehensive metric provides a holistic view of ranking stability, where values closer to 0 indicate highly stable rankings and values approaching 1 represent non-stable or highly variable rankings. 

Table 9 presents the _Rcomprehensive_ values for both Bing and Google search engines across Googlewhack queries and High-volume Biographical Queries. These values offer insights into the overall stability patterns of search engine rankings under different query complexities and search volumes. 

Analysis of the _Rcomprehensive_ values reveals several significant patterns in search engine ranking stability. For Googlewhack queries, Bing demonstrates consistently higher stability (lower _Rcomprehensive_ values) compared to Google across most N values, particularly for phrase-based queries. This suggests that Bing maintains more consistent rankings for queries with minimal result sets. The stability difference between Bing and Google is most pronounced at lower N values (N=10 to N=30) and gradually converges as N increases, indicating that both search engines tend to stabilize their rankings as more results are considered. 

For High-volume Biographical Queries, a different pattern emerges. Google’s token-based approach demonstrates comparable stability to Bing’s methods at lower N values, but as N increases beyond 70, Google’s _Rcomprehensive_ values consistently rise, indicating decreased stability for these biographical queries. This phenomenon may be attributed to Google’s algorithm placing greater emphasis on semantic relevance for biographical information, leading to more variability in ranking patterns as the result set expands. 

An interesting observation is that for both search engines, the phrase-based method generally shows higher stability (lower _Rcomprehensive_ values) than the token-based method for Googlewhack queries, while the opposite trend is observed 

for High-volume Biographical Queries. This suggests that the optimal query processing strategy differs based on the query type and expected result volume. 

The gradual convergence of _Rcomprehensive_ values for Googlewhack queries as N increases (particularly in Google’s results) indicates that ranking stability tends to improve with larger result sets for low-volume queries. Conversely, for High-volume Biographical Queries, we observe more consistent _Rcomprehensive_ values across different N values, suggesting that ranking stability is less dependent on result set size for these high-volume queries. 

These findings offer valuable insights for search engine optimization strategies, particularly for content targeting specific query types. Content optimized for high-volume biographical queries may benefit from token-based approaches on Bing, while phrase-based optimization might be more effective for low-volume, specialized queries across both search engines. 

## _H. STATISTICAL ANALYSIS OF RANKING STABILITY METRICS_ 

To assess the statistical significance of the differences observed between Bing and Google, we conducted paired t- tests on key ranking stability metrics across the query types and repetition methods. 

For _Roverlap_ , representing the consistency of overlapping results, paired comparisons on Googlewhack phrase queries ( _N_ = 12) showed a significant difference between Bing (mean = 0.096) and Google (mean = 0.074), with _t_ (11) = 4 _._ 38, _p_ = 0 _._ 0011. This indicates that Bing exhibits significantly higher overlap stability in these queries. Similarly, on high-volume biographical phrase queries, Bing consistently demonstrated greater stability with mean _Roverlap_ values higher than Google (data trends observed but exact statistics omitted for brevity). 

Average rank difference, a measure of rank position variability, also differed significantly. For Googlewhack phrase queries, Bing’s average rank difference (mean ≈ 6.0) was lower than Google’s (mean ≈ 9.0), suggesting more 

92256 

VOLUME 13, 2025 

K. Batri et al.: Beyond Precision and Recall: Measuring Search Engine Consistency 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0016-01.png)


**TABLE 9.** _Rcomprehensive_ values for Bing and Google (Values closer to 0 indicate higher stability). 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0016-03.png)


stable rankings. Paired t-tests on these values confirmed significance at _p <_ 0 _._ 05. 

Additionally, the comprehensive metric _Rcomprehensive_ , which integrates overlap and non-overlap stability components, consistently favored Bing across all query and repetition types. Statistical testing confirmed these differences were significant for Googlewhack queries with phrase repetition (p _<_ 0.01) and token repetition ( _p <_ 0 _._ 05). 

These analyses provide robust evidence that Bing’s search rankings are more stable than Google’s for the queries tested, supporting the conclusions drawn from the raw metric values. Incorporating statistical hypothesis testing strengthens the empirical rigor of the proposed Rmeasure evaluation framework and demonstrates its discriminative power across search engines. 

## _I. LIMITATIONS AND FUTURE WORK_ 

The experiments conducted in this study utilize a limited set of queries, comprising five low-volume Googlewhack queries and five high-volume biographical queries. While these queries were carefully selected to represent contrasting search scenarios, the relatively small and specific dataset limits the generalizability of our findings. To establish broader applicability and robustness of Rmeasure, future work should incorporate a larger and more diverse query set spanning multiple domains, query lengths, and user intents. Such an expanded evaluation would provide deeper insights into the metric’s behavior across varied search contexts and enhance its practical relevance. 

Our analysis assumes that repeated queries are independent, disregarding session-based personalization and temporal biases such as trending topics that may dynamically influence rankings. This simplification was necessary due to constraints in data collection and the inherent complexity of modeling user-specific and time-sensitive factors in web search behavior. Although the proposed Rmeasure framework is theoretically grounded, it currently lacks empirical validation through user studies that assess 

whether the measured rank stability aligns with actual user perceptions of consistency. Conducting such user-centric evaluations represents an important direction for future research, providing direct evidence of Rmeasure’s relevance and applicability in real-world search experiences. 

While our empirical evaluation focuses on Google and Bing—given their dominant market presence and accessibility—we acknowledge that the scalability of Rmeasure to other search engines, particularly those employing personalized or context-aware ranking systems, remains unexplored. Extending the framework to such personalized scenarios would require additional modeling of user context and session dynamics, which could significantly impact rank stability. Moreover, this study does not include a direct benchmark comparison against recent advanced rank correlation metrics such as Rank-Biased Overlap (RBO) and Average Precision Correlation ( _τAP_ ). These established metrics provide important baselines with complementary strengths, including support for incomplete rankings and topweighted sensitivity. Integrating a systematic comparative analysis with these metrics would substantiate the relative advantages and trade-offs of Rmeasure more comprehensively. We consider these extensions vital for validating the generalizability and practical utility of Rmeasure across diverse search environments and evaluation paradigms. 

## **VIII. CONCLUSION** 

This study introduced a novel rank correlation measure to assess search engine consistency, addressing the limitations of traditional information retrieval metrics. By analyzing rank stability in repeated queries, the proposed framework distinguishes between overlapping and non-overlapping results, providing a comprehensive evaluation of ranking fluctuations. 

Empirical analysis of Google and Bing revealed distinct ranking behaviors. **For overlapping results, Google exhibited greater fluctuations, with** _Roverlap_ **values ranging from** 0 _._ 0533 **to** 0 _._ 1177 **in low-volume queries and** 0 _._ 0634 **to** 0 _._ 1511 **in high-volume queries, compared to Bing’s more stable range of** 0 _._ 0823 **to** 0 _._ 1115 **and** 0 _._ 1334 **to** 0 _._ 1586 **,** 

92257 

VOLUME 13, 2025 

K. Batri et al.: Beyond Precision and Recall: Measuring Search Engine Consistency 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0017-01.png)


**respectively** . This represents approximately 30% higher variability in Google’s ranking patterns. Additionally, **the average rank difference analysis showed that Google’s high-volume queries had a rank fluctuation as high as** 21 _._ 622 **, whereas Bing’s highest fluctuation was** 14 _._ 285 - a significant 51% difference that translates to users potentially seeing substantially different results when repeating identical searches on Google. 

Further, **the non-overlapping rank stability metric (** _Rnon_ − _overlap_ **) ranged from** 0 _._ 2379 **to** 0 _._ 3594 **in Google and** 0 _._ 2299 **to** 0 _._ 2521 **in Bing** , indicating that Google introduces more new content with each repeated query, while Bing retains more consistency. Notably, the **minimum rank stability (** _RNminmin_ **) for Bing was as low as** 0 _._ 006 **, compared to Google’s** 0 _._ 069, reinforcing Bing’s ranking stability across query repetitions. Statistical analysis confirmed these differences were significant (p _<_ 0.05), validating the reliability of our comparative framework. 

These findings emphasize the importance of incorporating rank stability assessments in search engine evaluation to improve user experience and retrieval effectiveness. Future research can explore expanding this methodology to evaluate search engine behavior across different languages and regional search settings. Additionally, integrating machine learning models to predict rank variations could further enhance search engine evaluation frameworks. The insights from this research contribute to the development of fair, reliable, and user-centric search ranking algorithms, aligning with broader objectives of equitable information access and digital transparency. 

## **ACKNOWLEDGMENT** 

This work focuses on search engine consistency analysis and introduces a novel rank correlation measure to evaluate stability in web search results. 

## **REFERENCES** 

- [1] A. Spink and B. J. Jansen, _Web Search: Public Searching Web_ . Cham, Switzerland: Springer, 2004. 

- [2] D. Hawking, N. Craswell, and P. Bailey, ‘‘Measuring search engine quality,’’ _Inf. Retr._ , vol. 4, no. 1, pp. 33–59, 2001. 

- [3] Z. Edrees and H. Juma, ‘‘Comparative analysis of page ranking algorithms for efficient information retrieval,’’ _Amer. J. Inf. Sci. Technol._ , vol. 9, no. 1, pp. 15–23, Feb. 2025, doi: 10.11648/j.ajist.20250901.12. 

- [4] E. Garfield, ‘‘The concept of citation indexing: A unique and innovative tool for navigating the research literature,’’ Far Eastern State Univ., Vladivostok, Russia, Tech. Rep., 1997. [Online]. Available: https://garfield.library.upenn.edu/papers/vladivostok.html 

- [5] M. Melucci, ‘‘Search engines and rank correlation,’’ in _Web Search Engine Research_ (Library and Information Science), vol. 4, D. Lewandowski, Ed., Leeds, U.K.: Emerald Group Publishing Limited, 2012, pp. 203–224, doi: 10.1108/S1876-0562(2012)002012a010. 

- [6] L. Lyu, N. Roy, H. Oosterhuis, and A. Anand, ‘‘Is interpretable machine learning effective at feature selection for neural learning-to-rank?’’ in _Proc. Eur. Conf. Inf. Retr. (ECIR)_ , Jan. 2024, pp. 384–402. [Online]. Available: https://harrieo.github.io/files/2024-ecir-xltr.pdf 

- [7] W. C. Hoo, C. K. Loy, A. Y. Cheng, D. T. Sigar, Z. K. B. Zulkifli, and J. Jomitol, ‘‘Impact of search engine optimization dimensions on SME companies using online promotion in Malaysia,’’ _WSEAS Trans. Bus. Econ._ , vol. 20, pp. 998–1007, May 2023. 

- [8] B. Dean. (2025). _We Analyzed 11.8 Million Google Search Results. Here’s What We Learned About Seo_ . Accessed: May 15, 2025. [Online]. Available: https://backlinko.com/search-engine-ranking 

- [9] E. Yılmaz, J. A. Aslam, and S. Robertson, ‘‘A new rank correlation coefficient for information retrieval,’’ in _Proc. 31st Annu. Int. ACM SIGIR Conf. Res. Develop. Inf. Retr._ , Jul. 2008, pp. 587–594, doi: 10.1145/1390334.1390435. 

- [10] J. Cohen, _Statistical Power Analysis for the Behavioral Sciences_ . Evanston, IL, USA: Routledge, 1988. 

- [11] N. Gomes de Sá, L. Valem, and D. Pedronette, ‘‘A multi-level rank correlation measure for image retrieval,’’ in _Proc. 16th Int. Joint Conf. Comput. Vis., Imag. Comput. Graph. Theory Appl._ , 2021, pp. 370–378, doi: 10.5220/0010220903700378. 

- [12] M. Melucci, ‘‘Weighted rank correlation in information retrieval evaluation,’’ in _Proc. Asia Inf. Retr. Symp._ , Jan. 2009, pp. 75–86, doi: 10.1007/978-3-642-04769-5_7. 

- [13] B. Carterette and R. Jones, ‘‘Evaluating search engines by modeling the relationship between relevance and clicks,’’ in _Proc. Adv. Neural Inf. Process. Syst._ , vol. 20, Dec. 2007, pp. 217–224. 

- [14] A. Sutcliffe and A. Namoun, ‘‘Predicting user attention in complex Web pages,’’ _Behav. Inf. Technol._ , vol. 31, no. 7, pp. 679–695, Jul. 2012, doi: 10.1080/0144929x.2012.692101. 

- [15] E. Yılmaz, E. Kanoulas, and J. A. Aslam, ‘‘A simple and efficient sampling method for estimating AP and NDCG,’’ in _Proc. 31st Annu. Int. ACM SIGIR Conf. Res. Develop. Inf. Retr._ , Jul. 2008, pp. 603–610, doi: 10.1145/1390334.1390437. 

- [16] W. Webber, A. Moffat, and J. Zobel, ‘‘A similarity measure for indefinite rankings,’’ _ACM Trans. Inf. Syst._ , vol. 28, no. 4, pp. 1–38, Nov. 2010, doi: 10.1145/1852102.1852106. 

- [17] K. M. Elbedweihy, S. N. Wrigley, P. Clough, and F. Ciravegna, ‘‘An overview of semantic search evaluation initiatives,’’ _J. Web Semantics_ , vol. 30, pp. 82–105, Jan. 2015, doi: 10.1016/j.websem.2014.10.001. 

- [18] D. E. Critchlow, M. A. Fligner, and J. S. Verducci, ‘‘Probability models on rankings,’’ _J. Math. Psychol._ , vol. 35, no. 3, pp. 294–318, Sep. 1991, doi: 10.1016/0022-2496(91)90050-4. 

- [19] D. Li and E. Kanoulas, ‘‘Active sampling for large-scale information retrieval evaluation,’’ in _Proc. ACM Conf. Inf. Knowl. Manage._ , Nov. 2017, pp. 49–58, doi: 10.1145/3132847.3133015. 

- [20] D. Olteanu, ‘‘SPEX: Streamed and progressive evaluation of XPath,’’ _IEEE Trans. Knowl. Data Eng._ , vol. 19, no. 7, pp. 934–949, Jul. 2007, doi: 10.1109/TKDE.2007.1063. 

- [21] M. Stone, ‘‘Types of metrics for search evaluation,’’ in _Understanding and Evaluating Search Experience_ . Cham, Switzerland: Springer, 2022, pp. 41–61, doi: 10.1007/978-3-031-79216-8_7. 

- [22] B. Ostermaier, K. Römer, F. Mattern, M. Fahrmair, and W. Kellerer, ‘‘A real-time search engine for the Web of things,’’ in _Proc. Internet Things (IoT)_ , Nov. 2010, pp. 1–8. 

- [23] Y. Shao, J. Mao, Y. Liu, M. Zhang, and S. Ma, ‘‘Towards contextaware evaluation for image search,’’ in _Proc. 42nd Int. ACM SIGIR Conf. Res. Develop. Inf. Retr._ , Jul. 2019, pp. 1209–1212, doi: 10.1145/3331184.3331343. 

- [24] D. Gorman, _Dave Gorman’s Googlewhack Adventure_ . London, U.K.: Ebury Press, 2004. 

- [25] _Googlewhack Archive_ . Accessed: May, 15, 2025. [Online]. Available: https://www.googlewhack.com/ 

- [26] W. Weerkamp, R. Berendsen, B. Kovachev, E. Meij, K. Balog, and M. De Rijke, ‘‘People searching for people: Analysis of a people search engine log,’’ in _Proc. 34th Int. ACM SIGIR Conf. Res. Develop. Inf. Retr._ , 2011, pp. 45–54, doi: 10.1145/2009916.2009924. 

KRISHNAN BATRI received the Ph.D. degree in computer science and engineering from the National Institute of Technology, Tiruchirappalli, India. He is currently a Professor and the Deputy Director of courses and delivery with the School of Computer Science and Engineering, Jain University, Bengaluru, India. He has supervised 13 Ph.D. scholars and has published extensively in leading journals and conferences. He is also an advocate for curriculum development and fostering academic collaboration at both national and international levels. His research interests include information retrieval, artificial intelligence, genetic algorithms, data fusion techniques, and deep learning applications. 

92258 

VOLUME 13, 2025 

K. Batri et al.: Beyond Precision and Recall: Measuring Search Engine Consistency 


![](prepared/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability/images/Beyond_Precision_and_Recall_Measuring_Search_Engine_Consistency_Using_Rank_Stability.pdf-0018-01.png)


RAJERMANI THINAKARAN received the Bachelor of Science degree in computer science, the master’s degree in information technology, and the Ph.D. degree from the Universiti Teknologi Malaysia (UTM). She is currently affiliated with the Faculty of Data Science and Information Technology, INTI International University, Negeri Sembilan, Malaysia. Her research spans several key areas, including artificial intelligence, assistive technology, eLearning, and gaming, focusing on theory, design, implementation, and sustainability. In addition to her academic and research contributions, she serves on the editorial boards of various journals and is an active technical reviewer for local and international publications and conferences. 

S. LAKSHMI received the Ph.D. degree in information and communication engineering from Anna University, Chennai, in 2018, with research focused on web-search engine performance using AI-based algorithms. She is currently a Dedicated Researcher and an Academician with extensive experience in achieving organizational goals through effective and organized practices. She is an Associate Professor with Jain (Deemed-to-be University), Bengaluru, where she is responsible for coordinating the Department IQAC and managing the overall laboratory budget. she has previously held positions as an Associate Professor with the PSRR College of Engineering, Sivakasi, and an Assistant Professor with the RVS College of Engineering and Tech and Shree Venkateshwara Hi-Tech Engineering College. She has a strong research background in areas, such as communication systems, deep learning, and image segmentation, and has published several papers in international journals and conferences. 

R. SOWRIRAJAN is currently an Assistant Professor and the Head of the Department of Mathematics, Dr. N. G. P. Arts and Science College, Coimbatore, India. He completed his higher studies under Bharathiar University. With 16 years of experience in teaching and research, he has published research articles in international journals and is guiding doctoral students. He has conducted conferences, workshops, and refresher courses with support from government agencies and delivered lectures at various conferences and events. His research mainly focuses on real-life applications of mathematics. 

SIVARAM MURUGAN received the B.E. degree in computer science and engineering from the Bharath Niketan Engineering College, Madurai Kamaraj University, in 2002, the M.Tech. degree in computer science and engineering from the National Institute of Technology (NIT), Tiruchirappalli, in 2007, and the Ph.D. degree in computer science and engineering from Anna University, Chennai, in 2014. He was an Associate Professor with Jain University, India, and Galgotias University, Greater Noida, and an Assistant Professor with Saudi Electronic University, Saudi Arabia. He is currently an Accomplished Academician. He is a Professor with the Department of Computer Engineering, Faculty of Engineering and Natural Sciences, Sivas University of Science and Technology, Türkiye. With over 18 years of teaching experience, he has held key positions, such as a Professor and the Research Director of Lebanese French University, Erbil, Iraq, a Professor with Saveetha University, India, and a Professor/the Dean of the Selvam College of Technology, Namakkal. He has published more than 20 research papers in reputed national and international journals and conferences. As a Dedicated Researcher and an Educator, he continues to make significant contributions to the field of computer science and engineering, inspiring students and advancing technological innovation. His research interests include data mining, image retrieval, information retrieval, data fusion, image processing, and artificial intelligence. 

92259 

VOLUME 13, 2025 

