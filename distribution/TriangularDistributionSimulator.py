import math

class TriangularDistributionSimulator:

    def __init__(self, generator, min, max):
        self.generator = generator
        self.min = min
        self.max = max

    def get_next(self):
        pair = [self.generator.get_next(), self.generator.get_next()]
        return self.min + (self.max - self.min) * min(pair)

    def get_expected_value(self):
        return (self.min + self.max) / 2

    def get_dispersion(self):
        return ((self.max - self.min) ** 2) / 12
