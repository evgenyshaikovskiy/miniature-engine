from abstractions.driving_processor import AbstractDrivingProcessor
from abstractions.driving_display import AbstractDrivingDisplay
from abstractions.logger import AbstractLogger


class DrivingDisplay(AbstractDrivingDisplay):

    def __init__(self, driving_processor: AbstractDrivingProcessor,
                 logger: AbstractLogger):
        self.__driving_processor = driving_processor
        self.__logger = logger

    @property
    def actual_speed(self) -> float:
        self.__logger.log("Access actual car speed in driving display class.")
        return self.__get_driving_processor__.actual_speed

    @property
    def actual_consumption(self) -> float:
        self.__logger.log("Access actual consumption in driving display class")
        return self.__get_driving_processor__.last_consumption

    @property
    def __get_driving_processor__(self) -> AbstractDrivingProcessor:
        return self.__driving_processor
