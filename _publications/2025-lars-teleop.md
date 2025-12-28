---
title: "A Vision-Based Shared-Control Teleoperation Scheme for Controlling the Robotic Arm of a Four-Legged Robot"
collection: publications
category: conferences
pubtype: conference
tags: [teleoperation, shared-control, control, vision, perception, manipulation, grasping, mobile-manipulation, legged-robots]
doi: 10.1109/LARS69345.2025.11272961       # optional
code: https://github.com/EESC-LabRoM/MoveitServoing/blob/spot_teleop/
permalink: /publication/2025-lars-teleop
excerpt: 'This paper introduces a vision-based teleoperation shared control framework designed to overcome real-time teleoperation limitations, providing intuitive, real-time control of a quadruped’s manipulator'
date: 2025-10-03
venue: '2025 IEEE Latin American Robotics Symposium (LARS)'
paperurl: 'https://ieeexplore.ieee.org/document/11272961'
citation: 'M. V. D. Silva et al., "A Vision-Based Shared-Control Teleoperation Scheme for Controlling the Robotic Arm of a Four-Legged Robot," 2025 Latin American Robotics Symposium (LARS), Monterrey, Mexico, 2025, pp. 1-6, doi: 10.1109/LARS69345.2025.11272961. keywords: {Wrist;Service robots;Tracking;Robot vision systems;Manipulators;Real-time systems;Safety;Quadrupedal robots;Collision avoidance;Robots}

'
---

This paper received the Best Paper Award at LARS 20205!

<iframe width="560" height="315" src="https://www.youtube.com/embed/klgpq57c8UM?si=bR5CQGy6fnOEymTA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


In hazardous and remote environments, robotic systems perform critical tasks demanding improved safety and efficiency. Among these, quadruped robots with manipulator arms offer mobility and versatility for complex operations. However, teleoperating quadruped robots is challenging due to the lack of integrated obstacle detection and intuitive control methods for the robotic arm, increasing collision risks in confined or dynamically changing workspaces. Teleoperation via joysticks or pads can be non-intuitive and demands a high level of expertise due to its complexity, culminating in a high cognitive load on the operator. To address this challenge, a teleoperation approach that directly maps human arm movements to the robotic manipulator offers a simpler and more accessible solution. This work proposes an intuitive remote control by leveraging a vision-based pose estimation pipeline that utilizes an external camera with a machine learning-based model to detect the operator's wrist position. The system maps these wrist movements into robotic arm commands to control the robot's arm in real-time. A trajectory planner ensures safe teleoperation by detecting and preventing collisions with both obstacles and the robotic arm itself. The system was validated on the real robot, demonstrating robust performance in real-time control. This teleoperation approach provides a cost-effective solution for industrial applications where safety, precision, and ease of use are paramount, ensuring reliable and intuitive robotic control in high-risk environments.



