import pandas as pd
import yaml

def validate_and_clean(input_path, output_path, rules_path):
    df = pd.read_csv(input_path)

    # Normalize column names
    df.columns = df.columns.str.strip().str.lower()

    # Drop missing rows
    df = df.dropna()


    # Load validation rules
    with open(rules_path, "r") as f:
        rules = yaml.safe_load(f)

    # Apply rule-based validation
    for column, limits in rules.items():
        if column in df.columns:
            if "min" in limits:
                df = df[df[column] >= limits["min"]]
            if "max" in limits:
                df = df[df[column] <= limits["max"]]

    # Save cleaned data
    df.to_csv(output_path, index=False)

    return df