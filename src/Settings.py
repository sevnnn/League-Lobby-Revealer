from configparser import ConfigParser
from os.path import exists

import requests

SETTINGS_FILE_PATH = "./settings.ini"


class Settings:
    def __init__(self):
        self.__config = ConfigParser()
        if not exists(SETTINGS_FILE_PATH):
            with open(SETTINGS_FILE_PATH, "w") as settings_file:
                settings_file.write(
                    requests.get(
                        "https://raw.githubusercontent.com/sevnnn/League-Lobby-Revealer/master/settings.ini"
                    ).text
                )
            print("Did not found './settings.ini' file, created one for you")
        self.__config.read(SETTINGS_FILE_PATH)

    def get_league_of_legends_dir(self) -> str:
        return self.__config.get("PATH", "LeagueOfLegendsDir")
