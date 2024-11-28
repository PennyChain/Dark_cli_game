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

    ted.typing_effect("\nYou limp away with a stick as a support for your destroyed legs.\n")
    time.sleep(0.3)
    ted.typing_effect("As you walk, you cross ways with an old man, big beard, ragged clothes, survival gear.\n")
    time.sleep(0.3)
    ted.typing_effect("You didnt really have time to run or hide, since you're hurt.\n")
    time.sleep(0.3)
    ted.typing_effect("The guy tells you theres a abandoned hospital 2 miles back, and offers to help.\n")
    time.sleep(0.3)
    ted.typing_effect("\nDo you trust him?\n")
    ted.typing_effect("Do you decline the offer?\n")
    ted.faster_typing_effect("KILL HIM AND GRAB HIS GEAR!?\n\n")

    while True:
        if x >= 1:
            print("You're very insecure, and have to rethink your decision...\n")

        valg = input().strip().lower()

        action = ted.interpret_choice(valg, local_yes_choices, local_no_choices, local_third_choices, ted.four_choices, ted.quit_choices)

        if action == "yes":
            ted.typing_effect("\nTurns out he was telling you the truth, and as you walk you can see the abandoned hospital.\n")
            ted.typing_effect("As you approach, you can see that it has been overtaken, and it looks like someone lives there..\n")
            ted.typing_effect("You express your thoughts aloud,\n\nand the guy responds:\n")
            ted.typing_effect('"I didnt tell you this, but I live here..."\n')
            
            ted.typing_effect("\nYou answer with:\n")
            ted.typing_effect(""""oh... How come you didn't tell me that in the beginning?"\n""")
            
            print("\nHim:")
            ted.typing_effect('"I guess I just forgot..."\n')
            
            ted.typing_effect("\nYou shrug it off, and enter the hospital with him.\n")
            ted.typing_effect("he leads you in through corridors.\n")
            ted.typing_effect("the further in you go, the more concerned you get.\n")
            
            ted.typing_effect("\nYou ask him:\n")
            ted.typing_effect('"How far in are we going?"\n')
            
            ted.typing_effect("He answers:")
            ted.typing_effect(""""Aahh, eh- i- it's just down here some place..."\n""")

            ted.typing_effect("\nYou get the creeps, and you start feeling uneasy about the situation..\n")
            ted.typing_effect("You subtly start looking for exits.\n")
            ted.typing_effect("He notices you're scared.\n")
            
            ted.faster_typing_effect("He turns around in a quick motion!\n")
            ted.faster_typing_effect("BANG!\n")
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


