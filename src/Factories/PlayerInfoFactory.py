from src.Communicators.DataDragonCommunicator import DataDragonCommunicator
from src.Communicators.InGameAPICommunicator import InGameAPICommunicator
from src.Communicators.LCUCommunicator import LCUCommunicator
from src.Communicators.RiotClientCommunicator import RiotClientCommunicator
from src.DTOs.PlayerInfoDTO import PlayerInfoDTO


class PlayerInfoFactory:
    def __init__(
        self,
        lcu_communicator: LCUCommunicator,
        riot_client_communicator: RiotClientCommunicator,
        data_dragon_communicator: DataDragonCommunicator,
        in_game_api_communicator: InGameAPICommunicator | None = None,
    ):
        self.__lcu = lcu_communicator
        self.__riot_client = riot_client_communicator
        self.__data_dragon_communicator = data_dragon_communicator
        self.in_game_api = in_game_api_communicator

    def get_info_in_champ_select(self) -> list[PlayerInfoDTO]:
        return_list: list[PlayerInfoDTO] = []

        for player in self.__riot_client.get_chat_participants():
            summoner = self.__lcu.get_summoner_by_puuid(player.puuid)

            return_list.append(
                PlayerInfoDTO(
                    player.name,
                    summoner.summoner_level,
                    self.__lcu.get_sr_streak_status_by_puuid(player.puuid),
                    self.__lcu.get_top_mastery_champions_by_summoner_id(
                        summoner.summoner_id, self.__data_dragon_communicator
                    ),
                    self.__lcu.get_ranked_stats_by_puuid(player.puuid),
                )
            )

        return return_list

    def get_info_in_game(self) -> (list[PlayerInfoDTO], list[PlayerInfoDTO]):
        your_team: list[PlayerInfoDTO] = []
        enemy_team: list[PlayerInfoDTO] = []

        (
            your_team_summoner_names,
            enemy_team_summoner_names,
        ) = self.in_game_api.get_player_name_list(
            self.__lcu.get_current_summoner().display_name
        )

        for player_name in your_team_summoner_names:
            summoner = self.__lcu.get_summoner_by_name(player_name)

            your_team.append(
                PlayerInfoDTO(
                    summoner.display_name,
                    summoner.summoner_level,
                    self.__lcu.get_sr_streak_status_by_puuid(summoner.puuid),
                    self.__lcu.get_top_mastery_champions_by_summoner_id(
                        summoner.summoner_id, self.__data_dragon_communicator
                    ),
                    self.__lcu.get_ranked_stats_by_puuid(summoner.puuid),
                )
            )

        for player_name in enemy_team_summoner_names:
            summoner = self.__lcu.get_summoner_by_name(player_name)

            enemy_team.append(
                PlayerInfoDTO(
                    summoner.display_name,
                    summoner.summoner_level,
                    self.__lcu.get_sr_streak_status_by_puuid(summoner.puuid),
                    self.__lcu.get_top_mastery_champions_by_summoner_id(
                        summoner.summoner_id, self.__data_dragon_communicator
                    ),
                    self.__lcu.get_ranked_stats_by_puuid(summoner.puuid),
                )
            )

        return your_team, enemy_team
