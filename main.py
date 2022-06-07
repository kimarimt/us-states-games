import turtle
from gamehandler import GameHandler


SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500


def main():
    screen = turtle.getscreen()
    gamehandler = GameHandler()
    max_score = len(gamehandler.states)
    game_is_on = True

    screen.clearscreen()
    screen.title('U.S States Game')
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.bgpic('data/blank_states_img.gif')

    while game_is_on and len(gamehandler.states) != 0:
        screen.update()
        input = turtle.textinput(
            f'{gamehandler.score}/{max_score} States correct',
            'Enter states:').strip()
        answer = ' '.join([word.capitalize() for word in input.split(' ')])

        if not gamehandler.check_answer(answer):
            game_is_on = False
            gamehandler.save_states()

    turtle.bye()


if __name__ == '__main__':
    main()
