# Symulacja zespołu deweloperskiego

## Opis projektu
Projekt symuluje pracę zespołu deweloperskiego, którego zadaniem jest realizacja zadań w określonym czasie. Każde zadanie ma różne poziomy trudności i wymaga odpowiednich umiejętności. Zespół składa się z programistów o różnych specjalizacjach, a podczas realizacji projektu mogą wystąpić losowe utrudnienia, takie jak choroby, błędy w kodzie czy awarie systemów.

Celem symulacji jest wygenerowanie raportu, który podsumuje pracę zespołu: ukończone zadania, postęp oraz napotkane problemy.

## Funkcjonalności
- Definicja zadań z określonym poziomem trudności, wymaganymi umiejętnościami i deadline'em.
- Reprezentacja programistów z różnych specjalizacji (frontend, backend, DevOps).
- Losowe zdarzenia, takie jak awarie systemu, absencje programistów lub błędy w kodzie.
- Iteracyjna symulacja pracy zespołu nad zadaniami.
- Generowanie wyników pracy w formie czytelnego raportu.

## Struktura projektu
Projekt składa się z następujących modułów:

### 1. `task.py`
Klasa odpowiedzialna za reprezentację zadania:
- **Atrybuty**: nazwa, poziom trudności, wymagane umiejętności, deadline, postęp i status ukończenia.
- **Metody**: `work_on_task` - symulacja pracy nad zadaniem.

### 2. `developer.py`
Klasa opisująca programistę:
- **Atrybuty**: imię, specjalizacja, efektywność i lista umiejętności.
- **Metody**: `work` - realizacja pracy nad zadaniem, jeśli umiejętności programisty pasują do wymagań zadania.

### 3. `team.py`
Klasa zarządzająca zespołem programistów:
- **Atrybuty**: lista programistów.
- **Metody**: `assign_tasks` - przydział zadań do odpowiednich programistów.

### 4. `events.py`
Moduł reprezentujący losowe zdarzenia:
- **Enumy**: typy zdarzeń (`BUG_FIX`, `ABSENCE`, `SYSTEM_CRASH`).
- **Klasa `Event`**: obsługa i zastosowanie zdarzeń w symulacji.

### 5. `simulation.py`
Główny moduł uruchamiający symulację:
- Tworzy przykładowe zadania i programistów.
- Zarządza przebiegiem symulacji w iteracjach dziennych.
- Generuje losowe zdarzenia i wyświetla postępy.

## Wymagania
- Python 3.9+

## Instalacja i uruchomienie
1. Sklonuj repozytorium:
   ```bash
   git clone <URL-repozytorium>
   ```
2. Przejdź do katalogu projektu:
   ```bash
   cd <nazwa-katalogu>
   ```
3. Uruchom symulację:
   ```bash
   python simulation.py
   ```

## Przykładowy output
```
Day 1
Task(Build API, HARD, Deadline: 10, Completed: False)
Task(Create UI, MEDIUM, Deadline: 8, Completed: False)
Task(Fix Bug, EASY, Deadline: 3, Completed: True)
...
Event triggered: System Crash. Impact: System crash, all work paused.
...
```

## Rozwój projektu
### Propozycje ulepszeń:
- Dodanie bardziej szczegółowych raportów z wynikami pracy zespołu.
- Wprowadzenie bardziej rozbudowanych zdarzeń losowych.
- Import zadań i programistów z plików CSV.
- Obsługa interfejsu graficznego (GUI) dla lepszego śledzenia symulacji.

## Licencja
Projekt jest udostępniony na licencji MIT.

