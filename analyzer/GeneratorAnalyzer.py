from analyzer.GeneratorResult import GeneratorResult


class GeneratorAnalyzer:

    def __init__(self):
        self.result = GeneratorResult()

    def analyze(self, sequence):
        self.result.clear()
        if len(sequence) != 0:
            self.result.expected_value = self.__get_expected_value(sequence)
            self.result.dispersion = self.__get_dispersion(sequence, self.result.expected_value)
            self.result.indirect_sign = self.__indirect_verification(sequence)
            self.result.period = self.__get_period(sequence)
            self.result.aperiodicity = self.__get_aperiodicity(sequence, self.result.period)
        return self.result

    def __get_expected_value(self, sequence):
        sum_elements = 0
        for element in sequence:
            sum_elements += element
        return sum_elements / len(sequence)

    def __get_dispersion(self, sequence, exp_val):
        dispersion = 0
        for element in sequence:
            dispersion += (element - exp_val) ** 2
        return dispersion / len(sequence)

    def __indirect_verification(self, sequence):
        valid_pair_amount = 0
        for i in range(len(sequence) // 2):
            if sequence[i*2] ** 2 + sequence[i*2+1] ** 2 < 1:
                valid_pair_amount += 1
        return 2 * valid_pair_amount / len(sequence)

    def __get_period(self, sequence):
        i = len(sequence) - 1
        last_element = sequence[i]
        i -= 1
        while (i > 0) and (last_element != sequence[i]):
            i -= 1
        if i == 0:
            return None
        else:
            return len(sequence) - i - 1

    def __get_aperiodicity(self, sequence, period):
        if period is None:
            return None
        else:
            aperiodicity = 0
            for i in range(len(sequence) - period):
                if sequence[i] == sequence[i + period]:
                    aperiodicity = i
                    break
            return aperiodicity + period
