---
title: "Input-Contract-Aware Conditioning for Reproducible Volumetric Mapping Across Heterogeneous Robotic Platforms"
collection: publications
authors: "Sofia Milagros Castaño Vanegas, Dayana Katerin Paredes Melo, M. A. Pastrana, Ricardo V. Godoy, Daniel M. Muñoz, Marcelo Becker"
category: conferences
pubtype: conference
permalink: /publication/2026-input-contract-aware-mapping
excerpt: 'Accepted at the 2026 IEEE Latin American Robotics Symposium (LARS).'
date: 2026-09-21
venue: '2026 IEEE Latin American Robotics Symposium (LARS)'
tags: [mapping, perception]
---

Volumetric mapping pipelines rely on assumptions regarding pose validity,
frame interpretation, cloud-pose timing, and observation admissibility before
integration. In practice, these assumptions are rarely made explicit, making
mapping failures difficult to attribute and replay conditions difficult to
reproduce across heterogeneous robotic platforms and data sources. This paper
presents an explicit, auditable, and reproducible input-contract formulation
together with a backend-preserving wrapper that enforces the contract while
leaving the underlying mapping pipeline unchanged. The approach is evaluated
through paired replay experiments on Spot, ANYmal, and a retained Dynablox
data source using archived PCD-derived proxy metrics and a runtime
timing-admissibility audit. Results show that the wrapper is non-invasive when input assumptions already hold.
However, when they do not, it enables clear attribution of mapping differences to upstream assumption violations.
These findings support input-contract-aware conditioning as a practical mechanism for making mapping assumptions visible, checkable, and reproducible.
