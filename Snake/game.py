from config import Config
from snake import Snake
from apple import Apple
import pygame
import sys


class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(
            (Config.WINDOW_WIDTH, Config.WINDOW_WIDTH))
        self.clock = pygame.time.Clock()
        self.BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
        pygame.display.set_caption('Snake Game')
        self.apple = Apple()
        self.snake = Snake()

    def Grid(self):
        for x in range(0, Config.WINDOW_WIDTH, Config.CELLSIZE):
            pygame.draw.line(self.screen, Config.WHITE,
                             (x, 0), (x, Config.WINDOW_HEIGHT))
        for y in range(0, Config.WINDOW_HEIGHT, Config.CELLSIZE):
            pygame.draw.line(self.screen, Config.WHITE,
                             (0, y), (Config.WINDOW_WIDTH, y))

    def board(self):
        self.screen.fill(Config.BG_COLOR)
        self.Grid()
        pygame.display.update()
        self.clock.tick(Config.FPS)

    def handleKeyEvents(self, event):
        if event.key == pygame.K_ESCAPE:
            pygame.quit()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    self.handleKeyEvents(event)
            self.snake.update(self.apple)
            self.board()
            if self.isGameOver():
                break

        # DISPLAYURF.fill((255, 255, 255))
        # pygame.display.update()
        # CLOCK.tick(60)
