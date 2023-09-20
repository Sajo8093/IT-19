x = 1

def flippblipp(n):
    if n % 5 == 0 and n % 3 == 0:
        return("flipp blipp")
    elif n % 3 == 0:
        return("flipp")
    elif n % 5 == 0:
        return("blipp")
    else:
        return(str(n))
    
print("     ", x)

playing = "true"

while playing == "true":
    x = x + 1
    if input("Next? ") != flippblipp(x):
        print("Fel - " + flippblipp(x))
        print()
        print("Game Over")
        playing = "false"      