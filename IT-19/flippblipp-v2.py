n = 40

def flippblipp(n):
    if n % 5 == 0 and n % 3 == 0:
        return("flipp blipp")
    elif n % 3 == 0:
        return("flipp")
    elif n % 5 == 0:
        return("blipp")
    else:
        return(str(n))

for x in range(1, n+1):
    print(flippblipp(x))