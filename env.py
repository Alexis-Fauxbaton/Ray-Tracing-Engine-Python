import numpy as np
from entity import *
from ray import *
import pygame


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

    def render(self):
        pygame.init()
        window = pygame.display.set_mode(self.camera_dim.shape)
        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            """
            Extremely ugly and suboptimal, but wanted to write quick code that would let me render a scene easily
            TODO Rewrite this
            """
            for i in range(self.camera_dim[0]):
                for j in range(self.camera_dim[1]):
                    for k in range(self.nb_rays):
                        ray = Ray()

        pygame.quit()
