---
title: "From Perception to Assistance: VLM-Driven Potential Fields for Shared-Control Manipulation"
collection: publications
category: preprints
pubtype: preprint
featured: true
venue: 'Preprint'
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

<iframe width="560" height="315" src="https://www.youtube.com/embed/UNAeSZh0kCU?si=SlpDeKnhavhE5Z7W" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


Teleoperating a robotic manipulator in industrial environments demands precision that camera-based interfaces alone struggle to deliver. The operator must align the end-effector with a target in clutter, under limited depth perception, and without colliding with the surrounding structures. This paper presents a shared-autonomy framework that assists the operator throughout this process. A single RGB-D camera captures the operator's arm motion and hand gestures without wearables, fiducials, or a calibration stage. The intended target is specified by a free-form text prompt, grounded by a vision-language model in the robot's gripper camera, and tracked across its onboard cameras by a promptable video-segmentation model, resulting in a grasp frame continuously separated from the obstacle map. Every commanded motion is executed by a GPU-accelerated model-predictive controller that enforces self- and environment-collision avoidance against an online volumetric reconstruction, while a potential field corrects the operator's reference toward the grounded target during the final approach. An autonomous mode can be gesture-triggered to complete the grasp on the same target without a separate perception pipeline. The framework is validated on a quadruped mobile manipulator. The interface achieves a positional RMSE of 59 mm relative to motion-capture ground truth, and the controller keeps the arm at least 18 cm from obstacles while the operator deliberately commands the arm into them by 6 cm. In an industrial valve manipulation and a pick-and-place task, the full framework succeeded in all trials, while ablating either the collision or the assistance module produced failures through complementary mechanisms, and autonomous execution succeeded in four of five trials per task.

