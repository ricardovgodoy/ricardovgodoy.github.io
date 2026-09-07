---
title: "Language-Guided Grasping under Partial Observation for Mobile Manipulation in Field Inspection and Maintenance"
collection: publications
category: conferences
pubtype: conference
homepage_selected: true
short_contribution: "Combines object segmentation, shape completion, and 6-DoF grasp estimation to manipulate objects from partial RGB-D observations."
youtube_embed: 9Ca3zzUI8Ic
main_figure: /images/publications/language-guided-grasping-system-main.webp
main_figure_alt: "Language-guided grasping pipeline for target selection, object completion, grasp generation, pose selection, and robot execution."
main_figure_caption: "End-to-end language-guided grasping system under partial observation."
featured: true
thumbnail: /images/projects/language-guided-grasping.jpg
media_webm: /images/publications/language-guided-grasping.webm
media_mp4: /images/publications/language-guided-grasping.mp4
media_poster: /images/publications/language-guided-grasping.webp
authors: "Dilermando Almeida, Juliano Negri, Guilherme Lazzarini, Thiago H. Segreto, Ranulfo Bezerra, Gustavo J. G. Lahr, Ricardo V. Godoy, Marcelo Becker"
tags: [control,grasping,vision,manipulation,mobile-manipulation,perception]
doi: 
code: 
permalink: /publication/2026-vlm-grasp
excerpt: 'Accepted at SSRR 2026. A language-guided grasping system for field inspection and maintenance, combining object completion and grasp selection under partial observation on Spot.'
date: 2026-02-24
venue: '2026 IEEE International Symposium on Safety, Security, and Rescue Robotics (SSRR) · Accepted'
paperurl: 'https://arxiv.org/abs/2603.07866'
bibtexurl: ''
citation: ''
---



Offshore inspection and maintenance have increasingly been using legged robots for routine sensing, yet many useful interventions still require physical interaction with tools, containers, and task-relevant objects. Employing robots for these tasks can reduce operators' exposure in confined, elevated, or potentially explosive areas. This paper presents a language-guided grasping pipeline for a legged mobile manipulator operating under partial observation. An operator defines the target, the system grounds it in RGB with open-vocabulary detection and promptable segmentation, extracts an object-centric RGB-D point cloud, improves sparse geometry through depth compensation and point-cloud completion, and selects a 6-DoF grasp using collision, clearance, reachability, and approach constraints. The system is implemented on a quadruped robot with an arm and evaluated in two cluttered tabletop scenes motivated by small-object retrieval during inspection and maintenance. Across paired trials, the proposed pipeline achieved 9/10 successful grasps, compared with 3/10 for a view-dependent deployment baseline. In this controlled setting, object-centric completion and execution-aware selection reduced approach collisions and improved the reliability of language-guided grasping for supervised field manipulation.
