#Guessing Game
import random 
num = random.randint(1,1000)

guess = 0

print(f'A number has been generated.')
print(f'Take a guess!')
print(sep = '\n')

pick = int(input('What is your guess? [choose between 1 and 1000] '))
guess += 1
while (pick != num):
    guess += 1
    if(pick > num):
        print(pick,'is too high!')
        pick = int(input('What is your guess? [choose between 1 and 1000] '))
    elif(pick < num):
        print(pick,'is too low!')
        pick = int(input('What is your guess? [choose between 1 and 1000] '))
print(num,'is correct!','It took you ' + str(guess) + ' guesses') 
