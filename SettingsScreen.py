from kivy.uix.screenmanager import Screen

from FavouritesScreen import SwitchLayout
from Colors import *


class SwitchLayoutShowing(SwitchLayout):
    def __init__(self, showing, text, color, **kwargs):
        super(SwitchLayoutShowing, self).__init__(text, color, **kwargs)
        self.showing = showing


# Settings screen layout
class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)
        self.showing = []
        self.switch_save_settings = SwitchLayout("Zapisuj ustawienia", COLOR_LIGHT_GREY)

        self.switch_show_close = SwitchLayoutShowing('Close', "Pokazuj cenę zamknięcia", COLOR_ORANGE)
        self.showing.append(self.switch_show_close)

        self.switch_show_open = SwitchLayoutShowing('Open', "Pokazuj cenę otwarcia", COLOR_LIGHT_GREY)
        self.showing.append(self.switch_show_open)

        self.switch_show_high = SwitchLayoutShowing('High', "Pokazuj nawyższą cenę", COLOR_ORANGE)
        self.showing.append(self.switch_show_high)

        self.switch_show_low = SwitchLayoutShowing('Low', "Pokazuj najniższą cenę", COLOR_LIGHT_GREY)
        self.showing.append(self.switch_show_low)

        self.switch_show_volume = SwitchLayoutShowing('Volume', "Pokazuj dzienny obrót", COLOR_ORANGE)
        self.showing.append(self.switch_show_volume)

        self.ids.layout_settings.add_widget(self.switch_save_settings)
        self.ids.layout_settings.add_widget(self.switch_show_close)
        self.ids.layout_settings.add_widget(self.switch_show_open)
        self.ids.layout_settings.add_widget(self.switch_show_high)
        self.ids.layout_settings.add_widget(self.switch_show_low)
        self.ids.layout_settings.add_widget(self.switch_show_volume)

        self.switch_log_scale = SwitchLayout("Używaj skali logarytmicznej", COLOR_LIGHT_GREY)
        self.ids.layout_settings.add_widget(self.switch_log_scale)
