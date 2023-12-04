class Skater:
    def __init__(self, name, country):
    
        self.name = name
        self.country = country
        self.performance_score = 0

    def skate(self):
        print(f"{self.name} is performing!")

    def receive_score(self, score):
        self.performance_score += score
        print(f"{self.name} received a score of {score}")