import matplotlib.pyplot as plt
import math

from generator.Generator import Generator
from generator.GeneratorConfig import GeneratorConfig
from analyzer.GeneratorAnalyzer import GeneratorAnalyzer
from analyzer.GeneratorResult import GeneratorResult
from tkinter import *
from tkinter import messagebox
from AppContext import AppContext


class MainApp:

    def __init__(self, master):
        self.master = master

        self.a = StringVar()
        self.m = StringVar()
        self.n = StringVar()
        self.modulo = StringVar()
        self.expected_value = StringVar()
        self.dispersion = StringVar()
        self.sigma = StringVar()
        self.indirect_sign = StringVar()
        self.period = StringVar()
        self.aperiodicity = StringVar()

        self.context = AppContext()
        self.generator = Generator()
        self.analyzer = GeneratorAnalyzer()
        self.init_components()

    def init_components(self):
        a_label = Label(text="a")
        m_label = Label(text="m")
        n_label = Label(text="n")
        modulo_default_label = Label(text="default modulo")

        a_label.grid(row=0, column=0, sticky="w")
        m_label.grid(row=1, column=0, sticky="w")
        n_label.grid(row=2, column=0, sticky="w")
        modulo_default_label.grid(row=3, column=0, sticky="w")

        a_entry = Entry(textvariable=self.a)
        m_entry = Entry(textvariable=self.m)
        n_entry = Entry(textvariable=self.n)
        modulo_default_entry = Entry(textvariable=self.modulo)

        a_entry.grid(row=0, column=1, padx=5, pady=5)
        m_entry.grid(row=1, column=1, padx=5, pady=5)
        n_entry.grid(row=2, column=1, padx=5, pady=5)
        modulo_default_entry.grid(row=3, column=1, padx=5, pady=5)

        gen_btn = Button(text="Generate", command=self.generate_button)
        gen_btn.grid(row=4, column=0)

        res_btn = Button(text="Show results", command=self.results_button)
        res_btn.grid(row=4, column=1)

        diagram_btn = Button(text="Show diagram", command=self.show_histogram)
        diagram_btn.grid(row=4, column=2)

        expected_value_label = Label(textvariable=self.expected_value)
        dispersion_label = Label(textvariable=self.dispersion)
        sigma_label = Label(textvariable=self.sigma)
        indirect_sign_label = Label(textvariable=self.indirect_sign)
        period_label = Label(textvariable=self.period)
        aperiodicity_label = Label(textvariable=self.aperiodicity)

        expected_value_label.grid(row=5, column=1, sticky="w")
        dispersion_label.grid(row=6, column=1, sticky="w")
        sigma_label.grid(row=7, column=1, sticky="w")
        indirect_sign_label.grid(row=8, column=1, sticky="w")
        period_label.grid(row=9, column=1, sticky="w")
        aperiodicity_label.grid(row=10, column=1, sticky="w")

    def results_button(self):
        result = self.analyzer.analyze(self.context.sequence)
        self.__show_results(result)

    def show_histogram(self):
        plt.hist(self.context.sequence, bins=20)
        plt.show()

    def generate_button(self):
        try:
            self.__configure_generator(int(self.a.get()), int(self.m.get()), int(self.modulo.get()))
            self.__generate_sequence(int(self.n.get()))
        except ValueError:
            messagebox.showinfo("Error", "Value should be a number")

    def __generate_sequence(self, n):
        self.context.sequence = []
        for i in range(n):
            self.context.sequence.append(self.generator.get_next())

    def __configure_generator(self, a, m, modulo):
        config = GeneratorConfig(a=a, m=m, start_modulo=modulo)
        self.generator.configure(config)

    def __show_results(self, result):
        self.expected_value.set("Мат. ожидание: " + str(result.expected_value))
        self.dispersion.set("Дисперсия: " + str(result.dispersion))
        self.sigma.set("Ср. кв. откнонение:" + str(math.sqrt(result.dispersion)))
        self.indirect_sign.set("Косвенный признак" + str(result.indirect_sign))
        self.period.set("Период: " + str(result.period))
        self.aperiodicity.set("Участок апериодичности: " + str(result.aperiodicity))


def start_app():
    root = Tk()
    app = MainApp(root)
    root.title("Option")
    root.geometry("350x300")
    root.mainloop()


start_app()
