class Molecule:
    def __init__(self, name, charge, symbols, coordinates):
        self.name = name
        self.charge = charge
        self.symbols = symbols
        self.coordinates = coordinates
        self.num_atom = len(symbols)

    def __str__(self):
        return f"name: {self.name}\ncharge: {self.charge}\nsymbols: {self.symbols}"
