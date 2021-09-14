import pygame

class Button:
    
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y 
        self.width = width
        self.height = height 
        self.btn = pygame.Rect((self.x,self.y), (self.width, self.height))

    def draw(self, screen, color, b_radius):
        pygame.draw.rect(screen, color, self.btn, border_radius=b_radius) 


class Text:

    def __init__(self, text, size, color):
        self.font = pygame.font.SysFont("notomono", size, True)
        self.text = self.font.render(text, True, color) 
    
    def get(self):
        return self.text
        

    

