from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Todo:
    task: str
    category: str
    date_added: str = field(default_factory=lambda: datetime.now().isoformat())
    date_completed: str = None
    status: int = 1  # 1 = open, 2 = completed
    position: int = None

    def __repr__(self) -> str:
        return f"({self.task}, {self.category}, {self.date_added}, {self.date_completed}, {self.status}, {self.position})"

