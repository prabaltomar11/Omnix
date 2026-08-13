from ai.prompts import behaviour
from ai.user_profile import get_profile
import ollama

def ask_ai(user_input):
    purpose, domain, preference = get_profile()

    prompt = f"""{behaviour}
Purpose: {purpose}
Domain: {domain}
Preference: {preference}

Instructions: Follow the user's response preference when answering.
Use the user's purpose and domains as context.

User: {user_input}"""

    response = ollama.chat(
        model="qwen2.5:3b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    answer = response["message"]["content"]

    return answer


