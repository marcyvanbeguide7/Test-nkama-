import random
import time

moves = ['R', 'P', 'S']


# function to print text with a delay
def print_pause(message):
    print(message)
    time.sleep(1)

# 'Human class', which allows the users to play the game.
class HumanPlayer():
    def __init__(self):
        self.human_move = ""

    def move(self):
        # return input from the user
        self.human_move = random.choice(["R", "P", "S"])
        return self.human_move


# 'CyclePlayer' class, which cycles items from the 'moves' list
class CyclePlayer():
    def __init__(self):
        self.round = 0

    def move(self):
        while self.round == 0:
            self.round += 1
            return random.choice(["R", "P", "S"])
        try:
            return moves[moves.index('R') + 1]
        # If index exceeds the length of the list,
        # It circles back to its fist item
        except IndexError:
            return moves[0]

# 'RandomPlayer' class, which returns a random move from the 'moves' list
class RandomPlayer():
    def move(self):
        return random.choice(["R", "P", "S"])


# 'Constant player' class, which returns a constant move -> 'R'
class ConstantPlayer_R():
    def move(self):
        return 'R'

# 'Constant player' class, which returns a constant move -> 'S'
class ConstantPlayer_S():
    def move(self):
        return 'S'

# 'Constant player' class, which returns a constant move -> 'P'
class ConstantPlayer_P():
    def move(self):
        return 'P'


# 'Game class', which decides the length of the game, announce winner
# and controls game flow
class Game_case1_opponent():
    def __init__(self, p0, p1):
        self.p0 = p0
        self.p1 = p1
        self.p0.name = "Player 0"
        self.p1.name = "Player 1"
        # player 1 session wins count
        self.p0.win = 0
        # player 1 round wins count
        self.p0.won = 0
        self.p1.win = 0
        self.p1.won = 0
        self.round = 0
        self.game = "initialized"

    # 'beats' function, which returns a boolean value using game rules
    def beats(self, one, two):
        return ((one == 'R' and two == 'S') or
                (one == 'S' and two == 'P') or
                (one == 'P' and two == 'R'))

    def play_round(self):
        print_pause("------------[Session 1]------------")
        self.winner1 = self.play_sub_round(self.p0, self.p1)
        # loop to deal with the 'tie' scenario
        while self.winner1 == "tie":
            self.winner1 = self.play_sub_round(self.p0, self.p1)
        # prints individual wins of the 2 players in the round

    def play_sub_round(self, c1, c2):
        c1.session_win = 0
        c2.session_win = 0
        # calls the first player move
        move1 = c1.move()
        # calls the second player move
        move2 = c2.move()
        # prints both players moves
        print_pause(f"{c1.name} played\t: {move1}  \n{c2.name} Played"
                    f" : {move2}")
        # condition to determine first Player's victory scenario
        if self.beats(move1, move2):
            # increment individual wins
            c1.win += 1
            # increment session's wins
            c1.session_win += 1
            self.blink(f"Play_off Result\t: ** {c1.name} Wins **", 4)
            # statement to display score every session
            print_pause(f"Session Score \t: {c1.name} "
                        f"- {c1.session_win}, {c2.name} - {c2.session_win}")
            # reset session's score to zero
            c1.session_win = 0
            return c1
        # condition to determine 'game-tie' scenario
        elif move1 == move2:
            self.blink("Play_off Result\t: ** Game Tie **", 4)
            print_pause(f"Session Score \t: {c1.name} "
                        f"- {c1.session_win}, {c2.name} - {c2.session_win}")
            return "tie"
        # condition to determine second Player's victory scenario
        else:
            c2.win += 1
            c2.session_win += 1
            self.blink(f"Play_off Result\t: ** {c2.name} Wins **", 4)
            print_pause(f"Session Score \t: {c1.name} "
                        f"- {c1.session_win}, {c2.name} - {c2.session_win}")
            c2.session_win = 0
            return c2

    def play_game(self):
        self.spin(" GAME START ", 4)
        # Case: if player does not want to quit the game
        while self.game != "quit" and self.game != "no":
            # increment round count and display it
            self.round += 1
            print_pause(f"\n------------[ ROUND {self.round} ]-"
                        "-----------")
            # play another round
            self.play_round()
            self.game = input("\nPlay again? Type 'play' or 'quit' to go to the next case > ").lower()
            # Condition to handle unrecognized input on 'self.game'
            while (self.game != "play" and self.game != "yes") and \
                  (self.game != "quit" and self.game != "no"):
                self.game = input("Play again? Type"
                                  " 'play' or 'quit' > ").lower()
        # function method to announce winner
        print_pause("")
        self.spin(" GAME OVER ", 4)

    # function which limits game play to one round
    def play_game_once(self):
        self.spin(" GAME START ", 4)
        self.play_round()
        print_pause("")
        self.spin(" GAME OVER ", 4)

    # function to blink the text
    def blink(self, string, num):
        self.blank_list = []
        for letter in string:
            self.blank_list.append(" ")
            self.blank_string = "".join(self.blank_list)
        for _ in range(num):
            self.clear = "\b" * (len(string))
            print(string, end='', flush=True)
            time.sleep(0.2)
            print(self.clear, end='', flush=True)
            print(self.blank_string, end='', flush=True)
            time.sleep(0.2)
            print(self.clear, end='', flush=True)
        print(string)

    # funtion to display the text between spinning lines
    def spin(self, string, num):
        self.clear = "\b"*(4 + len(string))
        for _ in range(num):
            for ch in '-\\|/':
                print(ch + ch + string + ch + ch, end='', flush=True)
                time.sleep(0.1)
                print(self.clear, end='', flush=True)

    # funtion to display information related to the game
    def intro(self):
        print_pause("\n--------[INFORMATION]--------")
        print_pause("Player 0 : My robot")
        print_pause("Player 1 : robot 1")
        print_pause("Only one session between p0 and p1")
        print_pause("Session 1 : Play_off between Player 0 and Player 1")

