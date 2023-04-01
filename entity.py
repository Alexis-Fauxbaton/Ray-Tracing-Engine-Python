import numpy as np


class Entity:
    def __init__(self, center: np.array, albedo: np.array, roughness: float = 0, is_emissive=False, brightness: float = 0.5):
        if center.shape[0] != 3:
            Exception("Center of object is not 3-dimensional")
        elif albedo.shape[0] != 3:
            Exception("Albedo of object is not 3-dimensional")

        self.center = center
        self.roughness = roughness
        self.albedo = albedo
        self.emissive = is_emissive
        self.brightness = brightness


class SphereEntity(Entity):

    def __init__(self, center: np.array, radius: float, albedo: np.array, roughness: float = 0, is_emissive=False, brightness: float = 0.5):
        super().__init__(center, albedo, roughness, is_emissive, brightness)

        self.radius = radius


class CubeEntity(Entity):

    def __init__(self, center: np.array, side_length: float, albedo: np.array, roughness: float = 0, is_emissive=False, brightness: float = 0.5):
        super().__init__(center, albedo, roughness, is_emissive, brightness)

        self.side_length = side_length
