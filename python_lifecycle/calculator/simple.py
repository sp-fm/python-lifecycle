from typing import Union

import fire


def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Add two numbers

    Args:
        a (Union[int, float]): The first number
        b (Union[int, float]): The second number

    Returns:
        int or float: Sum of two numbers

    """
    return a + b


def main():
    fire.Fire(add)


if __name__ == "__main__":
    main()
