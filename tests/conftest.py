import pytest

from src.models.task import Task
from src.members.employee import Employee


@pytest.fixture
def employee() -> Employee:
    return Employee(1, "Kacper", 20)


@pytest.fixture
def task() -> Task:
    return Task(1, "Logowanie", "Formularz logowania użytkownika", "pending")
