from pseudo_random_numbers.helper import GeneratorBase


class SplitMix(GeneratorBase):
    def __init__(self, seed: int) -> None:
        self.state = seed

    def __next__(self) -> int:
        result = self.state
        self.state += 0x9E3779B97F4A7C15
        self.state &= 0xFFFFFFFF
        result = (result ^ (result >> 30)) * 0xBF58476D1CE4E5B9
        result &= 0xFFFFFFFF
        result = (result ^ (result >> 27)) * 0x94D049BB133111EB
        result &= 0xFFFFFFFF
        return (result ^ (result >> 31)) & 0xFFFFFFFF
