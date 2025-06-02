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
git clone https://github.com/twoj-username/python-jarvis.git
cd python-jarvis
```

### Instalacja zależności
```bash
pip install -r requirements.txt
```

### Uruchomienie
```bash
python main.py
```

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
- **commands/** - definicje komend.
- **speech/** - przetwarzanie mowy.
- **voice/** - synteza mowy.
- **wake_word/** - wykrywanie słowa kluczowego.
- **main.py** - integracja modułów.

## Testowanie
Projekt zawiera testy jednostkowe, które pokrywają kluczowe funkcjonalności, takie jak rozpoznawanie mowy, interpretacja intencji i wykonywanie poleceń.

## Wnioski
Jarvis to solidna podstawa dla asystenta głosowego. Możliwe usprawnienia obejmują:
- Rozszerzenie zestawu komend.
- Personalizację asystenta.
- Integrację z urządzeniami smart home.
- Tryb offline.

Jarvis jest modularny i łatwy w rozbudowie, co czyni go idealnym projektem do dalszego rozwoju.  