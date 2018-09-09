import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='Hanoi-v0',
    entry_point='gym_hanoi.envs:HanoiEnv',
)
