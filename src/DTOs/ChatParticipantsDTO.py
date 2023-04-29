class ChatParticipantsDTO:
    def __init__(
        self,
        game_name: str,
        game_tag: str,
        name: str,
        puuid: str,
        region: str,
    ):
        self.game_name = game_name
        self.game_tag = game_tag
        self.name = name
        self.puuid = puuid
        self.region = region
