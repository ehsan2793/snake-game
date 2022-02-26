from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.highest_score = 0
        self.penup()
        self.hideturtle()
        self.setposition(x=0.0, y=270)
        self.score_tracker()

    def score_tracker(self):
        self.clear()
        self.write(arg=f"Score: {self.score} highest score: {self.highest_score}", align="center",
                   font=('Courier', 20, 'bold'))

    def add_to_score(self):
        self.score += 1
        self.score_tracker()

    def reset_scoreBoard(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
        self.score = 0
        self.score_tracker()

        # def game_over(self):
        #     self.setposition(x=0.0, y=0.0)
        #     self.color('yellow')
        #     return self.write(arg="Game Over !! ", align="center", font=('Courier', 30, 'bold'))
