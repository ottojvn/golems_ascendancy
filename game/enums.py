from enum import Enum


class Resources(Enum):
    WOOD = "wood"
    MUD = "mud"
    STONE = "stone"
    GRANITE = "granite" 
    LIMESTONE = "limestone"
    SANDSTONE = "sandstone"
    WATER = "water"
    MUSHROOM = "mushroom"


class GolemMaterials(Enum):
    WATER = "water"
    STONE = "stone"
    GRANITE = "granite"
    LIMESTONE = "limestone"
    SANDSTONE = "sandstone"
    COPPER = "copper"
    TIN = "tin"
    MUD = "mud"


class Jobs(Enum):
    GATHERER = "gatherer"
    # Add other jobs here later
