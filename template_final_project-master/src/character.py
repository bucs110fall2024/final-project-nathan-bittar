import pygame


class Character:

    


    def __init__(self, x, y, img_file):
        """
        Initializes the character object
        args:
        - x : int - starting x coordinate
        - y : int - starting y coordinate
        - v : velocity
        - img_file : str - path to img file
    
        """
        self.x = x
        self.y = y
        self.image = pygame.image.load("9-2-ghost-png-file.png")
        self.rect = self.image.get_rect(bottomleft=(x, y))
        




    def move_right(self, keys, velocity):
        """
        Moves position right by 1
        args: None
        return: None
        """
        self.velocity = velocity
        self.keys = keys
        if keys[pygame.K_RIGHT]: 
            x+= velocity
            
        




    def move_left(self, keys, velocity, left_boundary):
        """
        moves position left by 1
        args: None
        return: None
        """
        self.keys = keys
        self.velocity = velocity
        self.left_boundary = left_boundary
        if keys[pygame.K_RIGHT] and x > left_boundary:
            x -= velocity

    def jump(self, keys, velocity):
        """
        moves character up
        args: None
        return: None
        """
        self.velocity = velocity
        self.keys = keys
        if keys[pygame.K_RIGHT]:
            y += velocity