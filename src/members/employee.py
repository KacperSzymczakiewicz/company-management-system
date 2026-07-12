import logging
from dataclasses import dataclass, field
from typing import override

from src.members.base import CompanyMember
from src.models.task import Task, TaskStatus


logger = logging.getLogger(__name__)

@dataclass
class Employee(CompanyMember):
    tasks: dict[int, Task] = field(default_factory=dict)

    def work(self) -> str:
        return f'Current tasks: {len(self.tasks)}'

    def add_task(self, task: Task) -> None:
        logger.debug(f"Adding task: {task.task_id}")
        self.tasks[task.task_id] = task
        logger.info(f"Task {task.task_id} added to {self.name} ({self.__class__.__name__})")

    def perform_task(self, task_id: int) -> None:
        if task_id not in self.tasks:
            logger.error(f"Task not found: task_id={task_id}")
            raise ValueError(f'Task {task_id} not found')
        self.tasks[task_id].status = TaskStatus.IN_PROGRESS
        logger.info(f"Task {task_id} in progress")

    @override
    def info(self) -> str:
        return f'ID: {self.member_id} | Name: {self.name} | Age: {self.age}\nTasks: {self.tasks}'




