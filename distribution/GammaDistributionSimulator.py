import math


class GammaDistributionSimulator:

    def __init__(self, generator, lam, iterations):
        self.generator = generator
        self.lam = lam
        self.iterations = iterations

    def get_next(self):
        multiply = 1.0
        for i in range(self.iterations):
            multiply *= self.generator.get_next()

        return -1 * 1 / self.lam * math.log(multiply)

    def get_expected_value(self):
        return self.iterations * self.lam

    def get_dispersion(self):
        return self.iterations / (self.lam ** 2)
