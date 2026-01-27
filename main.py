import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock

SERVER_URL = "https://Yujianye51.pythonanywhere.com"

class ClientApp(App):
    def build(self):
        self.label = Label(text="Client Idle")
        Clock.schedule_interval(self.check_command, 5)

        layout = BoxLayout()
        layout.add_widget(self.label)
        return layout

    def check_command(self, dt):
        try:
            r = requests.get(f"{SERVER_URL}/check_command", timeout=5)
            cmd = r.text.strip()
            if cmd != "NONE":
                self.label.text = f"CMD: {cmd}"
        except:
            self.label.text = "Server Error"

if __name__ == "__main__":
    ClientApp().run()