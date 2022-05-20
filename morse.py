class Encoder:
    MORSE_CODES = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}

    def __init__(self):
        pass

    def valid_character(self, letter):
        return letter is not None and letter.upper() in self.MORSE_CODES

    def lookup(self, letter):
        return self.MORSE_CODES[letter.upper()]

    def encode(self, message):
        encoded = ''
        for letter in message:
            if letter != ' ':
                # Looks up the dictionary and adds the
                # corresponding morse code
                # along with a space to separate
                # morse codes for different characters
                encoded += self.lookup(letter) + ' '
            else:
                # 1 space indicates different characters
                # and 2 indicates different words
                encoded += ' '

        return encoded
