"""
# python 实现 HMM模型
"""
import os
import logging
import numpy as np
from functools import partial

logger = logging.getLogger(__name__)


class HMM(object):
    def __init__(self, state_size, observation_size, max_iteration=2000, epsilon=1e-8):
        """
        :param state_size: 状态序列长度
        :param observation_size: 观测序列长度
        :param max_iteration: 迭代次数
        :param epsilon: 修正项
        """
        self.state_size = state_size
        self.observation_size = observation_size
        self.max_iteration = max_iteration
        self.epsilon = epsilon

    def fit(self, X):
        """
        :param X: no label training data
        :return:
        """
        pass

    @classmethod
    def baum_welch(cls, X, state_size, observation_size, max_iteration, epsilon=1e-8):
        """
        HMM use baum-welch for training
        """
        pass

    @classmethod
    def forward(cls, state2state, state2observation, initial_state, observation):
        """前向算法"""
        pass

    @classmethod
    def backward(cls, state2state, state2observation, initial_state, observation):
        """后向算法"""
        pass
