from game.constants import INITIAL_GOLEMS

def init_population(material):
    """Initializes population with total and available counts."""
    count = INITIAL_GOLEMS.get(material, 0)
    return {'material': material, 'total': count, 'available': count}

def update_population(pop, dt):
    """Placeholder for future population updates (births, deaths)."""
    # Currently, only allocation/deallocation changes counts.
    # This function might handle things like golem creation/destruction later.
    return pop # No changes based on time yet