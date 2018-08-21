from django.db import models
from django.utils.functional import cached_property
from django.core.validators import RegexValidator


# change this to manage colors
sequence_validator = RegexValidator(
        r'^[PGYO]{4}$',
        '4 characters P(Purple) G(Green) Y(Yellow) and O(Orange) are allowed.'
    )


class Board(models.Model):
    WON = 'won'
    ONGOING = 'ongoing'
    LOST = 'lost'
    TURNS = (
        (12, 'Long'),
        (10, 'Medium'),
        (8, 'Short')
    )

    solution = models.CharField(max_length=4, validators=[sequence_validator])
    turns = models.IntegerField(default=12, choices=TURNS)

    @property
    def status(self):
        count = self.guesses.count()
        if count == 0:
            return self.ONGOING

        latest_guess = self.guesses.latest('id')
        if latest_guess.feedback == 'RRRR':
            return self.WON

        if count < self.turns:
            return self.ONGOING

        return self.LOST


class Guess(models.Model):
    sequence = models.CharField(max_length=4, validators=[sequence_validator])
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='guesses')

    @cached_property
    def feedback(self):
        match = ''
        for seq, sol in zip(self.sequence, self.board.solution):
            if seq == sol:
                match += 'R' # red
            elif seq in self.board.solution:
                match += 'W' # white

        return match
