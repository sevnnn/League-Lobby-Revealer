from src.Communicators.DataDragonCommunicator import DataDragonCommunicator
from src.Communicators.LCUCommunicator import LCUCommunicator
from src.Communicators.RiotClientCommunicator import RiotClientCommunicator
from src.Factories.PlayerInfoFactory import PlayerInfoFactory

lcu = LCUCommunicator()

# prob will need to add "InGame" to this if, but need to test what the chat endpoint will return when ingame
if lcu.get_current_client_phase() != "ChampSelect":
    print("[ERR] Not in champion select")
    exit(1)

riot_client = RiotClientCommunicator()
data_dragon = DataDragonCommunicator()


for player in PlayerInfoFactory(lcu, riot_client, data_dragon).get_info():
    player.print_info()
