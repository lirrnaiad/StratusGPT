import re
import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def prompt_ai(prompt: str) -> str:
    """Asks for a response from the AI given the prompt"""
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("AI_KEY"),
    )

    completion = client.chat.completions.create(
        model="cognitivecomputations/dolphin3.0-r1-mistral-24b:free",
        messages=[
            {
                "role": "user",
                "content": f"Reply in 100 words or less using the following prompt: \n\n{prompt}"
            }
        ]
    )

    response = completion.choices[0].message.content
    return remove_thought_process(response)


def remove_thought_process(response: str) -> str:
    pattern = r"<think>.*?<\/think>\s*"
    cleaned_response = re.sub(pattern, "", response, flags=re.DOTALL)

    return cleaned_response

