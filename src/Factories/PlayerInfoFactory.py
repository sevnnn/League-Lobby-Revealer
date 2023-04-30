from src.Communicators.DataDragonCommunicator import DataDragonCommunicator
from src.Communicators.LCUCommunicator import LCUCommunicator
from src.Communicators.RiotClientCommunicator import RiotClientCommunicator
from src.DTOs.PlayerInfoDTO import PlayerInfoDTO


class PlayerInfoFactory:
    def __init__(
        self,
        lcu_communicator: LCUCommunicator,
        riot_client_communicator: RiotClientCommunicator,
        data_dragon_communicator: DataDragonCommunicator,
    ):
        self.lcu = lcu_communicator
        self.riot_client = riot_client_communicator
        self.data_dragon_communicator = data_dragon_communicator

    def getInfo(self) -> list[PlayerInfoDTO]:
        return_list: list[PlayerInfoDTO] = []

        for player in self.riot_client.get_chat_participants():
            summoner = self.lcu.get_summoner_by_puuid(player.puuid)

            return_list.append(
                PlayerInfoDTO(
                    player.name,
                    summoner.summoner_level,
                    self.lcu.get_sr_streak_status_by_puuid(player.puuid),
                    self.lcu.get_top_mastery_champions_by_summoner_id(
                        summoner.summoner_id, self.data_dragon_communicator
                    ),
                    self.lcu.get_ranked_stats_by_puuid(player.puuid),
                )
            )

        return return_list
