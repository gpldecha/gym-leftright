import unittest

import gym
from gym_leftright.envs.leftright_env import LeftRightEnv
from time import sleep

class TestLeftRightEnv(unittest.TestCase):

    def test_env(self):

        env = LeftRightEnv()
        env.reset()
        for _ in range(50):

            #env.render()
            action = env.action_space.sample()
            observation, reward, done, info = env.step(action)

            self.assertTrue(observation >= 0)
            self.assertTrue(observation <= 10)

            sleep(0.05)

        return True


if __name__ == '__main__':
    unittest.main()
