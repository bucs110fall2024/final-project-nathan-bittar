import pygame
from src.character import Character
from src.sawblades import Sawblade 
from src.scoreboard import Scoreboard




class Controller:


    def __init__(self, width = 800, height = 800):
        """
        Initializes the game window and objects
        args:
        - Width : Width of the window
        - Height : Height of the window
        """
        self.width = width
        self.height = height
        background_color_red = 243
        background_color_green = 211
        background_color_blue = 217
        scoreboard_x = 400
        scoreboard_y = 400
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('A "Very" Slight Chance of Sawblades')
        self.clock = pygame.time.Clock()
        
        # Game objects
        self.scoreboard = Scoreboard(scoreboard_x, scoreboard_y)
        
        # Background color
        self.bg_color = (background_color_red, background_color_green, background_color_blue)

    def mainloop():
        """
        docstring
        """
        
        velocity = 5
        x = 400
        y = 1
        left_boundary = 0
        jump_count = 10
        is_jumping = False
        # right_boundary = 50
        while(True): #this can also be a variable instead of just True
            #1. Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

      #2. detect collisions and update models
            keys = pygame.key.get_pressed
            Character.__init__(x, y, is_jumping, jump_count)
            Character.move_right(keys, velocity)
            Character.move_left(keys, velocity, left_boundary)
            Character.jump(keys, velocity, is_jumping)
      #3. Redraw next frame

      #4. Display next frame
            pygame.display.flip()
    