from dataclasses import dataclass
from typing import override

from src.members.manager import Manager
from src.members.engineer import Engineer
from src.models.task import Task


@dataclass
class TeamLead(Manager, Engineer):

    def lead(self) -> str:
        return f'Leading a team of {len(self.employees)} employees'

    def assign_task(self, employee_id: int, task: Task) -> None:
        self.employees[employee_id].add_task(task)

    @override
    def review_task(self, task_id: int) -> None:
        self.tasks[task_id].status = 'reviewed'
        print(f'TeamLead reviewed task: {self.tasks[task_id].title}')

    @override
    def info(self) -> str:
        return (f'ID: {self.member_id} | Name: {self.name} | Age: {self.age} | '
                f'Specialization: {self.specialization} | Employees: {len(self.employees)} | Tasks: {len(self.tasks)}')
