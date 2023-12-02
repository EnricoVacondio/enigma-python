from typing import List


class Plugboard:
    def __init__(self, connections: str):
        print(connections)
        self.wiring = self.decode_plugboard(connections)

    def forward(self, k: int) -> int:
        return self.wiring[k]

    @staticmethod
    def identity() -> List[int]:
        return [i for i in range(26)]

    @staticmethod
    def decode_plugboard(connections: str):
        if len(connections) == 0:
            return Plugboard.identity()

        pairings = connections.split()
        plugged_characters = set()
        mapping = Plugboard.identity()

        for pair in pairings:
            if len(pair) != 2:
                raise ValueError("Invalid plugboard configuration")

            c1 = ord(pair[0]) - 65
            c2 = ord(pair[1]) - 65

            if c1 in plugged_characters or c2 in plugged_characters:
                return Plugboard.identity()

            plugged_characters.add(c2)
            plugged_characters.add(c1)

            mapping[c1] = c2
            mapping[c2] = c1

        return mapping

    @staticmethod
    def get_unplugged_character(plugboard: str):
        unplugged = set(range(26))

        if len(plugboard) == 0:
            return unplugged

        pairings = plugboard.split()

        for pair in pairings:
            c1 = ord(pair[0]) - 65
            c2 = ord(pair[1]) - 65

            unplugged.remove(c1)
            unplugged.remove(c2)

        return unplugged
