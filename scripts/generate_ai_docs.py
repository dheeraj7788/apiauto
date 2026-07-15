import os
from pathlib import Path
from openai import OpenAI

# Read OpenAPI specification
openapi = Path("openapi/openapi.yaml").read_text(encoding="utf-8")

# Connect to GitHub Models
client = OpenAI(
    base_url="https://models.github.ai/inference",
    api_key=os.environ["GH_MODELS_TOKEN"]
)

# Prompt
prompt = f"""
You are a Senior API Technical Writer.

Review the following OpenAPI specification.

Check for:
1. Missing summaries
2. Missing descriptions
3. Missing parameter descriptions
4. Missing request examples
5. Missing response examples
6. Missing error responses

Return the review in Markdown.

{openapi}
"""

# Call GitHub Models
response = client.chat.completions.create(
    model="openai/gpt-4.1-mini",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

# Save AI review
Path("docs").mkdir(exist_ok=True)
Path("docs/AI_REVIEW.md").write_text(
    response.choices[0].message.content,
    encoding="utf-8"
)

print("AI review generated successfully.")
