# Importing all from circleshape.py as a new class needs to inherit
from circleshape import *

# Importing PLAYER_RADIUS and PLAYER_TURN_SPEED from contstants.py for use here
from constants import PLAYER_RADIUS
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SPEED
from constants import PLAYER_SHOOT_SPEED
from constants import PLAYER_SHOOT_COOLDOWN

# Importing bullets
from shot import *

# The following defines the player class
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0
        return

    # in the player class (code provided by Boot.dev course)
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    # Overriding the draw function from CircleShape
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
        return
    
    # Adding a rotation method
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        return
    
    def update(self, dt):
        self.shot_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
            return
        if keys[pygame.K_d]:
            self.rotate(dt)
            return
        if keys[pygame.K_w]:
            self.move(dt)
            return
        if keys[pygame.K_s]:
            self.move(-dt)
            return
        if keys[pygame.K_SPACE]:
            self.shoot()
        
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.shot_timer <= 0:
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
            self.shot_timer = PLAYER_SHOOT_COOLDOWN
        else:
            pass
