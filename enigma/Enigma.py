from typing import List

from enigma.Plugboard import Plugboard
from enigma.Reflector import Reflector
from enigma.Rotor import Rotor


class Enigma:
    def __init__(self, rotors: List[str], reflector: chr, rotor_position: List[int], ring_settings: List[int],  plugboard: str):
        if len(rotors) != 3:
            raise ValueError("Enigma requires at least 3 rotors")

        self.left_rotor = Rotor.create(rotors[0], rotor_position[0], ring_settings[0])
        self.middle_rotor = Rotor.create(rotors[1], rotor_position[1], ring_settings[1])
        self.right_rotor = Rotor.create(rotors[2], rotor_position[2], ring_settings[2])
        self.reflector = Reflector.create(reflector)
        self.plugboard = Plugboard(plugboard)

    def rotate(self):
        if self.middle_rotor.is_at_notch():
            self.middle_rotor.turnover()
            self.left_rotor.turnover()
        elif self.right_rotor.is_at_notch():
            self.middle_rotor.turnover()

        self.right_rotor.turnover()

    def encrypt_as_int(self, n: int) -> int:
        self.rotate()

        c = self.plugboard.forward(n)

        c1 = self.right_rotor.forward(c)
        c2 = self.middle_rotor.forward(c1)
        c3 = self.left_rotor.forward(c2)

        c4 = self.reflector.forward(c3)

        c5 = self.left_rotor.backward(c4)
        c6 = self.middle_rotor.backward(c5)
        c7 = self.right_rotor.backward(c6)

        c7 = self.plugboard.forward(c7)

        return c7

    def encrypt_char(self, c: chr) -> chr:
        return chr(self.encrypt_as_int(ord(c) - 65) + 65)

    def encrypt(self, s: str) -> str:
        return "".join([self.encrypt_char(c) for c in s])
