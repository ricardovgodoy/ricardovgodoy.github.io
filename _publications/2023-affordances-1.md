---
title: "An Affordances and Electromyography Based Telemanipulation Framework for Control of Robotic Arm-Hand Systems"
collection: publications
category: conferences
pubtype: conference
tags: [teleoperation, shared-control, wearable-sensing, control, biosignal, manipulation]
doi: 10.1109/IROS55552.2023.10341955        # optional
permalink: /publication/2023-affordances-1
excerpt: 'In this paper, we propose an intuitive, affordances-oriented EMG-based telemanipulation framework for a robot arm-hand system that allows for dexterous control of the device.'
date: 2023-10-01
venue: '2023 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)'
paperurl: 'https://ieeexplore.ieee.org/document/10341955'
bibtexurl: 'http://ricardovgodoy.github.io/files/2023-affordances-1.bib'
citation: 'R. V. Godoy, B. Guan, A. Dwivedi and M. Liarokapis, "An Affordances and Electromyography Based Telemanipulation Framework for Control of Robotic Arm-Hand Systems," 2023 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), Detroit, MI, USA, 2023, pp. 6998-7004, doi: 10.1109/IROS55552.2023.10341955.'
---

Over the last decades, significant research effort has been put into creating Electromyography (EMG) based controllers for intuitive, hands-free control of robotic arms and hands. To achieve this, machine learning models have been employed to decode human motion and intention using EMG signals as input and to deliver several applications, such as prosthesis control using gesture classification. Despite the advances introduced by new deep learning techniques, real-time control of robot arms and hands using EMG signals as input still lacks accuracy, especially when a plethora of gestures are included as labels in the case of classification. This has been observed to be due to the noise and non-stationarity of the EMG signals and the increased dimensionality of the problem. In this paper, we propose an intuitive, affordances-oriented EMG-based telemanipulation framework for a robot arm-hand system that allows for dexterous control of the device. An external camera is utilized to perform scene understanding and object detection and recognition, providing grasping and manipulation assistance to the user and simplifying control. Object-specific Transformer-based classifiers are employed based on the affordances of the object of interest, reducing the number of possible gesture outputs, dividing and conquering the problem, and resulting in a more robust and accurate gesture decoding system when compared to a single generic classification model. The performance of the proposed system is experimentally validated in a remote telemanipulation setting, where the user successfully performs a set of dexterous manipulation tasks.
