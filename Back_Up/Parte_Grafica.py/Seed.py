import pygame

# initialize Pygame
pygame.init()

# set the window size and create a Pygame window
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# set the colors of the pits and the seeds
pit_color = (0, 0, 255)  # blue
seed_color = (255, 255, 255)  # white

# set the size of the pits and the seeds
pit_width, pit_height = 100, 100
seed_radius = 10

# create a Mancala board with 6 pits on each side
board = [[4, 4, 4, 4, 4, 4], [4, 4, 4, 4, 4, 4]]

# draw the pits and seeds on the Pygame window
x_offset = 50
y_offset = 50
for i in range(2):
    for j in range(6):
        pygame.draw.rect(screen, pit_color, (x_offset, y_offset, pit_width, pit_height))
        seeds = board[i][j]
        for k in range(seeds):
            seed_x = x_offset + pit_width // 2 + (k % 3 - 1) * seed_radius * 2
            seed_y = y_offset + pit_height // 2 + (k // 3 - 1) * seed_radius * 2
            pygame.draw.circle(screen, seed_color, (seed_x, seed_y), seed_radius)
        x_offset += pit_width + 10
    y_offset += pit_height + 10
    x_offset = 50

# update the Pygame window
pygame.display.flip()

# run the Pygame loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# quit Pygame
pygame.quit()