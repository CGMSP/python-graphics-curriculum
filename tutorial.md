# Explanation of [python game](game.py) 
By Kaz Malhotra   
This is the explanation/tutorial/curriculum for [game.py](game.py)    
Let's start at the beginning.     

## Importing modules   
```
from graphics import *
import random, math, sys
```
Just as you can import a module like pygame or numpy installed with pip, you can also import a python file in the same directory as the program you are writing. Here, you will import `random`, `math`, `sys`, and [graphics.py](graphics.py)        

## Creating a window   
Here we are using the "graphics" library, in which the makeGraphicsWindow() function is defined.  setWindowTitle is used to the title of the window, the text at the top of the window. We create a window that is 800 pixels vertically, and 1,000 pixels horizontally. The default is 'pygame window', but we want a different title. Here, we use the example 'demo game', but you can change it to whatever you want.      

```
makeGraphicsWindow(1000, 800)
setWindowTitle('Demo Game')

```

## Starting the world    
Here, we define a bunch of variables mentioned later, such as the images for the enemies and bullets, and the lists of enemies and bullets that get appended to.


```

def startWorld(world):
    # Set background
    setBackground((70, 70, 70))
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



```


We also define the background to a dark grey, (an rgb of 69, 69, 69). We define the variable 'playerX' (used as the player's x axis) to 500 (the middle of the window as the window's width is 1,000 pixels). 
We define empty lists of enemies and bullets. These will be appended to later.
We set the enemy speed to 1, and increase it gradually in the updateWorld function. We set the enemy spawn rate to 2,000, which also increases in the updateWorld function. The reason we add to these variables is to make it more difficult for the player. 
We define the variables for the images for the player, bullet, and enemies. 

## Enemies   
Here we create a class called "Enemy" where we first define the function "\_\_init\_\_" with the parameter "self". We tell the enemy to spawn at the top of the screen, (0 on the y axis), and randomly horizontally (0 to 1,000 on the x axis).    


```
class Enemy:
    def __init__(self):
        self.x = random.randint(0, 1000)
        self.y = 0

```

### Updating the enemies
Here we define a function where we update the enemies.     

```     

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

```


First, we move the enemy down by updating it's position on the y axis by adding it to the enemySpeed. Next, if we find that the enemy's position on the y is below the border, in the terminal. print 'you died' and exit the game.
We then use the pythagorean theorem which says that in a triangle, a squared plus b squared equals c squared, or c = the square root of (a squared plus b squared), to figure out if the enemy is in the same space as a bullet, in which case, the enemy dies.     
### Drawing the enemy
Now, we define a function to draw the enemy called draw, with the parameter of self.     

```
def draw(self):
    # fillCircle(self.x, self.y, 30, "crimson")
    drawImage(getWorld().enemyImage, self.x, self.y)

```
We use the function 'drawImage' to draw the enemy with the image 'enemyImage' (defined earlier in the program as [assets/enemy.png](assets/enemy.png)), in the position of the enemy.

## Bullets
We now create a class called 'bullet' and define a function initializing the bullet (called \_\_init\_\_ with the parameter of self) where we set the x axis to there the player is, and the y to 750, this will later be updated as we make the bullet move.

```
class Bullet:
    def __init__(self):
        self.x = getWorld().playerX
        self.y = 750

```

### Moving the bullets     
We now define a function where we move the bullet up by 8 pixels (by subtracting 8 pixels from the bullet's y axis)

```
def update(self):
    self.y -= 8
```

### Drawing the bullets     
Here we define the function 'draw' with the parameter 'self' where we again use the function 'drawImage' with the image 'bulletImage' (defined earlier as [assets/bullet.png](assets/bullet.png)) in the position where we know the bullet is.

```
def draw(self):
    # fillCircle(self.x, self.y, 10, "black")
    drawImage(getWorld().bulletImage, self.x, self.y)

```



## Create enemies    
Here, we define a function called createEnemy with the parameter 'world' where we append 'Enemy' to the list world.enemies. We also set the variable 'world.lastSpawnedEnemy' to the elapsed time.

```

def createEnemy(world):
    world.enemies.append(Enemy())
    world.lastSpawnedEnemy = getElapsedTime()


```


## Shooting Bullets    

Here we make a function that simply appends 'Bullet' to a list called 'world.bullets'. 

```

def shootBullet(world):
    world.bullets.append(Bullet())

```


## Updating the world
Here, we define the function that updates the world. We first update the enemies and the bullets. We use the 'update' function in the 'bullet' class to update the bullets.     


```
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


```


Now, we check if the d of a key is pressed to move the player. This is fairly simple. D is to go right, and therefor, we add 8 to the player's x axis to make the player move 8 pixels to the right. This is the same with left, except it's the a key and subtracting 8 from player's x rather than adding it.

## Drawing the world
Here we define the function to draw the world. We draw the line near the bottom of the screen, indicating how far the enemies can go before they kill you. Then, for every enemy that exists, we draw the enemies. We then draw the player by drawing the player's image (assets/player.png) in the right position.

```

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


``` 


## Starting the game
In the 'graphics' library, there is a function called 'runGraphics'. To run our functions with the 'graphics' library, we need to use them as parameters with the 'runGraphics' library.

```
runGraphics(startWorld, updateWorld, drawWorld)


```
