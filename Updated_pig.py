import random
import argparse
import time


class Dice:
    def __init__(self, n=6):
        self.sides = n
        self.roll()

    def roll(self):
        self.value = int(random.random() * self.sides + 1)

class Game:
    def __init__(self):
        self.dice = Dice()
        players = Factory()
        self.p1 = players.p1
        self.p2 = players.p2

    def play(self):
        while (self.p1.score < 100 and self.p2.score < 100):
            self.p1.move()
            if self.p1.score < 100:
                self.p2.move()
        if (self.p1.score > self.p2.score):
            print(f'{self.p1.name} is the winner!')
        else:
            print(f'{self.p2.name} is the winner!')

class Player:
    def __init__(self, title):
        self.name = title
        self.score = 0
        self.dice = Dice(6)
    def move(self):
        round_score = 0
        again = 'r'

        while again == 'r':
            self.dice.roll()
            roll = self.dice.value
            if roll == 1:
                print('{} has rolled a 1'.format(self.name))
                round_score = 0
                again = 'h'
            else:
                print('{} has rolled a {}'.format(self.name, roll))
                round_score = round_score+roll
                print("{}'s round score is {}".format(self.name, round_score))
                again = input('Roll = r or Hold = h?')
        self.score += round_score
        print("{}'s turn is over".format(self.name))
        print("{}'s total score is {}\n\n".format(self.name, self.score))

class TimedGameProxy:
    def __init__(self):
        self.dice = Dice()
        players = Factory()
        self.p1 = players.p1
        self.p2 = players.p2
    def play(self):
        game_start = time.time()
        while (self.p1.score < 100 and self.p2.score < 100):
            game_end = time.time()
            if (game_end-game_start)<60:
                self.p1.move()
                if self.p1.score < 100:
                    game_end = time.time()
                    if (game_end-game_start)<60:
                        self.p2.move()
                    else:
                        print("60 Seconds Until Game Time is Over")
                        break
            else:
                 print("60 Seconds Until Game Time is Over")
                 break
        if (self.p1.score > self.p2.score):
            print(f'{self.p1.name} is the winner!')
        else:
            print(f'{self.p2.name} is the winner!')


class CPU_Player(Player):
    def move(self):
        round_score = 0
        again = 'y'
        while again == 'y':
            self.dice.roll()
            roll = self.dice.value
            if roll == 1:
                print('{} has rolled a 1'.format(self.name))
                round_score = 0
                again = 'n'
            else:
                print('{} has rolled a {}'.format(self.name, roll))
                round_score = round_score + roll
                if round_score < (25 if 25 < (100 - self.score) else (100 - self.score)):
                    print('{} will roll again'.format(self.name))
                else:
                    again = 'n'
        self.score += round_score
        print('Turn is over')
        print("{}'s scored the following for this round {}".format(self.name, round_score))
        print("{}'s scored the following for this round  {}\n\n".format(self.name, self.score))

class Factory:
    def __init__(self):
        print("Please select an option:\nPlease Enter the number 1 to play with PIG with a friend\nPlease Enter the number 2 to play against a Computer\nPlease Enter the number 3 to see two Computer players play : ")
        try:
            option = int(input())
            while option not in [1,2]:
                   print("Invlaid input")
                   print("Please select an option:\nPlease Enter the number 1 to play with PIG with a friend\nPlease Enter the number 2 to play against a Computer\nPlease Enter the number 3 to see two Computer players play : ")
                   option = int(input())
            if option == 1:
                    self.p1 =  Player("Player1")
                    self.p2 =  Player("Player2")
            elif option == 2:
                self.p1 =  Player("Player")
                self.p2 =  CPU_Player("Computer")
            else:
                self.p1 =  CPU_Player("Computer1")
                self.p2 =  CPU_Player("Computer2")
        except:
            print("Try again, Not an option")

if __name__ == "__main__":
    print('welcome to game of Pig!')
    pig = Game()
    pig.play()
    print()
    print('Rerun to play again')