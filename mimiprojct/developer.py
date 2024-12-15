from enum import Enum

class DeveloperRole(Enum):
    FRONTEND = "Frontend"
    BACKEND = "Backend"
    DEVOPS = "DevOps"
    GAME_DEVELOPER = "Game Developer"

class Developer:
    def __init__(self, name: str, role: DeveloperRole, efficiency: float, skills: list[str]):
        self.name = name
        self.role = role
        self.efficiency = efficiency
        self.skills = skills

    def work(self, task):
        """Work on a task if the skills match."""
        if any(skill in task.required_skills for skill in self.skills):
            task.work_on_task(self.efficiency)
        else:
            print(f"{self.name} cannot work on this task due to lack of skills.")

    def __str__(self):
        return f"Developer({self.name}, {self.role.name}, Efficiency: {self.efficiency})"