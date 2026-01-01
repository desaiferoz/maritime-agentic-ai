# Agentic AI Pipeline for Maritime Performance & Emissions Analytics

## Overview
This project demonstrates an agentic, validation-driven analytics pipeline designed to evaluate vessel performance, fuel efficiency, and emissions reduction using operational trial data.

The pipeline mirrors real-world engineering and maritime trial analysis, focusing on **data integrity, explainability, and defensible performance benchmarking** rather than black-box modeling.

It is structured to support downstream BI tools (e.g., Power BI) and customer-ready technical reporting.

---

## Problem Statement
Maritime fuel efficiency and emissions claims must be supported by:
- Clean, validated operational data
- Comparable pre/post trial analysis
- Transparent, auditable calculations

This project addresses these requirements by implementing a modular, agent-based workflow that:
1. Validates raw vessel data
2. Normalizes metrics for fair comparison
3. Computes performance and emissions KPIs
4. Produces BI-ready outputs

---

## Architecture (Agentic Workflow)

Raw Vessel Data
↓
Ingestion Agent
↓
Validation Agent
↓
Performance Analytics Agent
↓
Reporting Agent
↓

BI / Dashboard / Client Reports

This project demonstrates an end-to-end agentic analytics workflow with
validation-driven insights, executive dashboards, and engineering-grade
visualization artifacts suitable for customer and regulatory review.

### Requirements
- Python 3.10+
- pandas
- numpy
- matplotlib
- pyyaml

