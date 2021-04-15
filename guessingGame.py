import random

print("NUMBER GUESSING GAME")
num = random.randint(1,9)
chances = 0
while chances<5:
    guess = int(input("ENTER YOUR GUESS"))

    if guess == num:
        print("CORRECT!")
        break
    
    elif guess < num:
        print("YOUR GUESS IS TOO LOW")
        print("GUESS A NUMBER HIGHER THAN THIS")

    else:
        print("YOUR GUESS IS TOO HIGH.")
        print("GUESS A NUMBER LESSER THAN THIS")
    
    chances+=1

if chances==5 and guess!= num:
    print("YOU LOSE")

