import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("DEEPSEEK_API_KEY"), base_url="https://api.deepseek.com")



def ask_openai(prompt: str) -> str:
    try:
        print("🧠 Wysyłam zapytanie do OpenAI...")
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "Jesteś Jarvis, odpowiadaj na pytania"},
                {"role": "user", "content": prompt},
            ],
        )
        answer = response.choices[0].message.content
        return answer.strip()
    except Exception as e:
        print(f"❌ Błąd podczas komunikacji z OpenAI: {e}")
        return "Przepraszam, wystąpił błąd podczas przetwarzania twojego zapytania."