import math
import pygame
from constants import *

pygame.init()

screen = pygame.display.set_mode((INITIAL_SCREEN_SIZE, INITIAL_SCREEN_SIZE), pygame.RESIZABLE)


def get_screen_size():
    return pygame.display.get_surface().get_size()


def radius(initial_radius_in_pseudo_pixels):
    screen_width, screen_height = get_screen_size()

    initial_radius_in_pixels = PSEUDO_PIXEL_SIZE * initial_radius_in_pseudo_pixels

    radius_in_pixels = (initial_radius_in_pixels * min(screen_width, screen_height)) / INITIAL_SCREEN_SIZE

    return radius_in_pixels


def circle_center():
    screen_width, screen_height = get_screen_size()

    center_x = screen_width / 2 - PSEUDO_PIXEL_SIZE / 2
    center_y = screen_height / 2 - PSEUDO_PIXEL_SIZE / 2

    return center_x, center_y


def put_pseudo_pixel(position_x, position_y, color):
    pseudo_pixel = pygame.Rect((position_x, position_y), (PSEUDO_PIXEL_SIZE, PSEUDO_PIXEL_SIZE))
    pygame.draw.rect(screen, color, pseudo_pixel)


def draw_first_circle(circle_position_x, circle_position_y, circle_radius, color):
    current_x = -1 * circle_radius
    while current_x < circle_radius:
        current_y_positive = math.sqrt(circle_radius ** 2 - current_x ** 2)
        current_y_negative = -1 * current_y_positive

        put_pseudo_pixel(circle_position_x + current_x, circle_position_y + current_y_negative, color)
        put_pseudo_pixel(circle_position_x + current_x, circle_position_y + current_y_positive, color)

        current_x += 0.1


def draw_second_circle(circle_position_x, circle_position_y, circle_radius, color):
    angle_in_degrees = 0

    while angle_in_degrees < 360:
        angle_in_radians = angle_in_degrees * PI / 180

        pseudo_pixel_position_x = circle_radius * math.cos(angle_in_radians)
        pseudo_pixel_position_y = circle_radius * math.sin(angle_in_radians)

        angle_in_degrees += 2

        put_pseudo_pixel(circle_position_x + pseudo_pixel_position_x, circle_position_y + pseudo_pixel_position_y,
                         color)


running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    first_circle_radius = radius(INITIAL_FIRST_RADIUS_IN_PSEUDO_PIXELS)
    second_circle_radius = radius(INITIAL_SECOND_RADIUS_IN_PSEUDO_PIXELS)

    x, y = circle_center()

    draw_first_circle(x, y, first_circle_radius, RED)
    draw_second_circle(x, y, second_circle_radius, BLUE)

    pygame.display.flip()

pygame.quit()
