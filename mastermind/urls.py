from rest_framework_nested import routers

from django.conf.urls import url, include

from .views import BoardViewSet, GuessViewSet


router = routers.SimpleRouter()
router.register(r'boards', BoardViewSet, base_name='boards')

board_router = routers.NestedSimpleRouter(router, r'boards', lookup='board')
board_router.register(r'guesses', GuessViewSet, base_name='guesses')


urlpatterns = (
    url(r'^', include(router.urls)),
    url(r'^', include(board_router.urls))
)

