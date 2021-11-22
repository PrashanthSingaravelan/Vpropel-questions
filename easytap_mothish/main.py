import os

from kaki.app import App
from kivymd.app import MDApp
from kivy.factory import Factory

class EasyTap(App, MDApp):
    KV_FILES = [
        os.path.join(os.getcwd(), "Screens", "ManagerScreens", "manager_screens.kv"),
        os.path.join(os.getcwd(), "Screens", "LoginScreen", "login_screen.kv"),
        os.path.join(os.getcwd(), "Screens", "HomeScreen", "home_screen.kv"),
        os.path.join(os.getcwd(), "Screens", "HomeScreen", "Components", "cards.kv"),
        os.path.join(os.getcwd(), "Screens", "CameraScreen", "camera_screen.kv"),
        os.path.join(os.getcwd(), "Screens", "ImageToTextScreen", "image_to_text.kv"),
        os.path.join(os.getcwd(), "Screens", "PronounceScreen", "pronounce_text.kv"),
        os.path.join(os.getcwd(), "Screens", "TranslateScreen", "translate_text.kv"),
        os.path.join(os.getcwd(), "Screens", "ToolScreen", "tool_screen.kv")
    ]

    CLASSES = {
        'ManagerScreens'   : "Screens.ManagerScreens.manager_screens",
        'LoginScreen'      : "Screens.LoginScreen.login_screen",
        'HomeScreen'       : "Screens.HomeScreen.home_screen",
        'Cards'            : "Screens.HomeScreen.Components.cards",
        'CameraScreen'     : "Screens.CameraScreen.camera_screen",
        'ImagetoTextScreen': "Screens.ImagetoTextScreen.image_to_text",
        'TranslateScreen'  : "Screens.TranslateScreen.translate_text",
        'ToolScreen'       : "Screens.ToolScreen.tool_screen",
        'PronounceScreen'  : "Screens.PronounceScreen.pronounce_text",
    }
    
    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
    ]

    def build_app(self):
        self.theme_cls.primary_palette = "Brown"
        return Factory.ManagerScreens()

if __name__=='__main__':
    EasyTap().run()
