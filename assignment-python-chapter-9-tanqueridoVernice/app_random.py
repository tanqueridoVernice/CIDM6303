import random
import string

# Chapter 9.12- Generating Random Values
print("n\Chapter 9.12- Generating Random Values"+"-"*20)
print(random.random())
print(random.randint(1, 10))
print(random.choice([1, 2, 3, 4]))
print(random.choices([1, 2, 3, 4]))
print("".join(random.choices(string.ascii_letters + string.digits)))

numbers = [1, 2, 3, 4]
random.shuffle(numbers)
print(numbers)

# Examples
for i in range(10):
    print(random.random())

for i in range(10):
    print(random.randint(1, 100))

cards = ["Ace", "King", "Queen", "Jack", "Joker"]
random.shuffle(cards)
print(cards)
