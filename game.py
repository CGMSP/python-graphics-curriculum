from graphics import *

makeGraphicsWindow(1000, 800)

def startWorld(world):
    world.playerX = 500

def updateWorld(world):
    if isKeyPressed('d'):
        world.playerX += 5
    if isKeyPressed('a'):
        world.playerX -= 5

def drawWorld(world):
    fillCircle(world.playerX, 720, 30, "dimgrey")

runGraphics(startWorld, updateWorld, drawWorld)
