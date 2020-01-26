from graphics import *
import random, math, sys

makeGraphicsWindow(1000, 800)
setWindowTitle('Demo Game')


def startWorld(world):
    # Set background
    setBackground((69, 69, 69))
    # Declare variables
    world.playerX = 500
    world.enemies = []
    world.bullets = []
    world.enemySpeed = 1
    world.enemySpawnRate = 2000
    world.lastSpawnedEnemy = 0
    # Load images
    world.playerImage = loadImage('assets/player.png', scale=0.2)
    world.enemyImage = loadImage('assets/enemy.png', scale=0.1)
    world.bulletImage = loadImage('assets/bullet.png', scale=0.1)
    # Create listener for space key
    onKeyPress(shootBullet, 'space')


class Enemy:
    def __init__(self):
        self.x = random.randint(0, 1000)
        self.y = 0

    def update(self, world):
        # Move enemy down
        self.y += world.enemySpeed
        # Check if enemy hit the bottom of the screen
        if self.y >= 670:
            print('You died!')
            sys.exit()
        # Figure out if enemy gets shot
        for bullet in world.bullets:
            # Pythagorean theorem to calculate collisions
            distanceToBullet = math.sqrt(
                ((self.x - bullet.x) ** 2) +
                ((self.y - bullet.y) ** 2)
            )
            # Enemy size plus bullet size
            if distanceToBullet <= 40:
                return True
        return False

    def draw(self):
        # fillCircle(self.x, self.y, 30, "crimson")
        drawImage(getWorld().enemyImage, self.x, self.y)

class Bullet:
    def __init__(self):
        self.x = getWorld().playerX
        self.y = 750

    def update(self):
        self.y -= 8

    def draw(self):
        # fillCircle(self.x, self.y, 10, "black")
        drawImage(getWorld().bulletImage, self.x, self.y)

def createEnemy(world):
    world.enemies.append(Enemy())
    world.lastSpawnedEnemy = getElapsedTime()

def shootBullet(world):
    world.bullets.append(Bullet())



def updateWorld(world):
    # Update enemies
    for enemy in world.enemies:
        if enemy.update(world):
            world.enemies.remove(enemy)
    # Update bullets
    for bullet in world.bullets:
        bullet.update()
    # Spawn new enemies
    if getElapsedTime() - world.lastSpawnedEnemy >= world.enemySpawnRate:
        createEnemy(world)
        world.enemySpeed += 0.05
        world.enemySpawnRate *= 0.95
    # Move player
    if isKeyPressed('d') and world.playerX <= 960:
        world.playerX += 8
    if isKeyPressed('a') and world.playerX >= 40:
        world.playerX -= 8

def drawWorld(world):
    drawLine(0, 700, 1000, 700, thickness=5)
    # Draw bullets
    for bullet in world.bullets:
        bullet.draw()
    # Draw enemies
    for enemy in world.enemies:
        enemy.draw()
    # Draw player
    # fillCircle(world.playerX, 750, 40, "black")
    drawImage(world.playerImage, world.playerX, 750)

# Start the game
runGraphics(startWorld, updateWorld, drawWorld)
