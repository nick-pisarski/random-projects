#!usr/bin/python
import logging
from os import path

from lib.generators import (NameGenerator, NumberStringGenerator,
                            SpecialCharGenerator)
from lib.utilities import handle_error

logging.basicConfig(
    level=logging.INFO,
    format="(%(asctime)s) %(name)s:  %(message)s",
    datefmt="%m.%d.%y@%H:%M:%S",
)

log = logging.getLogger(path.basename(__file__))

MAX_NAME_SIZE = 7
MIN_NAME_SIZE = 5


def generate_password():
    name = NameGenerator(MIN_NAME_SIZE, MAX_NAME_SIZE).get_name()
    num_str = NumberStringGenerator().get_number_str(4)
    spec_char = SpecialCharGenerator().get_special_character()
    return f"{name}{num_str}{spec_char}"


def main():
    print("Generate a new password.")
    try:
        get_new_password = "Y"
        while get_new_password == "Y":
            print(f"---> {generate_password()}")
            get_new_password = str(
                input("Generate another password (Y/N): ")
            ).capitalize()
    except Exception as ex:
        handle_error(ex)
        print("Something when wrong")


if __name__ == "__main__":
    main()
