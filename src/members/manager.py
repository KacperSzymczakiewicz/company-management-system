import logging
from dataclasses import dataclass, field
from typing import override

from src.members.base import CompanyMember
from src.members.employee import Employee
from src.models.task import Task
from src.models.project import Project

logger = logging.getLogger(__name__)


@dataclass
class Manager(CompanyMember):
    employees: dict[int, Employee] = field(default_factory=dict)

    def manage(self) -> str:
        return f'Managing {len(self.employees)} employees'

    def create_task_for_project(self, project: Project, task: Task) -> None:
        project.tasks[task.task_id] = task
        logger.info(f"Manager created task: {task.task_id}")

    def review_task(self, task: Task) -> None:
        task.status = 'reviewed'
        logger.info(f"Manager reviewed task: {task.task_id}")

    def complete_task(self, task: Task) -> None:
        task.status = 'completed'
        logger.info(f"Manager closed task: {task.task_id}")

    def request_changes(self, task: Task) -> None:
        task.status = 'requires changes'
        logger.info(f"Manager requested changes for task: {task.task_id}")

    @override
    def info(self) -> str:
        return f'ID: {self.member_id} | Name: {self.name} | Age: {self.age} | Employees: {len(self.employees)}'
