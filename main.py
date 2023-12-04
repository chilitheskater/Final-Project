from skater import Skater
from skating_element import SkatingElement
from skating_routine import SkatingRoutine
from judge import Judge, ArtisticJudge
from skating_competition import SkatingCompetition

skater1 = Skater("Alice", "USA")
skater2 = Skater("Bob", "Canada")
element1 = SkatingElement("Jump", "Difficult")
element2 = SkatingElement("Spin", "Moderate")
routine1 = SkatingRoutine(skater1, [element1, element2])
judging_panel = [Judge(), ArtisticJudge()]
competition = SkatingCompetition([skater1, skater2], judging_panel)

competition.start_competition()
