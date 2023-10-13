options1 = {"l":"Lägg till", "v":"Visa innehåll", "x":"Logga ut"}
options2 = {"f":"Försök igen", "a":"Avsluta"}
options3 = {"l":"Logga in", "a":"Avsluta"}

def add(prompt, strings):
    x = input(prompt)
    strings.append(x)
    return strings

def view(description, strings):
    print(description)
    print()
    for x in range(len(strings)):
        print("  " + str(x + 1) + ") " + strings[x])
        
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

def login(users):
    user = input("Användarnamn: ")
    password = input("Lösenord: ")
    while user not in users or password != users[user]:
        
        if user not in users or password != users[user]:
            print("Ogiltigt användarnamn eller lösenord")
            if menu("", "Val: ", options1) == "a":
                return None
            
        user = input("Användarnamn: ")
        password = input("Lösenord: ")        
            
    return user

def user_actions(user, items):
    print(f"Välkommen {user}")
    print()
    view("Dina lagrade saker:", items)
    print()
    
    action = ""
    while action != "x":
        action = menu("Vad vill du göra?", "Val: ", options1)
    
        if action == "l":
            add("Lägg till: ", items)
        elif action == "v":
            view("Dina lagrade föremål:", items)
        
        print()
    
    print(f"Hejdå {user}, välkommen åter!")
    view("Dina föremål är:", items)
    return items

def main():
    users = {"Märta":"hemligt", "Sandra":"password"}
    data = {"Märta":["dator", "penna", "sudd"], "Sandra":["mattebok", "celsius"]}
    
    action = ""
    while action != "a":
        action = menu("Välkommen till Lagra™!", "Val: ", options3)
        if action == "l":
            user = login(users)
            if user != None:
                data[user] = user_actions(user, data[user])


main()
