# -*- coding: utf-8 -*-
"""
@author: Guillaume de Chambrier

    An addaptation of the “Left or Right” control problem, see "Tree-Based Batch Mode Reinforcement Learning"

"""

import math
import gym
from gym import spaces
from gym.utils import seeding
import numpy as np


class LeftRightEnv(gym.Env):

    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'video.frames_per_second': 30
    }

    def __init__(self):
        self.max_speed = 2
        self.left_boundary = 0
        self.right_boundary = 10

        self.viewer = None

        self.action_space = spaces.Discrete(2)
        self.observation_space = spaces.Box(low=self.left_boundary, high=self.right_boundary,shape=(1,))

        self._seed()
        self.reset()

    def _seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def _step(self, action):
        assert self.action_space.contains(action), "%r (%s) invalid" % (action, type(action))

        position = self.state
        if action == 0:
            velocity = -self.max_speed
        else:
            velocity = self.max_speed
        position += velocity

        position = np.clip(position, self.left_boundary, self.right_boundary)
        if (position==self.left_boundary and velocity<0): velocity = 0
        if (position==self.right_boundary and velocity>0): velocity = 0

        if bool(position >= self.right_boundary):
            reward = 100
            done   = True
        elif bool(position <= self.left_boundary):
            reward = 50
            done   = True
        else:
            reward = 0
            done   = False

        self.state = position
        return np.array(self.state), reward, done, {}

    def _reset(self):
        self.state = self.np_random.uniform(low=2, high=8)
        return np.array(self.state)

    def _height(self, xs):
        return np.sin(3 * xs)*.45+.55

    def _render(self, mode='human', close=False):
        if close:
            if self.viewer is not None:
                self.viewer.close()
                self.viewer = None
            return

        screen_width = 600
        screen_height = 400

        add_edge = 0.2 * (self.right_boundary - self.left_boundary)
        world_width = (self.right_boundary - self.left_boundary)  + add_edge
        scale = screen_width/world_width
        shift = (add_edge/2.0) * scale

        # Agent properties
        agent_pos = self.state
        agent_radius = 10


        if self.viewer is None:
            from gym.envs.classic_control import rendering
            self.viewer = rendering.Viewer(screen_width, screen_height)

            flagx = (self.right_boundary-self.left_boundary)*scale
            flagpole = rendering.Line((shift, screen_height/2.0), (flagx+shift, screen_height/2.0))
            self.viewer.add_geom(flagpole)

            self.cartrans = rendering.Transform()

            agent = rendering.make_circle(agent_radius)
            agent.add_attr(rendering.Transform(translation=(agent_pos + shift, screen_height/2.0)))
            agent.set_color(.0, .0, 1)
            agent.add_attr(self.cartrans)
            self.viewer.add_geom(agent)

        self.cartrans.set_translation((agent_pos-self.left_boundary)*scale, 0)

        return self.viewer.render(return_rgb_array = mode=='rgb_array')
