import numpy as np


class Entity:
    def __init__(self, center: np.array, albedo: np.array, roughness: float = 0, is_emissive=False,
                 brightness: float = 0.5):
        if center.shape[0] != 3:
            Exception("Center of object is not 3-dimensional")
        elif albedo.shape[0] != 3:
            Exception("Albedo of object is not 3-dimensional")

        self.center = center
        self.roughness = roughness
        self.albedo = albedo / 255  # Dividing here so that we can perform rgb channel multiplication during ray tinting
        self.emissive = is_emissive
        self.brightness = brightness

    def get_ray_collision(self, ray_position: np.array, ray_unit_vector: np.array):
        pass


class SphereEntity(Entity):

    def __init__(self, center: np.array, radius: float, albedo: np.array, roughness: float = 0, is_emissive=False,
                 brightness: float = 0.5):
        super().__init__(center, albedo, roughness, is_emissive, brightness)

        self.radius = radius

    def get_ray_collision(self, ray_position: np.array, ray_unit_vector: np.array):
        if np.linalg.norm(self.center - ray_position) < self.radius:
            return True

        return False


class CubeEntity(Entity):

    def __init__(self, center: np.array, side_length: float, albedo: np.array, roughness: float = 0, is_emissive=False,
                 brightness: float = 0.5):
        super().__init__(center, albedo, roughness, is_emissive, brightness)

        self.side_length = side_length

    def get_ray_collision(self, ray_position: np.array, ray_unit_vector: np.array):
        center_offset = self.side_length / 2
        corner_1 = self.center + center_offset
        corner_2 = self.center - center_offset

        t1 = np.dot(corner_1 - ray_position, ray_unit_vector)
        t1 = t1 if t1 >= 0 else np.inf
        t2 = np.dot(corner_2 - ray_position, ray_unit_vector)
        t2 = t2 if t2 >= 0 else np.inf

        t = min(t1, t2)

        if t == np.inf:
            return False, None, t

        intersection_point = ray_position + t * ray_unit_vector

        # TODO may want to rewrite that part
        if corner_1[0] >= intersection_point[0] >= corner_2[0] and \
                corner_1[1] >= intersection_point[1] >= corner_2[1] and \
                corner_1[2] >= intersection_point[2] >= corner_2[2]:
            return True, intersection_point, t

        return False, None, np.inf


class Plane(Entity):

    def __init__(self, center: np.array, dimensions: np.array, normal_vector: np.array, albedo: np.array,
                 roughness: float = 0, is_emissive=False, brightness: float = 0.5):
        super().__init__(center, albedo, roughness, is_emissive, brightness)
        self.dimensions = dimensions
        self.normal_vector = normal_vector

    def get_ray_collision(self, ray_position: np.array, ray_unit_vector: np.array):
        center_offset = None
        corner_1 = self.center + center_offset
        corner_2 = self.center - center_offset

        t1 = np.dot(corner_1 - ray_position, ray_unit_vector)
        t1 = t1 if t1 >= 0 else np.inf
        t2 = np.dot(corner_2 - ray_position, ray_unit_vector)
        t2 = t2 if t2 >= 0 else np.inf

        t = min(t1, t2)

        if t == np.inf:
            return False, None

        intersection_point = ray_position + t * ray_unit_vector

        # TODO may want to rewrite that part
        if corner_1[0] >= intersection_point[0] >= \
                corner_2[0] and corner_1[1] >= intersection_point[1] >= corner_2[1] and corner_1[2] >= \
                intersection_point[
                    2] >= corner_2[2]:
            return True, intersection_point

        return False, None, t
