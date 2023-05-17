from __future__ import annotations
from pseudo_random_numbers.helper import GeneratorBase


class Xorshift(GeneratorBase):
    def __init__(self, seed: int = 123456789) -> None:
        self.seed = seed
        self.state = seed

    def __next__(self) -> int:
        """Generate next random number."""
        self.state ^= (
            self.state << 13
        ) & 0xFFFFFFFF  # use bitwise AND for a 32-bit overflow
        self.state ^= (
            self.state >> 17
        ) & 0xFFFFFFFF  # use bitwise AND for a 32-bit overflow
        self.state ^= (
            self.state << 5
        ) & 0xFFFFFFFF  # use bitwise AND for a 32-bit overflow
        return self.state
