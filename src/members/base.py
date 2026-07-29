import logging
from dataclasses import dataclass
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)


@dataclass
class CompanyMember(ABC):
    """Abstract base class representing a company member.

    Attributes:
        member_id: Unique positive identifier of the member.
        name: Full name of the member.
        age: Age of the member in years.
    """

    member_id: int
    name: str
    age: int

    def __post_init__(self) -> None:
        """Validate member data after initialization.

        Raises:
            ValueError: If member_id or age is not positive, or name is empty.
        """
        if self.member_id <= 0 or not self.name or self.age <= 0:
            logger.error(
                f"Invalid member id: {self.member_id} or name: {self.name} or age: {self.age} !"
            )
            raise ValueError("Invalid member data")

    @abstractmethod
    def info(self) -> str:
        """Return a formatted string with member information."""
        pass
