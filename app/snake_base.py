import logging
from math import sqrt, pow
from random import randint
import pickle

from store import get_redis


class Snake:
    taunts = ["I'm a snake"]

    def __init__(self, game):
        self.game = game
        self.store = get_redis()
        self.get_state()

    def start(self, data):
        self.game = data['game_id']
        self.state = self.base_state
        self.save_state()

        return {
            'name': self.name,
            'color': self.color,
            'head_url': self.head_url,
            'taunt': self.start_taunt
        }

    def end(self, data):
        self.state = self.base_state
        self.save_state()

        return ''

    def get_key(self):
        return '%s-%s' % (self.name, self.game)

    def get_state(self):
        self.state = self.base_state

    def save_state(self):
        return

    def get_distance(self, start, end):
        return sqrt(
            pow(start[1] - end[1], 2) + pow(start[0] - end[0], 2)
        )

    def get_snake(self, data):
        for snake in data['snakes']:
            if snake['name'] == self.name:
                return snake

    def get_movement(self, start, end, valid=None):
        if not valid:
            valid = ['left', 'right', 'up', 'down']

        if start[0] < end[0] and 'right' in valid:
            return "right"
        elif start[0] > end[0] and 'left' in valid:
            return "left"
        elif start[1] < end[1] and 'down' in valid:
            return "down"
        elif 'up' in valid:
            return "up"

        return None

    def get_valid_moves(self, head, board):
        valid_types = ['empty', 'food']
        valid = []

        x = head[0]
        y = head[1]

        try:
            if board[x][y-1]['state'] in valid_types:
                valid.append('up')
        except:
            pass
        try:
            if board[x][y+1]['state'] in valid_types:
                valid.append('down')
        except:
            pass
        try:
            if board[x-1][y]['state'] in valid_types:
                valid.append('left')
        except:
            pass
        try:
            if board[x+1][y]['state'] in valid_types:
                valid.append('right')
        except:
            pass

        return valid

    def get_random_taunt(self):
        num = randint(0, len(self.taunts) - 1)
        return self.taunts[num]
