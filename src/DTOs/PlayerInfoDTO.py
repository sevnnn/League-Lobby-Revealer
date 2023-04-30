from src.DTOs.ChampionMasteryDTO import ChampionMasteryDTO
from src.DTOs.CurrentRankedInfoDTO import CurrentRankedInfoDTO


class PlayerInfoDTO:
    def __init__(
        self,
        username: str,
        level: int,
        streak: str,
        champion_masteries: list[ChampionMasteryDTO],
        ranked_stats: CurrentRankedInfoDTO,
    ):
        self.username = username
        self.level = level
        self.streak = streak
        self.champion_masteries = champion_masteries
        self.ranked_stats = ranked_stats

    def printInfo(self):
        print(
            f"{self.username}\t-\tLevel {self.level}\t-\t{self.streak}\t-"
            f"\t{self.ranked_stats.tier} {self.ranked_stats.division} {self.ranked_stats.league_points} LP "
            f"({self.ranked_stats.get_winrate_as_string()})"
        )
        print(f"\tTop 3 champions:")
        for champion in self.champion_masteries:
            print(
                f"\t\t{champion.champion_name} ({champion.champion_points}) - Level {champion.champion_level}"
            )
        print()
