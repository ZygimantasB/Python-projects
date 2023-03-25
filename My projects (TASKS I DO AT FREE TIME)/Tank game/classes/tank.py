import logging
import re
from random import randint
from CONSTANTS.constants import POINTS_DEDUCTIBLE
from logo.logo import tank_shot, tank_up, tank_down, tank_left, tank_right, information, \
    sad_face, game_end, game_name, game_rules

logger = logging.getLogger(__name__)
logging.basicConfig(filename='game.log', encoding="UTF-8",
                    level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(name)s:%('
                                                'message)s:%(module)s:%(funcName)s')


class Tank:
    """
    Definite information about mu game function
    """
    def __init__(self):
        self.x_tank: int = 0
        self.y_tank: int = 0
        self.tank_direction_at: str = 'forward'
        self.player_points: int = 150
        self.shots_direction: dict = {"forward": 0, "right": 0, "backward": 0, "left": 0}
        self.x_target: int = randint(-10, 10)
        self.y_target: int = randint(-10, 10)

    def map_limitations(self):
        """
        Map limitations
        """
        if self.x_tank == 11:
            print('Cannot move forward beyond map boundary')
            self.x_tank -= 1
        elif self.x_tank == -11:
            print('Cannot move backward beyond map boundary')
            self.x_tank += 1

        if self.y_tank == -11:
            print('Cannot move left beyond map boundary')
            self.y_tank += 1
        elif self.y_tank == 11:
            print('Cannot move right beyond map boundary')
            self.y_tank -= 1

    def forward(self):
        """
        Move tank forward by 1
        """
        print(tank_up)
        self.tank_direction_at = 'forward'
        self.x_tank += 1
        self.player_points -= POINTS_DEDUCTIBLE
        self.map_limitations()

    def backward(self):
        """
        Move tank backward by 1
        """
        print(tank_down)
        self.tank_direction_at = 'backward'
        self.x_tank -= 1
        self.player_points -= POINTS_DEDUCTIBLE
        self.map_limitations()

    def turn_right(self):
        """
        Move tank right by 1
        """
        print(tank_right)
        self.tank_direction_at = 'right'
        self.y_tank += 1
        self.player_points -= POINTS_DEDUCTIBLE
        self.map_limitations()

    def turn_left(self):
        """
        Move tank left by 1
        """
        print(tank_left)
        self.tank_direction_at = 'left'
        self.y_tank -= 1
        self.player_points -= POINTS_DEDUCTIBLE
        self.map_limitations()

    def direction_shot(self):
        """
        Count tank shots by direction
        """
        self.shots_direction[self.tank_direction_at] += 1

    def tank_shot(self):
        """
        Count all tank shots and results
        """
        print(tank_shot)
        if self.x_tank == self.x_target and self.y_tank == self.y_target:
            self.player_points += 100
            print(self.player_points)
            self.x_target = randint(-10, 10)
            self.y_target = randint(-10, 10)
            self.new_target_x = self.x_target = randint(-10, 10)
            self.new_target_y = self.y_target = randint(-10, 10)
            print('Congrats, target was eliminated')
            logging.info('Tank hit the target')
        else:
            print('You missed the target')
            logging.info('Tank missed the shot')

    def information(self):
        """
        Show game information
        """
        print(information)
        print('Tank direction: ', self.tank_direction_at)
        print("Tank position: ", self.x_tank, self.y_tank)
        print('Tank fired shots: ', sum(self.shots_direction.values()))
        print('Target position: ',  self.x_target, self.y_target)
        print('Player points: ', self.player_points)
        print('Shots by direction', self.shots_direction)
        print(self.tank_location())

    def game_functionality(self):
        """
        Game functionality
        """
        logging.info('Game started')
        while True:
            commander_action = input('Commander begin your battle: ').casefold()
            match commander_action:
                case 'forward':
                    self.forward()
                    logging.info('Tank moved forward')
                case 'backward':
                    self.backward()
                    logging.info('Tank moved backward')
                case 'left':
                    self.turn_left()
                    logging.info('Tank moved left')
                case 'right':
                    self.turn_right()
                    logging.info('Tank moved right')
                case 'info':
                    self.information()
                    logging.info('Commander asked for information')
                case 'fire':
                    self.tank_shot()
                    self.direction_shot()
                    logging.info('Tank performed a shot')
                case commander_action if commander_action == 'end' or self.player_points == 0 or \
                                         self.player_points >= 300:
                    try:
                        player_name = int(input('Enter player name for scoreboard: '))
                    except ValueError:
                        logging.error(ValueError)
                        print('Please enter the string')
                    finally:
                        while True:
                            player_name = input('Enter player name for scoreboard: ').upper()
                            if not re.match(r'^\s*$', player_name):
                                print(self.add_scores(player_name, self.player_points))
                                print(game_end)
                                logging.info(f'Game ended by player {player_name}')
                                break
                            else:
                                print('String is empty fix it Commander')
                                logging.info('Commander entered empty string')
                    break
                case 'score':
                    print(self.watch_scores())
                    logging.info('Commander watched scoreboard')
                case _:
                    print(sad_face)
                    print('Commander you entered invalid command')
                    logging.info('Commander entered wrong input')

    @staticmethod
    def information_about_the_game():
        """
        Information about the game
        """
        yield game_name
        yield 'Below are information for tank movement.'
        yield '--Forward-- x +1.'
        yield '--Backward-- x -1.'
        yield '--Left-- y -1.'
        yield '--Right-- y +1'
        yield game_rules
        yield 'You start with 150 points if you reach zero you lose if you reach 300 you win.'
        yield 'Then your tank is moving you loose -10 points.'
        yield 'Then tank hits the target you get 100 points.'
        yield 'You can end game any time by entering end and your score will save to score board.'
        yield 'Get game information write info.'
        yield 'If you want to shot use fire.'
        yield 'On the map tank will be marked ✪'
        yield 'On the map target will be marked ⦻'
        yield '\n'

    @staticmethod
    def add_scores(player_name, scores):
        """
        Save result to scoreboard
        """
        try:
            with open('results.txt', mode='a', encoding='utf-8') as player_result:
                player_result.write(f'\n{player_name} - {scores}')
                logging.info('File was created')
        except FileNotFoundError:
            logging.error('File exist')
        Tank.watch_scores()

    @staticmethod
    def watch_scores() -> dict:
        """
        Show scoreboard
        """
        leader_board = {}
        with open('results.txt', mode='r', encoding='utf-8') as read_results:
            for item in read_results:
                player_info = item.strip().split(' - ')
                player_name = player_info[0]
                player_score = int(player_info[1])
                leader_board[player_name] = player_score
        logging.info('Score board was updated with new result')
        return dict(
            enumerate(sorted(leader_board.items(), key=lambda value: value[1], reverse=True),
                      start=1))

    def tank_location(self):
        """
        Game map
        """
        row_1 = ['■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■']
        row_2 = ['■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■']
        row_3 = ['■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■']
        row_4 = ['■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■']
        row_5 = ['■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■']
        row_6 = ['■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■']
        row_7 = ['■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■']
        row_8 = ['■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■']
        row_9 = ['■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■']
        row_10 = ['■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■']
        row_11 = ['■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■']
        row_12 = ['■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■']
        row_13 = ['■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■']
        row_14 = ['■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■']
        row_15 = ['■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■']
        row_16 = ['■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■']
        row_17 = ['■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■']
        row_18 = ['■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■']
        row_19 = ['■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■']
        row_20 = ['■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■']
        row_21 = ['■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■']

        map = [row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8, row_9, row_10, row_11, row_12, row_13, row_14,
               row_15, row_16, row_17, row_18, row_19, row_20, row_21]

        position_tank = [self.x_tank, self.y_tank]
        tank_position_x = position_tank[0]
        tank_position_y = position_tank[1]

        map[tank_position_x - 11][tank_position_y - 11] = '✪'

        target_position = [self.x_target, self.y_target]
        target_position_x = target_position[0]
        target_position_y = target_position[1]

        map[target_position_x - 11][target_position_y - 11] = '⦻'
        print(f'{row_1}\n{row_2}\n{row_3}\n{row_4}\n{row_5}\n{row_6}\n{row_7}\n{row_8}\n{row_9}\n'
              f'{row_10}\n{row_11}\n{row_12}\n{row_13}\n{row_14}\n{row_15}\n{row_16}\n{row_17}\n'
              f'{row_18}\n{row_19}\n{row_20}\n{row_21}\n')
