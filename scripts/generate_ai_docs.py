import os
from openai import OpenAI

client = OpenAI(
    base_url="https://models.github.ai/inference",
    api_key=os.environ["GH_MODELS_TOKEN"],
)

with open("openapi/openapi.yaml", "r", encoding="utf-8") as f:
    spec = f.read()

prompt = f"""
You are an expert API Technical Writer.

Improve this OpenAPI specification.

Tasks:
1. Improve endpoint summaries.
2. Improve descriptions.
3. Generate parameter descriptions.
4. Improve request body descriptions.
5. Improve response descriptions.
6. Improve error documentation.
7. Suggest missing documentation.
8. Preserve valid OpenAPI syntax.

Return ONLY the updated YAML.

{spec}
"""

response = client.chat.completions.create(
    model="openai/gpt-5",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.2,
)

improved_spec = response.choices[0].message.content

with open("openapi/openapi.yaml", "w", encoding="utf-8") as f:
    f.write(improved_spec)

print("OpenAPI documentation improved successfully.")
