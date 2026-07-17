import subprocess

subprocess.run([

    "npx",
    "redoc-cli",
    "build",
    "openapi/openapi.yaml",
    "-o",
    "docs/index.html"

], check=True)

print("HTML documentation generated.")
