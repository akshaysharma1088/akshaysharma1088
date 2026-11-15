<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=Venom&color=0:0B0F19,50:111827,100:1E3A8A&height=200&section=header&text=Akshay%20Sharma&fontSize=46&fontColor=F8FAFC&fontAlignY=38&desc=Lead%20Member%20of%20Technical%20Staff%20%40%20Salesforce%20%20%E2%80%A2%20%20IEEE%20Senior%20Member&descSize=17&descAlignY=62&stroke=38BDF8&strokeWidth=1" width="100%" alt="Akshay Sharma" />
</div>

<p align="center">
  <a href="https://akshaysharma1088.github.io"><img src="https://img.shields.io/badge/Portfolio-akshaysharma1088.github.io-2563EB?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Portfolio"/></a>
  <a href="https://orcid.org/0009-0009-5718-2187"><img src="https://img.shields.io/badge/ORCID-0009--0009--5718--2187-A6CE39?style=for-the-badge&logo=orcid&logoColor=white" alt="ORCID"/></a>
  <a href="https://www.ieee.org"><img src="https://img.shields.io/badge/IEEE-Senior_Member-00629B?style=for-the-badge&logo=ieee&logoColor=white" alt="IEEE Senior Member"/></a>
  <a href="https://github.com/akshaysharma1088/dataranger"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/akshaysharma1088/akshaysharma1088/main/stats/ecosystem_badge.json&style=for-the-badge" alt="Ecosystem Downloads"/></a>
</p>

---

### Autonomous Data Pipeline Verification & Repair Ecosystem

**`pipeverify`** and **`dataranger`** form a closed-loop reliability architecture for enterprise lakehouses, Snowflake, DuckDB, and dbt pipelines:

<p align="left">
  <a href="https://pypi.org/project/pipeverify/"><img src="https://img.shields.io/pypi/v/pipeverify?label=pipeverify&style=flat-square&logo=pypi&logoColor=white&color=0284C7" alt="pipeverify PyPI"/></a>
  <a href="https://pepy.tech/project/pipeverify"><img src="https://static.pepy.tech/badge/pipeverify" alt="pipeverify Downloads"/></a>
  &nbsp;&nbsp;➔&nbsp;&nbsp;
  <a href="https://pypi.org/project/dataranger/"><img src="https://img.shields.io/pypi/v/dataranger?label=dataranger&style=flat-square&logo=pypi&logoColor=white&color=4F46E5" alt="dataranger PyPI"/></a>
  <a href="https://pepy.tech/project/dataranger"><img src="https://static.pepy.tech/badge/dataranger" alt="dataranger Downloads"/></a>
</p>

```mermaid
flowchart LR
    A[Snowflake / dbt / DuckDB] --> B(pipeverify: Deterministic Verification & Drift Telemetry)
    B -->|Structured Anomaly Payload| C(dataranger: Autonomous Root-Cause Diagnosis & Repair)
    C -->|Provable Patch & GitHub Action| A
```

| System | Architectural Role | Core Capabilities | Install |
| :--- | :--- | :--- | :--- |
| **[pipeverify](https://github.com/akshaysharma1088/pipeverify)** | **Stage 1: Verification & Telemetry** | Verifies that pipeline changes leave data provably right—not just the job green. Detects total-shift, schema drift, and invariant breaches across CSV, Parquet, Excel, and SQL sources. | `pip install pipeverify` |
| **[dataranger](https://github.com/akshaysharma1088/dataranger)** | **Stage 2: Autonomous Repair** | Open-source AI agent that consumes verification telemetry, fixes only what it can prove against the source, and routes ambiguous anomalies with evidence. Supports Snowflake, dbt, DuckDB, and MCP. | `pip install dataranger` |

---

### Research, Benchmarks & Open-Source Systems

| Focus Area | Project / Publication | Venue / Artifacts |
| :--- | :--- | :--- |
| **Enterprise Graph RAG** | *Partitioning Enterprise Knowledge Graphs for Governed Retrieval* | **IEEE CCWC 2027** (Accepted) |
| **Conversational AI Evaluation** | **[bird-dissatisfaction-research](https://github.com/akshaysharma1088/bird-dissatisfaction-research)** — Mid-dialogue customer dissatisfaction detection (BIRD, VADER, RoBERTa baselines) | Research Repository & Annotated Dataset |
| **Financial Graph RAG** | **[fraudrag](https://github.com/akshaysharma1088/fraudrag)** — Knowledge Graph-Augmented RAG for Financial Statement Fraud Detection | Open-Source Framework |
| **LLM Pipeline Benchmarks** | *Benchmarking Claude Haiku, Sonnet, and Opus on 64 Broken Data Pipelines* | **HackerNoon** Technical Benchmark |
| **Lakehouse & AI Architecture** | *From Support Transcripts to Trusted AI Agents: Snowflake, Apache Iceberg, Cortex AI & Neo4j* | **Medium** Architecture Deep-Dive |

* **Academic Peer Review & Mentorship:** Reviewer for *VLDB*, *IEEE Access*, *IEEE IT Professional*, *CAAI Transactions on Intelligence Technology*, and *Wiley* journals; Industry Mentor at *CodePath*.
