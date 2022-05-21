from abstractions.driving_display import AbstractDrivingDisplay
from abstractions.fuel_tank import AbstractFuelTank
from abstractions.logger import AbstractLogger
from abstractions.vehicle import AbstractVehicle
from abstractions.engine import AbstractEngine


class ModelComponent():

    def __init__(self, car: AbstractVehicle, logger: AbstractLogger):
        self.car: AbstractVehicle = car
        self.logger: AbstractLogger = logger
        self.engine: AbstractEngine = car.__getattribute__('__get_engine__')
        self.fuel_tank: AbstractFuelTank = car.__getattribute__('__get_fuel_tank__')
        self.driving_display: AbstractDrivingDisplay = car.__getattribute__('__get_driving_display__')

        # const param during program execution
        # add it just to explain on reserve and is full car concepts
        self.tank_size = self.fuel_tank.__getattribute__('__get_tank_size__')

    def refuel(self, liters):
        self.car.refuel(liters)

    def accelerate(self, speed):
        self.car.accelerate(speed)

    def brake_by(self, speed):
        self.car.brake_by(speed)

    def start_engine(self):
        self.car.engine_start()

    def stop_engine(self):
        self.car.engine_stop()

    def running_idle(self):
        self.car.running_idle()

    def free_wheel(self):
        self.car.free_wheel()

    def update_car_information(self) -> str:
        self.logger.disable_logging()
        current_data: str = 'Engine is'
        if self.engine.is_running:
            current_data += ' running.\n'
        else:
            current_data += ' not running.\n'

        current_data += f'Fill level is {self.fuel_tank.fill_level} liters.\n'
        current_data += f'Tank size is {self.tank_size} liters.\n'

        current_data += 'So car`s fuel tank is'
        if self.fuel_tank.is_full:
            current_data += ' full.\n'
        else:
            current_data += ' not full.\n'

        current_data += 'And so car is'
        if self.fuel_tank.is_on_reserve:
            current_data += ' not on reserve fuel mode.\n'
        else:
            current_data += ' on reserve fuel fuel mode.\n'

        current_data += f'Car actual speed is {self.driving_display.actual_speed} km/h.\n'
        current_data += f'Car actual consumption rate is {self.driving_display.actual_consumption} liters/per tick.'

        self.logger.enable_logging()
        return current_data
