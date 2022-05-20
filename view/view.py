from kivy.properties import ObjectProperty
from kivymd.color_definitions import colors
from kivymd.uix.screen import MDScreen
from kivymd.uix.screen import Screen
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.button import MDFlatButton
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.stacklayout import MDStackLayout


class ViewComponent(MDScreen):
    controller = ObjectProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.screen = Screen()
        self.stack_layout = MDStackLayout(orientation='lr-tb')

        default_size_hint = (.25, .1)
        self.start_engine_button = MDFlatButton(
            text='Start Engine',
            size_hint=default_size_hint,
        )
        self.stop_engine_button = MDFlatButton(
            text='Stop Engine',
            size_hint=default_size_hint,
        )
        self.run_idle_button = MDFlatButton(
            text='Run Idle',
            size_hint=default_size_hint
        )
        self.free_wheel_button = MDFlatButton(
            text='Free Wheel',
            size_hint=default_size_hint
        )
        self.brake_by_button = MDFlatButton(
            text='Brake by',
            size_hint=default_size_hint
        )
        self.accelerate_by_button = MDFlatButton(
            text='Accelerate by',
            size_hint=default_size_hint
        )
        self.refuel_car_button = MDFlatButton(
            text='Refuel Car',
            size_hint=default_size_hint
        )
        self.get_information_button = MDFlatButton(
            text='Get Information',
            size_hint=default_size_hint
        )
        self.exit_button = MDFillRoundFlatButton(
            text='Exit',
            size_hint=(1, 0.1),
            md_bg_color=colors['Red']['A700']
        )
        
        self.stack_layout.add_widget(self.start_engine_button)
        self.stack_layout.add_widget(self.stop_engine_button)
        self.stack_layout.add_widget(self.run_idle_button)
        self.stack_layout.add_widget(self.free_wheel_button)
        self.stack_layout.add_widget(self.brake_by_button)
        self.stack_layout.add_widget(self.accelerate_by_button)
        self.stack_layout.add_widget(self.refuel_car_button)
        self.stack_layout.add_widget(self.get_information_button)
        self.stack_layout.add_widget(self.exit_button)
        
        self.screen.add_widget(self.stack_layout)

        

    def build(self):
        return self.screen

    def on_controller_change(self, data):
        print(data)
