from dataclasses import dataclass, field

from src.models.task import Task


@dataclass
class Project:
    name: str
    budget: int
    tasks: dict[int, Task] = field(default_factory=dict)

    def add_task(self, task: Task) -> None:
        self.tasks[task.task_id] = task

    def info(self) -> str:
        return f'Name: {self.name}\nBudget: {self.budget}\nTasks:\n{self.tasks}'
