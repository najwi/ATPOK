from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, SlideTransition

from MenuScreen import MenuScreen
from FavouritesScreen import FavouritesScreen
from SettingsScreen import SettingsScreen


# Base App class
class AtpokApp(App):
    def build(self):
        # Default window size
        Window.size = (1100, 650)
        # Minimum window size
        Window.minimum_width = 500
        Window.minimum_height = 270
        # Create screen manager
        sm = ScreenManager(transition=SlideTransition())
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(FavouritesScreen(name='favourites'))
        sm.add_widget(SettingsScreen(name='settings'))
        return sm


if __name__ == '__main__':
    AtpokApp().run()
