from kivy.uix.screenmanager import Screen

from FavouritesScreen import SwitchLayout
from Colors import *


# Layout for settings switches
class SwitchLayoutShowing(SwitchLayout):
    def __init__(self, showing, text, color, **kwargs):
        super(SwitchLayoutShowing, self).__init__(text, color, **kwargs)
        self.showing = showing


# Settings screen layout
class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)
        self.showing = []
        settings = []

        try:
            with open("configs/settings.cfg") as f:
                for line in f:
                    settings = line.split(",")
        except FileNotFoundError:
            pass

        # Creating setting switches
        self.switch_show_close = SwitchLayoutShowing('Close', "Pokazuj cenę zamknięcia", COLOR_ORANGE)
        self.showing.append(self.switch_show_close)

        self.switch_show_open = SwitchLayoutShowing('Open', "Pokazuj cenę otwarcia", COLOR_VERY_LIGHT_GREY)
        self.showing.append(self.switch_show_open)

        self.switch_show_high = SwitchLayoutShowing('High', "Pokazuj nawyższą cenę", COLOR_ORANGE)
        self.showing.append(self.switch_show_high)

        self.switch_show_low = SwitchLayoutShowing('Low', "Pokazuj najniższą cenę", COLOR_VERY_LIGHT_GREY)
        self.showing.append(self.switch_show_low)

        self.switch_show_volume = SwitchLayoutShowing('Volume', "Pokazuj dzienny obrót", COLOR_ORANGE)
        self.showing.append(self.switch_show_volume)

        for s in self.showing:
            if s.showing in settings:
                s.children[0].active = True

        self.ids.layout_settings.add_widget(self.switch_show_close)
        self.ids.layout_settings.add_widget(self.switch_show_open)
        self.ids.layout_settings.add_widget(self.switch_show_high)
        self.ids.layout_settings.add_widget(self.switch_show_low)
        self.ids.layout_settings.add_widget(self.switch_show_volume)

        self.switch_log_scale = SwitchLayout("Używaj skali logarytmicznej", COLOR_VERY_LIGHT_GREY)
        if 'Log' in settings:
            self.switch_log_scale.children[0].active = True
        self.ids.layout_settings.add_widget(self.switch_log_scale)

    # Save settings
    def save_settings(self):
        with open("configs/settings.cfg", "w") as f:
            for s in self.showing:
                if s.children[0].active:
                    f.write(s.showing + ",")

            if self.switch_log_scale.children[0].active:
                f.write('Log')
