from src.models.task import Task
from src.models.project import Project
from src.members.manager import Manager


class TestManager:

    def test_create_task_for_project(self, project: Project, task: Task, manager: Manager) -> None:
        manager.create_task_for_project(project, task)

        assert project.tasks[task.task_id] == task
        assert len(project.tasks) == 1

    def test_change_status_for_task_to_review(self, task: Task, manager: Manager) -> None:
        manager.review_task(task)

        assert task.status == "reviewed"

    def test_change_status_for_task_to_complete(self, task: Task, manager: Manager) -> None:
        manager.complete_task(task)

        assert task.status == "completed"

    def test_change_status_for_task_to_requires_changes(self, task: Task, manager: Manager) -> None:
        manager.request_changes(task)

        assert task.status == "requires changes"
