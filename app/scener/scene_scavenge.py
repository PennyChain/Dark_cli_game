import time
from effects import ted

def scene_scavenge():
    x = 0

    local_third_choices = [
        "kill", "attack", "down"
    ]

    ted.typing_effect("You limp away with a stick as a support for your destroyed legs.\n")
    time.sleep(0.3)
    ted.typing_effect("As you walk you cross ways with an old man, big beard, ragged clothes, survival gear.\n")
    time.sleep(0.3)
    ted.typing_effect("You didnt really have time to run or hide, sice you're hurt.\n")
    time.sleep(0.3)
    ted.typing_effect("The guy tells you theres a abandoned hospital 2 miles back, and offers to help.\n")
    time.sleep(0.3)
    ted.typing_effect("\nDo you trust him?\n")
    time.sleep(0.3)
    ted.typing_effect("Do you decline the offer?\n")
    time.sleep(0.3)
    ted.faster_typing_effect("KILL HIM AND GRAB HIS GEAR!?\n")

    while True:
        if x >= 1:
            print("You're very insecure, and have to rethink your decision...")

        valg = input().strip().lower()

        action = ted.interpret_choice(valg, ted.yes_choices, ted.no_choices, local_third_choices, ted.quit_choices)

        if action == "yes":
            # It turns out he was truthfull and lead you to an abandoned hospital,
            # but he isn't a good guy, he knocks you out.
            # scene_roulette(# You wake up with something over your head, and the breathing and worrying of another guy.
            # The guy takes of both of the rags of your heads, theres a table in between you two.
            # he lays down a revolver and a single bullet. He wants you two to play russian roulette, the winner wins his life back.
            # If you dont play, he will torture you and kill you.(Her bruker du "random" biblioteket der det er en 1/6 sjangse for å dø for begge hver tur..))
            pass
        elif action == "no":
            # You walk away, and find supplies to recover.
            pass
        elif action == "third":
            # He kills you?
            pass
        elif action == "quit":

            break
        else:
            x += 1


