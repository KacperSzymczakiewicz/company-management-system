import pytest

from src.members.engineer import Engineer
from src.members.team_lead import TeamLead
from src.members.manager import Manager
from src.models.project import Project
from src.models.task import Task
from src.members.employee import Employee


@pytest.fixture
def employee() -> Employee:
    return Employee(member_id=1, name="Kacper", age=20)


@pytest.fixture
def task() -> Task:
    return Task(task_id=1, title="Logowanie", description="Formularz logowania użytkownika", status="pending")


@pytest.fixture
def project(task: Task) -> Project:
    return Project(name="System HR", budget=100000, tasks={})


@pytest.fixture
def manager(employee: Employee) -> Manager:
    return Manager(member_id=1, name="Kacper", age=20, employees={1: employee})

@pytest.fixture
def engineer(task: Task) -> Engineer:
    return Engineer(member_id=1, name="Kacper", age=20, tasks={1: task}, specialization="backend")

@pytest.fixture
def team_lead(task: Task, employee: Employee) -> TeamLead:
    return TeamLead(
        member_id=3,
        name="Piotr",
        age=35,
        specialization="fullstack",
        tasks={1: task},
        employees={1: employee},
    )