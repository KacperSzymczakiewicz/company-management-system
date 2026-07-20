import logging
from dataclasses import dataclass
from typing import override

from src.members.manager import Manager
from src.members.engineer import Engineer
from src.models.task import Task, TaskStatus

logger = logging.getLogger(__name__)


@dataclass
class TeamLead(Manager, Engineer):
    """Represents a team lead in the company.

    Inherits from both Manager and Engineer, combining managerial and technical responsibilities.
    """

    def lead(self) -> str:
        """Return a string describing the size of the led team."""
        return f'Leading a team of {len(self.employees)} employees'

    def assign_task(self, employee_id: int, task: Task) -> None:
        """Assign a task to a specific employee.

        Args:
            employee_id: ID of the employee to assign the task to.
            task: Task instance to be assigned.

        Raises:
            ValueError: If employee with given ID does not exist.
        """
        if employee_id not in self.employees:
            logger.error(f"Employee {employee_id} not found")
            raise ValueError(f'Employee {employee_id} does not exist')
        self.employees[employee_id].add_task(task)
        logger.info(f"TeamLead assigned task {task.task_id} to employee {employee_id}")

    @override
    def review_task(self, task: Task) -> None:
        """Set task status to REVIEWED.

        Args:
            task: Task instance to be reviewed.
        """
        task.status = TaskStatus.REVIEWED
        logger.info(f"TeamLead {self.name} reviewed task: {task.task_id}")

    @override
    def info(self) -> str:
        """Return a formatted string with team lead information."""
        return (f'ID: {self.member_id} | Name: {self.name} | Age: {self.age} | '
                f'Specialization: {self.specialization} | Employees: {len(self.employees)} | Tasks: {len(self.tasks)}')