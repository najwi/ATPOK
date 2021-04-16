from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

CURRENCIES = ["BTC", "ETH", "XRP", "DASH", "DOGE"]
COLOR_CURR_BUTTON_CLICKED = (232 / 255, 159 / 255, 0, 1)
COLOR_CURR_BUTTON_NOT_CLICKED = (130 / 255, 130 / 255, 130 / 255, 1)


class MyButton(Button):

    def __init__(self, **kwargs):
        super(MyButton, self).__init__(**kwargs)
        self.pressed = False


class RootWidget(FloatLayout):

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)

        for b in CURRENCIES:
            self.ids.layout_buttons.add_widget(MyButton(
                text=b,
                background_normal="",
                background_color=COLOR_CURR_BUTTON_NOT_CLICKED,
                background_down="",
                on_press=currency_button_press,
                size_hint=(1, 0.05)
            ))

    def favourites_button_press(self, instance):
        print("fv")

    def options_button_press(self, instance):
        print("opt")


def currency_button_press(instance):
    if instance.pressed:
        instance.background_color = COLOR_CURR_BUTTON_NOT_CLICKED
        instance.pressed = False
    else:
        instance.background_color = COLOR_CURR_BUTTON_CLICKED
        instance.pressed = True


class AtpokApp(App):

    def build(self):
        return RootWidget()


if __name__ == '__main__':
    AtpokApp().run()
