import pytest

from src.models.task import Task
from src.members.team_lead import TeamLead


class TestTeamLead:

    def test_assign_task_with_invalid_id_raises_value_error(self, team_lead: TeamLead, task: Task) -> None:
        with pytest.raises(ValueError):
            team_lead.assign_task(5, task)

    def test_assign_task_with_valid_id(self, team_lead: TeamLead, task: Task) -> None:
        team_lead.assign_task(1, task)

        assert team_lead.employees[1].tasks[1] == task

    def test_change_task_status_review(self, team_lead: TeamLead, task: Task) -> None:
        team_lead.review_task(task)
        
        assert task.status == "reviewed"