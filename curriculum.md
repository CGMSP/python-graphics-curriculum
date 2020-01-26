# Explanation of [python game](game.py)    
This is the explanation/toutorial/curriculum for [game.py](game.py)    
Let's start at the beginning.     

## Importing modules   
```
from graphics import *
import random, math, sys
```
Just as you can import a module like pygame or numpy installed with pip, you can also import a python file in the same directory as the program you are writing. Here, you will import random, math, sys, and [graphics.py](graphics.py)        

## Creating a window   
Here we are using the "graphics" library, in which the makeGraphicsWindow() function is defined.  setWindowTitle is used to the title of the window, the text at the top of the window. We create a window that is 800 pixels vertically, and 1,000 pixels horizontally. The default is 'pygame window', but we want a different title. Here, we use the example 'demo game', but you can change it to whatever you want.      

```
makeGraphicsWindow(1000, 800)
setWindowTitle('Demo Game')

```

## Enemies   
Here we create a class called "Enemy" where we first define the function "__init__" with the parameter "self". We tell the enemy to spawn at the top of the screen, (0 on the y axis), and randomly horizontally (0 to 1,000 on the x axis).    


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
We use the function 'drawImage' to draw the enemy with the image 'enemyImage' (which gets defined later in the program as [assets/enemy.png](assets/enemy.png)), in the position of the enemy.

## Bullets
We now create a class called 'bullet' and define a function initializing the bullet (called __init__ with the parameter of self) where we set the x axis to there the player is, and the y to 750, this will later be updated as we make the bullet move.

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
Here we define the function 'draw' with the parameter 'self' where we again use the function 'drawImage' with the image 'bulletImage' (defined later as [assets/bullet.png](assets/bullet.png)) in the position where we know the bullet is.

```
def draw(self):
    # fillCircle(self.x, self.y, 10, "black")
    drawImage(getWorld().bulletImage, self.x, self.y)

```