import time
from effects import ted
from scener import scene_died, scene_roulette

def scene_scavenge():
    x = 0

    local_yes_choices = ted.yes_choices.copy()
    local_yes_choices.extend ([
        "trust", "fine", "i trust him", "go ahead", "ofc"
    ])
    
    local_no_choices = ted.no_choices.copy()
    local_no_choices.extend ([
        "decline", "reject", "no thanks", "walk away"
    ])

    local_third_choices = [
        "kill", "attack", "down"
    ]

    ted.typing_effect("\n\nYou limp away with a stick as a support for your destroyed legs.\n")
    time.sleep(0.3)
    ted.typing_effect("As you walk, you cross ways with an old man, big beard, ragged clothes, survival gear.\n")
    time.sleep(0.3)
    ted.typing_effect("You didnt really have time to run or hide, since you're hurt.\n")
    time.sleep(0.3)
    ted.typing_effect("The guy tells you theres a abandoned hospital 2 miles back, and offers to help.\n")
    time.sleep(0.3)
    print("\nDo you trust him?")
    print("Do you decline the offer?")
    print("KILL HIM AND GRAB HIS GEAR!?\n")

    while True:
        if x >= 1:
            print("You're very insecure, and have to rethink your decision...\n")

        valg = input().strip().lower()

        action = ted.interpret_choice(valg, local_yes_choices, local_no_choices, local_third_choices, ted.four_choices, ted.quit_choices)

        if action == "yes":
            ted.typing_effect("\nTurns out he was telling you the truth. You walk you can see the abandoned hospital.\n")
            time.sleep(0.3)
            ted.typing_effect("As you approach, you can see that it has been overtaken, and it looks like someone lives there..\n")
            time.sleep(0.3)
            ted.typing_effect("You express your thoughts aloud,\n\nand the guy responds in a deep voice:\n")
            time.sleep(0.6)
            ted.typing_effect('"I didnt tell you this, but I live here')
            ted.slow_typing_effect('..."\n')

            time.sleep(0.4)
            ted.typing_effect("\nYou answer with:\n")
            time.sleep(0.3)
            ted.typing_effect(""""oh... How come you didn't tell me that in the beginning?"\n""")
            
            time.sleep(0.3)
            print("\nHim:")
            time.sleep(0.6)
            ted.typing_effect('"I guess I just forgot..."\n')
            
            time.sleep(0.75)
            ted.typing_effect("\nYou shrug it off, and enter the hospital with him.\n")
            time.sleep(0.3)
            ted.typing_effect("he leads you in through corridors.\n")
            time.sleep(0.2)
            ted.typing_effect("the further in you go, the more concerned you get.\n")
            
            time.sleep(0.2)
            ted.typing_effect("\nYou ask him:\n")
            time.sleep(0.5)
            ted.typing_effect('"How far in are we going?"\n')
            
            time.sleep(0.3)
            ted.typing_effect("\nHe answers:\n")
            time.sleep(0.75)
            ted.typing_effect(""""Aahh, eh- i- it's just down here some place..."\n""")

            time.sleep(0.3)
            ted.typing_effect("\nYou get the creeps, and you start feeling uneasy about the situation..\n")
            time.sleep(0.2)
            ted.typing_effect("You subtly start looking for exits.\n")
            time.sleep(0.1)
            ted.typing_effect("He notices you're scared.\n")
            
            time.sleep(0.3)
            ted.faster_typing_effect("\nHe turns around in a quick motion!\n")
            time.sleep(0.2)
            ted.faster_typing_effect("BANG!\n")
            time.sleep(0.5)
            ted.typing_effect("He knocks you out.\n")

            scene_roulette()
        elif action == "no":
            # You walk away, and find supplies to recover.
            pass
        elif action == "third":
            # Imprisons you, you need to escape?
            pass
        elif action == "quit":
            exit_game = True
            break
        else:
            x += 1


