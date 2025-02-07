import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import filedialog

# Function to upload dataset
def upload_file():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(
        title="Select your dataset",
        filetypes=[("CSV Files", "*.csv"), ("Excel Files", "*.xlsx;*.xls")]
    )
    return file_path

# Load dataset
def load_data(file_path):
    if file_path.endswith(".csv"):
        return pd.read_csv(file_path)
    elif file_path.endswith(".xlsx") or file_path.endswith(".xls"):
        return pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format. Please upload a CSV or Excel file.")

# Function to process the data and extract key metrics
def process_data(df):
    required_columns = [
        "Satisfaction Score", "Accuracy", "Ethics Compliance",
        "Response Time", "Data Retrieval Speed", "Scalability"
    ]
    
    # Ensure all required columns exist
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")
    
    # Compute mean scores for each model
    model_scores = df.groupby("Model")[required_columns].mean()
    
    return model_scores

# Function to plot a bar chart for comparison
def plot_comparison(model_scores):
    plt.figure(figsize=(10, 6))
    bar_width = 0.2
    index = np.arange(len(model_scores.columns))
    
    # Create bars for each model
    for i, model in enumerate(model_scores.index):
        plt.bar(index + i * bar_width, model_scores.loc[model], bar_width, label=model)
    
    # Formatting
    plt.xlabel("Metrics")
    plt.ylabel("Performance Values")
    plt.title("Model Performance Comparison")
    plt.xticks(index + bar_width, model_scores.columns, rotation=25, ha="right")
    plt.legend()
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    
    # Show the graph
    plt.tight_layout()
    plt.show()

# Main function to run the script
def main():
    print("Please select the dataset file (CSV or Excel).")
    file_path = upload_file()
    
    if not file_path:
        print("No file selected. Exiting.")
        return
    
    try:
        df = load_data(file_path)
        model_scores = process_data(df)
        
        print("\nModel Performance Comparison (Averaged Scores):\n")
        print(model_scores)
        
        plot_comparison(model_scores)
    
    except Exception as e:
        print(f"Error: {e}")

# Run the script
if __name__ == "__main__":
    main()
