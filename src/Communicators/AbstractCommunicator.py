from abc import ABC
from base64 import b64encode
from requests import Response
import requests
import urllib3


class AbstractCommunicator(ABC):
    def __init__(self, lockfile_path: str) -> None:
        urllib3.disable_warnings()
        try:
            with open(lockfile_path, "r") as f:
                lockfile = f.read().split(":")
                self.__host = f"{lockfile[4]}://127.0.0.1:{lockfile[2]}"
                self.__authorization = (
                    f"Basic {b64encode(f'riot:{lockfile[3]}'.encode()).decode()}"
                )
        except FileNotFoundError:
            print("[ERR] League Of Legends isn't open!")
            exit(1)

    def _GET(self, endpoint: str) -> Response:
        return requests.get(
            self.__host + endpoint,
            verify=False,
            headers={"Authorization": self.__authorization},
        )
