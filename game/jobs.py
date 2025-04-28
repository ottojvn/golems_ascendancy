from game.enums import Jobs, Resources
from game.constants import BASE_GATHERING_RATE

def init_jobs():
    """Initializes the jobs state with default values."""
    return {
        Jobs.GATHERER: {
            'assigned_golems': 0,
            # Define which resources this job can gather
            'target_resources': [
                Resources.WOOD,
                Resources.MUD,
                Resources.STONE,
                Resources.GRANITE,
                Resources.LIMESTONE,
                Resources.SANDSTONE,
                Resources.WATER,
                Resources.MUSHROOM
            ]
        }
        # Add other job types here later
    }

def allocate_golem_to_job(state, job_type, num_golems):
    """Allocates a number of available golems to a specific job."""
    if job_type not in state['jobs']:
        print(f"Error: Job type {job_type} not found.")
        return False

    available_golems = state['population']['available']
    if num_golems > available_golems:
        print(f"Error: Not enough available golems. Tried to allocate {num_golems}, but only {available_golems} available.")
        return False

    state['population']['available'] -= num_golems
    state['jobs'][job_type]['assigned_golems'] += num_golems
    print(f"Allocated {num_golems} golems to {job_type.value}. Available: {state['population']['available']}")
    return True

def deallocate_golem_from_job(state, job_type, num_golems):
    """Deallocates a number of golems from a specific job back to the available pool."""
    if job_type not in state['jobs']:
        print(f"Error: Job type {job_type} not found.")
        return False

    assigned_to_job = state['jobs'][job_type]['assigned_golems']
    if num_golems > assigned_to_job:
        print(f"Error: Not enough golems assigned to {job_type.value}. Tried to deallocate {num_golems}, but only {assigned_to_job} assigned.")
        return False

    state['jobs'][job_type]['assigned_golems'] -= num_golems
    state['population']['available'] += num_golems
    print(f"Deallocated {num_golems} golems from {job_type.value}. Available: {state['population']['available']}")
    return True

def calculate_resource_gain(jobs_state, population_state):
    """Calculates the total resources gained per day based on assigned golems."""
    gains = {res: 0 for res in Resources} # Initialize gains for all resources

    # --- Gatherer Job --- 
    gatherer_job = jobs_state.get(Jobs.GATHERER)
    if gatherer_job:
        num_gatherers = gatherer_job['assigned_golems']
        # For now, assume all gatherers collect all target resources at a base rate
        # This could be refined later based on golem type, terrain, etc.
        rate = BASE_GATHERING_RATE.get(population_state['material'], 1) # Get material-specific rate or default
        
        for resource in gatherer_job.get('target_resources', []):
            # Ensure the gain is an integer
            gains[resource] += int(num_gatherers * rate) 

    # --- Add calculations for other jobs here --- 

    return gains
