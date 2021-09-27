import sys
import pygame
from pygame.locals import KEYDOWN, K_q

SCREENSIZE = WIDTH, HEIGHT = 500, 600
BLACK_FILLING = (0, 0, 0)
GREY_FILLING = (160, 160, 160)

_VARIABLES = {'surf': False}


def main():
    pygame.init()
    _VARIABLES['surf'] = pygame.display.set_mode(SCREENSIZE)
    while True:
        checkEvents()
        _VARIABLES['surf'].fill(GREY_FILLING)
        makeGrid(50)
        pygame.display.update()


def makeGrid(divides_into_a_greed):
    CONTAINER_WIDTH_AND_HEIGHT = 1000
    coordinate_x, coordinate_y = 0, 0

    pygame.draw.line(
        _VARIABLES['surf'], BLACK_FILLING,
        (coordinate_x, coordinate_y),
        (CONTAINER_WIDTH_AND_HEIGHT + coordinate_x, coordinate_y), 2)

    pygame.draw.line(
        _VARIABLES['surf'], BLACK_FILLING,
        (coordinate_x, CONTAINER_WIDTH_AND_HEIGHT + coordinate_y),
        (CONTAINER_WIDTH_AND_HEIGHT + coordinate_x, CONTAINER_WIDTH_AND_HEIGHT + coordinate_y), 2)

    pygame.draw.line(
        _VARIABLES['surf'], BLACK_FILLING,
        (coordinate_x, coordinate_y),
        (coordinate_x, coordinate_y + CONTAINER_WIDTH_AND_HEIGHT), 2)

    pygame.draw.line(
        _VARIABLES['surf'], BLACK_FILLING,
        (CONTAINER_WIDTH_AND_HEIGHT + coordinate_x, coordinate_y),
        (CONTAINER_WIDTH_AND_HEIGHT + coordinate_x, CONTAINER_WIDTH_AND_HEIGHT + coordinate_y), 2)

    cellSize = CONTAINER_WIDTH_AND_HEIGHT / divides_into_a_greed

    for x in range(divides_into_a_greed):
        pygame.draw.line(
            _VARIABLES['surf'], BLACK_FILLING,
            (coordinate_x + (cellSize * x), coordinate_y),
            (coordinate_x + (cellSize * x), CONTAINER_WIDTH_AND_HEIGHT + coordinate_y), 2)

        pygame.draw.line(
            _VARIABLES['surf'], BLACK_FILLING,
            (coordinate_x, coordinate_y + (cellSize * x)),
            (coordinate_x + CONTAINER_WIDTH_AND_HEIGHT, coordinate_y + (cellSize * x)), 2)


def checkEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_q:
            pygame.quit()
            sys.exit()


if __name__ == '__main__':
    main()
