import fire
from loguru import logger

import python_lifecycle
from python_lifecycle.calculator.broken import BrokenCalculator
from python_lifecycle.calculator.complex import Calculator
from python_lifecycle.calculator.simple import add


class Main:
    def __init__(self, env: str = "development"):
        self.env = env
        logger.info(f"Environment: {self.env}")
        python_lifecycle.ENV = self.env

        self.simp = add
        self.complex = Calculator
        self.broken = BrokenCalculator


def main():
    fire.Fire(Main)


if __name__ == "__main__":
    main()
