import bottle
import json

from snakes import ASnake

SNAKES = {
    'asnake': ASnake
}


@bottle.get('/')
def index():
    list_of_snakes = "<ul>"
    for snake in SNAKES:
        list_of_snakes += "<li>https://mattsnake.herokuapp.com/%s</li>" % snake

    return list_of_snakes


@bottle.post('/<snake_name>/start')
def start(snake_name):
    data = bottle.request.json
    game = data['game_id']
    response = SNAKES[snake_name](game).start(data)
    return json.dumps(response)


@bottle.post('/<snake_name>/move')
def move(snake_name):
    data = bottle.request.json
    game = data['game_id']
    resp = SNAKES[snake_name](game).move(data)
    return json.dumps(resp)


@bottle.post('/<snake_name>/end')
def end(snake_name):
    data = bottle.request.json
    game = data['game_id']
    resp = SNAKES[snake_name](game).end(data)
    return json.dumps(resp)


# Expose WSGI app
application = bottle.default_app()
