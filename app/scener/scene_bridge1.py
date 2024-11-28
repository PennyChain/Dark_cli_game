import time
from effects import ted
from scener import scene_approach_man

def scene_bridge1():
    x = 0
        
    ted.typing_effect("You walk for half an hour.\n")
    ted.typing_effect("Through the woods you see a bridge.\n")
    ted.typing_effect("You walk to the bridge, and notice there's a light underneath it...")
    ted.typing_effect("\nCheck it out?\n")
    
    while True:
        if x >= 1:
            print("Do you check it out?")

        valg = input().strip().lower()

        action = ted.interpret_choice(valg, ted.yes_choices, ted.no_choices, ted.third_choices, ted.four_choices, ted.quit_choices)

        if action == "yes":
            scene_approach_man()

        elif action == "no":
            # scene_xxxxxxx()
            break
        elif action == "quit":
            ted.typing_effect("You sit down to rest...\n")
            exit_game = True
            break
        else:
            x += 1
            ted.typing_effect("\nYou're anxious.\n")
