# SPDX-License-Identifier: BSD-3-Clause

from typing import Literal, Union

import numpy as np


class Bot:
    """
    This is the bot that will be instantiated for the competition.
    """

    def __init__(self):
        self.name = "GramNegative"  # This is your team name
        self.color = None
        self.pattern = np.random.randint(0, 2, size=(14, 14))
