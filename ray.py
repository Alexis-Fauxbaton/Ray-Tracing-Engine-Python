import numpy as np
from entity import *
from commons import *


class Ray:

    def __init__(self, position: np.array, coordinates: np.array, step=0.01):
        if position.shape[0] != 3:
            Exception("Ray origin is not 3-dimensional")
        elif coordinates.shape[0] != 3:
            Exception("Ray unit vector is not 3-dimensional")

        self.origin = position
        self.unit_vector = coordinates
        self.step = step
        self.color = np.array([1.0, 1.0, 1.0])

    def check_entities_collision(self, entities: list[Entity]):
        t_min = np.inf
        intersection_albedo = np.array([1.0, 1.0, 1.0])
        # TODO might want to use a search tree that uses 3d coordinates to speed up search time
        for entity in entities:
            is_collision, intersection_point, t = entity.get_ray_collision(self.origin, self.unit_vector)

            # print(entity, is_collision, self.origin, self.unit_vector)

            if is_collision and t < t_min:
                t_min = t
                intersection_albedo = entity.albedo

        self.color = self.color * intersection_albedo  # TODO should be tinted according to the color of the point of
        # intersection
