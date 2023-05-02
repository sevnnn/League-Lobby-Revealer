from src.Exceptions.InvalidTeamException import InvalidTeamException
from re import sub
from subprocess import run
from requests import Response
import requests


class InGameAPICommunicator:
    def __init__(self):
        powershell_parser_output = (
            run(
                [
                    "powershell",
                    "-Command",
                    "Get-NetTCPConnection -OwningProcess $(Get-Process 'League of Legends').Id"
                    "| Where-Object { $_.LocalAddress -EQ '127.0.0.1' -And $_.RemoteAddress -EQ '0.0.0.0' }"
                    "| Select-Object LocalAddress,LocalPort",
                ],
                capture_output=True,
            )
            .stdout.decode("utf-8")
            .split("\r\n")[3]
        )
        self.__host = f"https://{sub(' +', ':', powershell_parser_output)}"

    def _GET(self, endpoint: str) -> Response:
        return requests.get(self.__host + endpoint, verify=False)

    def get_player_name_list(
        self, current_summoner_name: str
    ) -> (list[str], list[str]):
        json_response = self._GET("/liveclientdata/playerlist").json()
        players_order: list[str] = []
        players_chaos: list[str] = []
        player_team: str = ""

        for player in json_response:
            if player["isBot"]:
                continue

            if player["summonerName"] == current_summoner_name:
                player_team = player["team"]

            if player["team"] == "ORDER":
                players_order.append(player["summonerName"])
            elif player["team"] == "CHAOS":
                players_chaos.append(player["summonerName"])
            else:
                raise InvalidTeamException(player["team"])

        #  we want summoner team to always return first
        if player_team == "ORDER":
            return players_order, players_chaos
        else:
            return players_chaos, players_order
