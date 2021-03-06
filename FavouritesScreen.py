from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.switch import Switch
from kivy.graphics import Color, Rectangle
from Colors import *

currencies = []


# Layout for label and switch
class SwitchLayout(GridLayout):
    def __init__(self, text, color, bold=False, **kwargs):
        super(SwitchLayout, self).__init__(**kwargs)
        self.cols = 2
        label = Label(text=text, bold=bold)
        self.add_widget(label)
        self.add_widget(Switch())

        self.bind(size=self.update_rect, pos=self.update_rect)

        with self.canvas.before:
            Color(color[0], color[1], color[2], color[3])
            self.rect = Rectangle(size=self.size, pos=self.pos)

    @staticmethod
    def update_rect(instance, value):
        instance.rect.pos = instance.pos
        instance.rect.size = instance.size


# Favourites screen layout
class FavouritesScreen(Screen):
    def __init__(self, **kwargs):
        super(FavouritesScreen, self).__init__(**kwargs)
        self.switches = []
        fav = []

        try:
            # Read currencies from file
            with open("configs/currencies.cfg") as f:
                for line in f:
                    currencies.append(line[:-1])

            # Read fav currencies
            with open("configs/fav_currencies.cfg") as f:
                for line in f:
                    fav = line.split(",")
        except FileNotFoundError:
            pass

        orange = 0
        # Create switches
        for c in currencies:
            if orange < 3:
                sw = SwitchLayout(c, COLOR_ORANGE)
                if c in fav:
                    sw.children[0].active = True

                self.ids.layout_switches.add_widget(sw)
                self.switches.append(sw)

                orange += 1
            else:
                sw = SwitchLayout(c, COLOR_VERY_LIGHT_GREY)
                if c in fav:
                    sw.children[0].active = True

                self.ids.layout_switches.add_widget(sw)
                self.switches.append(sw)
                orange += 1
                if orange == 6:
                    orange = 0

    # Saving favourite currencies
    def save_settings(self):
        with open("configs/fav_currencies.cfg", "w") as f:
            for s in self.switches:
                if s.children[0].active:
                    f.write(s.children[1].text+",")
