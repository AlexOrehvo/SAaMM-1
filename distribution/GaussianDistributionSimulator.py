import math


class GaussianDistributionSimulator:

    def __init__(self, generator,expected_value, deviation, iterations):
        self.generator = generator
        self.expected_value = expected_value
        self.deviation = deviation
        self.iterations = iterations

    def get_next(self):
        generated_sum = 0
        for i in range(self.iterations):
            generated_sum += self.generator.get_next()

        return self.expected_value + self.deviation * math.sqrt(12 / self.iterations) * (generated_sum - self.iterations / 2)

    def get_expected_value(self):
        return self.expected_value

    def get_dispersion(self):
        return self.deviation ** 2
