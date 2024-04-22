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

    def run(self, iteration, board, tokens):
        """
        This method will be called by the game engine on each iteration.

        Parameters:
        ----------
        iteration : int
            The current iteration number.
        board : numpy array
            The current state of the board.
        tokens : list
            The list of tokens on the board.
        """
        if tokens >= 5:
            x = [1, 2, 0, 1, 2]
            y = [2, 1, 0, 0, 0]
            return x, y

        return np.random.randint(0, 14), np.random.randint(0, 14)
