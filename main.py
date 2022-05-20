import click
import asyncio

from abstractions.vehicle import AbstractVehicle
from utility.logger import Logger
from models.car import Car
from utility.restore import RestoreService
from utility.snapshot import SnapshotService


Logger.setup()
snapshot_service: SnapshotService = SnapshotService()
restore_service: RestoreService = RestoreService()


# setup CLI
@click.command()
@click.option(
    '--use-save',
    default=False,
    help="Set this parameter as 'True' to upload previous session, otherwise 'False'."
)
@click.option(
    '--disable-console',
    default=False,
    help="Set parameter as 'True' to disable console logging, otherwise 'False'."
)
@click.option(
    '--disable-file',
    default=False,
    help="Set this parameter as 'True' to disable file logging, otherwise 'False'."
)
def main(use_save, disable_console, disable_file):
    # setup logger parameters
    logger = Logger(disable_console, disable_file)

    if use_save:
        asyncio.run(run_car(restore_service.restore_car(logger), logger))
    else:
        asyncio.run(run_car(None, logger))


async def run_car(car: AbstractVehicle, logger):
    if car is None:
        car = Car(logger)
    else:
        car = restore_service.restore_car(logger)

    # start tracking new or already created car
    car.subscribe(snapshot_service)

    try:
        while (True):
            print('''Choose action:
                  1 - Start Engine.
                  2 - Stop Engine.
                  3 - Run Idle.
                  4 - Free Wheel.
                  5 - Brake by certain speed.
                  6 - Accelerate by certain speed.
                  7 - Refuel Car.
                  8 - Get information about car condition.
                  9 - To exit simulation.
                  ''')
            action: int = int(input())

            if action == 1:
                car.engine_start()
                await asyncio.sleep(0.5)
            elif action == 2:
                car.engine_stop()
                await asyncio.sleep(0.5)
            elif action == 3:
                car.running_idle()
                await asyncio.sleep(0.5)
            elif action == 4:
                car.free_wheel()
                await asyncio.sleep(0.5)
                print('Input count of km/h to brake by')
            elif action == 5:
                speed = float(input())
                car.brake_by(speed)
                await asyncio.sleep(0.5)
            elif action == 6:
                print('Input count of km/h to accelerate by')
                speed = float(input())
                car.accelerate(speed)
                await asyncio.sleep(0.5)
            elif action == 7:
                print('Input amount of liters to refuel')
                liters = float(input())
                car.refuel(liters)
                await asyncio.sleep(0.5)
            elif action == 8:
                car.get_report_on_car()
                await asyncio.sleep(0.5)
            elif action == 9:
                print('Stopping simulation...')
                car.unsubscribe(snapshot_service)
                break
    except Exception:
        print('Exception occurred.')


if __name__ == '__main__':
    main()
