import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def evaluate_robustness(survey_data_path):
    # Load survey data
    data = pd.read_csv(survey_data_path)

    # Key metrics to evaluate
    metrics = {
        "Consistency Score": [],
        "Fairness Score": [],
        "Accuracy Robustness": [],
        "Resilience Score": []
    }

    # Simulate calculations based on survey
    for _, row in data.iterrows():
        metrics["Consistency Score"].append(row['score'] * np.random.uniform(0.9, 1.1))
        metrics["Fairness Score"].append(row['fairness'] * np.random.uniform(0.95, 1.05))
        metrics["Accuracy Robustness"].append(row['accuracy'] * np.random.uniform(0.9, 1.0))
        metrics["Resilience Score"].append(row['resilience'] * np.random.uniform(0.85, 1.0))

    # Compute average metrics
    summary = {k: np.mean(v) for k, v in metrics.items()}
    return summary

# Path to your survey data
survey_data_path = "survey_results.csv"  # Replace with your actual file path

# Compute robustness summary
robustness_summary = evaluate_robustness(survey_data_path)

# Plot bar chart
plt.figure(figsize=(10, 6))
plt.bar(robustness_summary.keys(), robustness_summary.values(), color=['blue', 'green', 'red', 'purple'])
plt.xlabel("Metrics")
plt.ylabel("Mean Score")
plt.title("Robustness Metrics Visualization")
plt.ylim(0, max(robustness_summary.values()) + 0.1)  # Adjust y-axis dynamically
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Display values on top of bars
for i, (metric, score) in enumerate(robustness_summary.items()):
    plt.text(i, score + 0.02, f"{score:.2f}", ha='center', fontsize=12, fontweight='bold')

plt.show()
