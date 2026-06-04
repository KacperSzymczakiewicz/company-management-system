from dataclasses import dataclass
from typing import override

from src.members.employee import Employee

@dataclass
class Engineer(Employee):
    specialization: str = ""

    def develop(self) -> str:
        return f'Developing with specialization: {self.specialization}'

    def implement_task(self, task_id: int) -> None:
        self.tasks[task_id].status = 'implemented'

    @override
    def info(self) -> str:
        return f'ID: {self.member_id} | Name: {self.name} | Age: {self.age} | Specialization: {self.specialization}\nTasks: {self.tasks}'