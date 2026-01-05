---
title: "The impact of feature scaling in machine learning: Effects on regression and classification tasks"
collection: publications
category: manuscripts
pubtype: journal
tags: []
doi: 10.1109/ACCESS.2025.3635541      # optional
code: https://github.com/joaomh/article-impact-feature-scaling-classification
permalink: /publication/2025-scaling-1
excerpt: 'This paper addresses the critical lack of comprehensive studies on feature scaling by systematically evaluating 12 scaling techniques, including several less common transformations, across 14 different Machine Learning algorithms and 16 datasets for classification and regression tasks.'
date: 2025-11-20
venue: 'IEEE Access'
paperurl: 'https://ieeexplore.ieee.org/document/11261543'
bibtexurl: 'http://ricardovgodoy.github.io/files/2025-scaling-1.bib'
citation: 'J. M. H. Pinheiro et al., "The Impact of Feature Scaling in Machine Learning: Effects on Regression and Classification Tasks," in IEEE Access, vol. 13, pp. 199903-199931, 2025, doi: 10.1109/ACCESS.2025.3635541.'
---

This research addresses the critical lack of comprehensive studies on feature scaling by systematically evaluating 12 scaling techniques, including several less common transformations, across 14 different Machine Learning algorithms and 16 datasets for classification and regression tasks. We meticulously analyzed impacts on predictive performance (using metrics such as accuracy, MAE, MSE, and ) and computational costs (training time, inference time, and memory usage). Key findings reveal that while ensemble methods (such as Random Forest and gradient boosting models like XGBoost, CatBoost and LightGBM) demonstrate robust performance largely independent of scaling, other widely used models such as Logistic Regression, SVMs, TabNet, and MLPs show significant performance variations highly dependent on the chosen scaler. This extensive empirical analysis, with all source code, experimental results, and model parameters made publicly available to ensure complete transparency and reproducibility, offers model-specific crucial guidance to practitioners on the need for an optimal selection of feature scaling techniques.
