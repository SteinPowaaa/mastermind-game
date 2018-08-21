from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.response import Response

from .models import Board
from .serializers import BoardSerializer, GuessSerializer


class BoardViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        board_serializer = self.get_serializer(instance)
        guess_serializer = GuessSerializer(instance.guesses.order_by('id'), many=True)

        return Response(data={
            'board': board_serializer.data,
            'history': guess_serializer.data
        })


class GuessViewSet(GenericViewSet):
    serializer_class = GuessSerializer

    def create(self, request, board_pk, *args, **kwargs):
        board = get_object_or_404(Board.objects.all(), pk=board_pk)
        if board.status != 'ongoing':
            return Response(data={'data': 'This game is %s' % board.status})

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(board=board)

        return Response(data={
            'guess': serializer.data,
            'status': board.status
        }, status=status.HTTP_201_CREATED)
