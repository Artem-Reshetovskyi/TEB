from enum import Enum

class TaskDifficulty(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3

class Task:
    def __init__(self, name: str, difficulty: TaskDifficulty, required_skills: list[str], deadline: int):
        self.name = name
        self.difficulty = difficulty
        self.required_skills = required_skills
        self.deadline = deadline
        self.progress = 0  # 0% to 100%
        self.completed = False

    def work_on_task(self, efficiency: float):
        """Simulate work on the task based on efficiency."""
        self.progress += efficiency
        if self.progress >= 100:
            self.completed = True

    def __str__(self):
        return f"Task({self.name}, {self.difficulty.name}, Deadline: {self.deadline}, Completed: {self.completed})"