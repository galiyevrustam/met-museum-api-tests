"""Centralised logging configuration.

The logger is deliberately minimal: it does not attach its own handlers
and does not disable propagation.  This lets pytest's ``log_cli``
options in ``pytest.ini`` take effect so that HTTP logs are visible
in the console during a test run.
"""

import logging


def get_logger(name: str) -> logging.Logger:
    """Return a logger that propagates to the root logger.

    Pytest configures the root logger via ``log_cli``, so we must not
    disable propagation and must not add our own handler here — otherwise
    the logs would be swallowed or duplicated.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    return logger
