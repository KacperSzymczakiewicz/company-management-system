from dataclasses import dataclass, field
from typing import override

from src.members.base import CompanyMember
from src.models.task import Task


@dataclass
class Employee(CompanyMember):
    tasks: dict[int, Task] = field(default_factory=dict)

    def work(self) -> str:
        return f'Current tasks: {len(self.tasks)}'

    def add_task(self, task: Task) -> None:
        self.tasks[task.task_id] = task

    def perform_task(self, task_id: int) -> None:
        self.tasks[task_id].status = 'in progress'

    @override
    def info(self) -> str:
        return f'ID: {self.member_id} | Name: {self.name} | Age: {self.age}\nTasks: {self.tasks}'




