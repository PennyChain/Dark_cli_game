import time
from effects import ted
from scener.scene_roulette import scene_roulette
from scener.scene_more_walking import scene_more_walking
from scener.scene_imprisoned import scene_imprisoned

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

    time.sleep(1)
    ted.typing_effect("\n\nYou limp away with a stick as a support for your destroyed legs.\n")
    time.sleep(0.3)
    ted.typing_effect("As you walk, you cross ways with an old man. Big beard, ragged clothes, and survival gear.\n")
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
            ted.typing_effect("\nTurns out he was telling you the truth.\n")
            ted.typing_effect("While you walk you can see the abandoned hospital.\n")
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
            ted.typing_effect("You decline his offer and keep walking.\n")
            time.sleep(0.3)
            ted.typing_effect("He asks again with an slight aggressive tone while you were just about to walk away.\n")
            time.sleep(0.6)
            ted.typing_effect('\n"I- I can help you, you know that!?\n"')
            ted.typing_effect("\nYou respond in a nervous tone:\n")
            ted.typing_effect(""" "I- I- I'm good, thanks.."\n """)
            ted.typing_effect("\nYou really dodged a bullet there...\n")
            
            scene_more_walking()
        elif action == "third":
            ted.typing_effect("You take ur branch and swing at his face.\n")
            ted.typing_effect("Since you're badly hurt, he dodges it with ease.\n")
            ted.slow_typing_effect("\nWhat a mistake...\n")
            ted.typing_effect("\nHe takes out a revolver and points it at you.\n")
            ted.typing_effect("He goes behind you with the revolver pointing at the back of your head.")
            ted.typing_effect("Suddenly everything goes dark...\n")

            scene_imprisoned()
        elif action == "quit":
            exit_game = True
            break
        else:
            x += 1


