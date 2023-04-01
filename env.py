import numpy as np
from entity import *
from ray import *
import pygame
import sys

X = np.array([1, 0, 0])
Y = np.array([0, 1, 0])
Z = np.array([0, 0, 1])

class Env:

    def __init__(self, dimension: np.array, entities: list[Entity], camera_dim: np.array, camera_pos: np.array,
                 camera_orientation: np.array, nb_rays: int = 100, fov=114, px_to_m=0.01, font=np.array([0, 0, 0])):
        if camera_pos.shape[0] != 3:
            Exception("Camera position is not 3-dimensional")
        elif camera_orientation.shape[0] != 2:
            Exception("Camera orientation vector is not 2-dimensional")
        elif dimension.shape[0] != 3:
            Exception("Environment dimension is not 3-dimensional")
        elif camera_dim.shape[0] != 2:
            Exception("Camera dimension is not 2-dimensional")
        elif not isinstance(fov, int):
            Exception("fov should be an integer")

        self.dimension = dimension
        self.entities = entities
        self.camera_pos = camera_pos
        self.camera_orientation = camera_orientation
        self.camera_dim = camera_dim
        self.nb_rays = nb_rays
        self.fov = fov % 360
        self.px_to_m = px_to_m
        self.font_color = font
        self.camera_x = np.array([1, 0, 0])
        self.camera_y = np.array([0, 1, 0])
        self.camera_z = np.array([0, 0, 1])

    def render(self):
        pygame.init()
        print(self.camera_dim)
        window = pygame.display.set_mode(self.camera_dim)
        camera_center_px = self.camera_dim / 2
        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # calculate the angle difference between the scene origin and the camera
            theta = np.arccos(np.dot(Z, self.camera_orientation) / (np.linalg.norm(self.camera_orientation) * np.linalg.norm(Z)))
            psi = np.arccos(np.dot(X, self.camera_orientation) / (np.linalg.norm(self.camera_orientation) * np.linalg.norm(X)))

            print(theta, psi)

            cos_t = np.cos(-theta)
            sin_t = np.sin(theta)

            Rz = np.array([[cos_t, 0, sin_t], [0, 1, 0], [-sin_t, 0, cos_t]])

            cos_p = np.cos(psi)
            sin_p = np.sin(psi)

            Ry = np.array([[cos_p, -sin_p, 0], [sin_p, cos_p, 0], [0, 0, 1]])

            R = np.dot(Rz, Ry)
            R_1 = np.linalg.inv(R) # TODO change this so that we multiply instead by the rotation matrices with the reversed angles from above to save computation time

            self.camera_x = np.dot(R, X)
            self.camera_y = np.dot(R, Y)
            self.camera_z = np.dot(R, Z)

            print(self.camera_x, self.camera_y, self.camera_z)

            sys.exit()

            """
            Extremely ugly and suboptimal, but wanted to write quick code that would let me render a scene easily
            TODO Rewrite this
            """
            for i in range(self.camera_dim[0]):
                for j in range(self.camera_dim[1]):
                    ray_position_px = np.array([i, j, 0])
                    delta_px = camera_center_px - ray_position_px
                    delta_px[1] = -1 * delta_px[1] # Here we change the sign of the y coordinate since it is tipically reversed in the window
                    delta_m = delta_px * self.px_to_m
                    delta_m = np.dot(R_1, delta_m)
                    ray_origin = self.center - delta_m
                    ray_unit_vector = np.dot(R_1, self.camera_z)
                    for k in range(self.nb_rays):
                        ray = Ray(ray_origin, ray_unit_vector)

            pygame.display.flip()

        pygame.quit()
