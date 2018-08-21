from rest_framework import serializers

from .models import Board, Guess


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ('id', 'solution', 'turns', 'status')


class GuessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guess
        fields = ('id', 'sequence', 'feedback')
