class ChampionMasteryDTO:
    def __init__(
        self,
        champion_name: str,
        champion_level: int,
        champion_points: int,
    ):
        self.champion_name = champion_name
        self.champion_level = champion_level
        self.champion_points = champion_points
