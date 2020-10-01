import fire
from loguru import logger


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
        return a / b


def main():
    fire.Fire(Calculator)


if __name__ == "__main__":
    main()
