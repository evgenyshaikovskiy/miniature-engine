import click


from abstractions.vehicle import AbstractVehicle
from models.car import Car
from utility.logger import Logger
from utility.restore import RestoreService
from utility.snapshot import SnapshotService
from console import run_cli_interface
from gui import run_gui_interface

Logger.setup()



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
@click.option(
    '--interface-type',
    default='GUI',
    type=click.Choice(['GUI', 'CLI'], case_sensitive=False),
    help="Sets type of interface that application will use. Possible parameters are GUI and CLI."
)
def main(use_save, disable_console, disable_file, interface_type):
    # setup logger and services
    logger = Logger(disable_console, disable_file)
    snapshot_service: SnapshotService = SnapshotService()
    restore_service: RestoreService = RestoreService()
    
    if interface_type.lower() == 'gui':
        run_gui_interface(use_save, logger, snapshot_service, restore_service)
    else:
        if use_save:
            run_cli_interface(restore_service.restore_car(logger), logger, restore_service, snapshot_service)
        else:
            run_cli_interface(None, logger, restore_service, snapshot_service)

if __name__ == '__main__':
    main
