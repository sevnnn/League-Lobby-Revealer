class ChampionMasteryDTO:
    def __init__(self, champion_id: int, champion_level: int, champion_points: int):
        self.championPoints = champion_points
        self.championLevel = champion_level
        self.champion_id = champion_id
