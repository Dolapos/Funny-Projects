import random

class GuessGame:
    def __init__(self):
        self.pick = 0
        self.rand_value = 0
        self.guess = 0

    def __str__(self):
        return f'{self.rand_value} is correct! It took you {self.guess} guesses.'

    def random_select(self):
        self.rand_value = random.randint(1,100)
        return self.rand_value

    def start_game(self):
        print(f'A number has been generated.')
        print(f'Take a guess!')
        print(sep='\n')
        self.pick = int(input('What is your guess? [choose between 1 and 100]: '))
        self.guess += 1
        while (self.pick != self.rand_value):
            self.guess += 1
            if(self.pick > self.rand_value):
                print(self.pick,'is too high!')
                self.pick = int(input('What is your guess? [choose between 1 and 100]: '))
            elif(self.pick < self.rand_value):
                print(self.pick,'is too low!')
                self.pick = int(input('What is your guess? [choose between 1 and 100]: '))
            else:
                print('Please provide a valid input.')

def main():
    game = GuessGame()
    game.random_select()
    game.start_game()
    print(game.__str__())

if __name__ == '__main__':
    main()
