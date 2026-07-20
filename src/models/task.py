import logging
from dataclasses import dataclass
from typing import Self
from enum import StrEnum

logger = logging.getLogger(__name__)


class TaskStatus(StrEnum):
    """Enumeration of possible task statuses."""

    PENDING = "pending"
    IN_PROGRESS = "in progress"
    IMPLEMENTED = "implemented"
    REVIEWED = "reviewed"
    COMPLETED = "completed"
    REQUIRES_CHANGES = "requires changes"


@dataclass
class Task:
    """Represents a task in the company management system.

    Attributes:
        task_id: Unique identifier of the task.
        title: Short title of the task.
        description: Detailed description of the task.
        status: Current status of the task.
    """

    task_id: int
    title: str
    description: str
    status: TaskStatus

    def info(self) -> str:
        """Return a formatted string with task information."""
        return f"{self.task_id} | {self.title} | {self.description} | {self.status}"

    @classmethod
    def parse(cls, task_str: str) -> Self:
        """Parse a pipe-separated string into a Task instance.

        Args:
            task_str: String in format 'task_id|title|description|status'.

        Returns:
            Task instance created from the parsed string.

        Raises:
            ValueError: If the string format is invalid, status is unrecognized,
                or task_id is not a valid integer.
        """
        logger.debug(f"Parsing: {task_str}")
        parts = task_str.strip().split("|")

        if len(parts) != 4:
            logger.error(f"Invalid task: {task_str}")
            raise ValueError("Invalid task string!")

        task_id_str, title, description, task_status = parts

        try:
            task_status = TaskStatus(task_status)
        except ValueError:
            logger.error(f"Invalid task status: {task_status}")
            raise ValueError("Invalid task status!")

        try:
            task_id = int(task_id_str)
        except ValueError:
            logger.error(f"Invalid task id: {task_id_str}")
            raise ValueError("Invalid task id!")

        return cls(task_id, title, description, task_status)