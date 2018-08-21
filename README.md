# Setup

```sh
$ pip install -r requirements.txt
$ python manage.py runserver
```

# Usage
Check the full description of the game: [Mastermind](https://en.wikipedia.org/wiki/Mastermind_(board_game))

| METHOD | DATA | DESCRIPTION |
| ------ | ------ | ------ |
| POST `boards/` | solution(CHAR) turns(INTEGER) | create new board  |
| POST `boards/{id}/guesses`| sequence(CHAR) | create new guess for {id} board |
| GET `boards/` | | view all boards |
| GET `boards/{id}` | | view {id} board and its guess history |

> Solution must be 4 chars - one of - P(Purple), G(Green), Y(Yellow), O(Orange)
> To change available colors goto -> mastermind/models and edit sequence_validator
