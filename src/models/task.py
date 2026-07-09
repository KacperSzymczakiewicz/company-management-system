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
            raise ValueError("Invalid task string!")
        task_id_str, title, description, status = parts
        try:
            task_id = int(task_id_str)
        except ValueError:
            logger.error(f"Invalid task id: {task_id_str}")
            raise ValueError("Invalid task id!")
        return cls(task_id, title, description, status)
