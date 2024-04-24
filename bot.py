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


class FillerBot:
    """
    This is the bot that will be instantiated for the competition.

    The pattern can be either a numpy array or a path to an image.
    In the image, white color means 0 and any other color means 1.
    """

    def __init__(self):
        self.name = "YeastieBoys"  # This is your team name
        self.color = None
        self.pattern = np.random.randint(0, 2, size=(14, 14))
        # self.pattern = "filler.png"
        self.filler = helpers.image_to_array("filler.png")
        self.cost = self.filler.sum()
        # print(np.where(self.filler > 0))

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
        if tokens >= self.cost:
            # Pick a random empty patch of size 3x3
            empty_patches = helpers.find_empty_patches(board, self.filler.shape)
            npatches = len(empty_patches)
            if npatches == 0:
                return None
            ind = np.random.randint(0, npatches)

            y, x = np.where(self.filler > 0)
            x += empty_patches[ind, 1]
            y += empty_patches[ind, 0]
            return x, y


class PufferBot:
    """
    This is the bot that will be instantiated for the competition.

    The pattern can be either a numpy array or a path to an image.
    """

    def __init__(self):
        self.name = "PufferBoys"  # This is your team name
        self.color = None
        self.pattern = np.random.randint(0, 2, size=(18, 36))
        # self.pattern = "filler.png"
        self.puffer = helpers.image_to_array("puffer.png")
        self.cost = self.puffer.sum()
        # print(np.where(self.filler > 0))

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
        if tokens >= self.cost:
            # Pick a random empty patch of size 3x3
            empty_patches = helpers.find_empty_patches(board, self.puffer.shape)
            npatches = len(empty_patches)
            if npatches == 0:
                return None
            ind = np.random.randint(0, npatches)

            op = np.random.choice([None, np.flipud, np.fliplr, np.rot90])
            a = self.puffer
            if op is not None:
                a = op(a)

            y, x = np.where(a > 0)
            x += empty_patches[ind, 1]
            y += empty_patches[ind, 0]
            return x, y
