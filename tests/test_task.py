import pytest

from src.models.task import Task, TaskStatus


class TestTask:
    def test_parse_invalid_format_raises_value_error(self):
        with pytest.raises(ValueError) as err:
            Task.parse("1|Logow|anie|Formularz logowania użytkownika|pending")

        assert str(err.value) == "Invalid task string!"

    def test_parse_valid_format_returns_correct_task(self):
        res = Task.parse("1|Logowanie|Formularz logowania użytkownika|pending")

        assert isinstance(res, Task)
        assert res.task_id == 1
        assert res.title == "Logowanie"
        assert res.description == "Formularz logowania użytkownika"
        assert res.status == TaskStatus.PENDING

    def test_parse_invalid_task_id_raises_value_error(self):
        with pytest.raises(ValueError) as err:
            Task.parse("abc|Logowanie|Formularz logowania użytkownika|pending")

        assert str(err.value) == "Invalid task id!"

    def test_parse_invalid_task_status_raises_value_error(self):
        with pytest.raises(ValueError) as err:
            Task.parse("1|Logowanie|Formularz logowania użytkownika|pendin")

        assert str(err.value) == "Invalid task status!"