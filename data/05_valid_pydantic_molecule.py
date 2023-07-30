import numpy as np
from pydantic import BaseModel, field_validator, ConfigDict


class Molecule(BaseModel):
    name: str
    charge: float
    symbols: list[str]
    coordinates: np.ndarray

    model_config = ConfigDict(arbitrary_types_allowed=True)

    @field_validator("coordinates", mode='before')
    @classmethod
    def coord_to_numpy(cls, coords):
        try:
            coords = np.asarray(coords)
        except ValueError:
            raise ValueError(f"Could not cast {coords} to numpy array")
        return coords

    @field_validator("coordinates")
    @classmethod
    def coords_length_of_symbols(cls, coords, info):
        symbols = info.data["symbols"]
        if (len(coords.shape) != 2) or (len(symbols) != coords.shape[0]) or (coords.shape[1] != 3):
            raise ValueError(f"Coordinates must be of shape [Number Symbols, 3], was {coords.shape}")
        return coords

    @property
    def num_atoms(self):
        return len(self.symbols)
