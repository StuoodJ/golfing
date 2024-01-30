# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
dW = 500
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
ballx = 0
bally = 0
ballr = 50
ballc = (255, 0, 0)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    # RENDER YOUR GAME HERE
    ballpos = pygame.Vector2(ballx / 2, bally / 2)
    ball = (screen, ballc, ballpos, ballr)
    pygame.draw.circle(ball)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
