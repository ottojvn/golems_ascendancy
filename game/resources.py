from game.constants import INITIAL_RESOURCES
from game.enums     import Resources

def init_resources():
    return {
        r: {'description': r.value, 'quantity': INITIAL_RESOURCES.get(r, 0)}
        for r in Resources
    }

def update_resources(resources, dt):
    # exemplo: nada muda por enquanto
    return resources