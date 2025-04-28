from game.constants import INITIAL_GOLEMS

def init_population(material):
    """Inicializa população com contador de golems de um único material"""
    return {'material': material, 'count': INITIAL_GOLEMS.get(material, 0)}

def update_population(pop, dt):
    """Atualiza população de golems usando pop['material'] e dt"""
    material = pop['material']
    count = pop['count']
    return {'material': material, 'count': count}