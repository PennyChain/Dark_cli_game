import time
import os
from openai import OpenAI

# Sett opp API-nøkkelen
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)


# Funksjon for å tolke brukerens input med AI
def ai_interpret_choice(user_input, scene_description):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Du er en enkel AI som tolker brukeres valg i et tekstbasert spill. Du svarer kun med 'yes', 'no', eller 'quit'."},
                {"role": "user", "content": f"Dette er scenen: {scene_description}\n"
                                            f"Brukeren skrev: {user_input}\n"
                                            f"Hva betyr det? Svar med 'yes', 'no', eller 'quit'."}
            ],
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip().lower()
    except Exception as e:
        print("Det oppstod en feil med OpenAI: ", e)
        return None

# Funksjon for typing-effekt
def typing_effect(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.05)
    print()  # For å legge til en ny linje etter effekten

# Hovedløkken for spillet
exit_game = False
while not exit_game:
    velkommen = input("Play? (Yes/No)\n").strip().lower()
    if velkommen == "no":
        typing_effect("Bye..")
        exit_game = True

    elif velkommen == "yes":
        while True:
            typing_effect("You're at a road. You see a sign pointing directly into the dark forest.")
            typing_effect("Do you choose to follow the sign?")
            valg1 = input().strip().lower()
            scene_desc = "You're at a road. You see a sign pointing directly into the dark forest. Do you choose to follow the sign?"
            action = ai_interpret_choice(valg1, scene_desc)

            if action == "yes":
                typing_effect("You enter the forest, and walk for some miles..\n")
                break
            elif action == "no":
                typing_effect("You choose not to enter the forest and keep walking.\n")
                break
            elif action == "quit":
                typing_effect("You sit down to rest...\n")
                exit_game = True
                break
            else:
                typing_effect("I didn't understand that. Please try again.\n")

    else:
        typing_effect("You're standing still wondering what to do...\n")