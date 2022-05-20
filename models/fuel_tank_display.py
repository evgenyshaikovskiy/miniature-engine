from abstractions.logger import AbstractLogger
from abstractions.fuel_tank_display import AbstractFuelTankDisplay
from abstractions.fuel_tank import AbstractFuelTank


class FuelTankDisplay(AbstractFuelTankDisplay):

    def __init__(self, fuelTank: AbstractFuelTank, logger: AbstractLogger):
        self.__fuel_tank = fuelTank
        self.__logger = logger

    @property
    def fill_level(self) -> float:
        self.__logger.log("Access fill level in fuel tank display.")
        return self.__get_fuel_tank__.fill_level

    @property
    def is_on_reserve(self) -> bool:
        self.__logger.log("Check whether car is on reverse in tank display.")
        return self.__get_fuel_tank__.is_on_reserve

    @property
    def is_full(self) -> bool:
        self.__logger.log("Check whether fuel tank is full in tank display.")
        return self.__get_fuel_tank__.is_full

    @property
    def __get_fuel_tank__(self) -> AbstractFuelTank:
        return self.__fuel_tank
