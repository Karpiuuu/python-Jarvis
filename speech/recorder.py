import numpy as np
import sounddevice as sd
import scipy.io.wavfile as wav
import threading
import time
from collections import deque

SAMPLERATE = 44100
CHANNELS = 1
BUFFER_SECONDS = 5
RECORD_SECONDS = 3

audio_buffer = deque(maxlen=SAMPLERATE * BUFFER_SECONDS)
recording = True

def audio_callback(indata, frames, time_info, status):
    if status:
        print(f"Błąd audio: {status}")
    audio_buffer.extend(indata[:, 0])

def start_background_recording():
    print("🎤 Rolling buffer aktywny (ciągłe nasłuchiwanie mikrofonu)")
    stream = sd.InputStream(
        samplerate=SAMPLERATE,
        channels=CHANNELS,
        dtype='int16',
        callback=audio_callback
    )
    stream.start()
    return stream

def save_last_audio(filename="recording.wav", post_record_seconds=5):
    print("💾 Zapisuję nagranie z rolling buffera...")

    if not audio_buffer:
        print("⚠️ Bufor pusty – brak danych do zapisu.")
        return

    # Skopiuj dane z rolling buffera
    pre_audio = np.array(audio_buffer)[-SAMPLERATE * RECORD_SECONDS:]

    # Dograj jeszcze np. 3 sekundy po wykryciu Jarvisa
    print(f"🎤 Dogrywanie {post_record_seconds} sekund po aktywacji...")
    post_audio = sd.rec(int(SAMPLERATE * post_record_seconds), samplerate=SAMPLERATE, channels=1, dtype='int16')
    sd.wait()

    # Połącz pre + post
    full_audio = np.concatenate((pre_audio, post_audio.reshape(-1)))

    # Zapisz do pliku
    wav.write(filename, SAMPLERATE, full_audio)
    print(f"✅ Zapisano: {filename} (📊 długość: {len(full_audio) / SAMPLERATE:.2f} s)")

    # Opcjonalne opóźnione czyszczenie
    threading.Thread(target=lambda: (time.sleep(2), audio_buffer.clear()), daemon=True).start()
