#!/usr/etc/python3.4.3
# File: UpdateAllBookings.py

"""
James Bay, 11/23/2015 - Requires Python 3.4.3

"""

import os
import logging
import urllib.request

# Constant definitions
LOGGING_LEVEL = logging.INFO
FORMAT = "%(asctime)s %(levelname)-3.3s %(name)-20.20s %(message)s"
PASSWORD = ""

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

    # Read URL
    
    url = "https://www.google.com/search?q=test"
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    req = urllib.request.Request(url, headers = headers)
    response = urllib.request.urlopen(req)
    the_page = response.read()
    print( the_page )

    LOGGER.info("Tarentella.py exiting.")
    return

if __name__ == "__main__":
    main()

# End file: UpdateAllBookings.py
