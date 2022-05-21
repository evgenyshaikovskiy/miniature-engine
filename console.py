import click
from abstractions.vehicle import AbstractVehicle
from click_shell import shell


@shell(prompt='> ', intro='Launching CLI application...')
def app():
    pass


def run_cli_interface(model: AbstractVehicle):
    global car
    car = model
    app()


@app.command(help='Starts car engine.', name='start-engine')
def start_engine():
    car.engine_start()


@app.command(help='Stops car engine.', name='stop-engine')
def stop_engine():
    car.engine_stop()


@app.command(help='Runs car in free wheel mode.', name='free-wheel')
def free_wheel():
    car.free_wheel()


@app.command(help='Runs car in idle mode.', name='run-idle')
def run_idle():
    car.running_idle()


@app.command(help='Prints available information on car.', name='info')
def info():
    car.get_report_on_car()


@app.command(help='Refuels car by given amount of liters', name='refuel')
@click.argument('liters')
def refuel(liters):
    try:
        liters = float(liters)
    except ValueError:
        print('Error! Given amount of liters is not correct.')
        return

    car.refuel(liters)


@app.command(help='Accelerate car by given amount of km/h', name='accelerate')
@click.argument('speed')
def accelerate(speed):
    try:
        speed = int(speed)
    except ValueError:
        print('Error! Given speed accelerate to is not correct.')
        return

    car.accelerate(speed)

@app.command(help='Brake car by given amount of km/h', name='brake')
@click.argument('speed')
def brake(speed):
    try:
        speed = int(speed)
    except ValueError:
        print('Error! Given speed to brake by is not correct.')
        return

    car.brake_by(speed)
