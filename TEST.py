import time
import winsound

class SCRAMBLER:
    def __init__(self, message = None):
        self.message = str(message)
    def scramble(self):
        if self.message == None:
            print("No message ┗|｀O′|┛")
        else:
            alphabet = {" ": "  ","a": "._ ", "b": "_... ","c": "_._. ","d": "_.. ","e": ". ","f": ".._. ","g": "__. ","h": ".... ",
                    "i": ".. ","j": ".___ ","k": "_._ ","l": "._.. ","m": "__ ","n": "_. ","o": "___ ","p": ".__. ",
                        "q": "__._ ","r": "._. ","s": "... ","t": "_ ","u": ".._ ","v": "..._ ","w": ".__ ","x": "_.._ ","y": "_.__ ","z": "__.. "}

            translation = []
            sounds = []

            try: self.message.lower()
            except: pass

            for i in self.message:
                if i in alphabet:
                    sounds.append(alphabet[i])
                    translation.append(alphabet[i])
            print(' '.join(translation))

            msg = " ".join(sounds)
            for i in msg:
                time.sleep(0.3)
                if i == ".":
                    winsound.Beep(1200, 300)
                elif i == "_":
                    winsound.Beep(1200, 800)
                else:
                    pass
                

    def unscramble(self):
        morse = {" ": "", "._": "a", "_...": "b", "_._.": "c", "_..": "d", ".": "e", ".._.": "f", "__.": "g",
                 "....": "h",
                 "..": "i", ".___": "j", "_._": "k", "._..": "l", "__": "m", "_.": "n", "___": "o", ".__.": "p",
                 "__._": "q", "._.": "r", "...": "s", "_": "t", ".._": "u", "..._": "v", ".__": "w",
                 "_.._": "x", "_.__": "y", "__..": "z"}
        translation = ["Translation: "]
        
        try:
            text = self.message.split()
        except: pass

        for i in text:
            translation.append(morse[i])
        print(' '.join(translation))


running = True
while running:
    msg = input("Text: ")
    if msg == "stop":
        running = False
    try: SCRAMBLER(msg).unscramble()
    except: SCRAMBLER(msg).scramble()

