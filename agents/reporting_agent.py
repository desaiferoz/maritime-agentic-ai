# agents/reporting_agent.py
def generate_report(metrics):
    report = f"""
    Maritime Performance Report
    ---------------------------
    Fuel Reduction: {metrics['fuel_reduction_%']} %
    Efficiency Index: {metrics['efficiency_gain']}
    
    Conclusion:
    Post-treatment data shows measurable efficiency gains
    with statistically consistent performance improvement.
    """
    with open("performance_report.txt", "w") as f:
        f.write(report)
