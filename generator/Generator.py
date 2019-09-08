class Generator:
    __config = None
    __current_modulo = None

    def get_next(self):
        modulo = (self.__config.a * self.__current_modulo) % self.__config.m
        self.__current_modulo = modulo
        return modulo / self.__config.m

    def configure(self, config):
        self.__config = config
        self.__current_modulo = config.start_modulo
