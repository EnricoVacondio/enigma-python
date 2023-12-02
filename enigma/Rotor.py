from typing import List


class Rotor:
    def __init__(self, name, encoding: str, rotor_position: int, notch_position: int, ring_setting: int):
        self.name = name
        self.forward_wiring = self.decode_wiring(encoding)
        self.backward_wiring = self.inverse_wiring(self.forward_wiring)
        self.rotorPosition = rotor_position
        self.notchPosition = notch_position
        self.ringSetting = ring_setting

    @staticmethod
    def decode_wiring(encoding: str) -> List[int]:
        char_wiring = [char for char in encoding]
        wiring = []
        for i in range(len(char_wiring)):
            wiring.append(ord(char_wiring[i]) - 65)
        return wiring

    @staticmethod
    def inverse_wiring(wiring: List[chr]) -> List[chr]:
        inverse = [0 for _ in range(26)]
        for idx, value in enumerate(wiring):
            forward = wiring[idx]
            inverse[forward] = idx
        return inverse

    @staticmethod
    def encipher(k: int, pos: int, ring: int, mapping: List[int]) -> int:
        shift = pos - ring
        return (mapping[(k + shift + 26) % 26] - shift + 26) % 26

    def forward(self, k: int) -> int:
        return self.encipher(k, self.rotorPosition, self.ringSetting, self.forward_wiring)

    def backward(self, k: int) -> int:
        return self.encipher(k, self.rotorPosition, self.ringSetting, self.backward_wiring)

    def is_at_notch(self) -> bool:
        if self.name == "VI" or self.name == "VII" or self.name == "VIII":
            return self.rotorPosition == 12 or self.rotorPosition == 25
        return self.rotorPosition == self.notchPosition

    def turnover(self) -> None:
        self.rotorPosition = (self.rotorPosition + 1) % 26

    @staticmethod
    def create(name, rotor_position, ring_setting):
        rotor_configs = {
            "I": ("EKMFLGDQVZNTOWYHXUSPAIBRCJ", 16),
            "II": ("AJDKSIRUXBLHWTMCQGZNPYFVOE", 4),
            "III": ("BDFHJLCPRTXVZNYEIWGAKMUSQO", 21),
            "IV": ("ESOVPZJAYQUIRHXLNFTGKDCMWB", 9),
            "V": ("VZBRGITYUPSDNHLXAWMJQOFECK", 25),
            "VI": ("JPGVOUMFYQBENHZRDKASXLICTW", 0),
            "VII": ("NZJHGRCXMYSWBOUFAIVLPEKQDT", 0),
            "VIII": ("FKQHTLXOCBJSPDZRAMEWNIUYGV", 0),
        }

        encoding, notch_position = rotor_configs.get(name, ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 0))
        return Rotor(name, encoding, rotor_position, notch_position, ring_setting)
