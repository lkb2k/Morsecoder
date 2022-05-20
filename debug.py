from escpos.printer import Serial
import textwrap

class Printer:

    def __init__(self):
        self.p = Serial(devfile='/dev/serial0', baudrate=19200, bytesize=8, parity='N', stopbits=1, timeout=1.00, dsrdtr=True)
        self.p.set(
            width=2,
            height=2,
            smooth=True
        )

    def print(self, msg):
        for line in textwrap.wrap(msg, 16):
            self.p.text(line + "\n")
        self.p.cut()

Printer().print("1234 5678 9101 3193 49249 31919")


