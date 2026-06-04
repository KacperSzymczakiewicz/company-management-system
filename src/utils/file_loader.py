from src.models.task import Task
from src.models.project import Project

class FileLoader:

    @staticmethod
    def file_reader(file_path: str, project: Project) -> None:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if line.strip():
                    task = Task.parse(line)
                    project.add_task(task)

