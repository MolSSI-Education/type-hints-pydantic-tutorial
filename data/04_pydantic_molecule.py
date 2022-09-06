from pydantic import BaseModel


class Molecule(BaseModel):
    name: str
    charge: float
    symbols: list[str]
    coordinates: list[list[float]]

    @property
    def num_atoms(self):
        return len(self.symbols)
