# SPDX-License-Identifier: BSD-3-Clause
from typing import Optional, Tuple

import numpy as np

from cholerama import helpers

AUTHOR = "YeastieBoys"  # This is your team name


class Bot:
    """
    This is the bot that will be instantiated for the competition.

    The pattern can be either a numpy array or a path to an image.
    """

    def __init__(self, number: int, name: str, x: int, y: int):
        """
        Parameters:
        ----------
        number: int
            The player number. Numbers on the board equal to this value mark your cells.
        name: str
            The player's name
        x: int
            The starting x position of the lower-left corner of the pattern
        y: int
            The starting y position of the lower-left corner of the pattern
        """
        self.number = number  # Mandatory: this is your number on the board
        self.name = name  # Mandatory: player name
        self.color = None  # Optional

        # If we make the pattern too sparse, it just dies quickly
        self.pattern = np.zeros(14 * 14, dtype=int)
        cells = np.random.choice(len(self.pattern), 100, replace=False)
        self.pattern[cells] = 1
        self.pattern = self.pattern.reshape(14, 14)
        # The pattern can also be just an image
        # self.pattern = "mypattern.png"

    def iterate(
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
