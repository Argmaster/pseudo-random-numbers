from __future__ import annotations
from pseudo_random_numbers.helper import GeneratorBase

# This is the random number generation method used by Python random module, unless
# system randomness source is used.


class MersenneTwister(GeneratorBase):
    def __init__(self, seed: int) -> None:
        self.index = 624
        self.mt = [0] * 624
        self.mt[0] = seed
        for i in range(1, 624):
            self.mt[i] = (
                0x6C078965 * (self.mt[i - 1] ^ (self.mt[i - 1] >> 30)) + i
            ) & 0xFFFFFFFF

    def twist(self) -> None:
        for i in range(624):
            y = (self.mt[i] & 0x80000000) + (self.mt[(i + 1) % 624] & 0x7FFFFFFF)
            self.mt[i] = self.mt[(i + 397) % 624] ^ (y >> 1)
            if y % 2 != 0:
                self.mt[i] ^= 0x9908B0DF

    def __next__(self) -> int:
        if self.index == 624:
            self.twist()
            self.index = 0

        y = self.mt[self.index]
        y ^= y >> 11
        y ^= (y << 7) & 0x9D2C5680
        y ^= (y << 15) & 0xEFC60000
        y ^= y >> 18

        self.index += 1

        return y & 0xFFFFFFFF
