from typing import Union

import fire


def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a + b


def main():
    fire.Fire(add)


if __name__ == "__main__":
    main()
