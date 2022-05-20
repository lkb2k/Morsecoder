import keyboard
import display
import morse
import printer


class App:

    def __init__(self):
        self.buffer = ""
        self.encoder = morse.Encoder()
        self.display = display.Display()
        self.printer = printer.Printer()

    # Translate supported unicode characters
    def sanitize(self, letter):
        if letter == u'\u2212':
            return '-'
        return letter

    def key_down(self, key):
        letter = self.sanitize(key.name)
        if key.name == '/' and keyboard.is_pressed('shift'):
            letter = '?'
        if key.name == 'space':
            self.append(' ')
        if key.name == 'backspace':
            self.backspace()
        if key.name == 'enter':
            self.send()
        if self.encoder.valid_character(letter):
            self.append(letter)

    def append(self, letter):
        self.buffer = self.buffer + letter
        self.stdout()

    def backspace(self):
        self.buffer = self.buffer[:-1]
        self.stdout()

    def send(self):
        self.printer.print(self.encoder.encode(self.buffer))
        print(self.buffer)
        print(self.encoder.encode(self.buffer))
        self.clear()

    def clear(self):
        self.buffer = ""
        self.stdout()

    def stdout(self):
        self.display.update(self.buffer)

    def run(self):
        while True:
            keyboard.on_press(self.key_down)
            keyboard.wait()


App().run()
