import json

def log_step(step):
    with open("demo_logs.json", "a") as f:
        f.write(json.dumps(step, indent=2))
        f.write(",\n")
