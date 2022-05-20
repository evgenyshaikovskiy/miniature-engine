from exceptions.on_reserve_border_exception import OnReserveBorderException
from utility.config import config

from abstractions.logger import AbstractLogger
from abstractions.fuel_tank import AbstractFuelTank

from exceptions.fill_level_exception import FillLevelException
from exceptions.tank_size_exception import TankSizeException


class FuelTank(AbstractFuelTank):

    def __init__(self,
                 logger: AbstractLogger,
                 fill_level=config.get('fill_level'),
                 tank_size=config.get('tank_size'),
                 on_reserve_border=config.get('on_reserve_border')):

        if on_reserve_border < 0 or on_reserve_border > config.get('on_reserve_border'):
            raise OnReserveBorderException(on_reserve_border)

        if tank_size < config.get('min_tank_size') or tank_size > config.get('tank_size'):
            raise TankSizeException(tank_size)

        if fill_level < 0 or fill_level > tank_size:
            raise FillLevelException(fill_level)

        self.__on_reserve_border = on_reserve_border
        self.__logger = logger
        self.__fill_level = fill_level
        self.__tank_size = tank_size

    @property
    def fill_level(self) -> float:
        self.__logger.log("Access fill level in fuel tank class.")
        return self.__fill_level

    @property
    def is_on_reserve(self) -> bool:
        self.__logger.log("Calculating whether car on reverse in fuel tank.")
        return self.__fill_level < self.__get_on_reserve_border__

    @property
    def is_full(self) -> bool:
        self.__logger.log("Calculating whether fuel tank full in fuel tank.")
        return self.__fill_level == self.__get_tank_size__

    def consume(self, liters: float) -> None:
        self.__logger.log(f"Consuming {liters} liters in fuel tank class.")
        self.__fill_level -= liters
        self.__fill_level = round(self.__fill_level, 10)

        if self.__fill_level < 0:
            self.__fill_level = 0

    def refuel(self, liters: float) -> None:
        self.__logger.log(f"Refuel tank by {liters} liters in fuel tank.")
        self.__fill_level += liters

        if self.__fill_level > self.__get_tank_size__:
            self.__fill_level = self.__get_tank_size__

    @property
    def __get_tank_size__(self) -> float:
        return self.__tank_size

    @property
    def __get_on_reserve_border__(self) -> float:
        return self.__on_reserve_border
