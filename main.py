from wake_word.detector import listen_for_jarvis
from voice.speaker import speak
from speech.recorder import start_background_recording, save_last_audio
from speech.recognizer import transcribe
from brain.assistant import ask_openai


mic_stream = start_background_recording()

def jarvis_callback():
    print("🧠 Jarvis")
    # speak("Jarvis")


    save_last_audio()

    user_text = transcribe()
    print(f"👤 Użytkownik powiedział: {user_text}")
    ai_response = ask_openai(user_text)
    speak(ai_response)
    print(f"🤖 Jarvis odpowiedział: {ai_response}")

if __name__ == "__main__":
    listen_for_jarvis(jarvis_callback)