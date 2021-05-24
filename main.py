from kivy import Config
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, SlideTransition

from MenuScreen import MenuScreen
from FavouritesScreen import FavouritesScreen
from SettingsScreen import SettingsScreen


# Base App class
class AtpokApp(App):
    def build(self):
        self.icon = "images/icon.png"
        # Default window size
        Window.size = (1100, 650)
        # Minimum window size
        Window.minimum_width = 500
        Window.minimum_height = 270
        # Create screen manager
        self.sm = ScreenManager(transition=SlideTransition())
        self.sm.add_widget(MenuScreen(name='menu'))
        self.sm.add_widget(FavouritesScreen(name='favourites'))
        self.sm.add_widget(SettingsScreen(name='settings'))
        return self.sm

    # Saves settings on app close
    def on_stop(self):
        self.sm.get_screen('settings').save_settings()
        self.sm.get_screen('favourites').save_settings()


if __name__ == '__main__':
    Config.set('kivy', 'default_font', ['Segoe UI', 'fonts/segoeuib.ttf', 'fonts/segoeui.ttf'])
    Config.write()
    AtpokApp().run()
