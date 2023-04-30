from src.Communicators.DataDragonCommunicator import DataDragonCommunicator
from src.Communicators.LCUCommunicator import LCUCommunicator
from src.Communicators.RiotClientCommunicator import RiotClientCommunicator
from src.Factories.PlayerInfoFactory import PlayerInfoFactory

lcu = LCUCommunicator()
riot_client = RiotClientCommunicator()
data_dragon = DataDragonCommunicator()


for player in PlayerInfoFactory(lcu, riot_client, data_dragon).getInfo():
    player.printInfo()
