# skating_routine.py

class SkatingRoutine:
    def __init__(self, skater, elements):
        self.skater = skater
        self.elements = elements
        self.creativity_score = 0

    def perform_routine(self):
        print(f"{self.skater.name} is performing the routine!")

    def evaluate_creativity(self):
        self.creativity_score = len(self.elements) * 1.5
        print(f"Creativity score: {self.creativity_score}")
