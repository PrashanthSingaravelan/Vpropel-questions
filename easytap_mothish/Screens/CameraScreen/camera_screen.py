from kivymd.uix.screen import MDScreen

class CameraScreen(MDScreen):
    def return_button(self):
        self.manager.current = 'home'

    def image_to_text_switch(self):
        self.manager.current = 'imaget'