import numpy as np


class Ray:
    def __int__(self, position: np.array, coordinates: np.array):
        if position.shape[0] != 3:
            Exception("Ray position is not 3-dimensional")
        elif coordinates.shape[0] != 3:
            Exception("Ray coordinates are not 3-dimensional")
