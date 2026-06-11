"""Gridworld environment classes for CSCN8020 Assignment 1."""


class GridWorld:
    """Base gridworld environment placeholder."""

    def __init__(self, rows: int = 5, cols: int = 5):
        self.rows = rows
        self.cols = cols


class SimpleGridWorld(GridWorld):
    """A simple gridworld environment used for RL experiments."""

    pass
