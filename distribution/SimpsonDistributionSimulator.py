class SimpsonDistributionGenerator:

    def __init__(self, uniform_simulator):
        self.uniform_simulator = uniform_simulator

    def get_next(self):
        y = self.uniform_simulator.get_next()
        z = self.uniform_simulator.get_next()
        return y + z
