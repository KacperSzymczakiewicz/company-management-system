# Company Management System

A Python-based company management system demonstrating object-oriented programming, inheritance, multiple inheritance, and code organization into packages.

## Tech Stack

- Python 3.11+
- `dataclasses` — data modeling
- `abc` — abstract base classes
- `typing` — static type hints

## Project Structure

```
company-management-system/
├── src/
│   ├── members/
│   │   ├── base.py        # Abstract CompanyMember class
│   │   ├── employee.py    # Employee class
│   │   ├── engineer.py    # Engineer class
│   │   ├── manager.py     # Manager class
│   │   └── team_lead.py   # TeamLead class (multiple inheritance)
│   ├── models/
│   │   ├── task.py        # Task class with parser
│   │   └── project.py     # Project class
│   ├── utils/
│   │   └── file_loader.py # Loading tasks from file
│   └── company.py         # Main company management class
├── data/
│   └── tasks.txt          # Sample data
├── tests/                 # Unit tests (coming soon)
├── main.py                # Demo
├── pyproject.toml
└── README.md
```

## Features

- Role hierarchy: `CompanyMember` → `Employee` → `Engineer` / `Manager` → `TeamLead`
- `TeamLead` inherits from both `Manager` and `Engineer` (multiple inheritance, MRO)
- Full task workflow: `pending` → `in progress` → `implemented` → `reviewed` → `completed`
- Loading tasks from a `.txt` file via a custom parser (`Task.parse()`)
- Team and project management through the `Company` class

## Getting Started

```bash
git clone https://github.com/KacperSzymczakiewicz/company-management-system
cd company-management-system
python main.py
```

## tasks.txt Format

```
task_id|title|description|status
1|Login|User login form|pending
2|Register|New user registration form|pending
```

## Roadmap

- [x] Exception handling
- [x] JSON data export
- [ ] Unit tests (pytest)
- [ ] REST API (FastAPI)
- [ ] Database (PostgreSQL)