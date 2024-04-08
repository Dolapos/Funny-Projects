import random
import time


class RPS:
    def __init__(self, player=None, computer=None):
        self.choices = ['rock', 'paper', 'scissors']
        self.player = player
        self.computer = computer
        self.player_wins = 0
        self.computer_wins = 0
        self.total_games = 0

    def __str__(self):
        print()
        return f'Player: {self.player} | Computer: {self.computer}'

    def player_input(self):
        while True:
            print('Welcome to Rock, Paper, Scissors!')
            time.sleep(2)
            print('This is a game of pure luck!')
            time.sleep(2)
            print('You will be playing against a computer. You play on \'SHOOT!\'')
            time.sleep(2)
            print('Rock, Paper, Scissors...')
            time.sleep(2)
            player_choice = input('SHOOT!: ').lower()
            if player_choice in self.choices:
                self.player = player_choice
                break
            else:
                print('Please provide a valid input.')

    def comp_input(self):
        self.computer = random.choice(self.choices)

    def play_game(self):
        if ((self.computer == 'rock' and self.player == 'scissors') or
                (self.computer == 'paper' and self.player == 'rock') or
                (self.computer == 'scissors' and self.player == 'paper')):
            self.computer_wins += 1
            self.total_games += 1
            return 'Computer is the winner!'
        elif self.computer == self.player:
            time.sleep(2)
            return f'Draw!'
        else:
            self.player_wins += 1
            self.total_games += 1
            return f'Player is the winner!'

    def counter(self):
        while True:
            print()
            print('Do you want to play again?')
            player_choice1 = input('Yes or No? ').lower()
            print()
            if player_choice1 == 'yes':
                self.repeat()
                self.comp_input()
                result = self.play_game()
                print(self.__str__())
                print(result)
            else:
                print('Thanks for playing! \n')
                print(f'Player Wins: {self.player_wins}')
                print(f'Computer Wins: {self.computer_wins} \n')
                print(f'Total Games: {self.total_games}')
                break

    def repeat(self):
        print('Rock, Paper, Scissors...')
        time.sleep(2)
        player_choice2 = input('SHOOT!: ').lower()
        if player_choice2 in self.choices:
            self.player = player_choice2
        else:
            print('Please provide a valid input.')


def main():
    play = RPS()
    play.player_input()
    play.comp_input()
    print(play.__str__())
    print(play.play_game())
    play.counter()


if __name__ == '__main__':
    main()
