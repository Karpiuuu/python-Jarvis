from wake_word.detector import listen_for_jarvis
from voice.speaker import speak
from speech.recorder import start_background_recording, save_last_audio
from speech.recognizer import transcribe
from brain.assistant import classify_intent
from commands.registry import execute_command


mic_stream = start_background_recording()

def jarvis_callback():
    print("🧠 Jarvis")
    speak("Słucham?")


    save_last_audio()

    user_text = transcribe()
    print(f"👤 Użytkownik powiedział: {user_text}")
    
    intent, data = classify_intent(user_text)
    
    if intent == "COMMAND":
        result = execute_command(data)
        if result:
            speak(result)
        else:
            speak("Nie rozumiem tej komendy.")
    elif intent == "CHAT":
        speak(data)
    else:
        speak("Nie jestem pewien, jak odpowiedzieć.")
    print(f"🗣 Odpowiedź: {data}")

if __name__ == "__main__":
    listen_for_jarvis(jarvis_callback)