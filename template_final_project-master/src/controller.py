import pygame
from character import Character
from sawblades import Sawblade 
from scoreboard import Scoreboard

class Controller:
    def __init__(self):
        """
        docstring
        """

    def mainloop(self):
        """
        docstring
        """
        while(True): #this can also be a variable instead of just True
            #1. Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

      #2. detect collisions and update models
            velocity = 5
            x = 50
            y = 1
            left_boundary = 0
            right_boundary = 50
            background_color_red = 243
            background_color_green = 211
            background_color_blue = 217
            keys = pygame.key.get_pressed
            Character.__init__(x, y, img_file)
            Character.move_right(keys, velocity)
            Character.move_left(keys, velocity, left_boundary)
            Character.jump(keys, velocity)
            win.fill((background_color_red, background_color_green, background_color_blue))
        
      #3. Redraw next frame

      #4. Display next frame
            pygame.display.flip()
    