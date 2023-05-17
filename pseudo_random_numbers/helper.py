from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Iterable, Iterator

from matplotlib import pyplot as plt


class GeneratorBase(ABC):
    def __iter__(self) -> Iterator[int]:
        return self

    @abstractmethod
    def __next__(self) -> int:
        pass

    def sample(self, count: int) -> list[int]:
        return [*self.sample_iter(count)]

    def sample_iter(self, count: int) -> Iterable[int]:
        for _ in range(count):
            yield next(self)


def hist(
    data: list[int] | list[float] | GeneratorBase, max_sample: int = 10_000
) -> None:
    if isinstance(data, GeneratorBase):
        data = data.sample(max_sample)

    fig = plt.figure()
    plt.hist(data, rwidth=0.9)
    plt.show()