class Game_case3_opponents():
    def __init__(self, p0, p1, p2, p3):
        self.p0 = p0
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p0.name = "Player 0"
        self.p1.name = "Player 1"
        self.p2.name = "Player 2"
        self.p3.name = "Player 3"
        # player 1 session wins count
        self.p0.win = 0
        # player 1 round wins count
        self.p0.won = 0
        self.p1.win = 0
        self.p1.won = 0
        self.p2.win = 0
        self.p2.won = 0
        self.p3.win = 0
        self.p3.won = 0
        self.round = 0
        self.game = "initialized"

    # 'beats' function, which returns a boolean value using game rules
    def beats(self, one, two):
        return ((one == 'R' and two == 'S') or
                (one == 'S' and two == 'P') or
                (one == 'P' and two == 'R'))

    def play_round(self):
        print_pause("------------[Session 1]------------")
        self.winner1 = self.play_sub_round(self.p0, self.p1)
        # loop to deal with the 'tie' scenario
        while self.winner1 == "tie":
            self.winner1 = self.play_sub_round(self.p0, self.p1)
        print_pause("------------[Session 2]------------")
        self.winner2 = self.play_sub_round(self.p2, self.p3)
        # loop to deal with the 'tie' scenario
        while self.winner2 == "tie":
            self.winner2 = self.play_sub_round(self.p2, self.p3)
        print_pause("------------[Session 3]------------")
        self.winner3 = self.play_sub_round(self.winner1, self.winner2)
        # loop to deal with the 'tie' scenario
        while self.winner3 == "tie":
            self.winner3 = self.play_sub_round(self.winner1, self.winner2)
        # conditional statements to diaplay the round winner
        if self.winner3 == self.p0:
            self.p0.won += 1
            # blink's the string 4 times
            self.blink(f"[Round Result]\t: ** {self.p0.name} "
                       "wins the round **", 4)
        elif self.winner3 == self.p1:
            self.p1.won += 1
            self.blink(f"[Round Result]\t: ** {self.p1.name} "
                       "wins the round **", 4)
        elif self.winner3 == self.p2:
            self.p2.won += 1
            self.blink(f"[Round Result]\t: ** {self.p2.name} "
                       "wins the round **", 4)
        elif self.winner3 == self.p3:
            self.p3.won += 1
            self.blink(f"[Round Result]\t: ** {self.p3.name} "
                       "wins the round **", 4)

    def play_sub_round(self, c1, c2):
        c1.session_win = 0
        c2.session_win = 0
        # calls the first player move
        move1 = c1.move()
        # calls the second player move
        move2 = c2.move()
        # prints both players moves
        print_pause(f"{c1.name} played\t: {move1}  \n{c2.name} Played"
                    f" : {move2}")
        # condition to determine first Player's victory scenario
        if self.beats(move1, move2):
            # increment individual wins
            c1.win += 1
            # increment session's wins
            c1.session_win += 1
            self.blink(f"Play_off Result\t: ** {c1.name} Wins **", 4)
            # statement to display score every session
            print_pause(f"Session Score \t: {c1.name} "
                        f"- {c1.session_win}, {c2.name} - {c2.session_win}")
            # reset session's score to zero
            c1.session_win = 0
            return c1
        # condition to determine 'game-tie' scenario
        elif move1 == move2:
            self.blink("Play_off Result\t: ** Game Tie **", 4)
            print_pause(f"Session Score \t: {c1.name} "
                        f"- {c1.session_win}, {c2.name} - {c2.session_win}")
            return "tie"
        # condition to determine second Player's victory scenario
        else:
            c2.win += 1
            c2.session_win += 1
            self.blink(f"Play_off Result\t: ** {c2.name} Wins **", 4)
            print_pause(f"Session Score \t: {c1.name} "
                        f"- {c1.session_win}, {c2.name} - {c2.session_win}")
            c2.session_win = 0
            return c2

    def play_game(self):
        self.spin(" GAME START ", 4)
        # Case: if player does not want to quit the game
        while self.game != "quit" and self.game != "no":
            # increment round count and display it
            self.round += 1
            print_pause(f"\n------------[ ROUND {self.round} ]-"
                        "-----------")
            # play another round
            self.play_round()
            self.game = input("\nPlay again? Type 'play' or 'quit' to go to the next case > ").lower()
            # Condition to handle unrecognized input on 'self.game'
            while (self.game != "play" and self.game != "yes") and \
                  (self.game != "quit" and self.game != "no"):
                self.game = input("Play again? Type"
                                  " 'play' or 'quit' > ").lower()
        # function method to announce winner
        print_pause("")
        self.spin(" GAME OVER ", 4)

    # function which limits game play to one round
    def play_game_once(self):
        self.spin(" GAME START ", 4)
        self.play_round()
        print_pause("")
        self.spin(" GAME OVER ", 4)

    # function to blink the text
    def blink(self, string, num):
        self.blank_list = []
        for letter in string:
            self.blank_list.append(" ")
            self.blank_string = "".join(self.blank_list)
        for _ in range(num):
            self.clear = "\b" * (len(string))
            print(string, end='', flush=True)
            time.sleep(0.2)
            print(self.clear, end='', flush=True)
            print(self.blank_string, end='', flush=True)
            time.sleep(0.2)
            print(self.clear, end='', flush=True)
        print(string)

    # funtion to display the text between spinning lines
    def spin(self, string, num):
        self.clear = "\b"*(4 + len(string))
        for _ in range(num):
            for ch in '-\\|/':
                print(ch + ch + string + ch + ch, end='', flush=True)
                time.sleep(0.1)
                print(self.clear, end='', flush=True)

    # funtion to display information related to the game
    def intro(self):
        print_pause("\n--------[INFORMATION]--------")
        print_pause("Player 0 : My robot")
        print_pause("Player 1 : robot 1")
        print_pause("Player 2 : robot 2")
        print_pause("Player 3 : robot 3\n")
        print_pause("Each round has 3 sessions")
        print_pause("Session 1 : Play_off between Player 0 and Player 1")
        print_pause("Session 2 : Play_off between Player 2 and Player 3")
        print_pause("Session 3 : Play_off between session 1 and session 2"
                    " winners\n")

