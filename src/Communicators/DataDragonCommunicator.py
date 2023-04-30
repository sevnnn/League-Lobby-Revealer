import requests
from requests import Response


class DataDragonCommunicator:
    def __init__(self):
        versions = requests.get(
            "https://ddragon.leagueoflegends.com/api/versions.json"
        ).json()
        self.__host = f"http://ddragon.leagueoflegends.com/cdn/{versions[0]}/data/en_US"
        self.__champion_id_name_map: dict[int, str] = {}
        all_champions = self.__GET("/champion.json").json()
        for champ_key in all_champions["data"]:
            self.__champion_id_name_map[
                int(all_champions["data"][champ_key]["key"])
            ] = all_champions["data"][champ_key]["name"]

    def __GET(self, endpoint: str) -> Response:
        return requests.get(self.__host + endpoint)

    def get_champion_name_by_id(self, champion_id: int) -> str:
        return self.__champion_id_name_map[champion_id]
