class LeagueNotOpenException(Exception):
    def __init__(self):
        super().__init__("[ERR] League Of Legends is not open")
