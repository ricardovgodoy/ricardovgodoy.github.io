---
title: "Evaluating Zero‑Shot and One‑Shot Adaptation of Small Language Models in Leader‑Follower Interaction"
collection: publications
category: preprints
pubtype: preprint
tags: [human-robot-interaction]
doi: 
code: 
permalink: /publication/2026-leader-follower
excerpt: 'In this paper, we present the first benchmark of SLMs for leader–follower communication, introducing a novel dataset derived from a published database and augmented with synthetic samples to capture interaction-specific dynamics.'
date: 2026-02-24
venue: 'Paper submitted to BioRob 2026 - The preprint version will be made available soon.'
paperurl: ''
bibtexurl: ''
citation: ''
---



Leader–follower interaction is a central paradigm in human–robot interaction (HRI). Yet, assigning roles in real-time remains challenging for resource-constrained mobile and assistive robots. While large language models (LLMs) have shown promise for natural communication, their size and latency limit on-device deployment. Small language models (SLMs) offer a potential alternative, but their effectiveness for role classification in HRI has not been systematically evaluated. In this paper, we present the first benchmark of SLMs for leader–follower communication, introducing a novel dataset derived from a published database and augmented with synthetic samples to capture interaction-specific dynamics. We investigate two adaptation strategies: prompt engineering and fine-tuning. Both are studied under zero-shot and one-shot interaction modes. Experiments with Qwen2.5-0.5B reveal that fine-tuning achieves robust classification performance (up to 84.8\% accuracy) while maintaining low latency (around 18 ms per sample), outperforming both baseline and prompt-engineered approaches. Prompt engineering yields modest improvements over the baseline but remains sensitive to input ambiguity. These findings demonstrate that fine-tuned SLMs provide a potentially effective and efficient solution for leader–follower role assignment.

