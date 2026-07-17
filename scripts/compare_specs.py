import subprocess
import yaml
from pathlib import Path


SPEC_FILE = "openapi/openapi.yaml"


def load_yaml_from_git(revision):
    result = subprocess.run(
        [
            "git",
            "show",
            f"{revision}:{SPEC_FILE}"
        ],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        return None

    return yaml.safe_load(result.stdout)


def extract_paths(spec):
    if spec is None:
        return {}

    return spec.get("paths", {})


current = yaml.safe_load(open(SPEC_FILE))

previous = load_yaml_from_git("HEAD~1")

old_paths = extract_paths(previous)
new_paths = extract_paths(current)

changed = {}

for path, methods in new_paths.items():

    if path not in old_paths:
        changed[path] = methods

    elif methods != old_paths[path]:
        changed[path] = methods


yaml.dump(
    changed,
    open("changed_endpoints.yaml", "w"),
    sort_keys=False
)

print("Changed endpoints:", len(changed))
