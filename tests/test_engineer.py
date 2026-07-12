import pytest

from src.members.engineer import Engineer
from src.models.task import Task, TaskStatus


class TestEngineer:

    def test_invalid_task_id_raises_value_error(self) -> None:
        with pytest.raises(ValueError):
            engineer = Engineer(1, "Kacper", 20, specialization="backend")
            engineer.implement_task(2)

    def test_valid_task_change_status_implement_correctly(self, task: Task) -> None:
        engineer = Engineer(1, "Kacper", 20, {1: task}, specialization="backend")
        engineer.implement_task(1)
        assert engineer.tasks[1].status == TaskStatus.IMPLEMENTED
