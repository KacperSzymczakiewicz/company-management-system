import pytest

from src.members.employee import Employee


class TestCompanyMember:

    def test_member_invalid_id_raises_value_error(self) -> None:
        with pytest.raises(ValueError):
            member = Employee(-1, "Kacper", 20)

    def test_member_invalid_name_raises_value_error(self) -> None:
        with pytest.raises(ValueError):
            member = Employee(1, "", 20)

    def test_member_invalid_phone_raises_value_error(self) -> None:
        with pytest.raises(ValueError):
            member = Employee(1, "Kacper", -20)
