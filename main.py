from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

CURRENCIES = ["BTC", "ETH", "XRP", "DASH", "DOGE"]
BUTTON_COLOR_CLICKED = (232 / 255, 159 / 255, 0, 1)
BUTTON_COLOR_NOT_CLICKED = (130 / 255, 130 / 255, 130 / 255, 1)


class MyButton(Button):

    def __init__(self, **kwargs):
        super(MyButton, self).__init__(**kwargs)
        self.pressed = False


class RootWidget(FloatLayout):

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)

        for b in CURRENCIES:
            self.ids.buttons_grid.add_widget(MyButton(
                text=b,
                background_normal="",
                background_color=BUTTON_COLOR_NOT_CLICKED,
                background_down="",
                on_press=currency_button_press,
                size_hint_max_y=50
            ))


def currency_button_press(instance):
    if instance.pressed:
        instance.background_color = BUTTON_COLOR_NOT_CLICKED
        instance.pressed = False
    else:
        instance.background_color = BUTTON_COLOR_CLICKED
        instance.pressed = True


class AtpokApp(App):

    def build(self):
        return RootWidget()


if __name__ == '__main__':
    AtpokApp().run()
