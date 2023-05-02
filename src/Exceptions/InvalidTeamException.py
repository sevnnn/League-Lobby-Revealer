class InvalidTeamException(Exception):
    def __init__(self, team_name: str):
        super().__init__(
            f"[ERR] Invalid team name {team_name}, allowed: ORDER or CHAOS"
        )
