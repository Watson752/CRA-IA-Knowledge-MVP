---
title: Defence in Depth
aliases:
  - Defense in Depth
note_type: software-concept
primary_domain: software-data
domains:
  - software
  - data
  - control
  - risk
  - audit
domain: software
status: active
classification: public
content_origin: general-professional-knowledge
authoritative: false
official_source: null
publisher: null
publication_date: null
as_of_date: 2026-07-23
last_verified: 2026-07-23
source_url: null
source_status: unknown
owner: MVP-Author
review_status: unreviewed
approved_for_ai_retrieval: false
related_sources: []
related_cases: []
related_processes: []
related_organizations: []
related_systems: []
related_datasets: []
related_risks: []
related_controls: []
related_procedures: []
related_methods: []
tags: []
---

**Defence in depth** (defense in depth) is a security strategy that layers multiple independent [[Control]]s so that failure of one layer does not wholly compromise protection. Layers may include physical security, network segmentation, endpoint protection, identity and access management, application hardening, encryption, and monitoring. The goal is to increase attacker cost and reduce single points of failure.

The approach assumes breaches may occur and emphasizes detection, containment, and recovery—not perimeter-only thinking. It aligns with [[Cybersecurity]] programs and [[Security Controls]] catalogs that span preventive and detective measures.

Auditors assess whether layers are truly independent (shared dependencies can collapse “depth”) and whether gaps exist at integration points (APIs, cloud shared responsibility boundaries, legacy systems). [[Monitoring and Reporting]] is often a critical late layer for identifying successful bypass of earlier controls.

Defence in depth complements least privilege, secure defaults, and change management within [[IT Controls]].

## Related notes

- [[Cybersecurity]]
- [[Security Controls]]
- [[IT Controls]]
- [[Monitoring and Reporting]]
- [[Control]]

## Sources

General professional knowledge; NIST SP 800-series and cybersecurity architecture literature. See source register when linked.
