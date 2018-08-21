import pytest
from model_mommy import mommy

from rest_framework.test import APIClient


@pytest.fixture
def board():
    return mommy.make('Board', solution='YYGY', turns=8)

@pytest.fixture
def client():
    return APIClient()
