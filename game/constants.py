from game.enums import GolemMaterials, Resources

#
# GAME CONSTANTS
#
INITIAL_POPULATION_CAP = 10
LOGIC_TICK_RATE = 20


#
# GOLEMS
#

GOLEMS_DETAILS = {}

INITIAL_GOLEMS = {
    GolemMaterials.AGUA: 0,
    GolemMaterials.ARENITO: 0,
    GolemMaterials.ESTANHO: 0,
    GolemMaterials.PEDRA: 2,
    GolemMaterials.COBRE: 1,
    GolemMaterials.GRANITO: 0,
    GolemMaterials.LAMA: 3,
    GolemMaterials.CALCARIO: 0,
}

INITIAL_GOLEM_STATS = {"health": 100, "age": 0}


#
# RESOURCES
#
INITIAL_RESOURCES = {
    Resources.COMIDA: 100,
    Resources.PEDRA: 100,
    Resources.LAMA: 100,
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
