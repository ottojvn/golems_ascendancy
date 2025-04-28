from game.date       import init_date, advance_date
from game.resources  import init_resources, update_resources
from game.population import init_population, update_population

def init_state(selected_material):
    return {
        'date':        init_date(),
        'resources':   init_resources(),
        'golem_type':  selected_material,
        'population':  init_population(selected_material),
    }