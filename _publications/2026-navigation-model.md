---
title: "Towards Capability-Aware Traversability Navigation for Unstructured Environments"
collection: publications
authors: "Gianluca Capezzuto, Felipe Tommaselli, Matheus P. Angarola, Ricardo V. Godoy, Marcelo Becker"
category: conferences
pubtype: conference
homepage_selected: true
thumbnail: /images/projects/capability-aware-navigation.jpg
media_webm: /images/publications/capability-aware-traversability.webm
media_mp4: /images/publications/capability-aware-traversability.mp4
media_poster: /images/publications/capability-aware-traversability.webp
short_contribution: "Capability conditioning produces different traversability predictions for legged and wheeled robots from the same scene."
tags: [control]
doi: 
projecturl: 'https://capability-aware-traversability.github.io'
code: ''
permalink: /publication/2026-navigation-model
excerpt: 'Capability-Aware Traversability conditions spatial predictions on the physical limits of legged and wheeled robots.'
date: 2026-06-17
venue: '2026 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)'
paperurl: 'https://arxiv.org/pdf/2607.20679'
bibtexurl: ''
citation: ''
---

<iframe width="560" height="315" src="https://www.youtube.com/embed/6MZS3EgpG2I?si=BCG8viiP3XAYYBrV" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Estimating traversability in unstructured environments requires conditioning on robot embodiment, as the same terrain can be traversable for one platform and unsafe for another. Existing methods often transfer predictions across morphologies through late-stage trajectory filtering rather than encoding platform constraints in the learned representation. We propose Capability-Aware Traversability (CAT), a framework that embeds physical limits directly into the spatial feature space.

CAT grounds dense supervision masks in physical trajectories through an interactive annotation pipeline and modulates semantic terrain maps with robot-specific traversability vectors through Spatially-Adaptive Denormalization (SPADE) blocks. Across human-annotated and trajectory-aligned datasets, CAT leads all ranking-based metrics, improving AUROC by 11.0% on physically executed trajectories and AUPRC by 15.8% on human traces over the strongest baseline.

Ablations show that spatial conditioning and per-robot prototypes produce capability sensitivity beyond generic path prediction. Deployments on a legged quadruped and a wheeled skid-steer demonstrate embodiment-aware obstacle avoidance on embedded hardware at 4.8 Hz.
