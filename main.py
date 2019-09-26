import matplotlib.pyplot as plt
import math

from generator.GeneratorConfig import GeneratorConfig
from generator.Generator import Generator
from distribution.UniformDistributionSimulator import UniformDistributionSimulator
from distribution.GaussianDistributionSimulator import GaussianDistributionSimulator
from distribution.ExponentialDistributionSimulator import ExponentialDistributionSimulator
from distribution.GammaDistributionSimulator import GammaDistributionSimulator
from distribution.TriangularDistributionSimulator import TriangularDistributionSimulator
from distribution.SimpsonDistributionSimulator import SimpsonDistributionGenerator
from tkinter import *
from tkinter import messagebox
from AppContext import AppContext


class MainApp:

    def __init__(self, master):
        self.master = master

        self.min = StringVar()
        self.max = StringVar()
        self.n = StringVar()
        self.expected_value_entry = StringVar()
        self.deviation_entry = StringVar()
        self.lam = StringVar()
        self.mu = StringVar()
        self.expected_value_res = StringVar()
        self.dispersion = StringVar()
        self.sigma = StringVar()
        self.indirect_sign = StringVar()
        self.period = StringVar()
        self.aperiodicity = StringVar()
        self.iterations = StringVar()
        self.default_dropdown_value = StringVar(master)
        self.default_dropdown_value.set("Равномерное")

        self.context = AppContext()
        self.distribution_simulator = None
        self.generator = None
        self.init_components()
        self.__configure_generator(a=1233211, m=167, modulo=123776654)

    def init_components(self):
        min_label = Label(text="a")
        max_label = Label(text="b")
        n_label = Label(text="n")
        distribution_label = Label(text="Распределение")
        expected_value_label = Label(text="Мат. ожидание")
        deviation_label = Label(text="Ср. кв. отклонение")
        lam_label = Label(text="Лямбда")
        iterations_label = Label(text="Итерации")

        min_label.grid(row=0, column=0, sticky="w")
        max_label.grid(row=1, column=0, sticky="w")
        n_label.grid(row=2, column=0, sticky="w")
        expected_value_label.grid(row=3, column=0, sticky="w")
        deviation_label.grid(row=4, column=0, sticky="w")
        lam_label.grid(row=5, column=0, sticky="w")
        iterations_label.grid(row=6, column=0, sticky="w")
        distribution_label.grid(row=7, column=0, sticky="w")

        min_entry = Entry(textvariable=self.min)
        max_entry = Entry(textvariable=self.max)
        n_entry = Entry(textvariable=self.n)
        expected_value_entry = Entry(textvariable=self.expected_value_entry)
        deviation_entry = Entry(textvariable=self.deviation_entry)
        lam_entry = Entry(textvariable=self.lam)
        iterations_entry = Entry(textvariable=self.iterations)

        generator_dropdown = OptionMenu(self.master, self.default_dropdown_value,
                                        "Равномерное", "Гауссово", "Экспоненциальное", "Гамма", "Треугольное", "Симпсона")

        min_entry.grid(row=0, column=1, padx=5, pady=5)
        max_entry.grid(row=1, column=1, padx=5, pady=5)
        n_entry.grid(row=2, column=1, padx=5, pady=5)
        expected_value_entry.grid(row=3, column=1, padx=5, pady=5)
        deviation_entry.grid(row=4, column=1, padx=5, pady=5)
        lam_entry.grid(row=5, column=1, padx=5, pady=5)
        iterations_entry.grid(row=6, column=1, padx=5, pady=5)
        generator_dropdown.grid(row=7, column=1, padx=5, pady=5)

        gen_btn = Button(text="Generate", command=self.generate_button)
        gen_btn.grid(row=9, column=0)

        diagram_btn = Button(text="Show diagram", command=self.show_histogram)
        diagram_btn.grid(row=10, column=1)

        expected_value_label = Label(textvariable=self.expected_value_res)
        dispersion_label = Label(textvariable=self.dispersion)
        sigma_label = Label(textvariable=self.sigma)
        indirect_sign_label = Label(textvariable=self.indirect_sign)
        period_label = Label(textvariable=self.period)
        aperiodicity_label = Label(textvariable=self.aperiodicity)

        expected_value_label.grid(row=6, column=1, sticky="w")
        dispersion_label.grid(row=7, column=1, sticky="w")
        sigma_label.grid(row=8, column=1, sticky="w")
        indirect_sign_label.grid(row=9, column=1, sticky="w")
        period_label.grid(row=10, column=1, sticky="w")
        aperiodicity_label.grid(row=11, column=1, sticky="w")

    def results_button(self):
        result = self.analyzer.analyze(self.context.sequence)
        self.__show_results(result)

    def show_histogram(self):
        plt.hist(self.context.sequence, bins=20)
        plt.show()

    def generate_button(self):
        self.distribution_simulator = self.__define_simulator()
        self.__generate_sequence(int(self.n.get()))

    def __generate_sequence(self, n):
        self.context.sequence = []
        for i in range(n):
            self.context.sequence.append(self.distribution_simulator.get_next())

    def __configure_generator(self, a, m, modulo):
        config = GeneratorConfig(a=a, m=m, start_modulo=modulo)
        self.generator = Generator()
        self.generator.configure(config)

    def __show_results(self, result):
        self.expected_value_res.set("Мат. ожидание: " + str(result.expected_value))
        self.dispersion.set("Дисперсия: " + str(result.dispersion))
        self.sigma.set("Ср. кв. откнонение:" + str(math.sqrt(result.dispersion)))
        self.indirect_sign.set("Косвенный признак" + str(result.indirect_sign))
        self.period.set("Период: " + str(result.period))
        self.aperiodicity.set("Участок апериодичности: " + str(result.aperiodicity))

    def __define_simulator(self):
        try:
            # self.__configure_generator(int(self.a.get()), int(self.m.get()), int(self.modulo.get()))
            if self.default_dropdown_value.get() == 'Равномерное':
                return UniformDistributionSimulator(self.generator, int(self.min.get()), int(self.max.get()))
            if self.default_dropdown_value.get() == 'Гауссово':
                return GaussianDistributionSimulator(self.generator, float(self.expected_value_entry.get()),
                                                     float(self.deviation_entry.get()),  int(self.iterations.get()))
            if self.default_dropdown_value.get() == 'Экспоненциальное':
                return ExponentialDistributionSimulator(self.generator, float(self.lam.get()))
            if self.default_dropdown_value.get() == 'Гамма':
                return GammaDistributionSimulator(self.generator, float(self.lam.get()), int(self.iterations.get()))
            if self.default_dropdown_value.get() == 'Треугольное':
                return TriangularDistributionSimulator(self.generator, int(self.min.get()), int(self.max.get()))
            if self.default_dropdown_value.get() == 'Симпсона':
                return SimpsonDistributionGenerator(UniformDistributionSimulator(self.generator, float(self.min.get()),
                                                                                 float(self.max.get())))
        except ValueError:
            messagebox.showinfo("Error", "Value should be a number")

def start_app():
    root = Tk()
    app = MainApp(root)
    root.title("Option")
    root.geometry("350x300")
    root.mainloop()


start_app()
