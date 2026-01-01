import pandas as pd

def compute_performance_metrics(cleaned_data_path, output_path):
    df = pd.read_csv(cleaned_data_path)

    # Separate pre and post trials
    pre = df[df["trial_phase"] == "pre"]
    post = df[df["trial_phase"] == "post"]

    def summarize(data, phase):
        return {
            "trial_phase": phase,
            "avg_fuel_mass": data["fuel_mass"].mean(),
            "avg_co2_emissions": data["co2_emissions"].mean(),
            "avg_speed": data["speed"].mean(),
            "fuel_per_nm": (data["fuel_mass"] / data["speed"]).mean(),
            "co2_per_nm": (data["co2_emissions"] / data["speed"]).mean(),
            "efficiency_index": (data["fuel_mass"] / data["speed"]).mean()
        }

    summary_pre = summarize(pre, "pre")
    summary_post = summarize(post, "post")

    result = pd.DataFrame([summary_pre, summary_post])

    # Improvement percentages
    result["fuel_reduction_pct"] = (
        (summary_pre["avg_fuel_mass"] - summary_post["avg_fuel_mass"])
        / summary_pre["avg_fuel_mass"]
    ) * 100

    result["co2_reduction_pct"] = (
        (summary_pre["avg_co2_emissions"] - summary_post["avg_co2_emissions"])
        / summary_pre["avg_co2_emissions"]
    ) * 100

    result.to_csv(output_path, index=False)

    return result
