#!/usr/etc/python3.4.3
# File: UpdateAllBookings.py

"""
James Bay, 11/23/2015 - Requires Python 3.4.3

"""

import os
import logging

# Constant definitions
LOGGING_LEVEL = logging.INFO
FORMAT = "%(asctime)s %(levelname)-3.3s %(name)-20.20s %(message)s"

# If the environment variable exists, use it to set logging level.
if os.environ.get("LOGGING_LEVEL", "INFO") == "DEBUG":
    LOGGING_LEVEL = logging.DEBUG

# Define a Handler which writes messages of level INFO or higher to the
# sys.stderr (console) only.
CONSOLE = logging.StreamHandler()
CONSOLE.setLevel(LOGGING_LEVEL)
logging.getLogger("Tarentella").addHandler(CONSOLE)
LOGGER = logging.getLogger("UpdateAllBookings")

def main():
    """
    Execute ...
    """
    LOGGER.info("Tarentella.py running.")

    # Check to see that environment variables containing passwords for the SOAP
    # service and the database have been defined.
    if PASSWORD is None:
        LOGGER.error("Password environment variable(s) missing - exiting.")
        print("Try running SET_PASSWORDS.BAT")
        return

    # This is the whole shebang.
    # TBD

    LOGGER.info("Tarentella.py exiting.")
    return

if __name__ == "__main__":
    main()

# End file: UpdateAllBookings.py
