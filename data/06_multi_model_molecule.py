import re
from typing import Optional, Union
# Python 3.9+ you can just get Annotated from the standard typing module
from typing_extensions import Annotated

import numpy as np
from pydantic import BaseModel, field_validator, AfterValidator, ConfigDict
from pydantic.networks import AnyUrl


def strip_string(v: str):
    return v.strip()


def valid_email(v: str):
    if not re.match(r"(mailto:)?[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+", v):
        raise ValueError("mailto URL is not a valid mailto or email link")
    return v


MailTo = Annotated[str, AfterValidator(valid_email), AfterValidator(strip_string)]


class Contributor(BaseModel):
    name: str
    url: Union[MailTo, AnyUrl]
    Organization: Optional[str] = None  # Set default and explicitly make it Nullable


class Molecule(BaseModel):
    name: str
    charge: float
    symbols: list[str]
    coordinates: np.ndarray
    contributor: Optional[Contributor] = None  # <--- New, nested, optional model

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
