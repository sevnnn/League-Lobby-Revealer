from src.Communicators.AbstractCommunicator import AbstractCommunicator
from src.Communicators.DataDragonCommunicator import DataDragonCommunicator
from src.DTOs.ChampionMasteryDTO import ChampionMasteryDTO
from src.DTOs.CurrentRankedInfoDTO import CurrentRankedInfoDTO
from src.DTOs.SummonerDTO import SummonerDTO

summoners_rift_queue_ids: list[int] = [
    400,  # 5v5 Draft Pick games
    420,  # 5v5 Ranked Solo games,
    430,  # 5v5 Blind Pick games
    440,  # 5v5 Ranked Flex games
]


class LCUCommunicator(AbstractCommunicator):
    def __init__(self, league_of_legends_install_dir: str) -> None:
        super().__init__(f"{league_of_legends_install_dir}\\lockfile")

    def get_summoner_by_puuid(self, puuid: str) -> SummonerDTO:
        json_response = self._GET(f"/lol-summoner/v2/summoners/puuid/{puuid}").json()

        return SummonerDTO(
            json_response["accountId"],
            json_response["displayName"],
            json_response["internalName"],
            json_response["puuid"],
            json_response["summonerId"],
            json_response["summonerLevel"],
        )

    def get_ranked_stats_by_puuid(self, puuid: str):
        json_response = self._GET(f"/lol-ranked/v1/ranked-stats/{puuid}").json()

        return CurrentRankedInfoDTO(
            json_response["queueMap"]["RANKED_SOLO_5x5"]["tier"],
            json_response["queueMap"]["RANKED_SOLO_5x5"]["division"],
            json_response["queueMap"]["RANKED_SOLO_5x5"]["leaguePoints"],
            json_response["queueMap"]["RANKED_SOLO_5x5"]["wins"],
            json_response["queueMap"]["RANKED_SOLO_5x5"]["losses"],
        )

    def get_sr_streak_status_by_puuid(self, puuid: str) -> str:
        json_response = self._GET(
            f"/lol-match-history/v1/products/lol/{puuid}/matches"
        ).json()

        streak_result_list: list[bool] = []

        for game in json_response["games"]["games"]:
            if game["queueId"] not in summoners_rift_queue_ids:
                continue

            for team in game["teams"]:
                if team["teamId"] != game["participants"][0]["teamId"]:
                    continue
                streak_result_list.append(True if team["win"] == "Win" else False)

        match len(streak_result_list):
            case 0:
                return "Unknown"
            case 1:
                return f"1 {'Winning streak' if streak_result_list[0] else 'Losing streak'}"
            case _:
                for index in range(len(streak_result_list) - 1):
                    game_result = streak_result_list[index]
                    if game_result != streak_result_list[index + 1]:
                        return f"{index + 1} {'Winning streak' if game_result else 'Losing streak'}"

    def get_top_mastery_champions_by_summoner_id(
        self,
        summoner_id: int,
        data_dragon_communicator: DataDragonCommunicator,
        limit: int = 3,
    ) -> list[ChampionMasteryDTO]:
        json_response = self._GET(
            f"/lol-collections/v1/inventories/{summoner_id}/champion-mastery/top?limit={limit}"
        ).json()

        return_list: list[ChampionMasteryDTO] = []
        for champion in json_response["masteries"]:
            return_list.append(
                ChampionMasteryDTO(
                    data_dragon_communicator.get_champion_name_by_id(
                        champion["championId"]
                    ),
                    champion["championLevel"],
                    champion["championPoints"],
                )
            )

        return return_list

    def get_current_client_phase(self) -> str:
        return self._GET("/lol-gameflow/v1/gameflow-phase").text

    def get_current_player_server(self) -> str:
        return self._GET("/riotclient/region-locale").json()["webRegion"]
