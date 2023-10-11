users = {"Märta":"hemligt", "Sandra":"password"}
data = {"Märta":["dator", "penna", "sudd"], "Sandra":["mattebok", "celsius"]}

print("Användare:")
print()

for user in users:
    print(f"  {user}")

print()    
print("Användare och lösenord:")
print()

for user in users:
    print(f"  {user}) {users[user]}")

print()
print("Användare och deras data:")
print()

for user in data:
    print(f"  {user}) {data[user]}")

print()

lookup = input("Slå upp en användare: ")

if lookup in users:
    print(f"  Data lagrat för {lookup}: {data[lookup]}")
else:
    print(f"Användare {lookup} finns inte.")

