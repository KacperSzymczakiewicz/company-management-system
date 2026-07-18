# Company Management System 💼

> Pure Python system for managing employees, teams and projects — no frameworks, just clean OOP.

Built to demonstrate real-world code organization: multiple inheritance, design patterns, production-style logging and unit testing.

---

## What it does

The system simulates a company structure where you can:

- create employees, engineers, managers and team leads
- organize them into teams with assigned projects
- manage tasks through a workflow
- load tasks from a file and export a full company report to JSON

---

## Getting Started ✅

Requires [uv](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/KacperSzymczakiewicz/company-management-system
cd company-management-system
uv sync
uv run python main.py
```

---

## Project Structure 

```
company-management-system/
├── src/
│   ├── members/
│   │   ├── base.py             # Abstract CompanyMember class
│   │   ├── employee.py         # Employee class
│   │   ├── engineer.py         # Engineer class
│   │   ├── manager.py          # Manager class
│   │   └── team_lead.py        # TeamLead (multiple inheritance)
│   ├── models/
│   │   ├── task.py             # Task class with parser
│   │   └── project.py          # Project class
│   ├── utils/
│   │   └── file_handler.py     # File I/O and JSON export
│   └── company.py              # Main management class
├── data/
│   └── tasks.txt               # Sample data (id|title|description|status)
├── tests/
│   ├── conftest.py             # Shared fixtures
│   └── test_*.py               # Unit tests
└── main.py                     # Demo
```

---

## Tech highlights 

- `TeamLead` inherits from both `Manager` and `Engineer` — MRO in action
- every module has its own `getLogger(__name__)` — no root logger abuse
- `Task.parse()` handles file deserialization with validation
- `FileHandler` uses `asdict()` for clean JSON serialization

---

## Running Tests 

```bash
uv run pytest
```

---

## Roadmap 🚀

- [x] OOP with multiple inheritance and MRO
- [x] Exception handling
- [x] JSON export
- [x] Logging
- [x] Unit tests (pytest)
- [ ] REST API (FastAPI)
- [ ] Database (PostgreSQL)

---

## Author

**Kacper Szymczakiewicz** — [GitHub](https://github.com/KacperSzymczakiewicz) · [LinkedIn](https://www.linkedin.com/in/kacper-szymczakiewicz-1a2911417/)