---
title: "Viewpoint-Agnostic Grasp Pipeline using VLM and Partial Observations"
collection: publications
category: preprints
pubtype: preprint
tags: [control,grasping,vision,manipulation,mobile-manipulation,perception]
doi: 
code: 
permalink: /publication/2026-vlm-grasp
excerpt: 'We present an end-to-end pipeline for language-guided grasping that bridges open-vocabulary target selection to safe grasp execution on a real robot'
date: 2026-02-24
venue: 'Paper submitted to IROS 2026 - Preprint version available. Please click Download Paper below.'
paperurl: 'http://ricardovgodoy.github.io/files/2026_IROS_VLM_Grasping.pdf'
bibtexurl: ''
citation: ''
---


<iframe width="560" height="315" src="https://www.youtube.com/embed/lPNVJjJRWQk?si=zj9RXMVupE9ILUhs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Robust grasping in cluttered, unstructured environments remains challenging for mobile legged manipulators due to occlusions that lead to partial observations, unreliable depth estimates, and the need for collision-free, execution-feasible approaches. We present an end-to-end pipeline for language-guided grasping that bridges open-vocabulary target selection to safe grasp execution on a real robot. Given a natural-language command, the system grounds the target in RGB using open-vocabulary detection and promptable instance segmentation, extracts an object-centric point cloud from RGB-D, and improves geometric reliability under occlusion via back-projected depth compensation and two-stage point cloud completion. We then generate and collision-filter 6-DoF grasp candidates and select an executable grasp using safety-oriented heuristics that account for reachability, approach feasibility, and clearance. We evaluate the method on a quadruped robot with an arm in two cluttered tabletop scenarios, using paired trials against a view-dependent baseline. The proposed approach achieves a 90\% overall success rate (9/10) versus 30\% (3/10) for the baseline, demonstrating substantially improved robustness to occlusions and partial observations in clutter.



