from random import choice as pick


class Play:
    relations = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

    def __init__(self, choice=""):
        if not choice:
            self.choice = pick(list(Play.relations.values()))
        else:
            assert choice in Play.relations
            self.choice = choice

    def beats(self, other):
        """
        Returns 1 if this Play beats the other Play,
        0 if there is a tie, or
        -1 if the other Play beats this Play.
        """
        if Play.relations[self.choice] == other.choice:
            return 1
        elif self.choice == other.choice:
            return 0
        else:
            return -1


class Game:
    def __init__(self):
        self.score1 = 0
        self.score2 = 0

    def winner(self):
        """
        Returns 1 if player 1 wins,
        0 if there is a tie, or
        -1 if player 2 wins.
        """
        if self.score1 > self.score2:
            return 1
        elif self.score1 == self.score2:
            return 0
        else:
            return -1

    def play_round(self):
        choice = input("Rock, paper, or scissors: ").lower().strip()
        player1_play = Play(choice)
        player2_play = Play()
        print(f"Player 2 plays {player2_play.choice}.")
        result = player1_play.beats(player2_play)

        if result == 1:
            self.score1 += 1
            print("Player 1 beats Player 2 this round!")
        elif result == -1:
            self.score2 += 1
            print("Player 2 beats Player 1 this round!")
        else:
            print("It's a tie this round!")
        print(f"P1 Score: {self.score1} | P2 Score: {self.score2}")

        keep_playing = input("Do you want to keep playing? Enter Y or N: ").lower().strip()
        assert keep_playing == "y" or keep_playing == "n"
        print()
        return keep_playing == "n"


if __name__ == "__main__":
    print("Welcome to Rock, Paper, Scissors! You are Player 1.")
    game = Game()
    finished = False
    while not finished:
        finished = game.play_round()
    print("The game has concluded.")
    winner = game.winner()
    if winner == 1:
        print("You won! Congratulations.")
    elif winner == 0:
        print("It's a tie! Nicely played.")
    else:
        print("Uh oh! It looks like the bot beat you. Better luck next time.")
