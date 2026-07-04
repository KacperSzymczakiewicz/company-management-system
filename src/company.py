import logging
from dataclasses import dataclass, field
from pathlib import Path

from src.members.base import CompanyMember
from src.members.team_lead import TeamLead
from src.models.project import Project
from src.members.manager import Manager
from src.members.employee import Employee
from src.utils.file_handler import FileHandler

logger = logging.getLogger(__name__)


@dataclass
class Company:
    members: dict[int, CompanyMember] = field(default_factory=dict)
    teams: dict[int, list[int]] = field(default_factory=dict)
    projects: dict[int, list[Project]] = field(default_factory=dict)

    def add_member(self, member: CompanyMember) -> None:
        logger.debug(f"Members before adding: {list(self.members.keys())}")
        self.members[member.member_id] = member
        logger.debug(f"Members after adding: {list(self.members.keys())}")
        logger.info(f"Member {member.name} added")

    def add_manager_with_employees(self, manager: Manager, employees: list[Employee]) -> None:
        self.members[manager.member_id] = manager
        for employee in employees:
            self.members[employee.member_id] = employee
        logger.info(f"Manager {manager.name} added with {len(employees)} employees")

    def remove_member(self, member_id: int) -> None:
        self.members.pop(member_id, None)
        self.teams.pop(member_id, None)
        for team in self.teams.values():
            if member_id in team:
                team.remove(member_id)
        logger.info(f"Member {member_id} removed")

    def get_all_members(self) -> list[CompanyMember]:
        return list(self.members.values())

    def get_member_by_id(self, member_id: int) -> CompanyMember | None:
        return self.members.get(member_id, None)

    def create_team(self, team_lead: TeamLead, team_members: list[Employee]) -> None:
        self.teams[team_lead.member_id] = [member.member_id for member in team_members]
        logger.info(f"Team created for lead {team_lead.name}")

    def assign_project_to_team(self, team_lead: TeamLead, project: Project) -> None:
        logger.debug(f"Checking if team lead {team_lead.name} has a project list")
        if team_lead.member_id not in self.projects:
            self.projects[team_lead.member_id] = []
            logger.debug(f"Team lead {team_lead.name} has no projects yet, created empty list")
        self.projects[team_lead.member_id].append(project)
        logger.info(f"Project {project.name} assigned to {team_lead.name}")

    def get_team_projects(self, team_lead: TeamLead) -> list[Project]:
        return list(self.projects[team_lead.member_id])

    def load_tasks_from_file(self, file_path: str, project: Project) -> None:
        logger.debug(f"Checking if {file_path} exists")
        if not Path(file_path).exists():
            logger.error(f"File {file_path} does not exist")
            raise FileNotFoundError(f"Invalid file path: {file_path}")
        logger.debug(f"Loading tasks from {file_path}")
        FileHandler.file_reader(file_path, project)

    def save_report(self, file_path: str) -> None:
        logger.debug(f"Saving report to {file_path}")
        FileHandler.save_report(file_path, self)