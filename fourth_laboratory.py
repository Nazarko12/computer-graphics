from math import pi, sin, cos
import pygame

TITLE = 'Lab 4'
FPS = 60

GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

TRAJECTORY_RADIUS = 100
ELLIPSE_SIZE = {
    'Rx': 60,
    'Ry': 30,
    'rx': 20,
    'ry': 10,
}


def main():
    fps_clock = pygame.time.Clock()
    pygame.init()

    screensize = (width, height) = (500, 300)
    screen = pygame.display.set_mode(screensize)
    pygame.display.set_caption(TITLE)

    center = (int(width / 2), int(height / 2))
    coordinates = start_coordinates = [0, -TRAJECTORY_RADIUS]
    phi = 0.
    step = 0.05

    is_running = True
    while is_running:
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

        animate_ellipse(
            screen=screen,
            coordinates=(
                int(coordinates[0] + center[0]),
                int(coordinates[1] + center[1]),
            ),
            phi=phi,
        )

        coordinates = [
            cos(phi) * start_coordinates[0] - sin(phi) * start_coordinates[1],
            sin(phi) * start_coordinates[0] + cos(phi) * start_coordinates[1],
        ]

        phi += step
        if phi >= 2 * pi:
            phi = 0

        pygame.display.update()
        fps_clock.tick(FPS)


def animate_ellipse(screen, coordinates, phi):
    # Normalize phi from (0, 2 * pi) to (0, 1)
    # where 0 is top/bottom and 1 is left/right
    phi = phi if phi < pi else phi - pi
    phi -= pi / 2  # phi in (- pi / 2, pi / 2)
    phi *= 2 / pi  # phi in (-1, 1)
    phi = abs(phi)
    scale = 1 - phi

    x_radius = ELLIPSE_SIZE['rx'] + (ELLIPSE_SIZE['Rx'] - ELLIPSE_SIZE['rx']) * scale
    y_radius = ELLIPSE_SIZE['ry'] + (ELLIPSE_SIZE['Ry'] - ELLIPSE_SIZE['ry']) * scale

    ellipse_size = pygame.Rect(
        coordinates[0] - x_radius,
        coordinates[1] - y_radius,
        x_radius * 2,
        y_radius * 2,
    )
    pygame.draw.ellipse(screen, GREEN, ellipse_size)


if __name__ == '__main__':
    main()