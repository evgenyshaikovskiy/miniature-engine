from abstractions.vehicle import AbstractVehicle


def run_cli_interface(car: AbstractVehicle):
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
            elif action == 2:
                car.engine_stop()
            elif action == 3:
                car.running_idle()
            elif action == 4:
                car.free_wheel()
            elif action == 5:
                speed = float(input())
                car.brake_by(speed)
            elif action == 6:
                print('Input count of km/h to accelerate by')
                speed = float(input())
                car.accelerate(speed)
            elif action == 7:
                print('Input amount of liters to refuel')
                liters = float(input())
                car.refuel(liters)
            elif action == 8:
                car.get_report_on_car()
            elif action == 9:
                print('Stopping simulation...')
                break
    except Exception:
        print('Exception occurred.')
