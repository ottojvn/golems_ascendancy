from game.enums import Resources, GolemMaterials

TRANSLATIONS = {
    'en': {
        'day': 'Day',
        'year': 'Year',
        'golems': 'Golems',
        'press_escape': 'Press ESC to exit',
        'resources': {
            Resources.WOOD: 'Wood: Basic material for buildings and tools.',
            Resources.MUD: 'Mud: Used to create basic golems and fertilize crops.',
            Resources.STONE: 'Stone: Durable material for constructions.',
            Resources.GRANITE: 'Granite: Extremely strong for advanced structures.',
            Resources.LIMESTONE: 'Limestone: Used for building and making lime cement.',
            Resources.SANDSTONE: 'Sandstone: Decorative sedimentary rock.',
            Resources.WATER: 'Water: Essential for life, farming, and water golems.',
            Resources.MUSHROOM: 'Mushroom: Food and magical ritual component.',
        },
        'golems': {
            GolemMaterials.WATER: 'Water Golem: Agile, connected to rivers and rain.',
            GolemMaterials.STONE: 'Stone Golem: Strong and resilient in any climate.',
            GolemMaterials.GRANITE: 'Granite Golem: Extremely robust, ideal for buildings.',
            GolemMaterials.LIMESTONE: 'Limestone Golem: Sensitive to water but efficient in dry climates.',
            GolemMaterials.SANDSTONE: 'Sandstone Golem: Fragile but swift for quick tasks.',
            GolemMaterials.COPPER: 'Copper Golem: Conductor of energy, useful for advanced tech.',
            GolemMaterials.TIN: 'Tin Golem: Malleable and corrosion resistant.',
            GolemMaterials.MUD: 'Mud Golem: Versatile and easy to create, ideal for agriculture.',
        }
    },
    'pt': {
        'day': 'Dia',
        'year': 'Ano',
        'golems': 'Golems',
        'press_escape': 'Pressione ESC para sair',
        'resources': {
            Resources.WOOD: 'Madeira: Material básico para construções e ferramentas.',
            Resources.MUD: 'Lama: Usada para criar golems básicos e fertilizar plantações.',
            Resources.STONE: 'Pedra: Material resistente para construções duráveis.',
            Resources.GRANITE: 'Granito: Pedra extremamente resistente para estruturas avançadas.',
            Resources.LIMESTONE: 'Calcário: Usado em construções e para criar cal e cimento.',
            Resources.SANDSTONE: 'Arenito: Pedra sedimentar útil para decoração e esculturas.',
            Resources.WATER: 'Água: Essencial para vida, cultivo e criação de golems aquáticos.',
            Resources.MUSHROOM: 'Cogumelo: Alimento e componente mágico para rituais.',
        },
        'golems': {
            GolemMaterials.WATER: 'Golem de água: Ágil e adaptável, conectado aos rios e chuvas.',
            GolemMaterials.STONE: 'Golem de pedra: Forte e resistente, durável em qualquer clima.',
            GolemMaterials.GRANITE: 'Golem de granito: Extremamente resistente, ideal para construções.',
            GolemMaterials.LIMESTONE: 'Golem de calcário: Sensível à água, mas eficiente em ambientes secos.',
            GolemMaterials.SANDSTONE: 'Golem de arenito: Frágil mas veloz, excelente para tarefas rápidas.',
            GolemMaterials.COPPER: 'Golem de cobre: Condutor de energia, útil para tecnologias avançadas.',
            GolemMaterials.TIN: 'Golem de estanho: Maleável e resistente à corrosão.',
            GolemMaterials.MUD: 'Golem de lama: Versátil e fácil de criar, ideal para cultivo.',
        }
    }
}