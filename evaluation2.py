import time
start_time = time.time()
outputs = model.generate(inputs.input_ids)
end_time = time.time()

print("Latency (ms):", (end_time - start_time) * 1000)