# SPDX-License-Identifier: BSD-3-Clause
from typing import Optional, Tuple

from cholerama import helpers
import numpy as np


class Bot:
    """
    This is the bot that will be instantiated for the competition.

    The pattern can be either a numpy array or a path to an image.
    """

    def __init__(self):
        self.name = "YeastieBoys"  # This is your team name
        self.color = None
        self.pattern = np.random.randint(0, 2, size=(14, 14))
        # self.pattern = "filler.png"

    def run(
        self, iteration: int, board: np.ndarray, tokens: int
    ) -> Optional[Tuple[np.ndarray, np.ndarray]]:
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

        Returns:
        -------
        tuple
            A tuple containing the x and y coordinates of the new cells.
        """
        if tokens >= 5:
            # Pick a random empty patch of size 3x3
            empty_patches = helpers.find_empty_patches(board, (3, 3))
            npatches = len(empty_patches)
            if npatches == 0:
                return None
            ind = np.random.randint(0, npatches)
            x = np.array([1, 2, 0, 1, 2]) + empty_patches[ind, 1]
            y = np.array([2, 1, 0, 0, 0]) + empty_patches[ind, 0]
            return x, y
