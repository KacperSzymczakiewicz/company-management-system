import logging
from dataclasses import dataclass, field
from typing import override

from src.members.base import CompanyMember
from src.models.task import Task

logger = logging.getLogger(__name__)

@dataclass
class Employee(CompanyMember):
    tasks: dict[int, Task] = field(default_factory=dict)

    def work(self) -> str:
        return f'Current tasks: {len(self.tasks)}'

    def add_task(self, task: Task) -> None:
        logger.debug(f"Adding task: {task.task_id}")
        self.tasks[task.task_id] = task
        logger.info(f"Task {task.task_id} added")

    def perform_task(self, task_id: int) -> None:
        logger.debug(f"Checking existing task: task_id={task_id}")
        if task_id not in self.tasks:
            logger.error(f"Task not found: task_id={task_id}")
            raise ValueError(f'Task {task_id} not found')
        logger.debug(f"Task task_id={task_id} found")
        self.tasks[task_id].status = 'in progress'
        logger.info(f"Task {task_id} in progress")

    @override
    def info(self) -> str:
        return f'ID: {self.member_id} | Name: {self.name} | Age: {self.age}\nTasks: {self.tasks}'




