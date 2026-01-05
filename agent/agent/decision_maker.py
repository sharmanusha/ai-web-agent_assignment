from openai import OpenAI
import json
import os
import re

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

MODEL_NAME = "openai/gpt-oss-20b"

def extract_json(text):
    """
    Extract first JSON object from model output safely
    """
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        return None
    try:
        return json.loads(match.group())
    except json.JSONDecodeError:
        return None


def decide_action(observation):
    prompt = f"""
You are a semi-autonomous AI web agent.

Page title: {observation['title']}
Buttons visible: {observation['button_count']}
Links visible: {observation['link_count']}

Choose ONE next action.

Allowed actions:
- search product
- click navigation link
- stop

STRICT RULES:
- Respond with ONLY a JSON object
- No explanation
- No markdown
- No text outside JSON

JSON FORMAT:
{{
  "action": "<one action>",
  "reason": "<short reason>"
}}
"""

