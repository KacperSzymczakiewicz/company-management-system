import logging
from dataclasses import dataclass
from typing import override

from src.members.employee import Employee

logger = logging.getLogger(__name__)


@dataclass
class Engineer(Employee):
    specialization: str = ""

    def develop(self) -> str:
        return f'Developing with specialization: {self.specialization}'

    def implement_task(self, task_id: int) -> None:
        if task_id not in self.tasks:
            logger.error(f"Task not found: task_id={task_id}")
            raise ValueError(f'Task {task_id} not found')
        self.tasks[task_id].status = 'implemented'
        logger.info(f"Task {task_id} implemented")

    @override
    def info(self) -> str:
        return (f'ID: {self.member_id} | Name: {self.name} | Age: {self.age} '
                f'| Specialization: {self.specialization}\nTasks: {self.tasks}')
