import matplotlib.pyplot as plt

from generator.GeneratorConfig import GeneratorConfig
from generator.Generator import Generator
from GeneratorAnalyzer import GeneratorAnalyzer
from tkinter import *
from tkinter import messagebox
from AppContext import AppContext


class MainApp:

    def __init__(self, master):
        self.master = master
        self.context = AppContext()
        self.a = StringVar()
        self.m = StringVar()
        self.n = StringVar()
        self.modulo = StringVar()
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
        gen_btn.grid(row=4, column=1)

        res_btn = Button(text="Show results", command=self.results_button)
        res_btn.grid(row=5, column=1)

        diagram_btn = Button(text="Show diagram", command=self.show_diagram)
        diagram_btn.grid(row=6, column=1)

    def results_button(self):
        self.analyzer.analyze(self.context.sequence)

        print(self.context.sequence)
        print(self.analyzer.expected_value)
        print(self.analyzer.dispersion)
        print(self.analyzer.period)
        print(self.analyzer.aperiodicity)
        # print(self.analyzer.indirect_verification(self.context.sequence))

    def show_diagram(self):
        self.histogram(self.context.sequence, 20, False, "123", "321")

    def histogram(data, n_bins, cumulative=False, x_label="", y_label="", title=""):
        _, ax = plt.subplots()
        ax.hist(data, n_bins=n_bins, cumulative=cumulative, color='#539caf')
        ax.set_ylabel(y_label)
        ax.set_xlabel(x_label)
        ax.set_title(title)

    def generate_button(self):
        try:
           self.__configure_generator(int(self.a.get()), int(self.m.get()), int(self.modulo.get()))
           self.__generate_sequence(int(self.n.get()))
        except ValueError:
            messagebox.showinfo("Error", "Value should be a number")

    def __generate_sequence(self, n):
        for i in range(n):
            self.context.sequence.append(self.generator.get_next())

    def __configure_generator(self, a, m, modulo):
        config = GeneratorConfig(a=a, m=m, start_modulo=modulo)
        self.generator.configure(config)



def start_app():
    root = Tk()
    app = MainApp(root)
    root.title("Option")
    root.geometry("400x300")
    root.mainloop()


start_app()


