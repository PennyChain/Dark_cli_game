import time
import random


# Funksjon for typing-effekt
def typing_effect(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.05)

def slow_typing_effect(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.15)

def slower_typing_effect(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.75)

def faster_typing_effect(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.018)


# Funksjon for å tolke brukerens input
def interpret_choice(user_input, yes_choices, no_choices, third_choices, quit_choices):
    user_input = user_input.lower()
    
    # Sjekker om inputen matcher ja, nei eller quit
    if any(choice in user_input for choice in yes_choices):
        return "yes"
    elif any(choice in user_input for choice in no_choices):
        return "no"
    elif any(choice in user_input for choice in third_choices):
        return "third"
    elif any(choice in user_input for choice in quit_choices):
        return "quit"
    
    return "unknown"

# Global Ordbok/Nøkkelord
yes_choices = [
    "follow", "yes", "yep", "yeah", "sure", "yeh", "yh", "okay", "ok", "continue", "go", 
    "let's go", "absolutely", "of course", "why not", "alright", "sure thing", "definitely", 
    "let's do it", "okey-dokey", "let's roll", "ye", "yuh"
]

third_choices = []

no_choices = [
    "no", "nope", "nein", "nah", "don't", "dont", "do not", "not at all", "never", "no way", 
    "negative", "nah-uh", "nope", "no thanks", "not really", "not interested", "I don't think so", 
    "I'd rather not", "nope, thanks", "pass", "no, thanks"
]

quit_choices = ["quit", "leave"]

# Spillstart
def main():
    exit_game = False
    while not exit_game:
        velkommen = input("Play? (Yes/No)\n").strip().lower()
        if velkommen == "no":
            typing_effect("Bye..")
            exit_game = True
        elif velkommen == "yes":
            result = scene_1()
            if result == "quit":
                exit_game = True
        else:
            typing_effect("\nYou're standing still wondering what to do...\n")

###########################################################################################

# Første valg/scene
def scene_1():
    x = 0

    typing_effect("You're at a road. You see a sign pointing directly into the dark forest. ")
    typing_effect("Do you choose to follow the sign?\n")
    
    while True:
        if x >= 1:
            print("Do you follow the sign?\n")

        valg1 = input().strip().lower()
        
        action = interpret_choice(valg1, yes_choices, no_choices, third_choices, quit_choices)

        if action == "yes":
            typing_effect("\nYou enter the forest, and walk for some miles..\n")
            scene_forest1()
            break
        elif action == "no":
            typing_effect("You choose not to enter the forest and keep walking.\n")
            scene_bridge1()
            break
        elif action == "quit":
            typing_effect("You sit down to rest...\n")
            exit_game = True
            break
        else:
            typing_effect("You're standing still wondering what to do...\n")
            x += 1

###########################################################################################

def scene_forest1():
    x = 0
    local_yes_choices = yes_choices.copy()
    local_yes_choices.extend ([
        "on", "turn on", "switch on", "activate", "light", "turn the light on", 
        "flip on", "power on", "shine", "start", "begin", "open", "power up", 
        "illuminate", "brighten", "light up", "make it light", "trigger", 
        "turn it on", "flick on", "set on", "hit the switch", "turn the switch", 
        "set the light", "flick the switch", "turn it up", "turn on the flashlight", 
        "use the flashlight", "turn flashlight on", "flashlight on", "switch flashlight on", "I do"
    ])
    
    typing_effect("It's getting darker the further in you go.\n")
    typing_effect("Suddenly, everything goes quiet")
    slower_typing_effect("...\n")
    typing_effect("You remember you packed a small flashlight in your backpack.\n")
    typing_effect("Do you turn it on..?\n")

    while True:
        if x >= 1:
            print("Do you turn it on?\n")
        
        valg2 = input().strip().lower()

        action = interpret_choice(valg2, local_yes_choices, no_choices, third_choices, quit_choices)

        if action == "yes":
            typing_effect("\nWhy   did   you   do   THAT?!?!?!?!?!?\n")
            time.sleep(1.3)
            scene_creature1()
        elif action == "no":
            typing_effect("YOU\nHEAR\n")
            time.sleep(0.5)
            typing_effect("STEPS...")
            break
        elif action == "quit":
            typing_effect("You sit down to rest...\n")
            exit_game = True
            break
        else:
            typing_effect("You're standing still wondering what to do...\n")
            x += 1

