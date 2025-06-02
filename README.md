# Jarvis - Inteligentny Asystent Głosowy

## Opis projektu

### Temat projektu
Jarvis to inteligentny asystent głosowy inspirowany AI z filmów o Iron Manie. Wykorzystuje technologie rozpoznawania mowy, przetwarzania języka naturalnego i syntezy głosu, aby reagować na polecenia głosowe.

### Cel projektu i oczekiwane rezultaty
Celem jest stworzenie asystenta, który:
- Reaguje na słowo kluczowe "Jarvis".
- Rozpoznaje mowę i interpretuje intencje użytkownika.
- Wykonuje polecenia i odpowiada głosowo.
- Jest łatwo rozszerzalny o nowe funkcje.

### Funkcjonalności
1. Wykrywanie słowa kluczowego.
2. Nagrywanie i przetwarzanie dźwięku.
3. Rozpoznawanie mowy.
4. Interpretacja intencji.
5. Wykonywanie poleceń.
6. Synteza mowy.

## Instrukcja uruchomienia

### Klonowanie repozytorium
```bash
git clone https://github.com/Karpiuuu/python-Jarvis/
cd python-jarvis
```

### Wymagania systemowe
Przed instalacją upewnij się, że masz:
- Python 3.8 lub nowszy
- W przypadku systemów Linux/Mac: portaudio zainstalowane

#### Instalacja PortAudio (dla PyAudio):
- **Windows**: PyAudio powinien zainstalować się bez dodatkowych kroków
- **MacOS**: `brew install portaudio`
- **Linux (Ubuntu/Debian)**: `sudo apt-get install python3-pyaudio portaudio19-dev`

### Instalacja zależności
```bash
pip install -r requirements.txt

```
### Gdyby zależności się nie doinstalowały
```bash
pip install openai pyttsx3 pyaudio sounddevice scipy
pip install git+https://github.com/openai/whisper.git
pip install pvporcupine numpy

pip install PyAudio‑0.2.11‑cp311‑cp311‑win_amd64.whl
```

### Link do doinstalowania biblioteki odpowiedzialnej za TTS
```bash
https://ffmpeg.org/download.html
```

### Konfiguracja API
1. Utwórz plik `.env` w głównym katalogu projektu
2. Dodaj swoje klucze API:
   ```
   DEEPSEEK_API_KEY=twój_klucz_deepseek
   ```
3. W pliku `wake_word/detector.py` zastąp istniejący klucz dostępu do Porcupine swoim własnym, dostępnym na stronie [Picovoice Console](https://console.picovoice.ai/)

### Uruchomienie
```bash
python main.py
```

### Rozwiązywanie problemów
- Jeśli wystąpią problemy z instalacją PyAudio, wypróbuj pakiety prebuilt:
  - Windows: `pip install pipwin && pipwin install pyaudio`
  - Lub użyj wheel dostępnego na stronie [Unofficial Windows Binaries for Python](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)

### Użycie
1. Powiedz "Jarvis", aby aktywować asystenta.
2. Po sygnale dźwiękowym wydaj polecenie lub zadaj pytanie.
3. Asystent odpowie głosowo.

## Technologie użyte w projekcie
- **Python** - główny język programowania.
- **Porcupine** - wykrywanie słów kluczowych.
- **PyAudio** - obsługa audio.
- **Whisper** - rozpoznawanie mowy.
- **OpenAI API** - interpretacja intencji.
- **pyttsx3** - synteza mowy.
- **NumPy** - przetwarzanie danych audio.

## Analiza wymagań

### Wymagania funkcjonalne
- Wykrywanie słowa kluczowego "Jarvis".
- Rozpoznawanie mowy i interpretacja intencji.
- Wykonywanie poleceń i odpowiedzi głosowe.

### Wymagania niefunkcjonalne
- Działanie w czasie rzeczywistym.
- Łatwa rozbudowa i modularność.

## Organizacja kodu
- **brain/** - interpretacja intencji.
- **commands/** - definicje komend, w tym struktura danych `Command`.
- **speech/** - przetwarzanie mowy.
- **voice/** - synteza mowy.
- **wake_word/** - wykrywanie słowa kluczowego.
- **main.py** - integracja modułów.

## Testowanie
Projekt zawiera testy jednostkowe, które pokrywają kluczowe funkcjonalności, takie jak rozpoznawanie mowy, interpretacja intencji i wykonywanie poleceń.

## Wnioski
Jarvis to solidna podstawa dla asystenta głosowego. Możliwe usprawnienia obejmują:
- Rozszerzenie zestawu komend z wykorzystaniem klasy `Command`.
- Personalizację asystenta.
- Integrację z urządzeniami smart home.
- Tryb offline.

Jarvis jest modularny i łatwy w rozbudowie, co czyni go idealnym projektem do dalszego rozwoju.