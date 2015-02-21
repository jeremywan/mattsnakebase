from snake_base import Snake

class ASnake(Snake):
    color = ''  # HEX COLOR
    name = 'asnake'
    head_url = ''  # URL
    start_taunt = 'im a snake'

    base_state = {
    }

    taunts = [
        "enter taunts here"
    ]

    def move(self, data):
        move = None
        taunt = ''

        board = data['board']
        snake = self.get_snake(data)
        head = snake['coords'][0]

        valid_moves = self.get_valid_moves(head, board)

        self.save_state()

        return {
            'move': move,
            'taunt': taunt
        }
