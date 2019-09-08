import matplotlib.pyplot as plt

from generator.GeneratorConfig import GeneratorConfig
from generator.Generator import Generator
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

        gen_btn = Button(text="Show results", command=self.results_button)
        gen_btn.grid(row=5, column=1)

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

    def results_button(self):
        print(self.context.sequence)


def start_app():
    root = Tk()
    app = MainApp(root)
    root.title("Option")
    root.geometry("400x300")
    root.mainloop()


start_app()


