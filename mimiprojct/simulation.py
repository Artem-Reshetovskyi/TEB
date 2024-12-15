from team import Team
from task import Task, TaskDifficulty
from developer import Developer, DeveloperRole
from events import Event, EventType

import random

def run_simulation():
    # Sample data
    tasks = [
        Task("Build API", TaskDifficulty.HARD, ["Python", "REST"], 10),
        Task("Create UI", TaskDifficulty.MEDIUM, ["HTML", "CSS", "JavaScript"], 8),
        Task("Fix Bug", TaskDifficulty.EASY, ["Python"], 3),
    ]

    developers = [
        Developer("Alice", DeveloperRole.BACKEND, 0.8, ["Python", "Django", "REST"]),
        Developer("Bob", DeveloperRole.FRONTEND, 0.7, ["HTML", "CSS", "JavaScript"]),
        Developer("Charlie", DeveloperRole.DEVOPS, 0.9, ["Docker", "Kubernetes"]),
    ]

    team = Team(developers)

    # Simulate work
    for day in range(1, 11):  # Simulate 10 days
        print(f"Day {day}")
        team.assign_tasks(tasks)

        # Random event
        if random.random() < 0.3:  # 30% chance of an event
            event = random.choice([
                Event(EventType.BUG_FIX, "Fix a critical bug, slowing progress."),
                Event(EventType.ABSENCE, "Developer absent, progress halted."),
                Event(EventType.SYSTEM_CRASH, "System crash, all work paused."),
            ])
            event.apply_event()

        for task in tasks:
            print(task)

if __name__ == "__main__":
    run_simulation()