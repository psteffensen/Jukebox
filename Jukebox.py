import pygame
 
SIZE = WIDTH, HEIGHT = 480, 320 #the width and height of our screen
BACKGROUND_COLOR = pygame.Color('white') #The background colod of our window
FPS = 1 #Frames per second

class StopSprite(pygame.sprite.Sprite):
    def __init__(self):
        super(StopSprite, self).__init__()
 
        self.images = []
        self.images.append(pygame.image.load('images/stop.png'))

        self.index = 0
        self.clicked = 0
        
        self.image = self.images[self.index]
 
        self.rect = pygame.Rect(400, 120, 80, 80)
 
    def on_click(self):
        pygame.mixer.music.stop()
        return 1
    
        
class UpSprite(pygame.sprite.Sprite):
    def __init__(self, page):
        super(UpSprite, self).__init__()
 
        self.images = []
        self.image = pygame.image.load('images/arrow_up.png')
        self.rect = pygame.Rect(400, 0, 80, 120)
        self.page = page
 
    def on_click(self):
        return self.page.page_1()
        
       
        
class DownSprite(pygame.sprite.Sprite):
    def __init__(self, page):
        super(DownSprite, self).__init__()
 
        self.images = []
        self.image = pygame.image.load('images/arrow_down.png')
        self.rect = pygame.Rect(400, 200, 80, 120)
        self.page = page
        
    def on_click(self):
        return self.page.page_2()

      
       
class AnimateSprite(pygame.sprite.Sprite):
    def __init__(self, images, music, pos):
        super(AnimateSprite, self).__init__()
 
        self.music = music
        
        self.images = images
        #self.images.append(pygame.image.load('images/cirkeline_small_1.png'))
        #self.images.append(pygame.image.load('images/cirkeline_small_2.png'))
 
        self.index = 0
        self.clicked = 0
 
        self.image = self.images[self.index]
 
        self.rect = pygame.Rect(pos[0], pos[1], pos[2], pos[3])
 
    def on_click(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.load(self.music)
        pygame.mixer.music.play()
        #pygame.event.wait()
        pygame.time.Clock().tick(10)
    
        #self.clicked = not self.clicked
        self.clicked = 1
        return 1
        
    def update(self):
        if self.clicked == 1:
            self.index += 1
     
            if self.index >= len(self.images):
                self.index = 0
            
            self.image = self.images[self.index]
 
 
class RotateSprite(pygame.sprite.Sprite):
    def __init__(self, images, music, pos):
        super(RotateSprite, self).__init__()
 
        self.music = music
        self.images = images
        #self.images.append(pygame.image.load('images/cirkeline_small_1.png'))
        #self.images.append(pygame.image.load('images/cirkeline_small_2.png'))
 
        self.index = 0
        self.clicked = 0
 
        self.image = self.images[self.index]
        self.image_orig = self.image
        self.angle = 0
        self.angle_step = 10
        self.rect = pygame.Rect(pos[0], pos[1], pos[2], pos[3])
        self.rect_orig = self.rect
 
    def on_click(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.load(self.music)
        pygame.mixer.music.play()
        #pygame.event.wait()
        pygame.time.Clock().tick(10)
    
        #self.clicked = not self.clicked
        self.clicked = 1
        return 1
 
    def rotate(self, image, rect, angle):
        """Rotate the image while keeping its center."""
        # Rotate the original image without modifying it.
        new_image = pygame.transform.rotate(image, angle)
        # Get a new rect with the center of the old rect.
        rect = new_image.get_rect(center=rect.center)
        return new_image, rect
 
    def update(self):
        if self.clicked == 1:
            self.angle = self.angle + self.angle_step
            if self.angle >= 360:
                self.angle = 0
            self.image, self.rect = self.rotate(self.image_orig, self.rect_orig, self.angle)


class Page():
    def __init__(self, sprite_group, sprite_nav_group):
        self.sprite_group = sprite_group
        self.sprite_nav_group = sprite_nav_group
        
    def clear_screen(self):
        del self.sprite_group
        self.sprite_group = pygame.sprite.Group()
        stop_sprite = StopSprite()
        self.sprite_group.add(stop_sprite)
    
    def page_1(self):
        self.clear_screen()
        
        # Cirkeline Sprite
        images = []
        images.append(pygame.image.load('images/cirkeline_small_1.png'))
        images.append(pygame.image.load('images/cirkeline_small_2.png'))
        music = 'music/Cirkeline - Lossepladsen.mp3'
        pos = [0,0,100,160]
        cirkeline_sprite = AnimateSprite(images, music, pos)
        
        # Mamma Mia
        images = []
        images.append(pygame.image.load('images/abba - mamma mia.png'))
        music = 'music/ABBA - Mamma Mia.mp3'
        pos = [100,0,100,160]
        mammamia_sprite = RotateSprite(images, music, pos)
        
        self.sprite_group.add(mammamia_sprite)
        self.sprite_group.add(cirkeline_sprite)
        
        return self.sprite_group, images, music, pos
    
    def page_2(self):
        self.clear_screen()
        
        # Cirkeline Sprite
        images = []
        images.append(pygame.image.load('images/cirkeline_small_1.png'))
        images.append(pygame.image.load('images/cirkeline_small_2.png'))
        music = 'music/Cirkeline - Lossepladsen.mp3'
        pos = [10,0,100,160]
        cirkeline_sprite = AnimateSprite(images, music, pos)
        
        # Mamma Mia
        images = []
        images.append(pygame.image.load('images/abba - mamma mia.png'))
        music = 'music/ABBA - Mamma Mia.mp3'
        pos = [200,20,100,160]
        mammamia_sprite = RotateSprite(images, music, pos)

        self.sprite_group.add(mammamia_sprite)
        self.sprite_group.add(cirkeline_sprite)
        
        return self.sprite_group, images, music, pos

            
def main():
    pygame.init()
    pygame.mixer.init()
        
    screen = pygame.display.set_mode(SIZE)
    
    sprite_group = pygame.sprite.Group()
    sprite_nav_group = pygame.sprite.Group()
    page = Page(sprite_group, sprite_nav_group)
    
    # Starting on page 1
    sprite_group, images, music, position = page.page_1()

    # Faste knapper
    stop_sprite = StopSprite()
    up_sprite = UpSprite(page)
    down_sprite = DownSprite(page)

    sprite_nav_group.add(up_sprite)
    sprite_nav_group.add(down_sprite)
    sprite_group.add(stop_sprite)
    
    clock = pygame.time.Clock()
 
    stop_all = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
 
        sprite_group.update()
        sprite_nav_group.update()
        sprite_group
        screen.fill(BACKGROUND_COLOR)
        sprite_group.draw(screen)
        sprite_nav_group.draw(screen)
        pygame.display.update()
        clock.tick(5)
 
        # get all events
        ev = pygame.event.get()

        # proceed events
        for event in ev:

            # handle MOUSEBUTTONUP
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
      
                # Action for the clicked sprite
                for s in sprite_group:
                    if s.rect.collidepoint(pos):
                        stop_all = s.on_click()
                
                # Action for all the rest
                for s in sprite_group:
                    if stop_all == 1 and not s.rect.collidepoint(pos):
                        s.clicked = 0
                
                # Action for all navigation buttons
                for s in sprite_nav_group:
                    if s.rect.collidepoint(pos):
                        sprite_group, images, music, position  = s.on_click()
        
 
if __name__ == '__main__':
    main()
