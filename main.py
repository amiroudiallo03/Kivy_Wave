from kivymd.app import MDApp
from kivy.properties import ObjectProperty
from navigation_screen_manager import NavigationScreenManager


class MyScreenManager(NavigationScreenManager):
    pass

class MainApp(MDApp):
    manager = ObjectProperty(None)
    def build(self):
        self.manager = MyScreenManager()
        return self.manager
        


MainApp().run()