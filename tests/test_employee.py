import pytest

from src.members.employee import Employee
from src.models.task import Task


class TestEmployee:

    def test_add_task_to_tasks(self, employee: Employee, task: Task) -> None:
        employee.add_task(task)

        assert len(employee.tasks) == 1
        assert employee.tasks[1] == task

    def test_perform_task_with_invalid_id_raises_value_error(self, employee: Employee, task: Task) -> None:
        with pytest.raises(ValueError):
            employee.perform_task(2)

    def test_perform_task_with_valid_id(self, employee: Employee, task: Task) -> None:
        employee.add_task(task)
        employee.perform_task(1)

        assert employee.tasks[1].status == "in progress"
