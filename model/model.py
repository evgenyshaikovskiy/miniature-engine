from abstractions.vehicle import AbstractVehicle


class ModelComponent():

    def __init__(self, car: AbstractVehicle):
        self.car = car
