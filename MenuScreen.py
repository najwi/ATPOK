from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput
import datetime as dt
import re
from Chart import *
from Colors import *

time_buttons = []


# Buttons displaying crytpocurrencys names and time ranges
class MyButton(Button):
    def __init__(self, **kwargs):
        super(MyButton, self).__init__(**kwargs)
        self.pressed = False
        self.background_normal = ""
        self.background_color = COLOR_LIGHT_GREY
        self.background_down = ""


# Buttons displaying time ranges
class TimeButton(MyButton):
    def __init__(self, time=None, **kwargs):
        super(TimeButton, self).__init__(**kwargs)
        self.time = time


# Text input with filter for dates
class DateTextInput(TextInput):
    input_regex = re.compile(r"\d\d[.-/ ]\d\d[.-/ ]\d\d\d\d")

    def insert_text(self, substring, from_undo=False):
        s = ""
        if len(self.text) >= 10:
            if self.input_regex.fullmatch(self.text + substring):
                s = substring
            else:
                self.invalid_date()
        else:
            s = substring
        return super(DateTextInput, self).insert_text(s, from_undo=from_undo)

    def invalid_date(self):
        self.text = ""
        self.hint_text = "Niepoprawna data"
        self.hint_text_color = (0.9, 0, 0, 0.9)


# Root widget of the main window
class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        self.crypto_buttons = []
        fav = []

        try:
            # Read saved favourites
            with open("configs/fav_currencies.cfg") as f:
                for line in f:
                    fav = line[:-1].split(",")
        except FileNotFoundError:
            pass

        # Creating crytpo currencies buttons
        for c in fav:
            temp_button = MyButton(
                text=c,
                on_press=crypto_button_press,
                size_hint=(1, 0.05),
                size_hint_min_y=20
            )
            self.ids.layout_currency_buttons.add_widget(temp_button)
            self.crypto_buttons.append(temp_button)

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
        three_month_button.background_color = COLOR_ORANGE
        three_month_button.pressed = True
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
            text="Od początku",
            on_press=self.time_button_press,
        )
        self.ids.layout_time_buttons.add_widget(always_button)
        time_buttons.append(always_button)

        time_range_button = TimeButton(
            time="range",
            text="Wybrany przedział",
            on_press=self.time_button_press,
        )
        self.ids.layout_time_range.add_widget(time_range_button)
        time_buttons.append(time_range_button)

    @staticmethod
    # Time range buttons on press
    def time_button_press(instance):
        instance.background_color = COLOR_ORANGE
        instance.pressed = True
        for t in time_buttons:
            if t is not instance:
                t.pressed = False
                t.background_color = COLOR_LIGHT_GREY

    # Refresh button on press
    def refresh_button_press(self):
        Window.set_system_cursor("wait")
        self.refresh_chart()
        Window.set_system_cursor("arrow")

    # Resfresh chart image
    def refresh_chart(self):
        active_cryptos = []
        for b in self.crypto_buttons:
            if b.pressed:
                active_cryptos.append(b.text)

        end = None
        start = None
        for t in time_buttons:
            # Predefined ranges
            if t.pressed and type(t.time) == dt.timedelta:
                end = dt.datetime.today() - t.time
                start = dt.datetime.today()
            # Since beignning
            elif t.pressed and t.time is None:
                start = dt.datetime.today()
            # User dates range
            elif t.pressed and t.time == "range":
                end_split = self.ids.text_input_start_date.text
                start_split = self.ids.text_input_end_date.text
                end_split = re.split(r'\.|/|-| ', end_split)
                start_split = re.split(r'\.|/|-| ', start_split)

                try:
                    start = dt.datetime(int(start_split[2]), int(start_split[1]), int(start_split[0]))
                except ValueError and IndexError:
                    self.ids.text_input_start_date.invalid_date()
                    return

                try:
                    end = dt.datetime(int(end_split[2]), int(end_split[1]), int(end_split[0]))
                except ValueError and IndexError:
                    self.ids.text_input_end_date.invalid_date()
                    return

                if start < end:
                    self.ids.text_input_end_date.invalid_date()
                    self.ids.text_input_start_date.invalid_date()
                    return

        # What kind of chart will be generated
        showing = []
        for s in self.manager.get_screen('settings').showing:
            if s.children[0].active:
                showing.append(s.showing)

        # Checks for using log scale
        log_scale = self.manager.get_screen('settings').switch_log_scale.children[0].active

        # Gets chart and reload image
        if active_cryptos and showing:
            create_chart(active_cryptos, end, start, showing, log_scale)
            self.ids.image_chart.reload()

    # Refreshes currency buttons list
    def refresh_currency_buttons(self):
        self.ids.layout_currency_buttons.clear_widgets()
        self.crypto_buttons.clear()
        favourites = self.manager.get_screen('favourites')

        for s in favourites.switches:
            children = s.children
            if children[0].active:
                temp_button = MyButton(
                    text=children[1].text,
                    on_press=crypto_button_press,
                    size_hint=(1, 0.05),
                    size_hint_min_y=20
                )
                self.ids.layout_currency_buttons.add_widget(temp_button)
                self.crypto_buttons.append(temp_button)


# Cryptocrurrency button on press
def crypto_button_press(instance):
    if instance.pressed:
        instance.background_color = COLOR_LIGHT_GREY
        instance.pressed = False
    else:
        instance.background_color = COLOR_ORANGE
        instance.pressed = True
