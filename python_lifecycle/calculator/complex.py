import warnings

import fire
from loguru import logger

import python_lifecycle


class Calculator:
    @staticmethod
    def add(a, b):
        logger.info(f"Adding {a} with {b}")
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b

    @staticmethod
    def mul(a, b):
        return a * b

    @staticmethod
    def div(a, b):
        env = python_lifecycle.ENV
        logger.info(f"Environment: {env}")
        logger.info(f"Dividing {a} by {b}")
        if env == "production":
            try:
                return a / b
            except ZeroDivisionError as e:
                warnings.warn(str(e), RuntimeWarning)
        else:
            return a / b


def main():
    fire.Fire(Calculator)


if __name__ == "__main__":
    main()
