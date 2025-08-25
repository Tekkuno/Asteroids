# Imports for the pygame library, constants.py, and player.py
import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    # Initialize the imported pygame modules
    pygame.init()

    # Print boot messages to screen
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Create the game window, add the clock for FPS control, and set the delta time (dt)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Creating groups to keep the loop tidy and adding the player to them
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)

    # Creating the player before the main loop (it was in before, that resets the rotation due to repeatedly calling the constructor)
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    # Creating an instance of the asteroid field
    field = AsteroidField()

    # The gamestate variable is used as a emergency stop button
    # Standard state is "running" but other states can be set to break the while loop
    gamestate = "running"
    while gamestate == "running":

        # This segment checks if the game window is closed by the user
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # While the gamestate change should not be necessary, it is there as a backup
                gamestate = "closed"
                return
            
        # This fills the game window with a black color
        screen.fill("black")

        # This updates all items on the screen
        updatable.update(dt)

        # This checks for collision between the player and asteroids
        for rock in asteroids:
            if player.collision(rock) == True:
                print("Game over!")
                sys.exit()
            else:
                pass

        # This draws all the items on the screen
        for item in drawable:
            item.draw(screen)

        # This updates the game window
        pygame.display.flip()

        # This sets the framerate to 60 FPS by pausing the loop 1/60 of a second and it feeds the return into dt
        dt = clock.tick(10) / 1000



if __name__ == "__main__":
    main()
