import numpy as np
from constants import ENV_DIM
from entity import *


def in_bounds(pos: np.array):
    if pos[0] >= ENV_DIM[0] or pos[0] < 0 or pos[1] >= ENV_DIM[1] or pos[1] < 0 or pos[2] >= ENV_DIM[2] or pos[2] < 0:
        return False
    return True
