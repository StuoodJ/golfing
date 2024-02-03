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
    mousepos = pygame.mouse.get_pos()
    ballpos = pygame.Vector2(ballx / 2, bally / 2)
    if mousepos[0] <= ballx + ballr and mousepos[0] >= ballx and mousepos[1] <= bally + ballr and mousepos[1] >= bally:
        ballc = (0, 255, 0)
    else:
        ballc = (255, 0, 0)
    pygame.draw.circle(screen, ballc, ballpos, ballr)
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
