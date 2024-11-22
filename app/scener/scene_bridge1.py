import time
from effects import ted

def scene_bridge1():
    while True:
        ted.typing_effect("You walk for half an hour.\n")
        ted.typing_effect("Through the woods you see a bridge.\n")
        ted.typing_effect("You walk to the bridge, and notice there's a light underneath it...")
        ted.typing_effect("\nCheck it out?\n")
        
        valg = input().strip().lower()

        action = ted.interpret_choice(valg, ted.yes_choices, ted.no_choices, ted.third_choices, ted.quit_choices)

        if action == "yes":
            ted.typing_effect("\nAs you walk down the uneaven hill, and get closer to the light, you see a man sitting there.\n")
            ted.typing_effect("All alone with his campfire, he looks friendly,\n")
            ted.typing_effect("but his clothes are worn down to his skin...")
            ted.typing_effect("It looks like he is grilling some food with a stick, maybe a rabbit?")
            ted.typing_effect("Do you approach him?")

            valg = input().strip().lower()
            
            action = ted.interpret_choice(valg, ted.yes_choices, ted.no_choices, ted.third_choices, ted.quit_choices)

            if action == "yes":
                ted.typing_effect("You walk over to him, but you're very careful.\n")
            elif action == "no":
                ted.typing_effect("bridgetest2\n")
                break
            elif action == "quit":
                ted.typing_effect("You sit down to rest...\n")
                exit_game = True
                break
            else:
                ted.typing_effect("You're standing still wondering what to do...\n")

        elif action == "no":
            ted.typing_effect("bridgetest2\n")
            break
        elif action == "quit":
            ted.typing_effect("You sit down to rest...\n")
            exit_game = True
            break
        else:
            ted.typing_effect("You're standing still wondering what to do...\n")
