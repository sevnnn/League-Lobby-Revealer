class SummonerDTO:
    def __init__(
        self,
        account_id: int,
        display_name: str,
        internal_name: str,
        puuid: str,
        summoner_id: int,
        summoner_level: int,
    ):
        self.account_id = account_id
        self.display_name = display_name
        self.internal_name = internal_name
        self.puuid = puuid
        self.summoner_id = summoner_id
        self.summoner_level = summoner_level
