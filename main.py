from enigma.Enigma import Enigma
from enigma.Rotor import Rotor


def main():
    machine = Enigma(["VII", "V", "IV"], "B", [10, 5, 12], [1, 2, 3], "AD FT WH JO PN")

    encrypted = machine.encrypt("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    print(encrypted)
    assert encrypted == "UJFZBOKXBAQSGCLDNUTSNTASEF"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
