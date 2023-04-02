from env import *
from ray import *
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, ENV_DIM, PX_TO_M


def cube_collision_test():
    entity = CubeEntity(np.array([5, 5, 5]), 2, np.array([0.5, 0.5, 0.5]), 0.5, True, 0.5)

    ray = Ray(np.array([4, 5, 5]), np.array([1, 0, 0]))

    print(entity.get_ray_collision(ray.origin, ray.unit_vector))


def main():
    entity = CubeEntity(np.array([5, 5, 5]), 1, np.array([0.5, 0.5, 0.5]), 0.5, True, 0.5)
    entities = [entity]
    env = Env(ENV_DIM, entities, np.array([WINDOW_WIDTH, WINDOW_HEIGHT, 0]), np.array([4, 5, 5]),
              np.array([1, 0, 0]), px_to_m=PX_TO_M, nb_rays=1)

    env.render()


if __name__ == "__main__":
    main()
