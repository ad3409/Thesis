from transformers import AutoModelForCausalLM, AutoTokenizer
from datasets import load_dataset, load_metric

# Load the Mistral model
model_name = "mistralai/Mistral-7B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Dataset and Metric
dataset = load_dataset("squad", split="validation")
metric = load_metric("squad")

# Run evaluation
for example in dataset:
    input_text = example["question"] + " " + example["context"]
    inputs = tokenizer(input_text, return_tensors="pt", truncation=True)
    outputs = model.generate(inputs.input_ids)
    prediction = tokenizer.decode(outputs[0], skip_special_tokens=True)
    # Compare predictions to ground truth for metrics