from effects import ted

ted.typing_effect("\nAs you walk down the uneaven hill, and get closer to the light, you see a man sitting there.\n")
ted.slow_typing_effect("All alone with his campfire.\n")
ted.typing_effect("He looks friendly, ")
ted.typing_effect("but his clothes are worn down to his skin...\n")
ted.typing_effect("It looks like he is grilling some food with a stick, maybe a rabbit?\n")
ted.typing_effect("\nDo you approach him?\n")

def scene_approach_man():
    x = 0
    
    while True:
        if x >= 1:
            print("Do you approach him?")

            valg = input().strip().lower()
            
            action = ted.interpret_choice(valg, ted.yes_choices, ted.no_choices, ted.third_choices, ted.four_choices, ted.quit_choices)

            if action == "yes":
                ted.typing_effect("\n\nYou walk over to him, but you're very careful.\n")
                break
            elif action == "no":
                ted.typing_effect("fortsettelse\n")
                break
            elif action == "quit":
                ted.typing_effect("You sit down to rest...\n")
                exit_game = True
                break
            else:
                x += 1
                ted.typing_effect("You're standing still wondering what to do...\n")