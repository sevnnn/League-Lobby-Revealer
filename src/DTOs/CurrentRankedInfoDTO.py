class CurrentRankedInfoDTO:
    def __init__(
        self, tier: str, division: str, league_points: int, wins: int, losses: int
    ):
        self.tier = tier
        self.division = division
        self.league_points = league_points
        self.wins = wins
        self.losses = losses

    def get_winrate_as_string(self) -> str:
        return (
            "%.2f %%" % (self.wins / (self.wins + self.losses) * 100)
            if self.wins + self.losses > 0
            else "- %%"
        )
