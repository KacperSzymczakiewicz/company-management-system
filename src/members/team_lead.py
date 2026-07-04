import logging
from dataclasses import dataclass
from typing import override

from src.members.manager import Manager
from src.members.engineer import Engineer
from src.models.task import Task

logger = logging.getLogger(__name__)


@dataclass
class TeamLead(Manager, Engineer):

    def lead(self) -> str:
        return f'Leading a team of {len(self.employees)} employees'

    def assign_task(self, employee_id: int, task: Task) -> None:
        if employee_id not in self.employees:
            logger.error(f"Employee {employee_id} not found")
            raise ValueError(f'Employee {employee_id} does not exist')
        self.employees[employee_id].add_task(task)
        logger.info(f"TeamLead assigned task {task.task_id} to employee {employee_id}")

    @override
    def review_task(self, task: Task) -> None:
        task.status = 'reviewed'
        logger.info(f"TeamLead {self.name} reviewed task: {task.task_id}")

    @override
    def info(self) -> str:
        return (f'ID: {self.member_id} | Name: {self.name} | Age: {self.age} | '
                f'Specialization: {self.specialization} | Employees: {len(self.employees)} | Tasks: {len(self.tasks)}')
