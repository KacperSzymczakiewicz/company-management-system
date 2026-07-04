import logging
from dataclasses import dataclass
from typing import Self

logger = logging.getLogger(__name__)


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
        logger.debug(f"Parsing: {task_str}")
        parts = task_str.strip().split("|")
        if len(parts) != 4:
            logger.error(f"Invalid task: {task_str}")
            raise ValueError(f"Invalid task string: {task_str}")
        task_id, title, description, status = parts
        return cls(int(task_id), title, description, status)
