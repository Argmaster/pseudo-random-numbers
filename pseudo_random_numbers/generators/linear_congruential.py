from __future__ import annotations
from pseudo_random_numbers.helper import GeneratorBase

# Linear Congruential Generator is used in Java by implementation of `Math.random()`.


class LinearCongruentialGenerator(GeneratorBase):
    def __init__(
        self, seed: int, modulus: int = 2**16 + 1, a: int = 75, c: int = 74
    ) -> None:
        # parameters of the generator
        self.modulus = modulus
        self.a = a
        self.c = c
        self.state = seed

    def __next__(self) -> int:
        self.state = (self.a * self.state + self.c) % self.modulus
        return self.state
