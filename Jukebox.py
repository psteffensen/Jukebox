import pygame
import os
 
SIZE = WIDTH, HEIGHT = 480, 320 #the width and height of our screen
BACKGROUND_COLOR = pygame.Color('white') #The background colod of our window
FPS = 1 #Frames per second

class StopSprite(pygame.sprite.Sprite):
    def __init__(self):
        super(StopSprite, self).__init__()
 
        self.images = []
        self.images.append(pygame.image.load('images/stop2.png'))

        self.index = 0
        self.clicked = 0
        
        self.image = self.images[self.index]
 
        self.rect = pygame.Rect(400, 120, 80, 80)
 
    def on_click(self):
        pygame.mixer.music.stop()
    
        
class UpSprite(pygame.sprite.Sprite):
    def __init__(self, page):
        super(UpSprite, self).__init__()
 
        self.images = []
        self.image = pygame.image.load('images/arrow_up.png')
        self.rect = pygame.Rect(400, 0, 80, 120)
        self.page = page
 
    def on_click(self, page_num):
        page_num = page_num - 1
        if page_num < 0:
            page_num = 1
        return self.page.page(page_num)
        
       
        
class DownSprite(pygame.sprite.Sprite):
    def __init__(self, page):
        super(DownSprite, self).__init__()
 
        self.images = []
        self.image = pygame.image.load('images/arrow_down.png')
        self.rect = pygame.Rect(400, 200, 80, 120)
        self.page = page
        
    def on_click(self, page_num):
        page_num = page_num + 1
        if page_num > 1:
            page_num = 0
        return self.page.page(page_num)

      
       
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
 
        self.index = 0
        self.clicked = 0
 
        self.image = self.images[self.index]
        self.image_orig = self.image
        self.angle = 0
        self.angle_step = 10
        self.rect = pygame.Rect(pos[0]+pos[2]*0.293/2, pos[1]+pos[3]*0.293/2, pos[2]*0.707, pos[3]*0.707)
        self.clicked = 1
        self.update()
        self.clicked = 0
 
    def on_click(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.load(self.music)
        pygame.mixer.music.play()
        #pygame.event.wait()
        pygame.time.Clock().tick(10)
    
        #self.clicked = not self.clicked
        self.clicked = 1
 
    def rotate(self, image, rect, angle):
        """Rotate the image while keeping its center."""
        # Rotate the original image without modifying it.
        new_image = pygame.transform.rotate(image, angle)
        # Get a new rect with the center of the old rect.
        rect = new_image.get_rect(center=rect.center)
        return new_image, rect
 
    def update(self):
        if self.clicked == 1:
            if self.angle >= 360:
                self.angle = 0
            self.image, self.rect = self.rotate(self.image_orig, self.rect, self.angle)
            self.angle = self.angle + self.angle_step



class Page():
    def __init__(self, sprite_group, sprite_nav_group):
        self.sprite_group = sprite_group
        self.sprite_nav_group = sprite_nav_group
        
    def clear_screen(self):
        del self.sprite_group
        self.sprite_group = pygame.sprite.Group()
        stop_sprite = StopSprite()
        self.sprite_group.add(stop_sprite)
    
    def page(self, page_num):
        self.clear_screen()
        
        if page_num == 0:
            # Cirkeline - Bim bam busse
            images = []
            images.append(pygame.image.load('images/cirkeline_small_1.png'))
            images.append(pygame.image.load('images/cirkeline_small_2.png'))
            music = 'music/Cirkeline - BimBamBusse.mp3'
            pos = [0,0,130,160]
            cirkeline_sprite = AnimateSprite(images, music, pos)
            
            # Mamma Mia
            images = []
            images.append(pygame.image.load('images/abba - mamma mia.png'))
            music = 'music/ABBA - Mamma Mia.mp3'
            pos = [130,0,130,160]
            mammamia_sprite = RotateSprite(images, music, pos)
            
            # Emil - Snickerbo
            images = []
            images.append(pygame.image.load('images/Emil_Snickerbo_1.png'))
            images.append(pygame.image.load('images/Emil_Snickerbo_2.png'))
            music = 'music/Emil - Du Kaara Lille Snickerbo.mp3'
            pos = [260,0,130,160]
            emilsnickerbo_sprite = AnimateSprite(images, music, pos)
            
            # Georg Riedel - Sjoeroevar Fabbe
            images = []
            images.append(pygame.image.load('images/SjoeroevarFabbe_1.png'))
            images.append(pygame.image.load('images/SjoeroevarFabbe_2.png'))
            music = 'music/Georg Riedel - Sjoesoevar-Fabbe.mp3'
            pos = [0,160,130,160]
            sjoeroevarfabbe_sprite = AnimateSprite(images, music, pos)
            
            # Bolibompa
            images = []
            images.append(pygame.image.load('images/Bolibompa.png'))
            music = 'music/bolibompa.mp3'
            pos = [130,160,130,160]
            bolibompa_sprite = RotateSprite(images, music, pos)
            
            # Kaj og Andrea - Kajs sang
            images = []
            images.append(pygame.image.load('images/KajsSang.png'))
            images.append(pygame.image.load('images/KajsSang_2.png'))
            images.append(pygame.image.load('images/KajsSang.png'))
            images.append(pygame.image.load('images/KajsSang_3.png'))
            music = 'music/KajOgAndrea - KajsSang.mp3'
            pos = [260,160,130,160]
            kajssang_sprite = AnimateSprite(images, music, pos)
            
            self.sprite_group.add(kajssang_sprite)
            self.sprite_group.add(bolibompa_sprite)
            self.sprite_group.add(mammamia_sprite)
            self.sprite_group.add(cirkeline_sprite)
            self.sprite_group.add(emilsnickerbo_sprite)
            self.sprite_group.add(sjoeroevarfabbe_sprite)
            
            return self.sprite_group, images, music, pos, page_num
        elif page_num == 1:
            # Kaj og Andrea - Kajs og andreas Duet
            images = []
            images.append(pygame.image.load('images/KajsOgAndreasDuet_1.png'))
            images.append(pygame.image.load('images/KajsOgAndreasDuet_2.png'))
            images.append(pygame.image.load('images/KajsOgAndreasDuet_1.png'))
            images.append(pygame.image.load('images/KajsOgAndreasDuet_3.png'))
            music = 'music/KajOgAndrea - KajsOgAndreasDuet.mp3'
            pos = [0,0,130,160]
            kajsogandreasduet_sprite = AnimateSprite(images, music, pos)
            
            #Cirkeline - Lossepladsen
            images = []
            images.append(pygame.image.load('images/Cirkeline - Lossepladsen 1.png'))
            images.append(pygame.image.load('images/Cirkeline - Lossepladsen 2.png'))
            music = 'music/Cirkeline - Lossepladsen.mp3'
            pos = [130,0,130,160]
            cirkelinelossepladsen_sprite = AnimateSprite(images, music, pos)
            
            # Postmand Per
            images = []
            images.append(pygame.image.load('images/PostmandPer.png'))
            images.append(pygame.image.load('images/PostmandPer_2.png'))
            music = 'music/PostmandPer.mp3'
            pos = [260,0,130,160]
            postmandper_sprite = AnimateSprite(images, music, pos)
            
            self.sprite_group.add(postmandper_sprite)
            self.sprite_group.add(cirkelinelossepladsen_sprite)
            self.sprite_group.add(kajsogandreasduet_sprite)
            
            return self.sprite_group, images, music, pos, page_num
        else:
            images = []
            music = []
            pos = [0,0,0,0]
            return self.sprite_group, images, music, pos, page_num
            

            
def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir( dir_path )
    os.system('git pull')
    
    pygame.init()
    pygame.mixer.init()
        
    screen = pygame.display.set_mode(SIZE, pygame.FULLSCREEN)
    #screen = pygame.display.set_mode(SIZE)
    #pygame.mouse.set_visible(False)
    
    sprite_group = pygame.sprite.Group()
    sprite_nav_group = pygame.sprite.Group()
    page = Page(sprite_group, sprite_nav_group)
    
    # Starting on page 1
    page_num = 0
    sprite_group, images, music, position, page_num = page.page(page_num)

    # Faste knapper
    stop_sprite = StopSprite()
    up_sprite = UpSprite(page)
    down_sprite = DownSprite(page)

    sprite_nav_group.add(up_sprite)
    sprite_nav_group.add(down_sprite)
    sprite_group.add(stop_sprite)
    
    clock = pygame.time.Clock()
 
    sprite_clicked = 0
    running = True
    while running:
        sprite_group.update()
        sprite_nav_group.update()
        screen.fill(BACKGROUND_COLOR)
        sprite_group.draw(screen)
        sprite_nav_group.draw(screen)
        pygame.display.update()
        clock.tick(5)
 
        # get all events
        ev = pygame.event.get()
        
        if pygame.mixer.music.get_busy() == False:
            for s in sprite_group:
                s.clicked = 0       
            
        # proceed events
        for event in ev:
            sprite_clicked = 0
            # handle MOUSEBUTTONDOWN
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                
                # Action for pressed sprites
                for s in sprite_group:
                    if s.rect.collidepoint(pos):
                        s.on_click()
                        sprite_clicked = 1
                    else: # if sprite is clicked, the others should stop
                        s.clicked = 0
                
                # if no sprite in sprite_group was pressed
                if sprite_clicked == 0:
                    pygame.mixer.music.stop()
                    for s in sprite_group:
                        s.clicked = 0
                            
                # Action for all navigation buttons
                for s in sprite_nav_group:
                    if s.rect.collidepoint(pos):
                        sprite_group, images, music, position, page_num  = s.on_click(page_num)
            
            # Action for keypresses
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit() 
                    running = False
            
 
if __name__ == '__main__':
    main()
