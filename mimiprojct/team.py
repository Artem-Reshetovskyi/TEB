from task import Task
from developer import Developer

class Team:
    def __init__(self, developers: list[Developer]):
        self.developers = developers

    def assign_tasks(self, tasks: list[Task]):
        """Assign tasks to developers based on their skills."""
        for task in tasks:
            for developer in self.developers:
                if not task.completed and any(skill in developer.skills for skill in task.required_skills):
                    developer.work(task)