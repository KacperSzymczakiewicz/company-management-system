import logging
from dataclasses import dataclass
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)

@dataclass
class CompanyMember(ABC):
    member_id: int
    name: str
    age: int

    def __post_init__(self) -> None:
        if self.member_id <= 0 or not self.name or self.age <= 0:
            logger.error(f"Invalid member id: {self.member_id} or name: {self.name} or age: {self.age} !")
            raise ValueError("Invalid member data")

    @abstractmethod
    def info(self) -> str:
        pass
