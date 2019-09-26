import math


class ExponentialDistributionSimulator:

    def __init__(self, generator, lam):
        self.generator = generator
        self.lam = lam

    def get_next(self):
        return -1 * 1 / self.lam * math.log(self.generator.get_next())

    def get_expected_value(self):
        return 1 / self.lam

    def get_dispersion(self):
        return 1 / (self.lam ** 2)
