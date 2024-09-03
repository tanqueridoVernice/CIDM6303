# Follow the instructions for how to code this application
# Vernice Tanquerido

guests = []
guests.append(input("Enter a guest's name or type 'end' to stop.\n"))
name = ""
for x in guests:
    while name.lower() != "end":
        name = input("Enter a guest's name or type 'end' to stop.\n")
        if name.lower() != "end":
            guests.append(name)

for guest in guests:
    print(guest)

num_guests = len(guests)
cost_food = num_guests*12
print(f"You have invited {num_guests} at a cost of ${cost_food:.1f} for food")
