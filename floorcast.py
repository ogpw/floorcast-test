import arcade
from PIL import Image
import math


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = "test"

VIEWPORT_WIDTH = 100
VIEWPORT_HEIGHT = 100

HEIGHTMAP = Image.open("East_Anglia_Heightmap.png")
HEIGHTMAP_WIDTH, HEIGHTMAP_HEIGHT = HEIGHTMAP.size # E_A_HM is 1912x1912

class Camera:
    def __init__(self, x, y, dist): # x and y are coords of IMAGE ^
        self.x = x # x pos coord (ORIGIN) HORIZONTAL AXIS
        self.y = y # y pos coord (ORIGIN) VERTICAL AXIS
        self.angle = angle # angle camera is facing (in degrees). 0 is North/Up
        self.dist = dist # max view distance/culling distance from camera

        self.horizon_vector = (0, self.dist)
        
    def changeDirection(self, new_angle):
        self.horizon_vector = (math.cos(math.radians())
    
    def inRange(self, target_vector):
        pass

class Game(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color((100, 200, 255))

    def setup(self):
        hm_data = HEIGHTMAP.getdata()
        self.pixels = []
        for y in range(0, HEIGHTMAP_HEIGHT):
            new_row = []
            for x in range(0, HEIGHTMAP_WIDTH):
                new_row.append(hm_data[x])
            self.pixels.append(new_row)

        self.player = Camera(1000, 1000, 0, 20)

    def on_draw(self):
        self.clear()

        for x in pixels:
            for y in x:
                

    def on_update(self, delta_time):
        pass

    def on_key_press(self, key, key_modifiers):
        pass

    def on_key_release(self, key, key_modifiers):
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        pass

def main():
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()
