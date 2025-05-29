import pvporcupine
import pyaudio
import struct

def listen_for_jarvis(callback):
    porcupine = pvporcupine.create(
    access_key="hsjUsqX+B3kPnVJNSYgPSMb6N5OTCT9vJVkQ3OaJZS8YK5hTYwPJrQ==",
    keywords=["jarvis"]
)
    pa = pyaudio.PyAudio()

    stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length,
    )

    print("🎙 Nasłuchiwanie na słowo 'Jarvis'...")

    try:
        while True:
            pcm = stream.read(porcupine.frame_length, exception_on_overflow=False)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

            result = porcupine.process(pcm)
            if result >= 0:
                callback()  # po wykryciu wywołujemy funkcję

    except KeyboardInterrupt:
        print("🛑 Zatrzymano nasłuchiwanie.")

    finally:
        stream.stop_stream()
        stream.close()
        pa.terminate()
        porcupine.delete()
