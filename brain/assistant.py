import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("DEEPSEEK_API_KEY"), base_url="https://api.deepseek.com")

def classify_intent(text: str) -> tuple[str, str]:
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content":
                    (
                        "Twoim zadaniem jest klasyfikacja wypowiedzi użytkownika. "
                        "Jeśli wypowiedź to polecenie (np. 'otwórz YouTube', 'pokaż pogodę w Kłodzku'), "
                        "zwróć tylko w formacie: COMMAND: <nazwa_komendy> [argumenty]\n"
                        "Przykład: COMMAND: open_weather klodzko\n"
                        "Jeśli to zwykłe pytanie lub rozmowa, zwróć w formacie: CHAT: <odpowiedź>\n"
                        "Nie używaj języka naturalnego w odpowiedziach dla komend – tylko nazwy komend!"
                    )
                },
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