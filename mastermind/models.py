from django.db import models
from django.core.validators import RegexValidator


sequence_validator = RegexValidator(
        r'^[PGYO]{4}$',
        '4 characters P(Purple) G(Green) Y(Yellow) and O(Orange) are allowed.'
    )


class Board(models.Model):
    TURNS = (
        (12, 'Long'),
        (10, 'Medium'),
        (8, 'Short')
    )

    solution = models.CharField(max_length=4, validators=[sequence_validator])
    turns = models.IntegerField(default=12, choices=TURNS)


class Guess(models.Model):
    sequence = models.CharField(max_length=4, validators=[sequence_validator])
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='guesses')

