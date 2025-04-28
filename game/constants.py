from game.enums import GolemMaterials, Resources

#
# GAME CONSTANTS
#
INITIAL_POPULATION_CAP = 10
LOGIC_TICK_RATE = 20
GAME_START_DAY = 1
GAME_START_YEAR = 1
GAME_DAYS_IN_YEAR = 365
SECONDS_PER_DAY = 2  # real seconds that correspond to one in-game day

#
# GOLEMS
#

INITIAL_GOLEMS = {
    GolemMaterials.WATER: 0,
    GolemMaterials.SANDSTONE: 0,
    GolemMaterials.TIN: 0,
    GolemMaterials.STONE: 0,
    GolemMaterials.COPPER: 0,
    GolemMaterials.GRANITE: 0,
    GolemMaterials.MUD: 5,
    GolemMaterials.LIMESTONE: 0,
}


#
# RESOURCES
#

INITIAL_RESOURCES = {
    Resources.WOOD: 50,
    Resources.MUD: 100,
    Resources.STONE: 30,
    Resources.GRANITE: 10,
    Resources.LIMESTONE: 15,
    Resources.SANDSTONE: 20,
    Resources.WATER: 80,
    Resources.MUSHROOM: 25,
}

# Resource icons placeholders (to be replaced with actual icons)
RESOURCE_ICONS = {
    Resources.WOOD: "[W]",
    Resources.MUD: "[M]",
    Resources.STONE: "[S]",
    Resources.GRANITE: "[G]",
    Resources.LIMESTONE: "[L]",
    Resources.SANDSTONE: "[Sd]",
    Resources.WATER: "[Wt]",
    Resources.MUSHROOM: "[Mh]",
}

#
# ATTRIBUTES
#
ATTRIBUTES = {
    "Caos",
    "Sabedoria",
    "Fe",
    "Saude",
    "Astronomia",
    "Coragem",
    "Dominio",
    "Felicidade",
}

INITIAL_ATTRIBUTES = {
    "Caos": 0,
    "Sabedoria": 0,
    "Fe": 3,
    "Saude": 3,
    "Astronomia": 0,
    "Coragem": 2,
    "Dominio": 0,
    "Felicidade": 1,
}

#
# CONSTRUÇÕES
#


#
# TECH
#
