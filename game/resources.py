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

def add_resource(resources, kind, amount):
    r = dict(resources)
    r[kind] = {**r[kind], 'quantity': r[kind]['quantity'] + amount}
    return r

def consume_resource(resources, kind, amount):
    return add_resource(resources, kind, -amount)