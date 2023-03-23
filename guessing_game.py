#Guessing Game
import random 
num = random.randint(1,100)

guess = 0

pick = int(input('What is your guess? [choose between 1 and 100] '))
guess += 1
while (pick != num):
    guess += 1
    if(pick > num):
        print(pick,'is too high!')
        pick = int(input('What is your guess? [choose between 1 and 100] '))
    elif(pick < num):
        print(pick,'is too low!')
        pick = int(input('What is your guess? [choose between 1 and 100] '))
print(num,'is correct!','It took you ' + str(guess) + ' guesses') 