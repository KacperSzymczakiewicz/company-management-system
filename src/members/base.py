from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class CompanyMember(ABC):
    member_id: int
    name: str
    age: int

    @abstractmethod
    def info(self) -> str:
        pass
