from agents.validation_agent import validate_and_clean
from agents.performance_agent import compute_performance_metrics

RAW_DATA = "data/raw_vessel_data.csv"
CLEAN_DATA = "data/cleaned_data.csv"
PERF_DATA = "data/performance_summary.csv"
RULES = "rules/maritime_standards.yaml"

# Step 1: Validation & cleaning
validate_and_clean(RAW_DATA, CLEAN_DATA, RULES)

# Step 2: Performance analytics (pre vs post)
compute_performance_metrics(CLEAN_DATA, PERF_DATA)

print("Pipeline completed: validation + performance analytics done.")
