class NotValidClientPhaseException(Exception):
    def __init__(self, current_phase: str):
        super().__init__(f"[ERR] Not in Champ Select or In Game, current phase: {current_phase}")
