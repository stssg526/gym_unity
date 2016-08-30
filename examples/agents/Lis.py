import gym
env = gym.make('Lis-v2')
for _ in range(1000):
    env.step(env.action_space.sample()) #take a random action
env.close()

