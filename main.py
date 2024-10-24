# print("starting game...")
import pygame as pg

TITLE = "Grid Game"
TILES_HORIZONTAL = 12
TILES_VERTICAL = 12
TILE_SIZE = 80
WINDOW_WIDTH = TILE_SIZE * 12
WINDOW_HEIGHT = TILE_SIZE * 12

class Dot:
    def __init__(self, pos, typep, surface):
        self.pos = pos
        self.typep = typep
        self.surface = surface
    
    def draw(self, surface):
        if self.typep == 'NORMAL':
            pg.draw.circle(self.surface, (255,0,0), self.pos, 25)
        elif self.typep == 'RAMP':
            pg.draw.circle(self.surface, (255,0,255), self.pos, 25)

class Card:
    card_data = {
        "develop": {"display": 110110001, "size": 3, "durability": "depender", "effect1": "elevate any card to effect2", "effect2": "elevate any card to effect3", "effect3": "create beast", "ability": "pwrp ability"},
        "attack": {"display": 100010001, "size": 3, "durability": "temporary", "effect1": "deal one damage to target", "effect2": "deal three damage to any target", "effect3": "deal one damage to any target, become permanent", "ability": "atk ability"},
        "powerup": {"display": 101010101, "size": 3, "durability": "permanent", "effect1": "Double the amount of elixer/pieces gained in a turn", "effect2": "", "effect3": "", "ability": ""},
        "": {"display": 0, "size": 0, "durability": "", "effect1": "", "effect2": "", "effect3": "", "ability": ""},
        "": {"display": 0, "size": 0, "durability": "", "effect1": "", "effect2": "", "effect3": "", "ability": ""},
        "": {"display": 0, "size": 0, "durability": "", "effect1": "", "effect2": "", "effect3": "", "ability": ""},
        "": {"display": 0, "size": 0, "durability": "", "effect1": "", "effect2": "", "effect3": "", "ability": ""},
        "": {"display": 0, "size": 0, "durability": "", "effect1": "", "effect2": "", "effect3": "", "ability": ""}, # four by fours
        "": {"display": 0, "size": 0, "durability": "", "effect1": "", "effect2": "", "effect3": "", "ability": ""},
        "": {"display": 0, "size": 0, "durability": "", "effect1": "", "effect2": "", "effect3": "", "ability": ""},
        "": {"display": 0, "size": 0, "durability": "", "effect1": "", "effect2": "", "effect3": "", "ability": ""}
    }

    def __init__(self, name, attributes):
        self.name = name
        self.display = str(attributes["display"])
        self.size = attributes["size"]
        self.durability = attributes["durability"]
        self.effect1 = attributes["effect1"]
        self.effect2 = attributes["effect2"]
        self.effect3 = attributes["effect3"]
        self.ability = attributes["ability"]

        attributes = Card.card_data.get("none", {"display": 000000000, "size": 3, "durability": "temporary", "effect1": "none", "effect2": "none", "effect3": "none", "ability": "none"})
    
    def draw(self, surface, x, y):
        font = pg.font.Font(None, 36)
        name_surf = font.render(self.name, True, (255, 255, 255))
        surface.blit(name_surf, (x, y))

        grid_x  = x
        grid_y = y + 40
        for i in range(3):
            for j in range(3):
                value = int(self.display[i * 3 + j])
                if value == 1:
                    color = (255, 0, 0)
                elif value == 2:
                    color = (255, 0, 255)
                else:
                    color = (0, 0, 0)
                pg.draw.circle(surface, color, (grid_x+j*30,grid_y+i*30), 10)
        
        effect_surf = font.render(self.effect1, True, (255, 255, 255))
        surface.blit(effect_surf, (x, grid_y+100))

class Player:
    def __init__(self, surface):
        self.pos = (40, 40)
        self.surface = surface
        self.dots = []

    def draw(self):
        pg.draw.circle(self.surface, (0,0,0,255), self.pos, 30, 5)
        for dot in self.dots:
            dot.draw(self.surface)

    def place(self, pos, typep):
        new_dot = Dot(pos, typep, self.surface)
        self.dots.append(new_dot)

    def move(self, direction):
        new_pos = list(self.pos)
        if direction == 'UP':
            new_pos[1] -= TILE_SIZE
        elif direction == 'DOWN':
            new_pos[1] += TILE_SIZE
        elif direction == 'LEFT':
            new_pos[0] -= TILE_SIZE
        elif direction == 'RIGHT':
            new_pos[0] += TILE_SIZE
        if 0 <= new_pos[0] < TILES_HORIZONTAL * TILE_SIZE and 0 <= new_pos[1] < TILES_VERTICAL * TILE_SIZE:
            self.pos = tuple(new_pos)
# As a long-time sixers fan (why), I started load management for myself this year by not watching 1 second of this game.

class Game:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        pg.display.set_caption(TITLE)
        self.surface = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.loop = True
        self.player = Player(self.surface)
        self.player2 = Player(self.surface)
        self.current_typep = 'NORMAL'

        self.cards = [
            Card("develop", Card.card_data["develop"]),
            Card("attack", Card.card_data["attack"]),
            Card("powerup", Card.card_data["powerup"])
        ]

    def main(self):
        while self.loop:
            self.grid_loop()
        pg.quit()

    def grid_loop(self):
        self.surface.fill((0, 0, 100))
        for row in range(TILES_HORIZONTAL):
            for col in range(row % 2, TILES_VERTICAL, 2):
                pg.draw.rect(
                    self.surface,
                    (0,100,0),
                    (row * TILE_SIZE, col * TILE_SIZE, TILE_SIZE, TILE_SIZE),
                )
        self.player.draw()
        self.player2.draw()
        
        if False: # currently making the cards not render for future use
            x, y = 100, 100
            for card in self.cards:
                card.draw(self.surface, x, y)
                y += 150

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.loop = False
            elif event.type == pg.KEYDOWN:
                # current_typep = 'NORMAL'
                if event.key == pg.K_ESCAPE:
                    self.loop = False
                elif event.key == pg.K_w:
                    self.player.move('UP')
                elif event.key == pg.K_s:
                    self.player.move('DOWN')
                elif event.key == pg.K_a:
                    self.player.move('LEFT')
                elif event.key == pg.K_d:
                    self.player.move('RIGHT')
                elif event.key == pg.K_UP:
                    self.player2.move('UP')
                elif event.key == pg.K_DOWN:
                    self.player2.move('DOWN')
                elif event.key == pg.K_LEFT:
                    self.player2.move('LEFT')
                elif event.key == pg.K_RIGHT:
                    self.player2.move('RIGHT')
                elif event.key == pg.K_j:
                    if self.current_typep == 'NORMAL':
                        self.current_typep = 'RAMP'
                    else:
                        self.current_typep = 'NORMAL'
                elif event.key == pg.K_SPACE:
                    player_pos = (self.player.pos[0], self.player.pos[1])
                    self.player.place(player_pos, self.current_typep)
        pg.display.update()

if __name__ == "__main__":
    mygame = Game()
    mygame.main()
