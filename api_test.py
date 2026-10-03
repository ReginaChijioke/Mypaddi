import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY")
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "what is the capital of nigeria"
        }
    ],
    model="openai/gpt-oss-120b",
)
print(chat_completion.choices[0].message.content)