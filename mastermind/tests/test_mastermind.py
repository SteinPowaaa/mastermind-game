import pytest


@pytest.mark.django_db
def test_get_board(board, client):
    resp =  client.get('http://localhost:8000/boards/')
    assert resp.data[0]['solution'] == 'YYGY'


@pytest.mark.django_db
def test_create_board(client):
    resp = client.post('http://localhost:8000/boards/', data={'solution': 'YYYY'})
    assert resp.data['solution'] == 'YYYY'


@pytest.mark.django_db
def test_create_guess(client, board):
    resp = client.post('http://localhost:8000/boards/%s/guesses/' % board.id,
                       data={'sequence': 'YYOO'})
    assert resp.data['guess']['sequence'] == 'YYOO'
    assert resp.data['guess']['feedback'] == 'RR'
    assert resp.data['status'] == 'ongoing'


@pytest.mark.django_db
def test_correct_guess(client, board):
    resp = client.post('http://localhost:8000/boards/%s/guesses/' % board.id,
                       data={'sequence': 'YYGY'})
    assert resp.data['guess']['sequence'] == 'YYGY'
    assert resp.data['guess']['feedback'] == 'RRRR'
    assert resp.data['status'] == 'won'


@pytest.mark.django_db
def test_lost(client, board):
    for x in range(7):
        client.post('http://localhost:8000/boards/%s/guesses/' % board.id,
                    data={'sequence': 'YYYY'})

    resp = client.post('http://localhost:8000/boards/%s/guesses/' % board.id,
                    data={'sequence': 'YYYY'})

    assert resp.data['status'] == 'lost'
