options1 = {"1":"Add item", "2":"List items", "3":"Log out"}
options2 = {"1":"Try again", "2":"Quit"}

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
    
opt1 = menu("Select an action", "Action: ", options1)
print(f"You selected action {opt1}) {options1[opt1]}")
opt2 = menu("What do you want to do?", "My choice: ", options2)
print(f"You selected option {opt2}) {options2[opt2]}")