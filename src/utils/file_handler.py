import logging
import json
from dataclasses import asdict
from typing import TYPE_CHECKING

from src.models.task import Task
from src.models.project import Project

if TYPE_CHECKING:
    from src.company import Company

logger = logging.getLogger(__name__)

class FileHandler:

    @staticmethod
    def file_reader(file_path: str, project: Project) -> None:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if line.strip():
                    task = Task.parse(line)
                    project.add_task(task)

    @staticmethod
    def save_report(file_path: str, company: 'Company') -> None:
        report = {
            "members": [asdict(m) for m in company.members.values()],
            "teams": company.teams,
            "projects": {
                team_lead_id: [asdict(p) for p in projects]
                for team_lead_id, projects in company.projects.items()
            }
        }
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(report, file, indent=4, ensure_ascii=False)
        logger.info(f"Project report written to {file_path}")
