from __future__ import annotations
from pseudo_random_numbers.helper import GeneratorBase


class MiddleSquareGenerator(GeneratorBase):
    def __init__(self, seed: int = 5909) -> None:
        if 1000 <= seed < 10000:  # Seed should be a 4-digit number
            self.seed = seed
            self.state = seed
            self.counter = 0
        else:
            raise ValueError("Seed must be a four-digit number")

    def __next__(self) -> int:
        self.counter += 1
        self.state = int(
            str(self.state * self.state).zfill(8)[2:6]
        )  # zfill adds padding of zeroes
        return self.state
