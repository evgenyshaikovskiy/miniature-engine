from utility.config import config

from abstractions.logger import AbstractLogger
from abstractions.vehicle import AbstractVehicle
from abstractions.fuel_tank import AbstractFuelTank
from abstractions.engine import AbstractEngine
from abstractions.fuel_tank_display import AbstractFuelTankDisplay
from abstractions.driving_display import AbstractDrivingDisplay
from abstractions.driving_processor import AbstractDrivingProcessor
from abstractions.observable import Observable
from abstractions.observer import Observer

from models.driving_display import DrivingDisplay
from models.driving_processor import DrivingProcessor
from models.fuel_tank import FuelTank
from models.fuel_tank_display import FuelTankDisplay
from models.engine import Engine


class Car(AbstractVehicle, Observable):
    def __init__(
        self,
        logger: AbstractLogger,
        fill_level=config.get('fill_level'),
        max_acceleration_ratio=config.get('max_acceleration_ratio'),
        tank_size=config.get('tank_size'),
        on_reserve_border=config.get('on_reserve_border'),
        acceleration_ratio=config.get('acceleration_ratio'),
        min_acceleration_ratio=config.get('min_acceleration_ratio'),
        max_speed=config.get('max_speed'),
        braking_speed=config.get('braking_speed')
    ):
        self.__logger: AbstractLogger = logger
        self.__observers = []

        self.__fuel_tank: AbstractFuelTank = FuelTank(
            self.__logger,
            fill_level,
            tank_size,
            on_reserve_border
        )

        self.__fuel_tank_display: AbstractFuelTankDisplay = FuelTankDisplay(
            self.__fuel_tank,
            self.__logger)

        self.__engine: AbstractEngine = Engine(self.__logger, self.__fuel_tank)

        self.__driving_processor: AbstractDrivingProcessor = DrivingProcessor(
            self.__engine,
            self.__logger,
            acceleration_ratio,
            max_acceleration_ratio,
            min_acceleration_ratio,
            max_speed,
            braking_speed
        )

        self.__driving_display: AbstractDrivingDisplay = DrivingDisplay(
            self.__driving_processor,
            self.__logger
        )

    @property
    def engine_is_running(self):
        self.__logger.log("Checks whether engine is running in car class.")
        return self.__get_engine__.is_running

    def engine_start(self) -> None:
        self.__logger.log("Starts an engine in car class.")
        if not self.__get_engine__.is_running and self.__get_fuel_tank__.fill_level > 0:
            self.__get_engine__.start()

        self.notify()

    def engine_stop(self) -> None:
        self.__logger.log("Stops an engine in car class.")
        if self.__get_engine__.is_running:
            self.__get_engine__.stop()

        self.notify()

    def running_idle(self) -> None:
        self.__logger.log("Running idle in car class.")
        self.__get_engine__.consume(config.get('running_idle_consumption_rate'))
        self.notify()

    def free_wheel(self) -> None:
        self.__logger.log("Free wheel in car class.")
        self.__get_driving_processor__.reduce_speed_by(1)
        self.notify()

    def brake_by(self, speed: float) -> None:
        self.__logger.log(f"Break by {speed} in car class.")
        self.__get_driving_processor__.reduce_speed_by(speed)
        self.notify()

    def accelerate(self, speed: float) -> None:
        self.__logger.log(f"Accelerate by {speed} in car class")
        self.__get_driving_processor__.increase_speed_to(speed)
        self.notify()

    def refuel(self, liters: float) -> None:
        self.__logger.log(f"Refuel by {liters} in car class")
        self.__get_fuel_tank__.refuel(liters)
        self.notify()

    def subscribe(self, observer: Observer) -> None:
        self.__observers.append(observer)

    def unsubscribe(self, observer: Observer) -> None:
        self.__observers.remove(observer)

    def notify(self) -> None:
        for item in self.__observers:
            item.handle(self, self.__logger)

    def get_report_on_car(self) -> None:
        self.__logger.disable_logging()

        if self.engine_is_running:
            print('For current moment car engine is running')
        else:
            print('For current moment car engine is not running')

        print(f'Actual speed is  {self.__get_driving_display__.actual_speed}')
        print(f'Actual consumption {self.__get_driving_display__.actual_consumption}')
        print(f'Actual fill level is {self.__get_fuel_tank_display__.fill_level}')

        self.__logger.enable_logging()

    # private properties for reflection
    @property
    def __get_engine__(self) -> AbstractEngine:
        return self.__engine

    @property
    def __get_fuel_tank__(self) -> AbstractFuelTank:
        return self.__fuel_tank

    @property
    def __get_fuel_tank_display__(self) -> AbstractFuelTankDisplay:
        return self.__fuel_tank_display

    @property
    def __get_driving_display__(self) -> AbstractDrivingDisplay:
        return self.__driving_display

    @property
    def __get_driving_processor__(self) -> AbstractDrivingProcessor:
        return self.__driving_processor
