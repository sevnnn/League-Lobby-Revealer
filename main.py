from src.Communicators.DataDragonCommunicator import DataDragonCommunicator
from src.Communicators.InGameAPICommunicator import InGameAPICommunicator
from src.Communicators.LCUCommunicator import LCUCommunicator
from src.Communicators.RiotClientCommunicator import RiotClientCommunicator
from src.Exceptions.NotValidClientPhaseException import NotValidClientPhaseException
from src.Factories.PlayerInfoFactory import PlayerInfoFactory
from src.Settings import Settings
from urllib3 import disable_warnings
from urllib.parse import quote

if __name__ == "__main__":
    disable_warnings()

    settings = Settings()
    lcu = LCUCommunicator(settings.get_league_of_legends_dir())

    # faster execution
    if not lcu.get_current_client_phase() in ['"ChampSelect"', '"InProgress"']:
        raise NotValidClientPhaseException(lcu.get_current_client_phase())

    riot_client = RiotClientCommunicator()
    data_dragon = DataDragonCommunicator()
    player_info_factory = PlayerInfoFactory(lcu, riot_client, data_dragon)

    url_safe_player_names: list[str] = []
    match lcu.get_current_client_phase():
        case '"ChampSelect"':
            for player in player_info_factory.get_info_in_champ_select():
                url_safe_player_names.append(quote(player.username))
                player.print_info()
        case '"InProgress"':
            player_info_factory.in_game_api = InGameAPICommunicator()
            (
                your_team_players,
                enemy_team_players,
            ) = player_info_factory.get_info_in_game()
            print("=== YOUR TEAM ===")
            for player in your_team_players:
                url_safe_player_names.append(quote(player.username))
                player.print_info()
            print("=== ENEMY TEAM ===")
            for player in enemy_team_players:
                url_safe_player_names.append(quote(player.username))
                player.print_info()
        case _:
            raise NotValidClientPhaseException(lcu.get_current_client_phase())

    print(
        f"Multisearch url:\n"
        f"https://www.op.gg/multisearch/{lcu.get_current_player_server()}?summoners={','.join(url_safe_player_names)}"
    )
