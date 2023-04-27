from src.Communicators.AbstractCommunicator import AbstractCommunicator
import os


class RiotClientCommunicator(AbstractCommunicator):
    def __init__(self) -> None:
        super().__init__(
            os.getenv("localappdata") + "\\Riot Games\\Riot Client\\Config\\lockfile"
        )
