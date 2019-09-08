class GeneratorAnalyzer:

    def __init__(self):
        self.sequence = []
        self.expected_value = 0
        self.dispersion = 0

    # def __calculate_expected_value(self, element, amount):
    #     self.expected_value += element / amount
    #
    # def __calculate_dispersion(self, element, amount):
    #     self.dispersion += ((element - self.expected_value) ** 2) / amount

    def get_expected_value(self, sequence):
        self.expected_value = 0
        sum_elements = 0
        for element in sequence:
            sum_elements += element
        self.expected_value = sum_elements / len(sequence)

    def get_dispersion(self, sequence):
        self.dispersion = 0
        for element in sequence:
            self.dispersion += (element - self.expected_value) ** 2
        self.dispersion = self.dispersion / len(sequence)

    def get_metrics(self, sequence):
        self.get_expected_value(sequence)
        self.get_dispersion(sequence)

    def __clear(self):
        self.sequence = []
        self.expected_value = 0
        self.dispersion = 0