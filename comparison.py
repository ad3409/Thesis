 import time
import random
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, f1_score

# Simulating responses for three models\
models = ["RAG ONLY", "RAG + PDF for Training", "Without RAG (Only PDF)"]\
\
# Dummy ground truth and predicted labels for evaluation\
y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]  # Ground truth labels\
y_preds = \{\
    "RAG ONLY": [1, 0, 1, 1, 0, 1, 1, 0, 1, 0],\
    "RAG + PDF for Training": [1, 0, 1, 1, 0, 1, 0, 0, 1, 1],\
    "Without RAG (Only PDF)": [1, 1, 1, 1, 0, 1, 0, 0, 1, 0]\
\}\
\
# Function to measure latency\
def measure_latency(model):\
    start_time = time.time()\
    time.sleep(random.uniform(0.1, 0.5))  # Simulating response time\
    return round(time.time() - start_time, 3)\
\
# Function to evaluate ethical compliance (simulated)\
def evaluate_ethics(model):\
    scores = \{\
        "RAG ONLY": random.uniform(0.75, 0.9),\
        "RAG + PDF for Training": random.uniform(0.8, 0.95),\
        "Without RAG (Only PDF)": random.uniform(0.6, 0.85)\
    \}\
    return round(scores[model], 2)\
\
# Compute Accuracy, F1 Score, Latency, and Ethical Compliance for each model\
results = \{\}\
for model in models:\
    accuracy = accuracy_score(y_true, y_preds[model])\
    f1 = f1_score(y_true, y_preds[model])\
    latency = measure_latency(model)\
    ethical_compliance = evaluate_ethics(model)\
    \
    results[model] = \{"Accuracy": accuracy, "F1 Score": f1, "Latency": latency, "Ethical Compliance": ethical_compliance\}\
\
# Plot results\
metrics = ["Accuracy", "F1 Score", "Latency", "Ethical Compliance"]\
bar_width = 0.2\
x = np.arange(len(metrics))\
\
fig, ax = plt.subplots(figsize=(10, 6))\
for i, model in enumerate(models):\
    values = [results[model][metric] for metric in metrics]\
    ax.bar(x + i * bar_width, values, bar_width, label=model)\
\
ax.set_xticks(x + bar_width)\
ax.set_xticklabels(metrics)\
ax.set_ylabel("Score / Time (s)")\
ax.set_title("Comparison of RAG vs Non-RAG Approaches")\
ax.legend()\
plt.show()\
}
