def add(prompt, strings):
    x = input(prompt)
    strings.append(x)
    return strings

def view(description, strings):
    print(description)
    print()
    for x in range(len(strings)):
        print(str(x + 1) + ") " + strings[x])

strings = []
n = 2

print(n)
for x in range(n):
    print()
    strings = add("Lägg till en sträng: ", strings)

description = f"Du har matat in följande {n} strängar"

print()
view(description, strings)
print()

#names = ["nisse", "bosse"]
#animals = ["hund", "katt", "hamster"]
#view("Lista med namn", names)
#print()
#view("Lista med djur", animals)
     
#print(f"Lista med saker: {items}")
#items = add("Lägg till en grej: ", items)
#print(f"Lista med saker: {items}")
