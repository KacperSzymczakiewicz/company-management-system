# Company Management System

System zarządzania pracownikami i projektami firmowymi napisany w Pythonie. Projekt demonstruje znajomość programowania obiektowego, dziedziczenia, wielodziedziczenia oraz organizacji kodu w pakiety.

## Tech stack

- Python 3.11+
- `dataclasses` — modelowanie danych
- `abc` — klasy abstrakcyjne
- `typing` — typowanie statyczne

## Struktura projektu

```
company-management-system/
├── src/
│   ├── members/
│   │   ├── base.py        # Abstrakcyjna klasa CompanyMember
│   │   ├── employee.py    # Klasa Employee
│   │   ├── engineer.py    # Klasa Engineer
│   │   ├── manager.py     # Klasa Manager
│   │   └── team_lead.py   # Klasa TeamLead (wielodziedziczenie)
│   ├── models/
│   │   ├── task.py        # Klasa Task z parserem
│   │   └── project.py     # Klasa Project
│   ├── utils/
│   │   └── file_loader.py # Wczytywanie zadań z pliku
│   └── company.py         # Główna klasa zarządzająca firmą
├── data/
│   └── tasks.txt          # Przykładowe dane
├── tests/                 # Testy jednostkowe (w przygotowaniu)
├── main.py                # Demo działania systemu
├── pyproject.toml
└── README.md
```

## Funkcjonalności

- Hierarchia ról: `CompanyMember` → `Employee` → `Engineer` / `Manager` → `TeamLead`
- `TeamLead` dziedziczy jednocześnie po `Manager` i `Engineer` (wielodziedziczenie, MRO)
- Pełny workflow zadań: `pending` → `in progress` → `implemented` → `reviewed` → `completed`
- Wczytywanie zadań z pliku `.txt` przez własny parser (`Task.parse()`)
- Zarządzanie zespołami i projektami przez klasę `Company`

## Uruchomienie

```bash
git clone https://github.com/TWOJ_LOGIN/company-management-system.git
cd company-management-system
python main.py
```

## Format pliku tasks.txt

```
task_id|title|description|status
1|Logowanie|Formularz logowania użytkownika|pending
2|Rejestracja|Formularz rejestracji nowego użytkownika|pending
```

## Roadmap

- [ ] Obsługa wyjątków
- [ ] Eksport danych do JSON / ZIP
- [ ] Testy jednostkowe (pytest)
- [ ] REST API (FastAPI)
- [ ] Baza danych (PostgreSQL)