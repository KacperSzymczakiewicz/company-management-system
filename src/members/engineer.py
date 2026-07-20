import logging
from dataclasses import dataclass
from typing import override

from src.models.task import TaskStatus
from src.members.employee import Employee

logger = logging.getLogger(__name__)


@dataclass
class Engineer(Employee):
    """Represents an engineer in the company.

    Attributes:
        specialization: Technical specialization of the engineer.
    """

    specialization: str = ""

    def develop(self) -> str:
        """Return a string describing the engineer's current development work."""
        return f'Developing with specialization: {self.specialization}'

    def implement_task(self, task_id: int) -> None:
        """Set task status to IMPLEMENTED.

        Args:
            task_id: ID of the task to implement.

        Raises:
            ValueError: If task with given ID does not exist.
        """
        if task_id not in self.tasks:
            logger.error(f"Task not found: task_id={task_id}")
            raise ValueError(f'Task {task_id} not found')
        self.tasks[task_id].status = TaskStatus.IMPLEMENTED
        logger.info(f"Task {task_id} implemented")

    @override
    def info(self) -> str:
        """Return a formatted string with engineer information and specialization."""
        return (f'ID: {self.member_id} | Name: {self.name} | Age: {self.age} '
                f'| Specialization: {self.specialization}\nTasks: {self.tasks}')