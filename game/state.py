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

def update_state(state, dt):
    return {
        **state,
        'date':       advance_date(state['date'], dt),
        'resources':  update_resources(state['resources'], dt),
        'population': update_population(state['population'], dt),
    }

def get_resources(state):
    return state['resources']

def get_population(state):
    return state['population']

def get_date(state):
    return state['date']