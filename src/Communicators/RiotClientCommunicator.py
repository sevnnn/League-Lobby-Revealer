from src.Communicators.AbstractCommunicator import AbstractCommunicator
import os

from src.DTOs.ChatParticipantsDTO import ChatParticipantsDTO


class RiotClientCommunicator(AbstractCommunicator):
    def __init__(self) -> None:
        super().__init__(
            os.getenv("localappdata") + "\\Riot Games\\Riot Client\\Config\\lockfile"
        )

    def get_chat_participants(self) -> list[ChatParticipantsDTO]:
        json_response = self._GET("/chat/v5/participants").json()
        chat_participants = []
        for player in json_response["participants"]:
            chat_participants.append(
                ChatParticipantsDTO(
                    player["game_name"],
                    player["game_tag"],
                    player["name"],
                    player["puuid"],
                    player["region"],
                )
            )

        return chat_participants
