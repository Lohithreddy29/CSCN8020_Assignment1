"""Utility helpers for logging, formatting, and experiment support."""

import logging


def setup_logging(name: str = "CSCN8020_Assignment1", level: int = logging.INFO) -> logging.Logger:
    """Create and configure a reusable logger for the assignment project."""
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
        logger.addHandler(handler)
    logger.setLevel(level)
    logger.propagate = False
    return logger


def log(message: str, level: int = logging.INFO) -> None:
    """Log a message using the project logger."""
    logger = setup_logging()
    logger.log(level, message)
