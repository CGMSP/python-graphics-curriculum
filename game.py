from graphics import *
import random

makeGraphicsWindow(1000, 800)

class Enemy:
    def __init__(self):
        self.x = random.randint(0, 1000)
        self.y = 0

    def update(self):
        self.y += 2
        if self.y >= 800:
            del self

    def draw(self):
        fillCircle(self.x, self.y, 20, "red")

def startWorld(world):
    world.playerX = 500
    world.enemies = []
    for i in range(5):
        world.enemies.append(Enemy())

def updateWorld(world):
    for enemy in world.enemies:
        enemy.update()

    if isKeyPressed('d'):
        world.playerX += 5
    if isKeyPressed('a'):
        world.playerX -= 5

def drawWorld(world):
    for enemy in world.enemies:
        enemy.draw()

    fillCircle(world.playerX, 720, 30, "dimgrey")

runGraphics(startWorld, updateWorld, drawWorld)
