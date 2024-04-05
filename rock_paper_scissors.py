import random

class RPS:
    def __init__(self, player = None, computer = None):
        self.choices = ['rock', 'paper', 'scissors']
        self.player = player
        self.computer = computer

    def __str__(self):
        return f'Player: {self.player} | Computer: {self.computer}'

    def player_input(self):
        while True:
            player_choice = input('Rock, Paper, Scissors!: ').lower()
            if player_choice in self.choices:
                self.player = player_choice
                break
            else:
                print('Please provide a valid input.')

    def comp_input(self):
        self.computer = random.choice(self.choices)

    def play_game(self):
        if (self.computer == 'rock' and self.player == 'scissors') or (self.computer == 'paper' and self.player == 'rock') or (self.computer == 'scissors' and self.player == 'paper'):
            return 'Computer is the winner!'
        elif self.computer == self.player:
            return f'Draw!'
        else:
            return f'Player is the winner!'

def main():
    play = RPS()
    play.player_input()
    play.comp_input()
    print(play.__str__())
    print(play.play_game())

if __name__ == '__main__':
    main()
