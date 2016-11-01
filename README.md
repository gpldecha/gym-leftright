# gym-leftright

Left or right control problem environment. An agent must either reach the left
or right boundary of a 1D world. See [Tree-Based Batch Mode Reinforcement Learning](http://www.jmlr.org/papers/volume6/ernst05a/ernst05a.pdf)
for a description of the problem. 

# Installation

```bash
pip install gym-leftright
```

# Quick example

```python
  
  import gym
  import gym_leftright
  
  env = gym.make('leftright-v0')
  env.reset()
  
  for _ in range(50):
    env.render()
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)
```
