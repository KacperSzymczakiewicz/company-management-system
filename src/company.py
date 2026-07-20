import logging
from dataclasses import dataclass, field
from pathlib import Path

from src.members.base import CompanyMember
from src.members.team_lead import TeamLead
from src.models.project import Project
from src.members.employee import Employee
from src.utils.file_handler import FileHandler

logger = logging.getLogger(__name__)


@dataclass
class Company:
    """Represents a company with members, teams, and projects.

    Attributes:
        members: Dictionary of all company members, keyed by member ID.
        teams: Dictionary mapping team lead ID to a list of employee IDs.
        projects: Dictionary mapping team lead ID to a list of assigned projects.
    """

    members: dict[int, CompanyMember] = field(default_factory=dict)
    teams: dict[int, list[int]] = field(default_factory=dict)
    projects: dict[int, list[Project]] = field(default_factory=dict)

    def add_member(self, member: CompanyMember) -> None:
        """Add a member to the company.

        Args:
            member: CompanyMember instance to be added.
        """
        logger.debug(f"Members before adding: {list(self.members.keys())}")
        self.members[member.member_id] = member
        logger.debug(f"Members after adding: {list(self.members.keys())}")
        logger.info(f"Member {member.name} added")

    def remove_member(self, member_id: int) -> None:
        """Remove a member from the company and all teams.

        Args:
            member_id: ID of the member to be removed.
        """
        self.members.pop(member_id, None)
        self.teams.pop(member_id, None)
        for team in self.teams.values():
            if member_id in team:
                team.remove(member_id)
        logger.info(f"Member {member_id} removed")

    def get_all_members(self) -> list[CompanyMember]:
        """Return a list of all company members."""
        return list(self.members.values())

    def get_all_projects(self) -> list[Project]:
        """Return a flat list of all projects across all teams."""
        return [p for project in self.projects.values() for p in project]

    def get_member_by_id(self, member_id: int) -> CompanyMember | None:
        """Return a member by ID, or None if not found.

        Args:
            member_id: ID of the member to retrieve.
        """
        return self.members.get(member_id, None)

    def create_team(self, team_lead: TeamLead, team_members: list[Employee]) -> None:
        """Create a team under the given team lead.

        Args:
            team_lead: TeamLead instance who will lead the team.
            team_members: List of Employee instances to be added to the team.
        """
        self.teams[team_lead.member_id] = [member.member_id for member in team_members]
        team_lead.employees = {m.member_id: m for m in team_members}
        logger.info(f"Team created for lead {team_lead.name}")

    def assign_project_to_team(self, team_lead: TeamLead, project: Project) -> None:
        """Assign a project to a team lead.

        Args:
            team_lead: TeamLead instance to assign the project to.
            project: Project instance to be assigned.
        """
        logger.debug(f"Checking if team lead {team_lead.name} has a project list")
        if team_lead.member_id not in self.projects:
            self.projects[team_lead.member_id] = []
            logger.debug(f"Team lead {team_lead.name} has no projects yet, created empty list")
        self.projects[team_lead.member_id].append(project)
        logger.info(f"Project {project.name} assigned to {team_lead.name}")

    def get_team_projects(self, team_lead: TeamLead) -> list[Project]:
        """Return a list of projects assigned to the given team lead.

        Args:
            team_lead: TeamLead instance whose projects to retrieve.
        """
        return list(self.projects.get(team_lead.member_id, []))

    def load_tasks_from_file(self, file_path: str, project: Project) -> None:
        """Load tasks from a file and add them to the given project.

        Args:
            file_path: Path to the file containing task data.
            project: Project instance to which tasks will be added.

        Raises:
            FileNotFoundError: If the file does not exist at the given path.
        """
        logger.debug(f"Checking if {file_path} exists")
        if not Path(file_path).exists():
            logger.error(f"File {file_path} does not exist")
            raise FileNotFoundError(f"Invalid file path: {file_path}")
        logger.debug(f"Loading tasks from {file_path}")
        FileHandler.file_reader(file_path, project)

    def save_report(self, file_path: str) -> None:
        """Save a full company report to a JSON file.

        Args:
            file_path: Path to the output JSON file.
        """
        logger.debug(f"Saving report to {file_path}")
        FileHandler.save_report(file_path, self)