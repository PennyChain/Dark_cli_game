import time
from effects import ted

def scene_bridge1():
    while True:
        ted.typing_effect("You walk for half an hour.\n")
        ted.typing_effect("Through the woods you see a bridge.\n")
        ted.typing_effect("You walk to the bridge, and notice there's a light underneath it...")
        ted.typing_effect("\nCheck it out?\n")
        
        valg3 = input().strip().lower()

        action = ted.interpret_choice(valg3, ted.yes_choices, ted.no_choices, ted.third_choices, ted.quit_choices)

        if action == "yes":
            ted.typing_effect("\nbridgetest\n")
            break
        elif action == "no":
            ted.typing_effect("bridgetest2\n")
            break
        elif action == "quit":
            ted.typing_effect("You sit down to rest...\n")
            exit_game = True
            break
        else:
            ted.typing_effect("You're standing still wondering what to do...\n")
