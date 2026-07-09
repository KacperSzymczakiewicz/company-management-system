from unittest.mock import Mock, patch
import pytest

from src.models.project import Project
from src.members.team_lead import TeamLead
from src.company import Company
from src.members.employee import Employee


class TestCompany:

    def test_add_member_to_other_members(self, employee: Employee):
        company = Company()
        company.add_member(employee)

        assert len(company.members) == 1
        assert isinstance(company.members[employee.member_id], Employee)

    def test_remove_member_from_other_members(self, employee: Employee):
        company = Company(
            teams={
                employee.member_id: [1, 2, 3],
                99: [employee.member_id, 4, 5]
            }
        )
        company.add_member(employee)
        company.remove_member(employee.member_id)

        assert len(company.members) == 0
        assert len(company.teams) == 1
        assert employee.member_id not in company.teams[99]

    def test_get_member_with_invalid_id_returns_none(self, employee: Employee):
        company = Company()
        company.add_member(employee)

        assert company.get_member_by_id(employee.member_id + 1) is None

    def test_get_member_with_valid_id_returns_employee(self, employee: Employee):
        company = Company()
        company.add_member(employee)

        assert company.get_member_by_id(employee.member_id) == employee

    def test_create_team(self, team_lead: TeamLead, employees: list[Employee]):
        company = Company()
        company.create_team(team_lead, employees)

        assert len(company.teams) == 1
        assert company.teams[team_lead.member_id] == [e.member_id for e in employees]
        assert team_lead.employees == {e.member_id: e for e in employees}

    def test_remove_team(self, team_lead: TeamLead, employees: list[Employee]):
        company = Company()
        company.add_member(team_lead)
        company.create_team(team_lead, employees)
        company.remove_member(team_lead.member_id)

        assert len(company.teams) == 0

    def test_assign_project_to_team(self, team_lead: TeamLead, project: Project):
        company = Company()
        company.assign_project_to_team(team_lead, project)

        assert len(company.get_all_projects()) == 1

    def test_get_team_lead_projects(self, team_lead: TeamLead, projects: list[Project]):
        company = Company(projects={team_lead.member_id: projects})

        assert len(company.get_team_projects(team_lead)) == len(projects)

    def test_load_tasks_with_invalid_path_raises_file_not_found_error(self, project: Project):
        with pytest.raises(FileNotFoundError):
            company = Company()
            company.load_tasks_from_file(file_path="src/non_existent_file.json", project=project)

    @patch("src.company.FileHandler.file_reader")
    @patch("src.company.Path.exists")
    def test_load_tasks_with_valid_path(self, mock_exists: Mock, mock_file_reader: Mock, project: Project):
        mock_exists.return_value = True
        dummy_path = "src/config.json"
        company = Company()
        company.load_tasks_from_file(file_path=dummy_path, project=project)

        mock_exists.assert_called_once_with()
        mock_file_reader.assert_called_once_with(dummy_path, project)

    @patch("src.company.FileHandler.save_report")
    def test_save_tasks(self, mock_save_report: Mock):
        company = Company()
        company.save_report('src/report.txt')

        mock_save_report.assert_called_once_with('src/report.txt', company)

    def test_team_lead_with_no_projects_return_empty_list(self, team_lead: TeamLead):
        company = Company()

        assert company.get_team_projects(team_lead) == []
