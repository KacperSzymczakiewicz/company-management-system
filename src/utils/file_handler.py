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
    """Handles reading and writing company data to files."""

    @staticmethod
    def file_reader(file_path: str, project: Project) -> None:
        """Read tasks from a file and add them to the given project.

        Each non-empty line is parsed as a pipe-separated task string.

        Args:
            file_path: Path to the file containing task data.
            project: Project instance to which parsed tasks will be added.
        """
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if line.strip():
                    task = Task.parse(line)
                    project.add_task(task)

    @staticmethod
    def save_report(file_path: str, company: 'Company') -> None:
        """Save a full company report to a JSON file.

        Args:
            file_path: Path to the output JSON file.
            company: Company instance whose data will be serialized.
        """
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