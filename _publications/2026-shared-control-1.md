---
title: "From Perception to Assistance: VLM-Driven Potential Fields for Shared-Control Manipulation"
collection: publications
category: preprints
pubtype: preprint
tags: [control, manipulation, teleoperation, locomanipulation, shared-control]
doi: 
code: 
permalink: /publication/2026-shared-control-1
excerpt: ''
date: 2026-02-24
venue: 'Paper submitted to RA-L - The preprint version will be made available soon.'
paperurl: ''
bibtexurl: ''
citation: ''
---


In this paper we present a shared-autonomy system for mobile manipulation that remains robust in clutter and supports both assisted teleoperation and user-triggered autonomous execution. The robot continuously maintains a local 3D collision representation from onboard perception and performs online collision-aware motion generation to enable real-time obstacle avoidance during end-effector motion. To reduce operator workload during approach and alignment, we introduce a potential-field guidance layer that continuously corrects the operator's end-effector commands toward the intended target while preserving operator authority and enforcing collision constraints. We further generalize target specification by integrating an open-vocabulary perception module that grounds the operator's query in the scene and extracts manipulation-relevant task parameters, most notably the valve rotation axis, which is used consistently for both shared-control guidance and autonomous task execution. The autonomous execution module can be explicitly triggered via hand commands, enabling reliable task completion once intent is confirmed. We evaluate the complete pipeline on real-robot industrial tasks, including the operation of 3/4" ball valves and wheel valves, demonstrating safe, collision-aware manipulation, correct axis-conditioned motion, and successful contact-rich execution in clutter.

