<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./assets/hero-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="./assets/hero-light.svg">
    <img alt="Akshay Sharma - Lead Data & AI Systems Architect" src="./assets/hero-dark.svg" width="100%">
  </picture>
</div>

<br/>

<p align="center">
  <a href="https://akshaysharma1088.github.io"><img src="https://img.shields.io/badge/Portfolio-akshaysharma1088.github.io-2563EB?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Portfolio"/></a>
  <a href="https://www.ieee.org"><img src="https://img.shields.io/badge/IEEE-Senior_Member-00629B?style=for-the-badge&logo=ieee&logoColor=white" alt="IEEE Senior Member"/></a>
  <a href="https://github.com/akshaysharma1088/dataranger"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/akshaysharma1088/akshaysharma1088/main/stats/ecosystem_badge.json&style=for-the-badge" alt="Ecosystem Downloads"/></a>
</p>

---

### Autonomous Data Pipeline Verification & Repair Ecosystem

**`pipeverify`** and **`dataranger`** form a closed-loop reliability architecture for enterprise lakehouses, Snowflake, and dbt pipelines:

<p align="left">
  <a href="https://pypi.org/project/pipeverify/"><img src="https://img.shields.io/pypi/v/pipeverify?label=pipeverify&style=flat-square&logo=pypi&logoColor=white&color=0284C7" alt="pipeverify PyPI"/></a>
  <a href="https://pepy.tech/project/pipeverify"><img src="https://static.pepy.tech/badge/pipeverify" alt="pipeverify Downloads"/></a>
  &nbsp;&nbsp;➔&nbsp;&nbsp;
  <a href="https://pypi.org/project/dataranger/"><img src="https://img.shields.io/pypi/v/dataranger?label=dataranger&style=flat-square&logo=pypi&logoColor=white&color=4F46E5" alt="dataranger PyPI"/></a>
  <a href="https://pepy.tech/project/dataranger"><img src="https://static.pepy.tech/badge/dataranger" alt="dataranger Downloads"/></a>
</p>

```mermaid
flowchart LR
    A[Snowflake / dbt / Lakehouse] --> B(pipeverify: Deterministic Verification & Drift Telemetry)
    B -->|Structured Anomaly Payload| C(dataranger: Autonomous Root-Cause Diagnosis & Repair)
    C -->|Validated Patch & CI/CD Action| A