class Game_case7_opponents():
    def __init__(self, p0, p1, p2, p3, p4, p5, p6, p7):
        self.p0 = p0
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.p5 = p5
        self.p6 = p6
        self.p7 = p7
        self.p0.name = "Player 0"
        self.p1.name = "Player 1"
        self.p2.name = "Player 2"
        self.p3.name = "Player 3"
        self.p4.name = "Player 4"
        self.p5.name = "Player 5"
        self.p6.name = "Player 6"
        self.p7.name = "Player 7"
        # player 1 session wins count
        self.p0.win = 0
        # player 1 round wins count
        self.p0.won = 0
        self.p1.win = 0
        self.p1.won = 0
        self.p2.win = 0
        self.p2.won = 0
        self.p3.win = 0
        self.p3.won = 0
        self.p4.win = 0
        self.p4.won = 0
        self.p5.win = 0
        self.p5.won = 0
        self.p6.win = 0
        self.p6.won = 0
        self.p7.win = 0
        self.p7.won = 0
        self.round = 0
        self.game = "initialized"

    # 'beats' function, which returns a boolean value using game rules
    def beats(self, one, two):
        return ((one == 'R' and two == 'S') or
                (one == 'S' and two == 'P') or
                (one == 'P' and two == 'R'))

    def play_round(self):
        print_pause("------------[Session 1]------------")
        self.winner1 = self.play_sub_round(self.p0, self.p1)
        # loop to deal with the 'tie' scenario
        while self.winner1 == "tie":
            self.winner1 = self.play_sub_round(self.p0, self.p1)
        print_pause("------------[Session 2]------------")
        self.winner2 = self.play_sub_round(self.p2, self.p3)
        # loop to deal with the 'tie' scenario
        while self.winner2 == "tie":
            self.winner2 = self.play_sub_round(self.p2, self.p3)
        print_pause("------------[Session 3]------------")
        self.winner3 = self.play_sub_round(self.p4, self.p5)
        # loop to deal with the 'tie' scenario
        while self.winner3 == "tie":
            self.winner3 = self.play_sub_round(self.p4, self.p5)
        print_pause("------------[Session 4]------------")
        self.winner4 = self.play_sub_round(self.p6, self.p7)
        # loop to deal with the 'tie' scenario
        while self.winner4 == "tie":
            self.winner4 = self.play_sub_round(self.p6, self.p7)
        print_pause("------------[Session 5]------------")
        self.winner5 = self.play_sub_round(self.winner3, self.winner4)
        # loop to deal with the 'tie' scenario
        while self.winner5 == "tie":
            self.winner5 = self.play_sub_round(self.winner3, self.winner4)
        print_pause("------------[Session 6]------------")
        self.winner6 = self.play_sub_round(self.winner1, self.winner2)
        # loop to deal with the 'tie' scenario
        while self.winner6 == "tie":
            self.winner6 = self.play_sub_round(self.winner1, self.winner2)
        print_pause("------------[Session 7]------------")
        self.winner7 = self.play_sub_round(self.winner6, self.winner5)
        # loop to deal with the 'tie' scenario
        while self.winner7 == "tie":
            self.winner7 = self.play_sub_round(self.winner6, self.winner5)
        # conditional statements to diaplay the round winner
        if self.winner7 == self.p0:
            self.p0.won += 1
            # blink's the string 4 times
            self.blink(f"[Round Result]\t: ** {self.p0.name} "
                       "wins the round **", 4)
        elif self.winner7 == self.p1:
            self.p1.won += 1
            self.blink(f"[Round Result]\t: ** {self.p1.name} "
                       "wins the round **", 4)
        elif self.winner7 == self.p2:
            self.p2.won += 1
            self.blink(f"[Round Result]\t: ** {self.p2.name} "
                       "wins the round **", 4)
        elif self.winner7 == self.p3:
            self.p3.won += 1
            self.blink(f"[Round Result]\t: ** {self.p3.name} "
                       "wins the round **", 4)
        elif self.winner7 == self.p4:
            self.p4.won += 1
            self.blink(f"[Round Result]\t: ** {self.p4.name} "
                       "wins the round **", 4)
        elif self.winner7 == self.p5:
            self.p5.won += 1
            self.blink(f"[Round Result]\t: ** {self.p5.name} "
                       "wins the round **", 4)
        elif self.winner7 == self.p6:
            self.p6.won += 1
            self.blink(f"[Round Result]\t: ** {self.p6.name} "
                       "wins the round **", 4)
        elif self.winner7 == self.p7:
            self.p7.won += 1
            self.blink(f"[Round Result]\t: ** {self.p7.name} "
                       "wins the round **", 4)

    def play_sub_round(self, c1, c2):
        c1.session_win = 0
        c2.session_win = 0
        # calls the first player move
        move1 = c1.move()
        # calls the second player move
        move2 = c2.move()
        # prints both players moves
        print_pause(f"{c1.name} played\t: {move1}  \n{c2.name} Played"
                    f" : {move2}")
        # condition to determine first Player's victory scenario
        if self.beats(move1, move2):
            # increment individual wins
            c1.win += 1
            # increment session's wins
            c1.session_win += 1
            self.blink(f"Play_off Result\t: ** {c1.name} Wins **", 4)
            # statement to display score every session
            print_pause(f"Session Score \t: {c1.name} "
                        f"- {c1.session_win}, {c2.name} - {c2.session_win}")
            # reset session's score to zero
            c1.session_win = 0
            return c1
        # condition to determine 'game-tie' scenario
        elif move1 == move2:
            self.blink("Play_off Result\t: ** Game Tie **", 4)
            print_pause(f"Session Score \t: {c1.name} "
                        f"- {c1.session_win}, {c2.name} - {c2.session_win}")
            return "tie"
        # condition to determine second Player's victory scenario
        else:
            c2.win += 1
            c2.session_win += 1
            self.blink(f"Play_off Result\t: ** {c2.name} Wins **", 4)
            print_pause(f"Session Score \t: {c1.name} "
                        f"- {c1.session_win}, {c2.name} - {c2.session_win}")
            c2.session_win = 0
            return c2

    def play_game(self):
        self.spin(" GAME START ", 4)
        # Case: if player does not want to quit the game
        while self.game != "quit" and self.game != "no":
            # increment round count and display it
            self.round += 1
            print_pause(f"\n------------[ ROUND {self.round} ]-"
                        "-----------")
            # play another round
            self.play_round()
            self.game = input("\nPlay again? Type 'play' or 'quit' to go to the next case > ").lower()
            # Condition to handle unrecognized input on 'self.game'
            while (self.game != "play" and self.game != "yes") and \
                  (self.game != "quit" and self.game != "no"):
                self.game = input("Play again? Type"
                                  " 'play' or 'quit' > ").lower()
        # function method to announce winner
        print_pause("")
        self.spin(" GAME OVER ", 4)

    # function which limits game play to one round
    def play_game_once(self):
        self.spin(" GAME START ", 4)
        self.play_round()
        print_pause("")
        self.spin(" GAME OVER ", 4)

    # function to blink the text
    def blink(self, string, num):
        self.blank_list = []
        for letter in string:
            self.blank_list.append(" ")
            self.blank_string = "".join(self.blank_list)
        for _ in range(num):
            self.clear = "\b" * (len(string))
            print(string, end='', flush=True)
            time.sleep(0.2)
            print(self.clear, end='', flush=True)
            print(self.blank_string, end='', flush=True)
            time.sleep(0.2)
            print(self.clear, end='', flush=True)
        print(string)

    # funtion to display the text between spinning lines
    def spin(self, string, num):
        self.clear = "\b"*(4 + len(string))
        for _ in range(num):
            for ch in '-\\|/':
                print(ch + ch + string + ch + ch, end='', flush=True)
                time.sleep(0.1)
                print(self.clear, end='', flush=True)

    # funtion to display information related to the game
    def intro(self):
        print_pause("\n--------[INFORMATION]--------")
        print_pause("Player 0 : My robot")
        print_pause("Player 1 : robot 1")
        print_pause("Player 2 : robot 2")
        print_pause("Player 3 : robot 3")
        print_pause("Player 4 : robot 4")
        print_pause("Player 5 : robot 5")
        print_pause("Player 6 : robot 6")
        print_pause("Player 7 : robot 7\n")
        print_pause("Each round has 7 sessions")
        print_pause("Session 1 : Play_off between Player 0 and Player 1")
        print_pause("Session 2 : Play_off between Player 2 and Player 3")
        print_pause("Session 3 : Play_off between Player 4 and Player 5")
        print_pause("Session 4 : Play_off between Player 6 and Player 7")
        print_pause("Session 5 : Play_off between session 3 and session 4"
                    " winners")
        print_pause("Session 6 : Play_off between session 1 and session 2"
                    " winners")
        print_pause("Session 7 : Play_off between session 5 and session 6"
                    " winners\n")


# condition to run the code only if executed directly
if __name__ == '__main__':
    game_case1 = Game_case1_opponent(HumanPlayer(), CyclePlayer())
    game_case1.intro()
    game_case1.play_game()

    game_case3 = Game_case3_opponents(HumanPlayer(), ConstantPlayer_R(), ConstantPlayer_P(), ConstantPlayer_S())
    game_case3.intro()
    game_case3.play_game()

    game_case7 = Game_case7_opponents(HumanPlayer(), CyclePlayer(), RandomPlayer(), RandomPlayer(), RandomPlayer(), RandomPlayer(), CyclePlayer(), RandomPlayer())
    game_case7.intro()
    game_case7.play_game()
