import random

SECTION = 2

VELOCITY = 20000

MASS = 0.4


def get_code():
    press0 = random.randint(300, 900)
    press = press0 * 1.74
    thrust = round(MASS * VELOCITY + SECTION * (press - press0), 1)
    return f'Thrust of engine {thrust}'


get_code()


