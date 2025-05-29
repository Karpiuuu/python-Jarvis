import os
from dotenv import load_dotenv
from openai import OpenAI

from commands.registry import get_commands_json

load_dotenv()
client = OpenAI(api_key=os.getenv("DEEPSEEK_API_KEY"), base_url="https://api.deepseek.com")

def classify_intent(text: str) -> tuple[str, str]:
    try:
        system_message = (
            "Jesteś głosowym asystentem Jarvis. "
            "Twoim zadaniem jest rozpoznanie, czy użytkownik chce wykonać jedną z dostępnych komend, czy prowadzi zwykłą rozmowę.\n\n"
            "Jeśli wypowiedź użytkownika pasuje do jakiejkolwiek z dostępnych komend, "
            "odpowiedz tylko w formacie: `COMMAND: <nazwa_komendy> [argumenty opcjonalne]`\n"
            "Jeśli użytkownik zadaje pytanie niezwiązane z komendami – odpowiadaj normalnie, ale poprzedź odpowiedź `CHAT:`.\n\n"
            "Lista dostępnych komend (name + description):\n"
            f"{get_commands_json()}\n\n"
            "Pamiętaj – zawsze zaczynaj odpowiedź od `COMMAND:` lub `CHAT:`.\n"
        )

        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": text},
            ],
        )
        content = response.choices[0].message.content.strip()
        if content.startswith("COMMAND:"):
            return "COMMAND", content.replace("COMMAND:", "").strip()
        elif content.startswith("CHAT:"):
            return "CHAT", content.replace("CHAT:", "").strip()
        else:
            return "UNKNOWN", content
    except Exception as e:
        print(f"❌ Błąd klasyfikacji intencji: {e}")
        return "ERROR", "Wystąpił problem."