
class SkatingCompetition:
    def __init__(self, skaters, judges):
        self.skaters = skaters
        self.judges = judges

    def start_competition(self):
        for skater in self.skaters:
            skater.skate()
            total_score = sum(judge.evaluate_performance(skater) for judge in self.judges)
            skater.receive_score(total_score)
