import requests

BASE_URL = "http://localhost:8000/v1/chat/completions"

API_KEY = "abc123"

MODEL = "Qwen3-4B"


def analyze_policy_changes(
        legacy_text,
        modern_text):

    prompt = f"""
You are an expert compliance and policy analyst.

Compare the following two policies.

POLICY A (LEGACY)
----------------
{legacy_text[:12000]}

POLICY B (MODERNIZED)
----------------
{modern_text[:12000]}

Tasks:

1. Executive Summary

2. Key Changes

3. Semantic Differences

4. Regulatory Impact

5. Compliance Risks

6. Business Impact

7. Recommendations

Return markdown.
"""

    payload = {
        "model": MODEL,
        "messages": [
            {
                "role": "system",
                "content": "You are a policy modernization expert."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.1,
        "max_tokens": 2000
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(
        BASE_URL,
        headers=headers,
        json=payload,
        timeout=300
    )

    response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"]
