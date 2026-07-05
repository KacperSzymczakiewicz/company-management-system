import pytest

from src.members.manager import Manager
from src.models.project import Project
from src.models.task import Task
from src.members.employee import Employee


@pytest.fixture
def employee() -> Employee:
    return Employee(1, "Kacper", 20)


@pytest.fixture
def task() -> Task:
    return Task(1, "Logowanie", "Formularz logowania użytkownika", "pending")

@pytest.fixture
def project(task: Task) -> Project:
    return Project("System HR", 100000, {})

@pytest.fixture
def manager() -> Manager:
    return Manager(member_id=1, name="Kacper", age=20)