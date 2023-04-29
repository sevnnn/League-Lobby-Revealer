from src.Communicators.LCUCommunicator import LCUCommunicator
from src.Communicators.RiotClientCommunicator import RiotClientCommunicator


lcu = LCUCommunicator()
riot_client = RiotClientCommunicator()

summoner = lcu.get_summoner_by_puuid("3f6c792e-8c56-5e21-8199-e8d38c22bbce")
