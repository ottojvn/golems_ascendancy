from game.constants import INITIAL_GOLEM_STATS
from game.enums import GolemMaterials


class Golem:
    def __init__(self, id: str, material: GolemMaterials):
        self.id = id
        self.health = INITIAL_GOLEM_STATS["health"]
        self.age = INITIAL_GOLEM_STATS["age"]
        self.material = material
