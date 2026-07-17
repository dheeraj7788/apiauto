import yaml

openapi = yaml.safe_load(open("openapi/openapi.yaml"))

updates = yaml.safe_load(open("ai_output.yaml"))

for path in updates:

    openapi["paths"][path] = updates[path]

with open(
    "openapi/openapi.yaml",
    "w",
    encoding="utf-8"
) as f:

    yaml.dump(
        openapi,
        f,
        sort_keys=False
    )

print("OpenAPI updated.")
