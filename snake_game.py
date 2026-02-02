"""
Snake Water Gun Game
1  = Snake
-1 = Water
0  = Gun
"""

import random                     # random module import kiya

# Computer randomly snake, water ya gun choose karega
computer = random.choice([-1, 0, 1])

# User se input liya (s = snake, w = water, g = gun)
yous = input("Enter your choice (s, w, g): ").lower()

# Ye dictionary user ke input ko number me convert karegi
ydict = {
    "s": 1,        # s likhne par snake (1)
    "w": -1,       # w likhne par water (-1)
    "g": 0         # g likhne par gun (0)
}

# Ye dictionary number ko wapas word me convert karegi
dictreverse = {
    1: "snake",    # 1 ko snake banaya
    -1: "water",   # -1 ko water banaya
    0: "gun"       # 0 ko gun banaya
}

# User ke input (s/w/g) ko number me convert kiya
you = ydict[yous]

# User aur computer ka choice print kar rahe hain
print(f"Your choice: {dictreverse[you]}")
print(f"Computer choice: {dictreverse[computer]}")

# Agar dono ka choice same ho
if computer == you:
    print("It's a draw!")

# Agar choice same nahi hai to winner decide karo
else:
    # Snake (you) vs Water (computer) → you win
    if computer == -1 and you == 1:
        print("You win!")

    # Water (you) vs Snake (computer) → you lose
    elif computer == 1 and you == -1:
        print("You lose!")

    # Gun (you) vs Water (computer) → you lose
    elif computer == -1 and you == 0:
        print("You lose!")

    # Gun (you) vs Snake (computer) → you win
    elif computer == 1 and you == 0:
        print("You win!")

    # Snake (you) vs Gun (computer) → you lose
    elif computer == 0 and you == 1:
        print("You lose!")

    # Water (you) vs Gun (computer) → you win
    elif computer == 0 and you == -1:
        print("You win!")

    # Agar koi unexpected error aaye
    else:
        print("Something went wrong!")
