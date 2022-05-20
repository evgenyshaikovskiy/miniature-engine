from abstractions.logger import AbstractLogger
from abstractions.engine import AbstractEngine
from abstractions.fuel_tank import AbstractFuelTank


class Engine(AbstractEngine):

    def __init__(self, logger: AbstractLogger, fuel_tank: AbstractFuelTank):
        self.__fuel_tank: AbstractFuelTank = fuel_tank
        self.__is_running: bool = False
        self.__logger = logger

    @property
    def is_running(self) -> bool:
        self.__logger.log("Check whether car is running in engine class.")
        return self.__is_running

    def start(self) -> None:
        self.__logger.log("Start car engine in engine class.")
        self.__is_running = True

    def stop(self) -> None:
        self.__logger.log("Stop car engine in engine class.")
        self.__is_running = False

    def consume(self, liters: float) -> None:
        self.__logger.log(f"Consume {liters} liters in engine class.")
        if self.__is_running:
            self.__get_fuel_tank__.consume(liters)

            if self.__get_fuel_tank__.fill_level == 0:
                self.stop()

    @property
    def __get_fuel_tank__(self) -> AbstractFuelTank:
        return self.__fuel_tank
