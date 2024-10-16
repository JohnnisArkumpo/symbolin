print("starting game...")
import pygame as pg

TITLE = "Grid Game"
TILES_HORIZONTAL = 12
TILES_VERTICAL = 12
TILE_SIZE = 80
WINDOW_WIDTH = TILE_SIZE * 12
WINDOW_HEIGHT = TILE_SIZE * 12

class Player:
    def __init__(self, surface):
        self.surface = surface
        self.pos = (40, 40)

    def draw(self):
        pg.draw.circle(self.surface, (0,0,0), self.pos, 30)

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
                    (40, 40, 40),
                    (row * TILE_SIZE, col * TILE_SIZE, TILE_SIZE, TILE_SIZE),
                )
        self.player.draw()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.loop = False
            elif event.type == pg.KEYDOWN:
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
        pg.display.update()

if __name__ == "__main__":
    mygame = Game()
    mygame.main()
