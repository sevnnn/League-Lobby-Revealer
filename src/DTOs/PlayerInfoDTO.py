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
        role: str | None = None,
    ):
        self.username = username
        self.level = level
        self.streak = streak
        self.champion_masteries = champion_masteries
        self.ranked_stats = ranked_stats
        self.role = role

    def print_info(self):
        print(
            "  |  ".join(
                [
                    self.username,
                    f"Level {self.level}",
                    self.streak,
                    f"{self.role}" if self.role else "UNKNOWN ROLE",
                    f"{self.ranked_stats.tier} {self.ranked_stats.division} {self.ranked_stats.league_points} LP",
                    f"{self.ranked_stats.get_winrate_as_string()} WR",
                ]
            )
        )
        print(f"  Top 3 champions:")
        for champion in self.champion_masteries:
            print(
                f"    {champion.champion_name} ({champion.champion_points})  |  Level {champion.champion_level}"
            )
        print()
