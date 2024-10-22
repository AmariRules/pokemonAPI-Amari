class Pokemon:
    def __init__(self, name, id, types):
        self.name = name
        self.id = id
        self.types = types

    def __repr__(self):
        return f"<Pokemon name={self.name}, id={self.id}>"

class Generation:
    def __init__(self, id, name, pokemon_species):
        self.id = id
        self.name = name
        self.pokemon_species = pokemon_species

    def __repr__(self):
        return f"<Generation id={self.id}, name={self.name}>"
