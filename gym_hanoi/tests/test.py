import os
import unittest
import gym
import gym_hanoi


class Environment(unittest.TestCase):

    def test_hanoi_env_make(self):
        gym.make("Hanoi-v0")

    def test_hanoi_env_reset(self):
        env = gym.make("Hanoi-v0")
        env.reset()

    def test_hanoi_env_step(self):
        env = gym.make("Hanoi-v0")
        env.reset()
        state, reward, done, info = env.step(0)
        self.assertEqual(len(state), 4)
        self.assertEqual(env.env_noise, 0)

    def test_hanoi_env_make_noise(self):
        env = gym.make("Hanoi-v0")
        env.set_env_parameters(env_noise=0.5)
        self.assertEqual(env.env_noise, 0.5)

    def test_hanoi_env_make_disks(self):
        env = gym.make("Hanoi-v0")
        env.set_env_parameters(num_disks=7)
        env.reset()
        state, reward, done, info = env.step(0)
        self.assertEqual(len(7), 7)
        self.assertEqual(env.env_noise, 0)

    def test_hanoi_env_make_noise_and_disks(self):
        env = gym.make("Hanoi-v0")
        env.set_env_parameters(env_noise=0.3, num_disks=7)
        env.reset()
        state, reward, done, info = env.step(0)
        self.assertEqual(len(7), 7)
        self.assertEqual(env.env_noise, 0.3)


if __name__ == '__main__':
    unittest.main()
