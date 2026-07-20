import logging
from dataclasses import dataclass, field

from src.models.task import Task

logger = logging.getLogger(__name__)


@dataclass
class Project:
    """Represents a project in the company.

    Attributes:
        name: Name of the project.
        budget: Budget allocated for the project.
        tasks: Dictionary of tasks in the project, keyed by task ID.
    """

    name: str
    budget: int
    tasks: dict[int, Task] = field(default_factory=dict)

    def add_task(self, task: Task) -> None:
        """Add a task to the project.

        Args:
            task: Task instance to be added.
        """
        self.tasks[task.task_id] = task
        logger.info(f"Added task {task.task_id}: {task.title}")

    def info(self) -> str:
        """Return a formatted string with project information and tasks."""
        return f'Name: {self.name}\nBudget: {self.budget}\nTasks:\n{self.tasks}'