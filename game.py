from graphics import *
import random

makeGraphicsWindow(1000, 800)

class Enemy:
    def __init__(self):
        self.x = random.randint(0, 1000)
        self.y = 0

    def update(self):
        self.y += getWorld().enemySpeed

    def draw(self):
        fillCircle(self.x, self.y, 20, "red")

def createEnemy(world):
    world.enemies.append(Enemy())
    world.lastSpawnedEnemy = getElapsedTime()

def startWorld(world):
    world.playerX = 500
    world.enemies = []
    world.enemySpeed = 1
    world.enemySpawnRate = 2000
    world.lastSpawnedEnemy = 0

def updateWorld(world):
    for enemy in world.enemies:
        enemy.update()
    if getElapsedTime() - world.lastSpawnedEnemy >= world.enemySpawnRate:
        createEnemy(world)
        world.enemySpeed += 0.05
        world.enemySpawnRate *= 0.95

    if isKeyPressed('d'):
        world.playerX += 5
    if isKeyPressed('a'):
        world.playerX -= 5

def drawWorld(world):
    for enemy in world.enemies:
        enemy.draw()
    fillCircle(world.playerX, 720, 30, "dimgrey")

runGraphics(startWorld, updateWorld, drawWorld)
