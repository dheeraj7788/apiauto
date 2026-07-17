import yaml
import json
from pathlib import Path


def load_yaml(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def save_yaml(data, file_path):
    with open(file_path, "w", encoding="utf-8") as f:
        yaml.dump(
            data,
            f,
            sort_keys=False,
            allow_unicode=True
        )


def pretty_json(data):
    return json.dumps(data, indent=2)
