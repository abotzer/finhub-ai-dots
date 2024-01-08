"""Random variables implelementations."""

from abc import abstractmethod, ABC

import numpy as np
from scipy import stats


class RandomVariable(ABC):
    """Random variable class."""
    @abstractmethod
    def sample(self):
        """Sample from the random variable."""


class BinomialRandomVariable(RandomVariable):
    """Binomial random variable class."""
    def __init__(self, n, p) -> None:
        self.n = n
        self.p = p
        self.variable = np.random.binomial
    
    def sample(self):
        return self.variable(self.n, self.p)


class PoissonRandomVariable(RandomVariable):
    """Poisson random variable class"""
    def __init__(self, lmbda) -> None:
        self.lmbda = lmbda
        self.variable = stats.poisson

    def sample(self):
        return self.variable(self.lmbda)


class GeometricRandomVariable(RandomVariable):
    """Geometric random variable class."""
    def __init__(self, p) -> None:
        super().__init__()
        self.p = p
        self.variable = stats.geom


class NegativeBinomialRandomVariable(RandomVariable):
    """Negative binomial random variable""" 
    def __init__(self, r, p) -> None:
        super().__init__()
        self.r = r
        self.p = p
        self.variable = stats.nbinom


class UniformRandomVariable(RandomVariable):
    """Continuous uniform random variable"""
    def __init__(self, a, b) -> None:
        super().__init__()
        self.a = a
        self.b = b
        self.variable = np.random.uniform


class ExponentialRandomVariable(RandomVariable):
    """Exponential random variable class."""
    def __init__(self, lmbda) -> None:
        super().__init__()
        self.lmbda = lmbda
        self.variable = stats.expon


class GammaRandomVariable(RandomVariable):
    """Gamma random variable class."""
    def __init__(self, alpha, beta) -> None:
        super().__init__()
        self.alpha = alpha
        self.beta = beta
        self.variable = stats.gamma


class NormalRandomVariable(RandomVariable):
    """Normal random variable class."""
    def __init__(self, mu, sigma) -> None:
        super().__init__()
        self.mu = mu
        self.sigma = sigma
        self.variable = stats.norm

