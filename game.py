from graphics import *
import random, math, sys


windowX = 1000 # int(sys.argv[1])
windowY = 800 # int(sys.argv[2])

makeGraphicsWindow(windowX, windowY)
setWindowTitle('Demo Game')

class Enemy:
    def __init__(self):
        self.x = random.randint(40, windowX - 40)
        self.y = 0

    def update(self, world):
        # Move enemy down
        self.y += world.enemySpeed
        # Check if enemy hit the bottom of the screen
        if self.y >= windowY - 130:
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
        self.y = windowY - 50

    def update(self):
        self.y -= 8

    def draw(self):
        # fillCircle(self.x, self.y, 10, "black")
        drawImage(getWorld().bulletImage, self.x, self.y)

def startWorld(world):
    # Set background
    setBackground((70, 70, 70))
    # Declare variables
    world.playerX = windowX / 2
    world.playerY = windowY - 50
    world.score = 0
    world.enemies = []
    world.bullets = []
    world.enemySpeed = 1
    world.enemySpawnRate = 2000
    world.lastSpawnedEnemy = 0
    # Load images
    world.playerImage = loadImage('assets/player.png', scale=0.8)
    world.enemyImage = loadImage('assets/enemy.png', scale=0.1)
    world.bulletImage = loadImage('assets/bullet.png', scale=0.03)
    # Create listener for space key
    onKeyPress(shootBullet, 'space')

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
            world.score += 100
    # Update bullets
    for bullet in world.bullets:
        bullet.update()
    # Spawn new enemies and increase speed + spawn rate
    if getElapsedTime() - world.lastSpawnedEnemy >= world.enemySpawnRate:
        createEnemy(world)
        world.enemySpeed += 0.05
        world.enemySpawnRate *= 0.95
    # Move player
    if isKeyPressed('d') and world.playerX <= windowX - 40:
        world.playerX += 8
    if isKeyPressed('a') and world.playerX >= 40:
        world.playerX -= 8


def drawWorld(world):
    lineY = windowY - 100
    drawLine(0, lineY, windowX, lineY, thickness=5)
    # Draw bullets
    for bullet in world.bullets:
        bullet.draw()
    # Draw enemies
    for enemy in world.enemies:
        enemy.draw()
    # Draw player
    # fillCircle(world.playerX, 750, 40, "black")
    drawImage(world.playerImage, world.playerX, world.playerY)
    drawString("Score: " + str(world.score), 10, 10, size=50)

# Start the game
runGraphics(startWorld, updateWorld, drawWorld)
