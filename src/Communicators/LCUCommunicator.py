from src.Communicators.AbstractCommunicator import AbstractCommunicator


class LCUCommunicator(AbstractCommunicator):
    def __init__(self) -> None:
        super().__init__("C:\\Riot Games\\League of Legends\\lockfile")
