from enum import Enum

class DeveloperRole(Enum):
    FRONTEND = "Frontend"
    BACKEND = "Backend"
    DEVOPS = "DevOps"

class Developer:
    def __init__(self, name: str, role: DeveloperRole, efficiency: float, skills: list[str]):
        self.name = name
        self.role = role
        self.efficiency = efficiency
        self.skills = skills

    def work_on_task(self, efficiency: float):
        """Simulate work on the task based on efficiency."""
        self.progress += efficiency
        if self.progress >= 100:
            self.completed = True

    def __str__(self):
        return f"Task({self.name}, {self.difficulty.name}, Deadline: {self.deadline}, Completed: {self.completed})"