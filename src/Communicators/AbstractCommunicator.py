from abc import ABC
from base64 import b64encode
from requests import Response
from src.Exceptions.LeagueNotOpenException import LeagueNotOpenException
import requests


class AbstractCommunicator(ABC):
    def __init__(self, lockfile_path: str) -> None:
        try:
            with open(lockfile_path, "r") as f:
                lockfile = f.read().split(":")
                self.__host = f"{lockfile[4]}://127.0.0.1:{lockfile[2]}"
                self.__authorization = (
                    f"Basic {b64encode(f'riot:{lockfile[3]}'.encode()).decode()}"
                )
        except FileNotFoundError:
            raise LeagueNotOpenException

    def _GET(self, endpoint: str, debug: bool = False) -> Response:
        response = requests.get(
            self.__host + endpoint,
            verify=False,
            headers={"Authorization": self.__authorization},
        )

        if debug:
            file_name = (
                endpoint[: endpoint.find("?")] if endpoint.find("?") != -1 else endpoint
            )
            file_name = "-".join(file_name.split("/")[1:]) + ".json"
            with open(f"./cache/{file_name}", "w") as debug_file:
                debug_file.write(response.text)

        return response
