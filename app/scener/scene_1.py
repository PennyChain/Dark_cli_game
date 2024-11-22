import time
import effects.ted as ted
from scener.scene_forest1 import scene_forest1
from scener.scene_bridge1 import scene_bridge1



# Første valg/scene
def scene_1():
    x = 0

    ted.typing_effect("\nYou've been walking on a new path.\n")
    ted.typing_effect("After a while you come to a crossection.\n")
    ted.typing_effect("There's a sign there, pointing into the forest.\n")
    time.sleep(0.8)
    ted.typing_effect("\nDo you choose to follow the sign?\n")
    
    while True:
        if x >= 1:
            print("Do you follow the sign?\n")

        valg1 = input().strip().lower()
        
        action = ted.interpret_choice(valg1, ted.yes_choices, ted.no_choices, ted.third_choices, ted.quit_choices)

        if action == "yes":
            ted.typing_effect("\n\nYou enter the forest.\n")
            time.sleep(0.3)
            ted.typing_effect("You continue walking into the thick forest.\n")
            time.sleep(0.15)
            scene_forest1()
            break
        elif action == "no":
            ted.typing_effect("You choose not to enter the forest and keep walking.\n")
            time.sleep(1)
            scene_bridge1()
            break
        elif action == "quit":
            ted.typing_effect("You sit down to rest...\n")
            exit_game = True
            break
        else:
            ted.typing_effect("You're standing still wondering what to do...\n")
            x += 1