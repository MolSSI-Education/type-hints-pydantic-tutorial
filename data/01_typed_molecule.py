from typing import Union


class Molecule:
    def __init__(self,
                 name: str,
                 charge: Union[float, int],
                 symbols: list[str],
                 coordinates: list[list[float]]):
        self.name = name
        self.charge = charge
        self.symbols = symbols
        self.coordinates = coordinates
        self.num_atom = len(symbols)

    def __str__(self):
        return f"name: {self.name}\ncharge: {self.charge}\nsymbols: {self.symbols}"
