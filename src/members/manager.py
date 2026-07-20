import logging
from dataclasses import dataclass, field
from typing import override

from src.members.base import CompanyMember
from src.members.employee import Employee
from src.models.task import Task, TaskStatus
from src.models.project import Project

logger = logging.getLogger(__name__)


@dataclass
class Manager(CompanyMember):
    """Represents a manager in the company.

    Attributes:
        employees: Dictionary of employees managed by this manager, keyed by member ID.
    """

    employees: dict[int, Employee] = field(default_factory=dict)

    def manage(self) -> str:
        """Return a string describing the number of managed employees."""
        return f'Managing {len(self.employees)} employees'

    def create_task_for_project(self, project: Project, task: Task) -> None:
        """Add a task to the given project.

        Args:
            project: Project to which the task will be added.
            task: Task instance to be added.
        """
        project.tasks[task.task_id] = task
        logger.info(f"Manager created task: {task.task_id}")

    def review_task(self, task: Task) -> None:
        """Set task status to REVIEWED.

        Args:
            task: Task instance to be reviewed.
        """
        task.status = TaskStatus.REVIEWED
        logger.info(f"Manager reviewed task: {task.task_id}")

    def complete_task(self, task: Task) -> None:
        """Set task status to COMPLETED.

        Args:
            task: Task instance to be completed.
        """
        task.status = TaskStatus.COMPLETED
        logger.info(f"Manager closed task: {task.task_id}")

    def request_changes(self, task: Task) -> None:
        """Set task status to REQUIRES_CHANGES.

        Args:
            task: Task instance that requires changes.
        """
        task.status = TaskStatus.REQUIRES_CHANGES
        logger.info(f"Manager requested changes for task: {task.task_id}")

    @override
    def info(self) -> str:
        """Return a formatted string with manager information and employee count."""
        return f'ID: {self.member_id} | Name: {self.name} | Age: {self.age} | Employees: {len(self.employees)}'