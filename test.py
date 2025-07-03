import openai
from openai import OpenAI
from openai.types.chat import ChatCompletion

client = OpenAI(api_key="")  # API key removed

try:
    response: ChatCompletion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Say hello"}]
    )
    print("✅ API key is working!")
    print("Response:", response.choices[0].message.content)

except openai.AuthenticationError:
    print("❌ Invalid API key.")
except Exception as e:
    print("⚠️ Something went wrong:", str(e))
