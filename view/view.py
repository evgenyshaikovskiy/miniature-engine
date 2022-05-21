from kivy.properties import ObjectProperty

from sys import exit

from kivymd.color_definitions import colors
from kivymd.uix.screen import MDScreen
from kivymd.uix.screen import Screen
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.button import MDFlatButton
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.stacklayout import MDStackLayout
from kivymd.uix.label import MDLabel

from view.popup import PopupWindow


class ViewComponent(MDScreen):
    controller = ObjectProperty()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.screen = Screen()
        self.stack_layout = MDStackLayout(orientation='lr-tb')

        self.car_label = MDLabel(
            text='',
            halign='center',
            theme_text_color='Primary'
        )

        default_size_hint = (.25, .1)
        self.start_engine_button = MDFlatButton(
            text='Start Engine',
            size_hint=default_size_hint,
            on_press=self.on_button_press,
        )
        self.stop_engine_button = MDFlatButton(
            text='Stop Engine',
            size_hint=default_size_hint,
            on_press=self.on_button_press,
        )
        self.run_idle_button = MDFlatButton(
            text='Run Idle',
            size_hint=default_size_hint,
            on_press=self.on_button_press,
        )
        self.free_wheel_button = MDFlatButton(
            text='Free Wheel',
            size_hint=default_size_hint,
            on_press=self.on_button_press,
        )
        self.brake_by_button = MDFlatButton(
            text='Brake by',
            size_hint=default_size_hint,
            on_press=self.on_button_press,
        )
        self.accelerate_by_button = MDFlatButton(
            text='Accelerate by',
            size_hint=default_size_hint,
            on_press=self.on_button_press,
        )
        self.refuel_car_button = MDFlatButton(
            text='Refuel Car',
            size_hint=default_size_hint,
            on_press=self.on_button_press,
        )
        self.exit_button = MDFillRoundFlatButton(
            text='Exit',
            size_hint=default_size_hint,
            md_bg_color=colors['Red']['A700'],
            on_press=self.on_button_press,
        )

        self.stack_layout.add_widget(self.start_engine_button)
        self.stack_layout.add_widget(self.stop_engine_button)
        self.stack_layout.add_widget(self.run_idle_button)
        self.stack_layout.add_widget(self.free_wheel_button)
        self.stack_layout.add_widget(self.brake_by_button)
        self.stack_layout.add_widget(self.accelerate_by_button)
        self.stack_layout.add_widget(self.refuel_car_button)
        self.stack_layout.add_widget(self.exit_button)

        self.screen.add_widget(self.car_label)

        self.screen.add_widget(self.stack_layout)

        # first update the label with startup car condition
        self.update_label()

    def build(self):
        return self.screen

    def update_label(self):
        self.car_label.text = self.controller.update_car_information()

    def on_button_press(self, button):
        button_text = button.text

        popup_title = None
        action = None

        match button_text:
            case 'Exit':
                exit()
            case 'Refuel Car':
                popup_title = 'Input amount of liters to refuel car.'
                action = 'refuel'
            case 'Accelerate by':
                popup_title = 'Input amount of km/h to accelerate by.'
                action = 'accelerate'
            case 'Brake by':
                popup_title = 'Input amount of km/h to brake by.'
                action = 'brake'
            case 'Free Wheel':
                action = 'free'
            case 'Run Idle':
                action = 'idle'
            case 'Stop Engine':
                action = 'stop'
            case 'Start Engine':
                action = 'start'

        if action and popup_title:
            self.controller.open_dialog(popup_title, action)
        else:
            self.controller.action_on_car(action)
            self.update_label()
