from math import gcd

from pseudo_random_numbers.helper import GeneratorBase


class BlumBlumShub(GeneratorBase):
    def __init__(self, seed: int, p: int = 993319, q: int = 8191):
        """Take two large prime numbers p and q."""
        if gcd(seed, p * q) != 1:
            raise ValueError("Seed must be coprime with p*q")
        self.state = seed
        self.n = p * q

    def __next__(self) -> int:
        value = 0
        for _ in range(64):
            self.state = (self.state * self.state) % self.n
            value = (value << 1) | (self.state & 1)  # Return least significant bit
        return value
