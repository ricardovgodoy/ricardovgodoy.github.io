---
title: "Towards Capability-Aware Traversability Navigation for Unstructured Environments"
collection: publications
category: conferences
pubtype: conference
homepage_selected: true
thumbnail: /images/projects/capability-aware-navigation.jpg
short_contribution: "Capability conditioning produces different traversability predictions for legged and wheeled robots from the same scene."
tags: [control]
doi: 
projecturl: 'https://capability-aware-traversability.github.io'
code: ''
permalink: /publication/2026-navigation-model
excerpt: 'Capability-Aware Traversability conditions spatial predictions on the physical limits of legged and wheeled robots.'
date: 2026-06-17
venue: '2026 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)'
paperurl: '/files/IROS___Conditioned_Traversability.pdf'
bibtexurl: ''
citation: ''
---

<iframe width="560" height="315" src="https://www.youtube.com/embed/reXul8PdFEo?si=eEC2l-ouvTjhPA_L" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Estimating traversability in unstructured environments requires conditioning on robot embodiment, as the same terrain can be traversable for one platform and unsafe for another. Yet, existing methods often struggle to transfer policies across distinct robot morphologies, relying on late-stage trajectory filtering that fails to intrinsically encode platform-specific constraints. In this paper, we propose Capability-Aware Traversability (CAT), a unified framework that embeds physical limits directly into the spatial feature space. CAT leverages an interactive zero-shot annotation pipeline grounded in physical trajectories to generate dense supervision masks. To align visual representations with specific robotic embodiments, the architecture dynamically modulates semantic terrain maps using robot-specific traversability vectors via Spatially-Adaptive Denormalization (SPADE) blocks. Extensive evaluations on both human-annotated and trajectory-aligned datasets demonstrate that CAT outperforms state-of-the-art baselines, achieving a 12.6% improvement in mean traversability and a 13.5% increase in Area Under the Curve (AUC). Real-world deployments on diverse platforms, including a legged quadruped and a wheeled skid-steer, further demonstrate the framework's ability to perform robust, real-time (5 Hz) embodiment-aware obstacle avoidance in unstructured environments.
