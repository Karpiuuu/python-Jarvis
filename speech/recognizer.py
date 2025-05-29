import whisper

model = whisper.load_model("base")  # możesz zmienić na "small" lub "medium"

def transcribe(filename="recording.wav"):
    print("🧠 Transkrypcja nagrania...")
    result = model.transcribe(filename, language="pl")
    print("📜 Rozpoznany tekst:", result["text"])
    return result["text"]
