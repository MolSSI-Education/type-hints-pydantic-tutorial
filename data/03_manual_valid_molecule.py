from dataclasses import dataclass
from typing import Union

# Type Helpers
fi = Union[float, int]
lfi = list[fi]
tfi = tuple[fi, ...]
inner = Union[lfi, tfi]
lo = list[inner]
tupo = tuple[inner, ...]


@dataclass
class Molecule:
    name: str
    charge: fi
    symbols: Union[list[str], tuple[str, ...]]
    coordinates: Union[lo, tupo]

    def __post_init__(self):
        # We'll validate the inputs here.
        if not isinstance(self.name, str):
            raise ValueError(f"'name' must be a str, was {self.name}")

        if not (isinstance(self.charge, float) or isinstance(self.charge, int)):
            raise ValueError(f"'charge' must be a float or int, was {self.charge}")

        try:
            if not (isinstance(self.symbols, list) or isinstance(self.symbols, tuple)):
                raise TypeError
            for content in self.symbols:  # Loop over elements
                if not isinstance(content, str):  # Check content
                    raise ValueError(content, type(content))
        except TypeError as exec:  # Trap not iterable item
            # This will throw if you can't iterate over self.symbols
            raise ValueError(f"'symbols' must be a list or tuple of string, was {type(self.symbols)}") from exec
        except ValueError as exec:  # Trap the content error
            raise ValueError(f"Each element of 'symbols' must be a string, was {exec.args[0]} of type {exec.args[1]}") from exec

        try:
            if not (isinstance(self.coordinates, list) or isinstance(self.coordinates, tuple)):
                raise TypeError
            for inner in self.coordinates:  # Loop over elements
                try:
                    if not (isinstance(inner, list) or isinstance(inner, tuple)):
                        raise TypeError
                    for content in inner:  # Loop over elements
                        if not (isinstance(content, int), isinstance(content, float)):  # Check content
                            raise ValueError(content, type(content))
                except TypeError as exec:  # Trap not iterable item
                    # This will throw if you can't iterate over self.symbols
                    raise ValueError(f"'coordinates' inner elements must be a list or tuple of float/int, was {type(inner)}") from exec
                except ValueError as exec:  # Trap the content error
                    raise ValueError(f"Each inner element of 'coordinates' must be a string, was {exec.args[0]} of type {exec.args[1]}") from exec
        except TypeError as exec:  # Trap not iterable item
            # This will throw if you can't iterate over self.symbols
            raise ValueError(f"'coordinates' must be a list or tuple of int/float, was {type(inner)}") from exec
        except ValueError as exec:  # Trap the content error
            raise ValueError(f"'coordinates' must be a list or tuple of int/float, however the following error was thrown: {exec}") from exec

    @property
    def num_atoms(self):
        return len(self.symbols)

    def __str__(self):
        return f"name: {self.name}\ncharge: {self.charge}\nsymbols: {self.symbols}"