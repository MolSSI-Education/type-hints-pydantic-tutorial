import re
from typing import Union

import numpy as np
from pydantic import BaseModel, validator, AnyUrl


class MailTo(str):
    @classmethod
    def __get_validators__(cls):
        for valid in [cls.valid_str, cls.valid_email]:
            yield valid

    @classmethod
    def valid_str(cls, v: str):
        if not isinstance(v, str):
            raise TypeError("Not a valid mailto Email format")
        v = v.strip()
        return v

    @classmethod
    def valid_email(cls, v: str):
        if not re.match(r"(mailto:)?[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+", v):
            raise ValueError("mailto URL is not a valid mailto or email link")
        return v


class Contributor(BaseModel):
    name: str
    url: Union[MailTo, AnyUrl]
    Organization: str = None  # Set default that makes it optional


class Molecule(BaseModel):
    name: str
    charge: float
    symbols: list[str]
    coordinates: np.ndarray
    contributor: Contributor = None

    class Config:
        arbitrary_types_allowed = True

    @validator("coordinates", pre=True)
    def coord_to_numpy(cls, coords):
        try:
            coords = np.asarray(coords)
        except ValueError:
            raise ValueError(f"Could not cast {coords} to numpy array")
        return coords

    @validator("coordinates")
    def coords_length_of_symbols(cls, coords, values):
        symbols = values["symbols"]
        if (len(coords.shape) != 2) or (len(symbols) != coords.shape[0]) or (coords.shape[1] != 3):
            raise ValueError(f"Coordinates must be of shape [Number Symbols, 3], was {coords.shape}")
        return coords

    @property
    def num_atoms(self):
        return len(self.symbols)