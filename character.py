import keyboard
import display
import morse
import printer


class App:

    def __init__(self):
        self.buffer = ""

    def key_down(self, key):
        print(key)

    def run(self):
        while True:
            keyboard.on_press(self.key_down)
            keyboard.wait()


App().run()
