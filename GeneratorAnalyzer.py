class GeneratorAnalyzer:

    def __init__(self):
        self.sequence = []
        self.expected_value = 0
        self.dispersion = 0
        self.period = 0
        self.aperiodicity = 0

    def analyze(self, sequence):
        self.__calculate_expected_value(sequence)
        self.__calculate_dispersion(sequence)
        self.__calculate_period(sequence)
        self.__calculate_aperiodicity(sequence)

    def __calculate_expected_value(self, sequence):
        self.expected_value = 0
        sum_elements = 0
        for element in sequence:
            sum_elements += element
        self.expected_value = sum_elements / len(sequence)

    def __calculate_dispersion(self, sequence):
        self.dispersion = 0
        for element in sequence:
            self.dispersion += (element - self.expected_value) ** 2
        self.dispersion = self.dispersion / len(sequence)

    def indirect_verification(self, sequence):
        i = 0
        valid_pair_amount = 0
        while i < len(sequence) - 1:
            if (sequence[i] ** 2 + sequence[i+1] ** 2) < 1:
                valid_pair_amount += 1
        return 2 * valid_pair_amount / len(sequence)

    def __calculate_period(self, sequence):
        i = len(sequence) - 1
        last_element = sequence[i]
        i -= 1
        while (i > 0) and (last_element != sequence[i]):
            i -= 1
        self.period = len(sequence) - i - 1

    def __calculate_aperiodicity(self, sequence):
        for i in range(len(sequence) - self.period):
            if sequence[i] == sequence[i + self.period]:
                self.aperiodicity = i
                break
        self.aperiodicity += self.period
