from dataclasses import dataclass, field
from typing import override

from src.members.base import CompanyMember
from src.members.employee import Employee
from src.models.task import Task
from src.models.project import Project


@dataclass
class Manager(CompanyMember):
    employees: dict[int, Employee] = field(default_factory=dict)

    def manage(self) -> str:
        return f'Managing {len(self.employees)} employees'

    def create_task_for_project(self, project: Project, task: Task) -> None:
        project.tasks[task.task_id] = task

    def review_task(self, task: Task) -> None:
        task.status = 'reviewed'

    def complete_task(self, task: Task) -> None:
        task.status = 'completed'

    def request_changes(self, task: Task) -> None:
        task.status = 'requires changes'

    @override
    def info(self) -> str:
        return f'ID: {self.member_id} | Name: {self.name} | Age: {self.age} | Employees: {len(self.employees)}'
