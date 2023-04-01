from env import *

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

if __name__ == "__main__":
    entity = SphereEntity(np.array([5, 5, 5]), 0.1, np.array([0.5, 0.5, 0.5]), 0.5, True, 0.5)
    entities = [entity]
    env = Env(np.array([10, 10, 10]), entities, np.array([WINDOW_WIDTH, WINDOW_HEIGHT]), np.array([4, 5, 5], np.array([1, 0, 0])))