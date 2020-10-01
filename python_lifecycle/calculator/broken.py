import fire
from loguru import logger

from config import settings
from python_lifecycle.calculator.complex import Calculator


class BrokenCalculator(Calculator):
    def __init__(self):
        offset = settings.offset
        logger.info(f"Offset: {offset}")
        self.offset = offset

    def add(self, a, b):
        return super(BrokenCalculator, self).add(a, b) - self.offset

    def sub(self, a, b):
        return super(BrokenCalculator, self).sub(a, b) - self.offset

    def mul(self, a, b):
        return super(BrokenCalculator, self).mul(a, b) - self.offset

    def div(self, a, b):
        return super(BrokenCalculator, self).div(a, b) - self.offset


def main():
    fire.Fire(BrokenCalculator)


if __name__ == "__main__":
    main()
