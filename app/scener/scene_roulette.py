import time
import random
from effects import ted

def scene_roulette():
    x = 0
        
    ted.typing_effect("")
    ted.typing_effect("")
    ted.typing_effect("")
    ted.typing_effect("")
    
    while True:
        if x >= 1:
            print("Do you xxxxxx?")

        valg = input().strip().lower()

        action = ted.interpret_choice(valg, ted.yes_choices, ted.no_choices, ted.third_choices, ted.four_choices, ted.quit_choices)

        if action == "yes":
            scene_
        elif action == "no":
            scene_
        elif action == "quit":
            ted.typing_effect("You sit down to rest...\n")
            exit_game = True
            break
        else:
            x += 1
            ted.typing_effect("\nYou're standing still wondering what to do...\n")


# scene_roulette(# You wake up with something over your head, and the breathing and worrying of another guy.
# The guy takes of both of the rags of your heads, theres a table in between you two.
# he lays down a revolver and a single bullet. He wants you two to play russian roulette, the winner wins his life back.
# If you dont play, he will torture you and kill you.(Her bruker du "random" biblioteket der det er en 1/6 sjangse for å dø for begge hver tur..))