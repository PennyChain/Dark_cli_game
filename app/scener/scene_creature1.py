import time
from effects import ted
from scener.scene_died import scene_died
from scener.scene_scavenge import scene_scavenge

def scene_creature1():
    x = 0
    local_yes_choices = [
        "climb", "tree", "nearest", "closest"
    ]
    local_no_choices = [
        "run", "away", "sprint", "zoom", "bounce"
    ]
    local_third_choices = [
        "fight", "fuck", "it", "kill"
    ]
    local_quit_choices = ted.quit_choices.copy()
    local_quit_choices.extend ([
        "myself", "kms"
    ])
    
    ted.faster_typing_effect("\nTHERE IS SOMETHING RUNNING TOWARDS YOU!\n")
    time.sleep(0.3)
    ted.faster_typing_effect("WHAT DO YOU DO?\n")
    time.sleep(0.6)
    ted.faster_typing_effect("\nCLIMB THE NEAREST TREE\n")
    time.sleep(0.35)
    ted.faster_typing_effect("RUN AWAY\n")
    time.sleep(0.3)
    ted.faster_typing_effect("FIGHT WHATEVER IT IS\n\n")

    while True:
        if x >= 1:
            ted.faster_typing_effect("\nYOU HAVE TO CHOOSE. NOW!\n")
        
        valg = input().strip().lower()

        action = ted.interpret_choice(valg, local_yes_choices, local_no_choices, local_third_choices, local_quit_choices)

        if action == "yes":
            ted.typing_effect("\nYou find the closest tree and climb up it as fast as you can!\n")
            time.sleep(0.2)
            ted.typing_effect("You camp the tree until the sun rises\n")
            ted.typing_effect("You notice as the sun rise, the creature flees...!\n")
            ted.typing_effect("You climb down and try to get the hell out of the forest, but you dont remember where you came from...\n")
            time.sleep(0.2)
            ted.slow_typing_effect("You realise you're lost...\n")
            # scene_lost()
        elif action == "no":
            ted.typing_effect("\nYou run away as fast as you can, but the creature is much faster than you.\n")
            ted.typing_effect("The creature catches up to you and you get a glimse of it...\n")
            ted.slow_typing_effect("\nWHAT. IS. THAT THING???\n")
            time.sleep(0.2)
            ted.typing_effect("\nThe creature gets ahold of you..\n")
            ted.slow_typing_effect("\nIt kills you slowly....")
            time.sleep(0.6)
            scene_died()
            break
        elif action == "third":
            ted.typing_effect("\nYou grab a branch on the ground and swing at the creature.\n")
            ted.typing_effect("While you try to defend yourself you get a good look at how the creature looks.\n")
            time.sleep(0.2)
            ted.typing_effect("It looks like some sort of morphed human being, but its just ")
            ted.slow_typing_effect("not a human..\n")
            ted.faster_typing_effect("\nIT SLASHES YOUR ARM!\n")
            ted.typing_effect("You fight back with all your force\n")
            ted.typing_effect("You manage to defend yourself ")
            ted.slow_typing_effect("barely... \n")
            time.sleep(0.2)
            ted.typing_effect("The creature limps away, ")
            ted.slow_typing_effect("so do you.\n")
            time.sleep(0.2)
            ted.typing_effect("You need to find some healing supplies..\n")
            scene_scavenge()
        elif action == "quit":
            ted.typing_effect("You kill yourself out of fear.\n")
            time.sleep(0.6)
            scene_died()
            break
        else:
            x += 1
