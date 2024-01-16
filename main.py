class Rover:
    '''Класс управления марсохода.'''

    FORWARD = 'F'
    BACK = 'B'
    LEFT = 'L'
    RIGHT = 'R'

    NORTH = 'N'
    EAST = 'E'
    SOUTH = 'S'
    WEST = 'W'

    DIRECTIONS = (NORTH, EAST, SOUTH, WEST)

    def __init__(self, x: int = 0, y: int = 0, direction: str = NORTH):
        '''Устанавливает все необходимые атрибуты для объекта.'''
        self.x = x
        self.y = y
        self.direction = direction

    def forward_or_back(self, side: str):
        '''Определяет направление движения.'''
        return 1 if side == self.FORWARD else -1

    def move(self, side: str):
        '''Передвигает объект вперед-назад.'''
        if self.direction == self.NORTH:
            self.y += self.forward_or_back(side)
        elif self.direction == self.EAST:
            self.x += self.forward_or_back(side)
        elif self.direction == self.SOUTH:
            self.y -= self.forward_or_back(side)
        else:
            self.x -= self.forward_or_back(side)

    def move_forward(self):
        '''Двигает объект вперед.'''
        self.move(self.FORWARD)

    def move_back(self):
        '''Двигает объект назад.'''
        self.move(self.BACK)

    def turn(self, side: str):
        '''Поворачивает объект.'''
        index = self.DIRECTIONS.index(self.direction)
        index += (1 if side == self.RIGHT else -1)
        self.direction = self.DIRECTIONS[index % len(self.DIRECTIONS)]

    def move_right(self):
        '''Двигает объект вправо.'''
        self.turn(self.RIGHT)
        self.move_forward()

    def move_left(self):
        '''Двигает объект влево.'''
        self.turn(self.LEFT)
        self.move_forward()

    def get_position(self):
        '''Определяет позицию объекта.'''
        return (self.x, self.y)

    def get_direction(self):
        '''Определяет направление камеры.'''
        return self.direction


class TestRover:
    '''Тесты управления марсохода.'''

    def test_move_forward(self):
        '''Тест движения вперед.'''
        rover = Rover()
        rover.move_forward()
        return rover.get_position() == (0, 1) and rover.get_direction() == 'N'

    def test_move_back(self):
        '''Тест движения назад.'''
        rover = Rover()
        rover.move_back()
        return rover.get_position() == (0, -1) and rover.get_direction() == 'N'

    def test_move_left(self):
        '''Тест движения влево.'''
        rover = Rover()
        rover.move_left()
        return rover.get_position() == (-1, 0) and rover.get_direction() == 'W'

    def test_move_right(self):
        '''Тест движения вправо.'''
        rover = Rover()
        rover.move_right()
        return rover.get_position() == (1, 0) and rover.get_direction() == 'E'
