# agents/ingestion_agent.py
import pandas as pd

def ingest_data(file_path):
    df = pd.read_csv(file_path)
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    df = df.dropna(subset=["fuel_mass", "shaft_power"])
    return df
