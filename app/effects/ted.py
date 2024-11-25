import time

te_effect:float = 0.05

# Funksjon for typing-effekt
def typing_effect(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(te_effect)

def slow_typing_effect(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(te_effect*3)

def slower_typing_effect(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(te_effect*12.5)

def faster_typing_effect(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(te_effect/2.77)


# Funksjon for å tolke brukerens input
def interpret_choice(user_input, yes_choices, no_choices, third_choices, quit_choices):
    user_input = user_input.lower().strip()

    # Sjekk hele inputen mot forhåndsdefinerte valg
    if user_input in yes_choices:
        return "yes"
    elif user_input in no_choices:
        return "no"
    elif user_input in third_choices:
        return "third"
    elif user_input in quit_choices:
        return "quit"

    return "unknown"

# Global Ordbok/Nøkkelord
yes_choices = [
    "follow", "yes", "yep", "yup", "yeah", "sure", "yeh", "yh", "okay", "ok", "continue", "go", 
    "let's go", "absolutely", "of course", "why not", "alright", "sure thing", "definitely", 
    "let's do it", "okey-dokey", "let's roll", "ye", "yuh", "ait", "perchance"
]

third_choices = []

no_choices = [
    "no", "nope", "nein", "nah", "don't", "dont", "do not", "not at all", "never", "no way", 
    "negative", "nah-uh", "nope", "no thanks", "not really", "not interested", "I don't think so", 
    "I'd rather not", "nope, thanks", "pass", "no, thanks", "of course not", "not"
]

quit_choices = ["quit", "leave"]
