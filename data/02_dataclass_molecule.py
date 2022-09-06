from dataclasses import dataclass
from typing import Union


@dataclass
class Molecule:
    name: str
    charge: Union[float, int]
    symbols: list[str]
    coordinates: list[list[float]]

    @property
    def num_atoms(self):
        return len(self.symbols)

    def __str__(self):
        return f"name: {self.name}\ncharge: {self.charge}\nsymbols: {self.symbols}"
