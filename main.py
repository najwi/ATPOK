from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
import datetime as dt

from Chart import *

CURRENCIES = ["BTC", "ETH", "XRP", "DASH", "DOGE"]
COLOR_MY_BUTTON_CLICKED = (232 / 255, 159 / 255, 0, 1)
COLOR_MY_BUTTON_NOT_CLICKED = (0.4, 0.4, 0.4, 1)

crypto_buttons = []
time_buttons = []


# Buttons displaying crytpocurrencys names and time ranges
class MyButton(Button):
    def __init__(self, **kwargs):
        super(MyButton, self).__init__(**kwargs)
        self.pressed = False
        self.background_normal = ""
        self.background_color = COLOR_MY_BUTTON_NOT_CLICKED
        self.background_down = ""


class TimeButton(MyButton):
    def __init__(self, time: dt.timedelta, **kwargs):
        super(TimeButton, self).__init__(**kwargs)
        self.time = time


# Root widget of the main window
class RootWidget(FloatLayout):
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)

        # Default window size
        Window.size = (860, 600)

        # Creating crytpo currencies buttons
        for c in CURRENCIES:
            temp_button = MyButton(
                text=c,
                on_press=self.crypto_button_press,
                size_hint=(1, 0.05),
                size_hint_min_y=20
            )
            self.ids.layout_buttons.add_widget(temp_button)
            crypto_buttons.append(temp_button)

        # Creating time buttons
        week_button = TimeButton(
            time=dt.timedelta(days=7),
            text="1 tydzień",
            on_press=self.time_button_press,
        )
        self.ids.layout_time_buttons.add_widget(week_button)
        time_buttons.append(week_button)

        one_month_button = TimeButton(
            time=dt.timedelta(days=30),
            text="1 miesiąc",
            on_press=self.time_button_press,
        )
        self.ids.layout_time_buttons.add_widget(one_month_button)
        time_buttons.append(one_month_button)

        three_month_button = TimeButton(
            time=dt.timedelta(days=90),
            text="3 miesiące",
            on_press=self.time_button_press,
        )
        self.ids.layout_time_buttons.add_widget(three_month_button)
        time_buttons.append(three_month_button)

        one_year_button = TimeButton(
            time=dt.timedelta(days=365),
            text="1 rok",
            on_press=self.time_button_press,
        )
        self.ids.layout_time_buttons.add_widget(one_year_button)
        time_buttons.append(one_year_button)

        always_button = TimeButton(
            time=None,
            text="Od początku",
            on_press=self.time_button_press,
        )
        self.ids.layout_time_buttons.add_widget(always_button)
        time_buttons.append(always_button)

    @staticmethod
    def time_button_press(instance):
        instance.background_color = COLOR_MY_BUTTON_CLICKED
        instance.pressed = True
        for t in time_buttons:
            if t is not instance:
                t.pressed = False
                t.background_color = COLOR_MY_BUTTON_NOT_CLICKED

    @staticmethod
    def favourites_button_press(instance):
        print("fv")

    @staticmethod
    def options_button_press(instance):
        print("opt")

    # Resfresh chart image
    def refresh_chart(self):
        Window.set_system_cursor("wait")
        active_cryptos = []
        for b in crypto_buttons:
            if b.pressed:
                active_cryptos.append(b.text)

        end = None
        for t in time_buttons:
            if t.pressed and t.time:
                end = dt.datetime.today() - t.time

        if active_cryptos:
            Chart.create_chart(active_cryptos, end, dt.datetime.today())
            self.ids.image_chart.reload()
        Window.set_system_cursor("arrow")

    # Cryptocrurrency button on press
    @staticmethod
    def crypto_button_press(instance):
        if instance.pressed:
            instance.background_color = COLOR_MY_BUTTON_NOT_CLICKED
            instance.pressed = False
        else:
            instance.background_color = COLOR_MY_BUTTON_CLICKED
            instance.pressed = True


# Base App class
class AtpokApp(App):
    def build(self):
        Window.minimum_width = 500
        Window.minimum_height = 270
        return RootWidget()


if __name__ == '__main__':
    AtpokApp().run()
