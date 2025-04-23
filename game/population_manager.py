import uuid
from typing import Dict, Set

from game.constants import INITIAL_GOLEMS
from game.enums import GolemMaterials
from game.golem import Golem


class PopulationManager:
    def __init__(self) -> None:
        self.golems = dict()
        self.golem_count = {material: 0 for material in GolemMaterials}
        self.idle_golems = set()
        self.working_golems = set()
        init_golems(self)

    def update(self, dt):
        pass

    def create_golem(self, material: GolemMaterials) -> None:
        id = str(uuid.uuid4())
        golem = Golem(id, material)
        self.golems[id] = golem
        self.golem_count[material] += 1
        self.idle_golems.add(id)


def init_golems(population_manager):
    for material in GolemMaterials:
        for _ in range(INITIAL_GOLEMS[material]):
            population_manager.create_golem(material)
