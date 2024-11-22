import time
import random
import effects.ted as ted
from scener import scene_1

exit_game = False

# Spillstart
def main(exit_game):
    while not exit_game:
        velkommen = input("Play? (Yes/No)\n").strip().lower()
        if velkommen == "no":
            ted.typing_effect("Bye..")
            exit_game = True
        elif velkommen == "yes":
            result = scene_1()
            if result == "quit":
                exit_game = True
        else:
            ted.typing_effect("\nYou're standing still wondering what to do...\n")

if __name__ == "__main__":
    main(exit_game)