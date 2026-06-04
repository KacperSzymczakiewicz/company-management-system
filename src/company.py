from dataclasses import dataclass, field

from src.members.base import CompanyMember
from src.members.team_lead import TeamLead
from src.models.project import Project
from src.members.manager import Manager
from src.members.employee import Employee

@dataclass
class Company:
    members: dict[int, CompanyMember] = field(default_factory=dict)
    teams: dict[int, list[int]] = field(default_factory=dict)
    projects: dict[int, list[Project]] = field(default_factory=dict)

    def add_member(self, member: CompanyMember) -> None:
        self.members[member.member_id] = member

    def add_manager_with_employees(self, manager: Manager, employees: list[Employee]) -> None:
        self.members[manager.member_id] = manager
        for employee in employees:
            self.members[employee.member_id] = employee

    def remove_member(self, member_id: int) -> None:
        self.members.pop(member_id, None)
        self.teams.pop(member_id, None)
        for team in self.teams.values():
            if member_id in team:
                team.remove(member_id)

    def get_all_members(self) -> list[CompanyMember]:
        return list(self.members.values())

    def get_member_by_id(self, member_id: int) -> CompanyMember:
        return self.members.get(member_id, None)

    def create_team(self, team_lead: TeamLead, team_members: list[Employee]) -> None:
        self.teams[team_lead.member_id] = [member.member_id for member in team_members]

    def assign_project_to_team(self, team_lead: TeamLead, project: Project) -> None:
        if team_lead.member_id not in self.projects:
            self.projects[team_lead.member_id] = []
        self.projects[team_lead.member_id].append(project)

    def get_team_projects(self, team_lead: TeamLead) -> list[Project]:
        return list(self.projects[team_lead.member_id])

    def load_tasks_from_file(self, file_path: str, project: Project) -> None:
        ...