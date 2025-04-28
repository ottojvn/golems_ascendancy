from game.constants import INITIAL_RESOURCES
from game.enums     import Resources
from game.jobs      import calculate_resource_gain # Import calculation function

def init_resources():
    return {
        r: {'description': r.value, 'quantity': INITIAL_RESOURCES.get(r, 0)}
        for r in Resources
    }

def update_resources(state, dt):
    """Updates resource quantities based on job outputs over dt days."""
    resources = state['resources']
    jobs_state = state['jobs']
    population_state = state['population']

    # Calculate gains per day based on current job assignments
    daily_gains = calculate_resource_gain(jobs_state, population_state)

    # Apply gains for the number of days passed (dt)
    for resource, gain in daily_gains.items():
        if resource in resources:
            resources[resource]['quantity'] += gain * dt
        else:
            # Handle case where a new resource type might be gathered
            print(f"Warning: Gathered unexpected resource type {resource}")
            # Optionally initialize it: resources[resource] = {'description': resource.value, 'quantity': gain * dt}

    # Placeholder for other resource changes (consumption, decay, etc.)
    
    return resources