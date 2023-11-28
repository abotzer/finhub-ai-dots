"""Random variables implelementations."""


from typing import Dict


class RandomVariable:
    """Random variable class."""
    def __init__(self) -> None:
        pass


class DiscreteRandomVariable(RandomVariable):
    """Discrete random variable class."""
    def __init__(self, probabilities_dict: Dict) -> None:
        self.probabilities_dict = probabilities_dict
        self.values = list(probabilities_dict.keys())
        self.probabilities = list(probabilities_dict.values())
        assert sum(self.probabilities) == 1, "Probabilities must sum to 1."

    def get_probability(self, value):
        """Returns the probability of a value."""
        return self.probabilities_dict[value]


class NormalRandomVariable(RandomVariable):
    """Normal random variable class."""
    def __init__(self, mean: float, std: float) -> None:
        self.mean = mean
        self.std = std

    def get_mean(self):
        """Returns the mean."""
        return self.mean

    def get_std(self):
        """Returns the standard deviation."""
        return self.std


class UniformRandomVariable(RandomVariable):
    """Uniform random variable class."""
    def __init__(self, lower_bound: float, upper_bound: float) -> None:
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def get_lower_bound(self):
        """Returns the lower bound."""
        return self.lower_bound

    def get_upper_bound(self):
        """Returns the upper bound."""
        return self.upper_bound
