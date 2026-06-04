from dataclasses import dataclass
from typing import Self

@dataclass
class Task:
    task_id: int
    title: str
    description: str
    status: str

    def info(self) -> str:
        return f"{self.task_id} | {self.title} | {self.description} | {self.status}"

    @classmethod
    def parse(cls, task_str: str) -> Self:
        task_id, title, description, status = task_str.strip().split("|")
        return cls(int(task_id), title, description, status)

