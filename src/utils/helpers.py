# ~~~ helpers/helpers.py ~~~

#* ----- NORMAL IMPORTS -----
import os
import time
import logging as log
from colorama import Fore, Style, init
init()

#* ----- FUNCTIONS -----    
def highlight(msg: str, color: str = Fore.LIGHTCYAN_EX, style: str = Style.NORMAL) -> str:
    """Highlight a string in a selected color with optional underline."""
    try:
        result = f"{style}{color}{msg}{Style.RESET_ALL}"
        return result
    except Exception as e:
        print(f"Error occurred: {e}")

def timeit(func):
    """Times a Function"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        log.info(f"Function {func.__name__} took {end_time - start_time} seconds to execute.")
        return result
    return wrapper
