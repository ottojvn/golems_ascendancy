from game.date       import init_date, advance_date
from game.resources  import init_resources, update_resources
from game.population import init_population, update_population
from game.jobs       import init_jobs # Import job initialization

def init_state(selected_material):
    population_state = init_population(selected_material)
    return {
        'date':        init_date(),
        'resources':   init_resources(),
        'golem_type':  selected_material, # Keep track of the primary golem type
        'population':  population_state,
        'jobs':        init_jobs() # Initialize the jobs structure
    }