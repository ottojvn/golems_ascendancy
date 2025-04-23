from game.constants import INITIAL_RESOURCES
from game.enums import Resources


class ResourceManager:
    def __init__(self):
        self.resources = init_resources()

    def update(self, dt):
        pass


def init_resources():
    resources = dict()
    for resource in Resources:
        if resource in INITIAL_RESOURCES.keys():
            resources[resource] = INITIAL_RESOURCES[resource]
        else:
            resources[resource] = 0
    return resources
