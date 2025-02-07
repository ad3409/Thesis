import time
import random
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, f1_score

# Model names
models = ["RAG ONLY", "RAG + PDF for Training", "Without RAG (Only PDF)"]

# Dummy ground truth and predictions for evaluation
y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]  
y_preds = {
    "RAG ONLY": [1, 0, 1, 1, 0, 1, 1, 0, 1, 0],
    "RAG + PDF for Training": [1, 0, 1, 1, 0, 1, 0, 0, 1, 1],
    "Without RAG (Only PDF)": [1, 1, 1, 1, 0, 1, 0, 0, 1, 0]
}

# Function to measure latency
def measure_latency():
    start_time = time.time()
    time.sleep(random.uniform(0.1, 0.5))  # Simulating response time
    return round(time.time() - start_time, 3)

# Function to evaluate ethical compliance (simulated)
def evaluate_ethics(model):
    scores = {
        "RAG ONLY": random.uniform(0.75, 0.9),
        "RAG + PDF for Training": random.uniform(0.8, 0.95),
        "Without RAG (Only PDF)": random.uniform(0.6, 0.85)
    }
    return round(scores[model], 2)

# Function to simulate perplexity (lower is better)
def compute_perplexity():
    return round(random.uniform(20, 60), 2)  # Simulated perplexity score

# Compute metrics for each model
results = {}
for model in models:
    accuracy = accuracy_score(y_true, y_preds[model])
    f1 = f1_score(y_true, y_preds[model])
    latency = measure_latency()
    ethical_compliance = evaluate_ethics(model)
    perplexity = compute_perplexity()
    
    results[model] = {
        "Accuracy": accuracy, 
        "F1 Score": f1, 
        "Latency (s)": latency, 
        "Ethical Compliance": ethical_compliance, 
        "Perplexity": perplexity
    }

# Visualization
metrics = ["Accuracy", "F1 Score", "Latency (s)", "Ethical Compliance", "Perplexity"]
bar_width = 0.15
x = np.arange(len(metrics))

fig, ax = plt.subplots(figsize=(12, 6))
for i, model in enumerate(models):
    values = [results[model][metric] for metric in metrics]
    ax.bar(x + i * bar_width, values, bar_width, label=model)

ax.set_xticks(x + bar_width)
ax.set_xticklabels(metrics)
ax.set_ylabel("Score / Time / Perplexity")
ax.set_title("Comparison of RAG vs Non-RAG Approaches Across Key Metrics")
ax.legend()
plt.show()
