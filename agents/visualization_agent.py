import pandas as pd
import matplotlib.pyplot as plt

def plot_fuel_trend(df):
    plt.figure(figsize=(8,5))
    for phase in df["trial_phase"].unique():
        subset = df[df["trial_phase"] == phase]
        plt.plot(subset["timestamp"], subset["fuel_mass"], marker='o', label=phase)

    plt.xlabel("Time")
    plt.ylabel("Fuel Mass")
    plt.title("Fuel Consumption Trend (Pre vs Post)")
    plt.legend()
    plt.tight_layout()
    plt.savefig("outputs/fuel_trend.png", dpi=300)
    plt.close()



def plot_co2_trend(df):
    plt.figure(figsize=(8,5))
    for phase in df["trial_phase"].unique():
        subset = df[df["trial_phase"] == phase]
        plt.plot(subset["timestamp"], subset["co2_emissions"], marker='o', label=phase)

    plt.xlabel("Time")
    plt.ylabel("CO₂ Emissions")
    plt.title("CO₂ Emissions Trend (Pre vs Post)")
    plt.legend()
    plt.tight_layout()
    plt.savefig("outputs/co2_trend.png", dpi=300)
    plt.close()



def plot_speed_vs_power(df):
    plt.figure(figsize=(6,5))
    for phase in df["trial_phase"].unique():
        subset = df[df["trial_phase"] == phase]
        plt.scatter(subset["speed"], subset["shaft_power"], label=phase)

    plt.xlabel("Speed")
    plt.ylabel("Shaft Power")
    plt.title("Speed vs Shaft Power (Operational Envelope)")
    plt.legend()
    plt.tight_layout()
    plt.savefig("outputs/speed_vs_power.png", dpi=300)
    plt.close()
