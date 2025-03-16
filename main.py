from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MyApp(BoxLayout):
    def on_button_click(self):
        user_input = self.ids.text_input.text
        self.ids.label.text = f"You entered: {user_input}"

class MainApp(App):
    def build(self):
        return MyApp()

if __name__ == "__main__":
    MainApp().run()
