from __future__ import annotations
from pseudo_random_numbers.helper import GeneratorBase


class MultiplyWithCarry(GeneratorBase):
    def __init__(
        self,
        seed: int = 0,
        multiplier: int = 7,
        carry: int = 1,
        modulo: int = 10,
    ):
        self.seed = seed
        self.multiplier = multiplier
        self.carry = carry
        self.modulo = modulo

    def __next__(self):
        value = self.multiplier * self.seed + self.carry
        self.seed = value % self.modulo
        self.carry = value // self.modulo
        return self.seed
