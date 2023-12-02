
class Reflector:
    def __init__(self, encoding: str):
        self.forward_wiring = self.decode_wiring(encoding)

    @staticmethod
    def decode_wiring(encoding: str):
        return [ord(char) - 65 for char in encoding]

    def forward(self, k: int):
        return self.forward_wiring[k]

    @staticmethod
    def create(name: str):
        if name == "B":
            return Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
        elif name == "C":
            return Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")
        else:
            return Reflector("ZYXWVUTSRQPONMLKJIHGFEDCBA")
