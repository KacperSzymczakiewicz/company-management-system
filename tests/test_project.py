from src.models.project import Project
from src.models.task import Task

class TestProject:

    def test_add_task(self):
        task = Task(1, "Logowanie", "Formularz logowania użytkownika", "pending")
        project = Project("Projekt", 1000)
        project.add_task(task)
        assert len(project.tasks) == 1
        assert project.tasks[1] == task
