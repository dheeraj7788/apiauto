import os
import yaml

from openai import OpenAI


client = OpenAI(
    base_url="https://models.github.ai/inference",
    api_key=os.environ["GH_MODELS_TOKEN"]
)


changed = yaml.safe_load(open("changed_endpoints.yaml"))

if not changed:
    print("No endpoint changes.")
    exit()


prompt = f"""
Improve the following OpenAPI endpoints.

Generate

- better summary
- description
- parameter descriptions
- request examples
- response examples
- error documentation

Return VALID YAML only.

{yaml.dump(changed)}
"""


response = client.chat.completions.create(

    model="openai/gpt-5",

    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ],

    temperature=0.2
)

content = response.choices[0].message.content

with open("ai_output.yaml", "w", encoding="utf-8") as f:
    f.write(content)

print("AI documentation generated.")
