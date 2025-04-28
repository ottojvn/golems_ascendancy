import pygame

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#').lstrip('0x')
    if len(hex_color) not in (3, 4, 6, 8):
        raise ValueError(f"Invalid hex color string: '{hex_color}'")
    if len(hex_color) in (3, 4):
        hex_color = ''.join([c * 2 for c in hex_color])
    try:
        red = int(hex_color[0:2], 16)
        green = int(hex_color[2:4], 16)
        blue = int(hex_color[4:6], 16)
    except ValueError:
        raise ValueError(f"Invalid hex color string: '{hex_color}'")
    return (red, green, blue)


def load_img(path, pos, mpos):
    path = "sprites/"+path+".png"
    img = pygame.image.load(path).convert()
    img = pygame.transform.scale(img,
                                 (img.get_width() * 2,
                                  img.get_height() * 2))
    img.set_colorkey((0, 0, 0))

    screen.blit(img, pos)
    
    hitbox = pygame.Rect(pos[0], pos[1], img.get_width(), img.get_height())
    collision = hitbox.collidepoint(mpos)
    return {"hitbox": hitbox, "collision": collision}


def layout(sprites, left, top, width, height, mpos):
    first = "sprites/"+sprites[0]+".png"
    img_dim = pygame.image.load(first).convert().get_height() * 2
    rows = int(height / img_dim)
    padding = (height % img_dim) / (rows + 1)

    x = left + padding
    y = top + padding
    space = img_dim + padding

    column = 0
    collisions = []

    for n, i in enumerate(sprites):
        if type(i) != str:
            collisions.append(False)
            continue
        
        collisions.append(load_img(i, (x + int(n/rows) * space, y + n%rows * space), mpos)["collision"])

    if True in collisions:
        mouse_over = sprites[collisions.index(True)]
    else:
        mouse_over = None
    return mouse_over




pygame.init()

dim = (1280, 720)
screen = pygame.display.set_mode(dim)
pygame.display.set_caption("Golems Ascendancy")


running = True
clock = pygame.time.Clock()
delta_time = 0.1

font = pygame.font.Font(None, size=30)




# Loop
while running:
    # Clean everything from last frame
    screen.fill((63, 63, 63))
    # Mouse position
    mpos = pygame.mouse.get_pos()
    
    # Rectangle
    materials = pygame.Rect(0, 0, dim[0], dim[1]/4)
    materials_col = materials.collidepoint(mpos)
    pygame.draw.rect(screen, (127, 127, 127), materials)

    log = pygame.Rect(dim[0]*3/4, dim[1]/4, dim[0]/4, dim[1]*3/4)
    log_col = log.collidepoint(mpos)
    pygame.draw.rect(screen, (31, 31, 31), log)

    area = pygame.Rect(0, dim[1]/4, dim[0]*3/4, dim[1]*3/4)
    area_col = log.collidepoint(mpos)
    pygame.draw.rect(screen, (63, 63, 63), area)

    # Blits
    sprites = ["chaos", "creativity", "justice", "health", 0, "astronomy", "courage", "dominance", "happiness", 
               0, 0, 0, 0, "golem", 0, 0, "damaged_golem", 
               0, 0, 0, 0, "water", "mud", "wood", "stone", "sandstone", "granite", "limestone", 
               0, 0, 0, 0, 0, "tin_ore", "copper_ore", "iron_ore", "coal", "gold_ore", "platinum_ore", "chrome_ore", "aluminum_ore", "titanium_ore", "uranium_ore", "nickel_ore", 
               0, 0, 0, 0, "bronze_ingot", "iron_ingot", "steel_ingot", "stainless_steel_ingot", "superalloy_ingot"]
    
    mouse_over = layout(sprites, 0, 0, dim[0], dim[1]/4, mpos)

    text = font.render(mouse_over, True, (255, 255, 255))
    screen.blit(text, (dim[0]*3/4 + 9, dim[1]/4 + 9))

    # Event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Framerate
    pygame.display.flip()
    delta_time = clock.tick(60) / 1000
    delta_time = max(0.001, min(0.1, delta_time))
pygame.quit()
