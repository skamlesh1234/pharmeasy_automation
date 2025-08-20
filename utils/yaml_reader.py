import yaml
import os

def read_yaml(file):
    if not os.path.exists(file):
        raise FileNotFoundError(f"YAML file not found: {file}")
    
    with open(file, "r") as f:
        data = yaml.safe_load(f)
        if data is None:
            raise ValueError(f"YAML file {file} is empty")
        return data
