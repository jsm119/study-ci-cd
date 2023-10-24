import os

import math


def plus(a, b) -> int:
    return math.floor(a + b)


def get_path() -> str:
    return os.getcwd()
