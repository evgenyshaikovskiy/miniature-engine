from ast import Raise
from sys import maxsize
from exceptions.acceleration_ratio_exception import AccelerationRatioException
from exceptions.braking_speed_exception import BrakingSpeedException
from exceptions.max_acceleration_ratio_exception import MaxAccelerationRatioException
from exceptions.max_speed_exception import MaxSpeedException
from exceptions.min_acceleration_ratio_exception import MinAccelerationRatioException
from utility.config import config

from abstractions.logger import AbstractLogger
from abstractions.driving_processor import AbstractDrivingProcessor
from abstractions.engine import AbstractEngine


class DrivingProcessor(AbstractDrivingProcessor):
    def __init__(self,
                 engine: AbstractEngine,
                 logger: AbstractLogger,
                 acceleration_ratio=config.get('acceleration_ratio'),
                 max_acceleration_ratio=config.get('max_acceleration_ratio'),
                 min_acceleration_ratio=config.get('min_acceleration_ratio'),
                 max_speed=config.get('max_speed'),
                 braking_speed=config.get('braking_speed'),
                 ):

        if max_speed < config.get('min_speed') or max_speed > config.get('max_speed'):
            raise MaxSpeedException(max_speed)

        if braking_speed < config.get('min_braking_speed') or braking_speed > config.get('max_braking_speed'):
            raise BrakingSpeedException(braking_speed)

        if max_acceleration_ratio < config.get('min_max_acceleration_ratio') or max_acceleration_ratio > config.get('max_acceleration_ratio'):
            raise MaxAccelerationRatioException(max_acceleration_ratio)

        if min_acceleration_ratio < 0 or min_acceleration_ratio > config.get('min_acceleration_ratio'):
            raise MinAccelerationRatioException(min_acceleration_ratio)

        if acceleration_ratio < 0 or acceleration_ratio > config.get('acceleration_ratio'):
            raise AccelerationRatioException(acceleration_ratio)

        if acceleration_ratio < min_acceleration_ratio:
            acceleration_ratio = min_acceleration_ratio

        # optional?
        if acceleration_ratio > max_acceleration_ratio:
            acceleration_ratio = max_acceleration_ratio

        self.__max_speed: float = max_speed
        self.__braking_speed: float = braking_speed
        self.__actual_speed: float = 0

        # consumption on init is 0
        self.__last_consumption: float = 0

        self.__engine: AbstractEngine = engine
        self.__acceleration_ratio: float = acceleration_ratio
        self.__max_acceleration_ratio: float = max_acceleration_ratio
        self.__min_acceleration_ratio: float = min_acceleration_ratio
        self.__logger = logger

    @property
    def actual_speed(self) -> float:
        self.__logger.log("Access actual car speed in driving processor.")
        return self.__actual_speed

    @property
    def last_consumption(self) -> float:
        self.__logger.log("Access last consumption in driving processor.")
        return self.__last_consumption

    def calculate_consumption_rate(
        self,
        is_accelerating: bool = False,
        is_braking: bool = False
    ) -> float:
        current_speed = self.actual_speed
        consumption: float = 0

        self.__logger.log("Calculating consumption rate in driving processor.")

        if current_speed > 0:
            if current_speed < self.__get_car_maxspeed__ * 0.25:
                consumption = config.get('running_quater_consumption_rate')
            elif current_speed < self.__get_car_maxspeed__ * 0.5:
                consumption = config.get('running_half_consumption_rate')
            elif current_speed < self.__get_car_maxspeed__ * 0.75:
                consumption = config.get('running_upper_half_consumption_rate')
            elif current_speed < self.__get_car_maxspeed__:
                consumption = config.get('running_before_max_consumption_rate')
            elif current_speed == config.default_max_speed():
                consumption = config.get('running_max_speed_consumption_rate')
        else:
            consumption = 0

        if is_accelerating:
            consumption *= config.get('acceleration_coefficient')
        elif is_braking:
            consumption *= config.get('braking_coefficient')

        self.__last_consumption = consumption * config.get('car_coefficient')
        return self.__last_consumption

    def increase_speed_to(self, speed: float) -> None:
        self.__logger.log(f"Increasing speed by {speed} in driving processor.")
        if not self.__get_car_engine__.is_running:
            return

        if speed < self.__actual_speed:
            self.__actual_speed -= 1

        while self.__actual_speed < speed:
            self.__actual_speed = min(
                speed,
                self.__actual_speed + self.__get_car_acceleration_ratio__
            )

        if self.__actual_speed > self.__get_car_maxspeed__:
            self.__actual_speed = self.__get_car_maxspeed__

        self.__get_car_engine__.consume(self.calculate_consumption_rate(True))

    def reduce_speed_by(self, reduce_by: float) -> None:
        self.__logger.log(f"Reducing speed by {reduce_by} km/h in driving pro.")
        if not self.__get_car_engine__.is_running:
            return

        self.__actual_speed -= min(reduce_by, self.__get_car_braking_speed__)

        if self.__actual_speed < 0:
            self.__actual_speed = 0

        self.__get_car_engine__.consume(
            self.calculate_consumption_rate(False, True),
        )

    @property
    def __get_car_engine__(self) -> AbstractEngine:
        return self.__engine

    @property
    def __get_car_maxspeed__(self) -> float:
        return self.__max_speed

    @property
    def __get_car_braking_speed__(self) -> float:
        return self.__braking_speed

    @property
    def __get_car_acceleration_ratio__(self) -> float:
        return self.__acceleration_ratio

    @property
    def __get_car_max_acceleration_ratio__(self) -> float:
        return self.__max_acceleration_ratio

    @property
    def __get_car_min_acceleration_ratio__(self) -> float:
        return self.__min_acceleration_ratio
