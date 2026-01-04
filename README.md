# Maritime Performance & Emissions Analytics
Agent-Inspired, Validation-Driven Analytics Pipeline

## Overview

This project demonstrates an agent-inspired, modular analytics pipeline designed to evaluate vessel fuel efficiency, performance, and emissions across pre- and post-trial operating conditions.

The system ingests raw vessel operational data, applies structured validation rules, computes normalized performance metrics, and produces Power BI–ready outputs alongside engineering-grade Python visualizations.
The focus is on explainability, traceability, and defensible analytics, rather than black-box automation.

The architecture reflects real-world performance verification workflows used in maritime, energy, and industrial efficiency studies.

## Architecture & Modular Design
The pipeline follows an agent-inspired modular design, where each module encapsulates a single, clearly defined analytical responsibility.
This enables:
  Transparent reasoning
  Reproducible outputs
  Quality-controlled analysis

Future extensibility toward autonomous agent execution

Each module mirrors how an expert analyst would structure the workflow, while remaining deterministic and audit-ready.
## Modules (Agent-Inspired Responsibilities)
## Ingestion Module
  Reads raw vessel operational datasets
  Standardizes schema and column naming
  Prepares structured data for validation
## Validation Module
  Cleans missing or malformed records
  Safely converts numeric fields
  Enforces consistent data types using externalized rules
  Outputs a clean, analysis-ready dataset
## Performance Analytics Module
  Segregates data into pre- and post-trial phases
  Computes average fuel consumption, speed, and emissions
  Normalizes metrics using fuel-per-nautical-mile logic
  Calculates:
    Fuel reduction percentage
    CO₂ reduction percentage
    Efficiency index
## Reporting & Visualization Module
  Produces summarized, BI-ready tables for dashboards
  Generates engineering validation plots using Python
  Supports executive reporting and technical verification

| Metric            | Description                           |
| ----------------- | ------------------------------------- |
| Avg Fuel Mass     | Mean fuel consumption per trial phase |
| Avg CO₂ Emissions | Mean emissions per phase              |
| Avg Speed         | Average vessel speed                  |
| Fuel per NM       | Fuel normalized by speed              |
| CO₂ per NM        | Emissions normalized by speed         |
| Efficiency Index  | Fuel-per-NM efficiency indicator      |
| Fuel Reduction %  | Pre vs post fuel improvement          |
| CO₂ Reduction %   | Pre vs post emissions improvement     |

## Sample Results (Demo Dataset)
Fuel reduction: ~10.7%
CO₂ reduction: ~7.3%
Speed: Slight increase post-trial
Efficiency: ~13% improvement
These results are conservative, realistic, and engineering-defensible, aligned with real-world trial validation expectations.

## Tech Stack
Python
Pandas, NumPy
Matplotlib (engineering validation plots)
YAML-based rule configuration
Modular, agent-inspired architecture
BI-ready CSV outputs

## How to Run
pip install -r requirements.txt
python main.py


## Outputs
  Cleaned and validated datasets in /data
  Performance summary CSVs in /outputs
  Engineering validation plots in /outputs






