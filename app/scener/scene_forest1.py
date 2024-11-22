import time
import effects.ted as ted
from scener.scene_creature1 import scene_creature1


def scene_forest1():
    x = 0
    local_yes_choices = ted.yes_choices.copy()
    local_yes_choices.extend ([
        "on", "turn on", "switch on", "activate", "light", "turn the light on", 
        "flip on", "power on", "shine", "start", "begin", "open", "power up", 
        "illuminate", "brighten", "light up", "make it light", "trigger", 
        "turn it on", "flick on", "set on", "hit the switch", "turn the switch", 
        "set the light", "flick the switch", "turn it up", "turn on the flashlight", 
        "use the flashlight", "turn flashlight on", "flashlight on", "switch flashlight on", "I do"
    ])
    
    ted.typing_effect("It's getting darker the further in you go.\n")
    time.sleep(0.4)
    ted.typing_effect("Suddenly, everything goes quiet")
    ted.slower_typing_effect("...\n")
    time.sleep(0.2)
    ted.typing_effect("You remember you packed a small flashlight in your backpack.\n")
    time.sleep(0.3)
    ted.typing_effect("\nDo you turn it on..?\n")

    while True:
        if x >= 1:
            print("Do you turn it on?\n")
        
        valg2 = input().strip().lower()

        action = ted.interpret_choice(valg2, local_yes_choices, ted.no_choices, ted.third_choices, ted.quit_choices)

        if action == "yes":
            ted.typing_effect("\n\nWhy   did   you   do   that..?\n")
            time.sleep(1.3)
            scene_creature1()
        elif action == "no":
            ted.typing_effect("YOU\nHEAR\n")
            time.sleep(0.5)
            ted.typing_effect("STEPS...")
            break
        elif action == "quit":
            ted.typing_effect("You sit down to rest...\n")
            exit_game = True
            break
        else:
            ted.typing_effect("You're standing still wondering what to do...\n")
            x += 1
