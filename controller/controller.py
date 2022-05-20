from view.view import ViewComponent
from view.popup import PopupWindow


class ControllerComponent:
    def __init__(self, model):
        self.model = model
        self.view = ViewComponent(controller=self)
        self.dialog = None

    def get_screen(self):
        return self.view.build()

    def open_dialog(self, title, window_type):
        self.dialog = PopupWindow(
            controller=self,
            title=title,
            window_type=window_type,
        )

        self.dialog.open()

    def close_dialog(self, data):
        self.view.update_label()

        match self.dialog.window_type:
            case 'refuel-window':
                pass
            case 'accelerate-window':
                pass
            case 'brake-window':
                pass

        self.dialog = None
        print(data)

    def update_car_information(self):
        return 'yet empty'
