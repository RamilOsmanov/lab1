import pygame
import sys
import time

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

clock_image = pygame.image.load("/mnt/data/clock.png")
minute_hand = pygame.image.load("/mnt/data/min_hand.png")
second_hand = pygame.image.load("/mnt/data/sec_hand.png")

clock_rect = clock_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    minute_angle = -((minutes % 60) * 6)
    second_angle = -((seconds % 60) * 6)

    rotated_minute = pygame.transform.rotate(minute_hand, minute_angle)
    rotated_second = pygame.transform.rotate(second_hand, second_angle)

    minute_rect = rotated_minute.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    second_rect = rotated_second.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    screen.blit(clock_image, clock_rect)
    screen.blit(rotated_minute, minute_rect)
    screen.blit(rotated_second, second_rect)

    pygame.display.flip()
    pygame.time.Clock().tick(30)