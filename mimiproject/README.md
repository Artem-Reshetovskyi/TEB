# Symulacja zespołu deweloperskiego

Projekt to symulacja pracy zespołu deweloperskiego, w którym symulowane są zadania, zdarzenia losowe oraz postępy w realizacji projektów. Zespół deweloperski wykonuje dwa rodzaje projektów:
- **Tworzenie oprogramowania** (np. API, UI, poprawki błędów),
- **Tworzenie gry komputerowej** (np. projektowanie poziomów, implementacja fizyki, modelowanie 3D).

## Funkcjonalności

- Definiowanie zadań o różnej trudności i wymaganiach kompetencyjnych.
- Tworzenie zespołów z deweloperami posiadającymi różne role i umiejętności.
- Automatyczne przypisywanie zadań do deweloperów na podstawie ich kompetencji.
- Obsługa zdarzeń losowych, takich jak awarie systemu, absencje czy konieczność naprawy błędów.
- Symulacja postępu zadań w zależności od wydajności deweloperów.

## Technologie

Projekt został zrealizowany w języku Python z wykorzystaniem:
- Programowania obiektowego (klasy, dziedziczenie).
- Enumów do reprezentacji różnych typów trudności, ról i zdarzeń losowych.
- Podziału kodu na moduły zgodnie z zasadami SOLID.

## Pliki projektu

- `task.py` - Definicja zadań oraz ich trudności.
- `developer.py` - Implementacja deweloperów oraz ich ról i umiejętności.
- `team.py` - Zarządzanie zespołem deweloperskim i przypisywanie zadań.
- `events.py` - Obsługa zdarzeń losowych wpływających na postęp pracy.
- `simulation.py` - Główna symulacja dla projektów oprogramowania i gier.

## Uruchomienie

1. Sklonuj repozytorium:
   ```bash
   git clone <URL-REPOZYTORIUM>
   ```
2. Przejdź do folderu projektu:
   ```bash
   cd <NAZWA-FOLDERU>
   ```
3. Uruchom symulację:
   ```bash
   python simulation.py
   ```

## Przykładowe dane

### Zadania do realizacji
- **Tworzenie oprogramowania**: Budowa API, tworzenie UI, poprawki błędów.
- **Tworzenie gry**: Projektowanie poziomów, implementacja fizyki, tworzenie modeli 3D.

### Deweloperzy
- Alice: Backend Developer z umiejętnościami Python, Django, REST.
- Bob: Frontend Developer z umiejętnościami HTML, CSS, JavaScript.
- Eve: Game Developer specjalizujący się w Unity i C++.

## Rozwój projektu

Rozwój kodu był prowadzony zgodnie z dobrymi praktykami:
- Regularne commity opisujące wprowadzone zmiany.
- Testowanie poprawności działania symulacji po dodaniu nowych funkcjonalności.

## Autor
Projekt został stworzony w celach edukacyjnych w celu praktycznego wykorzystania zasad SOLID i programowania obiektowego w Pythonie.

