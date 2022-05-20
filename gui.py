from kivymd.app import MDApp

from kivy.core.window import Window

from controller.controller import ControllerComponent
from model.model import ModelComponent


def run_gui_interface(use_save, logger, snapshot_service, restore_service):
    CarGraphicApplication().run()


class CarGraphicApplication(MDApp):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.model = ModelComponent()
        self.controller = ControllerComponent(self.model)

        self.theme_cls.theme_style = 'Dark'

    def build(self):
        Window.size = (1280, 800)
        return self.controller.get_screen()
