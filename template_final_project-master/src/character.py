import pygame


class Character:

    
    


    def __init__(self, x, y, isjumping, jump_count, img_file = 'assets/ghost.png'):
        """
        Initializes the character object
        args:
        - x : int - starting x coordinate
        - y : int - starting y coordinate
        - img_file : str - path to img file
    
        """
        self.x = x
        self.y = y
       
        self.jump_count = 10
        self.is_jumping = False
        self.image = pygame.image.load(img_file)
        self.rect = self.image.get_rect(bottomleft=(x,y))





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
            self.rect.x = self.x
            
        




    def move_left(self, keys, velocity, left_boundary):
        """
        moves position left by 1
        args: None
        return: None
        """
        self.keys = keys
        self.velocity = velocity
        self.left_boundary = left_boundary
        if keys[pygame.K_LEFT] and x > left_boundary:
            x -= velocity
            self.rect.x = self.x

    def jump(self, keys, velocity, isjump, jump_count):
        """
        moves character up
        args: None
        return: None
        """
        self.velocity = velocity
        self.keys = keys
        self.is_jumping = isjump
        self.jump_count = jump_count
        
        if not is_jumping:
            if keys[pygame.K_SPACE]:
                is_jumping = True
                jump_count = 10
        
        if is_jumping:
            if jump_count >= -10:
                neg = 1
                if jump_count < 0:
                    neg = -1
                y -= (jump_count ** 2) * 0.5 * neg
                jump_count -= 1
                self.rect.y = self.y
            else:
                is_jumping = False
    def draw(self, screen):
        """
        Draws the character on the screen
        args:
        - screen : pygame window
        Return: None
        """
        if self.image:
            screen.blit(self.image, self.rect)
        # else:
        #     # Fallback drawing if no image
        #     pygame.draw.rect(screen, (255, 255, 255), self.rect)
        
        