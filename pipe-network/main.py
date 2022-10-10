import logging
from os import path

from lib.networks import PipeNetwork

logging.basicConfig(
    level=logging.INFO,
    format="(%(asctime)s) %(name)s:  %(message)s",
    datefmt="%m.%d.%y@%H:%M:%S",
)

log = logging.getLogger(path.basename(__file__))


def main():
    log.info("pipe-network")

    network = PipeNetwork()


if __name__ == "__main__":
    main()
