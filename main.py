from src.Communicators.DataDragonCommunicator import DataDragonCommunicator
from src.Communicators.LCUCommunicator import LCUCommunicator
from src.Communicators.RiotClientCommunicator import RiotClientCommunicator
from src.Factories.PlayerInfoFactory import PlayerInfoFactory
from src.Settings import Settings
from urllib.parse import quote

settings = Settings()
lcu = LCUCommunicator(settings.get_league_of_legends_dir())

# will handle "InGame" in another issue
if lcu.get_current_client_phase() != '"ChampSelect"':
    print("[ERR] Not in champion select")
    exit(1)

riot_client = RiotClientCommunicator()
data_dragon = DataDragonCommunicator()

url_safe_player_names: list[str] = []
for player in PlayerInfoFactory(lcu, riot_client, data_dragon).get_info():
    url_safe_player_names.append(quote(player.username))
    player.print_info()

print(
    f"Multisearch url:\n"
    f"https://www.op.gg/multisearch/{lcu.get_current_player_server()}?summoners={','.join(url_safe_player_names)}"
)
