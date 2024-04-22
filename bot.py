# SPDX-License-Identifier: BSD-3-Clause


import numpy as np


class Bot:
    """
    This is the bot that will be instantiated for the competition.

    The pattern can be either a numpy array or a path to an image.
    """

    def __init__(self):
        self.name = "GramNegative"  # This is your team name
        self.color = None
        self.pattern = np.random.randint(0, 2, size=(14, 14))
        # self.pattern = "filler.png"
