# judge.py

class Judge:
    def evaluate_performance(self, skater):
        return 8.5  # Placeholder score

class ArtisticJudge(Judge):
    def evaluate_performance(self, skater):
        return super().evaluate_performance(skater) + 1.0
