def splash():
    print()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("|                             |")
    print("|           P(y)lugg          |")
    print("|                             |")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()

def menu(title, prompt, options):
    print(title)
    print()
    for option in options:
        print(f"  {option}) {options[option]}")
    
    print()
    action = input(prompt)
    while action not in options:
        action = input(prompt)
    
    return action

def swedish(difficulty):
    

def main():
    options_main = {"1":"Svenska ord", "2":"Engelska-Svenska", "3":"Avsluta"}
    options_difficulty = {"1":"Lätt", "2":"Svårt"}
    
    
    action = ""
    while action != "3":
        action = menu("Vad vill du p(y)lugga på?", "Val: ", options_main)
        difficulty = menu("Välj svårighetsgrad:", "Val: ", options_difficulty)
        if action == "l":
            

                
                
                