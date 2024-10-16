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


class Player:
    def __init__(self, surface):
        self.pos = (40, 40)
        self.surface = surface
        self.dots = []

    def draw(self):
        pg.draw.circle(self.surface, (0,0,0,255), self.pos, 30)
        for dot in self.dots:
            dot.draw(self.surface)

    def place(self, pos, typep):
        new_dot = Dot(pos, typep)
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
    

class Game:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        pg.display.set_caption(TITLE)
        self.surface = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.loop = True
        self.player = Player(self.surface)

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
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.loop = False
            elif event.type == pg.KEYDOWN:
                current_typep = 'NORMAL'
                if event.key == pg.K_ESCAPE:
                    self.loop = False
                elif event.key == pg.K_UP:
                    self.player.move('UP')
                elif event.key == pg.K_DOWN:
                    self.player.move('DOWN')
                elif event.key == pg.K_LEFT:
                    self.player.move('LEFT')
                elif event.key == pg.K_RIGHT:
                    self.player.move('RIGHT')
                elif event.key == pg.K_f:
                    if current_typep == 'NORMAL':
                        current_typep = 'RAMP'
                    else:
                        current_typep = 'NORMAL'
                elif event.key == pg.K_SPACE:
                    player_pos = (self.player.pos[0], self.player.pos[1])
                    self.player.place(player_pos, current_typep)
        pg.display.update()

if __name__ == "__main__":
    mygame = Game()
    mygame.main()
