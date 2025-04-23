from game.population_manager import PopulationManager
from game.resource_manager import ResourceManager


class GameState:
    def __init__(self) -> None:
        self.resource_manager = ResourceManager()
        self.population_manager = PopulationManager()

    def update(self, dt) -> None:
        self.population_manager.update(dt)
        self.resource_manager.update(dt)

    def get_resources(self):
        return self.resource_manager.resources

    def get_population(self):
        return self.population_manager.golem_count