###########################################################################################

def scene_bridge1():
    while True:
        typing_effect("You walk for half an hour.\n")
        typing_effect("Through the woods you see a bridge.\n")
        typing_effect("You walk to the bridge, and notice there's a light underneath it...")
        typing_effect("Check it out?\n")
        
        valg3 = input().strip().lower()

        action = interpret_choice(valg3, yes_choices, no_choices, third_choices, quit_choices)

        if action == "yes":
            typing_effect("\nbridgetest\n")
            break
        elif action == "no":
            typing_effect("bridgetest2\n")
            break
        elif action == "quit":
            typing_effect("You sit down to rest...\n")
            exit_game = True
            break
        else:
            typing_effect("You're standing still wondering what to do...\n")

###########################################################################################

def scene_creature1():
    x = 0
    local_yes_choices = [
        "climb", "tree", "nearest", "closest"
    ]
    local_no_choices = [
        "run", "away", "sprint", "zoom", "bounce"
    ]
    local_third_choices = [
        "fight", "fuck", "it"
    ]
    local_quit_choices = quit_choices.copy()
    local_quit_choices.extend ([
        "kill", "myself", "kms"
    ])
    
    faster_typing_effect("\nTHERE IS SOMETHING RUNNING TOWARDS YOU!\n")
    time.sleep(0.3)
    faster_typing_effect("WHAT DO YOU DO?\n")
    time.sleep(0.3)
    faster_typing_effect("\nCLIMB THE NEAREST TREE\n")
    time.sleep(0.35)
    faster_typing_effect("RUN AWAY\n")
    time.sleep(0.3)
    faster_typing_effect("FIGHT WHATEVER IT IS\n")

    while True:
        if x >= 1:
            faster_typing_effect("YOU HAVE TO CHOOSE. NOW!\n")
        
        valg4 = input().strip().lower()

        action = interpret_choice(valg4, local_yes_choices, local_no_choices, local_third_choices, local_quit_choices)

        if action == "yes":
            typing_effect("You run towards the closest tree and climb up it as fast as you can!\n")
            typing_effect("You camp the tree until the sun rises\n")
            typing_effect("You notice as the sun rise, the creature flees...!\n")
            typing_effect("You climb down and try to get the hell out of the forest, but you dont remember where you came from...\n")
            slow_typing_effect("You realise you're lost...\n")
            # scene_lost()
        elif action == "no":
            typing_effect("You run away as fast as you can, but the creature is much faster than you.\n")
            typing_effect("The creature catches up to you and u get a glimse of it...\n")
            slow_typing_effect("WHAT. IS. THAT THING...\n")
            typing_effect("The creature gets ahold of you..\n")
            slow_typing_effect("It kills you slowly....")
            exit_game = True
            break
        elif action == "third":
            typing_effect("You grab a branch on the ground and swing at the creature.\n")
            typing_effect("While you try to defend yourself you get a good look at how the creature looks.\n")
            typing_effect("It looks like some sort of morphed human being, but its just ")
            slow_typing_effect("not a human..\n")
            faster_typing_effect("\nIT SLASHES YOUR ARM!\n")
            typing_effect("You fight back with all your force\n")
            typing_effect("You manage to defend yourself ")
            slow_typing_effect("barely... ")
            typing_effect("The creature limps away, ")
            slow_typing_effect("so do you.\n")
            typing_effect("You need to find some healing supplies..")
            # scene_scavange()
        elif action == "quit":
            typing_effect("You kill yourself out of fear.\n")
            exit_game = True
            break
        else:
            x += 1

if __name__ == "__main__":
    main()