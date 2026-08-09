# 3. Results

## 3.1 Publication Trends

Figure 1 (citespace_trend.png) presents the annual distribution of publications by database source. The temporal distribution shows consistent research output across the 2022–2026 window, with Scopus contributing 44 of the 50 reviewed studies (88%) and Web of Science accounting for the remaining 6 (12%). The Scopus-dominant distribution reflects the interdisciplinary nature of this domain, spanning computer science, engineering, and applied physics. The 2025–2026 period includes a noticeable increase in Web of Science contributions, suggesting growing recognition of this research area within broader scientific literature. The distribution also lists a peak in 2024 outputs, likely corresponding to the maturation of YOLOv8 and transformer-based architectures that catalyzed a wave of applied surveillance studies during this period.

## 3.2 Keyword Co-occurrence Analysis

Figure 2 (vosviewer_keyword_network.png) illustrates the keyword co-occurrence network derived from the 50 reviewed studies. The term "deep learning" exhibits the highest frequency (23 occurrences) and serves as the central hub of the network, connecting to nearly all other keywords. "Violence detection" (19 occurrences) and "anomaly detection" (16 occurrences) form the primary application-oriented nodes. "Convolutional neural network" (15 occurrences), "CNN" (12 occurrences), and "LSTM" (11 occurrences) constitute the dominant architectural terms. Edge density analysis of the network (vosviewer_density.png) confirms that the highest density region centers on the deep learning—CNN—violence detection nexus, reflecting the core convergence of methodology and application in this literature.

The temporal overlay visualization (vosviewer_overlay.png) reveals that attention mechanisms, YOLO-based architectures, and transformer-integrated approaches are concentrated in the 2025–2026 period, indicating a recent methodological pivot toward more sophisticated feature weighting strategies. In contrast, earlier publications (2022–2023) more frequently emphasize autoencoder-based reconstruction and traditional 3D CNN frameworks. This temporal gradient suggests a field transitioning from generic video understanding models toward architectures specifically optimized for surveillance anomaly detection.

## 3.3 Thematic Clusters

Four distinct thematic clusters emerge from the co-occurrence analysis, color-coded in the network diagram:

**Cluster 1 — Deep Learning Architectures (Red):** This cluster encompasses CNN, LSTM, GRU, ResNet, MobileNet, 3D CNN, YOLO, and autoencoder. Papers in this cluster focus on designing and optimizing neural network topologies for spatiotemporal feature extraction. Representative works include the C3D-LSTM attention fusion framework by Altowairqi et al. [2026] and the VD-Net architecture employing lightweight temporal convolutional networks [Khan et al., 2024].

**Cluster 2 — Temporal and Motion Analysis (Green):** Comprising optical flow, spatiotemporal features, action recognition, behavior recognition, and skeleton-based methods. This cluster captures the temporal modeling dimension, with contributions such as the optical flow statistical feature approach by Mahmoodi and Nezamabadi-Pour [2025] and the skeleton-based campus violence detection system by Omarov et al. [2022].

**Cluster 3 — Application and Deployment (Blue):** The largest application cluster includes violence detection, anomaly detection, weapon detection, firearm detection, video surveillance, CCTV, real-time detection, IoT, edge computing, and crowd analysis. Works in this cluster prioritize deployment considerations, exemplified by the edge-device weapon detection framework by Berardini et al. [2024] and the IoT-integrated violence detection system by Vo et al. [2024].

**Cluster 4 — Methods and Techniques (Yellow):** Includes deep learning, attention mechanism, transfer learning, pose estimation, feature extraction, convolutional neural network, and object detection. This cluster bridges the architecture and application domains, with studies such as the transfer learning-enhanced YOLO framework by Dalal et al. [2024] and the multimodal attention feature fusion approach by Shin et al. [2025].

## 3.4 Top Authors and Journals

Table 1 (top10_authors.csv) lists the most prolific contributors to this research area. The analysis identifies several author groups with sustained publication records, predominantly affiliated with institutions in South Korea, India, Pakistan, and the Middle East — reflecting a notable geographic concentration of research activity outside Western academic centers. The IEEE Access, Sensors (MDPI), and Applied Sciences (MDPI) journals account for the largest share of publications, followed by Elsevier venues including Neurocomputing and Procedia Computer Science.

## 3.5 Citation Burst Analysis

Figure 3 (citespace_burst_timeline.png) displays the top 15 keywords ranked by total frequency, with burst years highlighted in red. The burst analysis reveals that "attention mechanism" and "transfer learning" exhibit pronounced burst activity concentrated in 2025–2026, indicating their emergence as focal methodological innovations. "Edge computing" and "IoT" show a similar late-period concentration, consistent with a growing emphasis on deployable, lightweight solutions. In contrast, "CNN" and "LSTM" demonstrate sustained presence across the entire 2022–2026 window, confirming their status as foundational techniques.

## 3.6 Literature Matrix Summary

The literature analysis matrix (matrix_literature.csv) provides a structured overview of all 50 studies, enumerating their aims, methods, datasets, findings, and limitations. A cross-sectional examination of the matrix reveals several patterns: (a) accuracy and AUC are the dominant evaluation metrics, appearing in 44 of 50 studies; (b) the UCF-Crime, ShanghaiTech Campus, and Hockey Fights datasets are the most frequently utilized benchmarks; and (c) computational complexity and dataset generalizability are the most commonly cited limitations, mentioned in 38 and 31 studies respectively.
