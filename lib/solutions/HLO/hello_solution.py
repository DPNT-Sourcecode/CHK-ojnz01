# noinspection PyUnusedLocal
# friend_name = unicode string
from solutions.HLO import hello_solution


def hello(friend_name):
    if friend_name:
        return f"Hello, {friend_name}!"

    else:
        return None
