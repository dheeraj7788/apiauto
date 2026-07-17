import yaml
import json
from pathlib import Path

OLD_SPEC = "openapi/old-openapi.yaml"
NEW_SPEC = "openapi/openapi.yaml"

REPORT = "docs/api-change-report.md"


def load_yaml(file):
    with open(file, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def get_endpoints(spec):
    endpoints = {}

    for path, methods in spec.get("paths", {}).items():
        for method in methods:
            endpoints[f"{method.upper()} {path}"] = methods[method]

    return endpoints


old_spec = load_yaml(OLD_SPEC)
new_spec = load_yaml(NEW_SPEC)

old_endpoints = get_endpoints(old_spec)
new_endpoints = get_endpoints(new_spec)

added = sorted(set(new_endpoints) - set(old_endpoints))
removed = sorted(set(old_endpoints) - set(new_endpoints))
common = sorted(set(old_endpoints) & set(new_endpoints))

report = []

report.append("# API Change Report\n")

report.append("## Added Endpoints\n")

if added:
    for item in added:
        report.append(f"- {item}")
else:
    report.append("- None")

report.append("\n## Removed Endpoints\n")

if removed:
    for item in removed:
        report.append(f"- {item}")
else:
    report.append("- None")

report.append("\n## Existing Endpoints\n")

for item in common:
    report.append(f"- {item}")

Path("docs").mkdir(exist_ok=True)

with open(REPORT, "w", encoding="utf-8") as f:
    f.write("\n".join(report))

print("Report generated:", REPORT)
