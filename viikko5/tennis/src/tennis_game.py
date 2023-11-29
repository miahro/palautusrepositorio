class TennisGame:

    SCORE_CALLS = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        """ Evaluates current score
        and calls corresponding call method
        """

        if self.player1_score == self.player2_score:
            return self.tie()

        elif self.player1_score >= 4 or self.player2_score >= 4:
            return self.set_point()
        else:
            return self.normal_score()

    def tie(self):
        """returns call in case of tie
        Args: self
        Returns: call (str)
        """
        if self.player1_score == 0:
            call = "Love-All"
        elif self.player1_score == 1:
            call = "Fifteen-All"
        elif self.player1_score == 2:
            call = "Thirty-All"
        else:
            call = "Deuce"
        return call

    def set_point(self):
        """Returns call in case set point is decidable
        i.e. score over 4 for either player
        Args: self
        Returns: call (str)
        """
        minus_result = self.player1_score - self.player2_score
        if minus_result == 1:
            call = f"Advantage {self.player1_name}"
        elif minus_result == -1:
            call = f"Advantage {self.player2_name}"
        elif minus_result >= 2:
            call = f"Win for {self.player1_name}"
        else:
            call = f"Win for {self.player2_name}"
        return call

    def normal_score(self):
        """Returns call for normal score
        Args: self
        Returns: call (str) """

        call = ""
        for i, player_score in enumerate([self.player1_score, self.player2_score]):
            if i > 0:
                call += "-"
            call += self.SCORE_CALLS[player_score]

        return call
