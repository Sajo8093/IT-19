users = {"Märta":"hemligt", "Sandra":"password"}
options = {"1":"Försök igen", "2":"Avsluta"}

def login(users):
    user = input("Användarnamn: ")
    password = input("Lösenord: ")
    while user not in users or password != users[user]:
        
        if user not in users or password != users[user]:
            print(f"Ogiltigt användarnamn eller lösenord")
            if menu("", "Val: ", options) == "2":
                return None
            
        user = input("Användarnamn: ")
        password = input("Lösenord: ")        
            
    return user

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

user = login(users)
if user != None:
    print()
    print(f"Välkommen {user}")