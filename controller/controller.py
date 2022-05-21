from view.view import ViewComponent
from view.popup import PopupWindow
from kivymd.uix.snackbar import Snackbar


class ControllerComponent:
    def __init__(self, model):
        self.model = model
        self.view = ViewComponent(controller=self)
        self.dialog = None

    def get_screen(self):
        return self.view.build()

    def open_dialog(self, title, action):
        self.dialog = PopupWindow(
            controller=self,
            title=title,
            action=action,
        )

        self.dialog.open()

    def close_dialog(self, data):
        converted_data = None
        try:
            converted_data = float(data)
            self.action_on_car(self.dialog.action, converted_data)
        except ValueError:
            Snackbar(text='Error! Invalid data given.').open()

        self.dialog = None
        self.view.update_label()

    def action_on_car(self, action, additional_data=None):
        match action:
            case 'refuel':
                self.model.refuel(additional_data)
            case 'accelerate':
                self.model.accelerate(additional_data)
            case 'brake':
                self.model.brake_by(additional_data)
            case 'start':
                self.model.start_engine()
            case 'stop':
                self.model.stop_engine()
            case 'idle':
                self.model.running_idle()
            case 'free':
                self.model.free_wheel()

    def update_car_information(self):
        return self.model.update_car_information()
