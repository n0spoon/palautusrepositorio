class TennisGame:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.player1_score = 0
        self.player2_score = 0
        self.scores = ["Love", "Fifteen", "Thirty", "Forty"]

    def won_point(self, player):
        if player == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1

    def tie_score(self):
        if self.player1_score == 4 or (self.player1_score == 40 and self.player2_score == 40):
            return "Deuce"
        return f'{self.scores[self.player1_score]}-All'

    def short_game(self):
        return f"{self.scores[self.player1_score]}-{self.scores[self.player2_score]}"

    def long_game(self):
        score_difference = self.player1_score - self.player2_score
        if score_difference == 1:
            return "Advantage player1"
        if score_difference == -1:
            return "Advantage player2"
        if score_difference > 1:
            return "Win for player1"
        return "Win for player2"

    def get_score(self):
        if self.player1_score == self.player2_score:
            return self.tie_score()
        if self.player1_score < 4 and self.player2_score < 4:
            return self.short_game()
        return self.long_game()
