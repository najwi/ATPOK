from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.switch import Switch
from kivy.graphics import Color, Rectangle

CURRENCIES = []

COLOR_ORANGE = (232 / 255, 159 / 255, 0, 1)
COLOR_LIGHT_GREY = (0.4, 0.4, 0.4, 1)


# Layout for label and switch
class SwitchLayout(GridLayout):
    def __init__(self, code, color, **kwargs):
        super(SwitchLayout, self).__init__(**kwargs)
        self.cols = 2
        label = Label(text=code, bold=True)
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


class FavouritesScreen(Screen):
    def __init__(self, **kwargs):
        super(FavouritesScreen, self).__init__(**kwargs)
        self.switches = []

        # Read currencies from file
        with open("configs/currencies.txt") as f:
            for line in f:
                CURRENCIES.append(line[:-1])

        orange = 0
        # Create switches
        for c in CURRENCIES:
            if orange < 3:
                sw = SwitchLayout(c, COLOR_ORANGE)
                self.ids.layout_switches.add_widget(sw)
                self.switches.append(sw)
                orange += 1
            else:
                sw = SwitchLayout(c, COLOR_LIGHT_GREY)
                self.ids.layout_switches.add_widget(sw)
                self.switches.append(sw)
                orange += 1
                if orange == 6:
                    orange = 0
