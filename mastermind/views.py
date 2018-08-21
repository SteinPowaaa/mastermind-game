from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.response import Response

from .models import Board
from .serializers import BoardSerializer, GuessSerializer


class BoardViewSet(GenericViewSet, CreateModelMixin, ListModelMixin):
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
        board = Board.objects.get(pk=board_pk)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(board=board)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
