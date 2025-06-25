from enum import Enum

class Outcome(Enum):
    INVALID_MOVE = -4
    INVALID_STATE = -2
    CONTINUE = 0
    X_WINS = 1
    O_WINS = 2
    DRAW = 3