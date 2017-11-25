
import pygame
import random
import os
import time
import pickle
#import _thread

#pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init() # initialize pygame
window = pygame.display.set_mode((400,430)) # create display
pygame.display.set_caption('Shut Meat Holes')
icoImg = pygame.image.load('images\\Package.png')
pygame.display.set_icon(icoImg)
screen = pygame.Surface((400,400))
fill_screen = pygame.Surface((400, 30)) 

death_sound = pygame.mixer.Sound('sounds\\metal.ogg')
shot_sound = pygame.mixer.Sound('sounds\\shot.ogg')

sounds = dict(death_sound = death_sound, shot_sound = shot_sound)

black = 0,0,0
white = 255,255,255
red = 255,0,0
green = 0,255,0

"""
                                    NOW STRATING MY SHIT-CODE

"""

class SoudsWhores:

    """
    Prepares sounds for future use.
    """
    
    def __init__(self, **sounds):
        self.sounds= {}
        for each in sounds:
            self.sounds[each] = pygame.mixer.Sound(sounds[each])

        '''
        self.brittany = pygame.mixer.Sound('sounds\\brittanyvsays.ogg')
        self.karina = pygame.mixer.Sound('sounds\\karinatyan.ogg')
        self.olyasha = pygame.mixer.Sound('sounds\\olyasha.ogg')
        '''

    def play(self, string):
        #print(string)
        if os.path.split(string)[1] == 'brittaniventi.png':
            pygame.mixer.Sound.play(self.sounds['brittany'])
        elif os.path.split(string)[1] == 'olyasha.png':
            pygame.mixer.Sound.play(self.sounds['olyasha'])
        elif os.path.split(string)[1] == 'sharishaxd.png':
            pygame.mixer.Sound.play(self.sounds['karina'])
        elif os.path.split(string)[1] == 'diana.png':
            pygame.mixer.Sound.play(self.sounds['diana'])
        elif os.path.split(string)[1] == 'nastya.png':
            pygame.mixer.Sound.play(self.sounds['nastya'])
        elif os.path.split(string)[1] == 'pink.png':
            pygame.mixer.Sound.play(self.sounds['pink'])

class Sprite:
    """
    Class which instance is game objects.
    When create new instance settings coordinate object, download image and bind it to object.
    """
    def __init__(self, xpos, ypos, filename):
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load(filename)
        self.bitmap.set_colorkey((255,255,255)) # delete white background
    def render(self):
        """
        Displays images object (binded to) on game surface
        """
        screen.blit(self.bitmap, (self.x,self.y))

##def dumbPkl(pos):
##    '''
##    Function save time when music stop play if game exit.
##    For old version with long song.
##    '''
##    f = open('files//dumbPkl.pkl', 'wb')
##    pickle.dump(pos, f)
##    f.close()

def dumbRecord(point):
    """
    Save current score at record.pkl file, if now score more less than.
    """
    #print(point)
    file = open('files\\Record.pkl', 'rb')
    old = pickle.load(file)
    file.close()
    if point > old:
        fw = open('files\\Record.pkl', 'wb')
        pickle.dump(point, fw)
        fw.close()
        return True
    else:
        fw = open('files\\Record.pkl', 'wb')
        pickle.dump(old, fw)
        fw.close()
        return False

#    except FileNotFoundError:
#        file = open('files\\Record.pkl', 'wb')
#        nole = 0
#        pickle.dump(nole, file)
#        file.close()
#        dumbRecord(point)


def paused():
    """
    Function derteminating action when the pause active. Similar to the menu function.
    """
    pygame.mixer.music.pause()
    
    text_death = pygame.font.Font('fonts\\Regular1.ttf', 22)
    font = text_death.render('Paused', True, (255,0,0))
    rect = font.get_rect()
    rect.center = (200,200)

    pygame.mouse.set_visible(True)
    pygame.key.set_repeat(0,0)
    hero.dead = True
    while hero.dead:

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    menuLoop(('Game','Options', 'Exit'))
                elif e.key == pygame.K_p:
                    pygame.mixer.music.unpause()
                    pygame.mouse.set_visible(False)
                    pygame.key.set_repeat(1,1)
                    hero.dead = False

        button('Continue', 50,300,100,25,(0,200,0),(0,255,0))
        button('Menu',250,300,100,25,(200,0,0),(255,0,0))             
        #pygame.draw.rect(window, (0,255,0), (50,300,50,50))
        window.blit(font, rect)
        pygame.display.update()

def deathFunc(score):
    """
    Function determinate action after hero death, use function creating button for creat
    two button - "Start new game" and "Menu ".
    """
    text_death = pygame.font.Font('fonts\\Regular1.ttf', 22)
    
    res = dumbRecord(score)
    if res:
        font = text_death.render(('Grac, New RECORD - %s' % str(int(score))), True, (255,0,0))
        rect = font.get_rect()
        rect.center = (200,200)
    else:
        font = text_death.render('You Dead!!! Game is over.', True, (255,0,0))
        rect = font.get_rect()
        rect.center = (200,200)

    pygame.mixer.Sound.play(death_sound)
    pygame.mixer.music.stop()
    pygame.mixer.music.load('music\\' + random.choice(os.listdir('music\\')))

    pygame.key.set_repeat(0,0)
    pygame.mouse.set_visible(True)
    hero.dead = True
    while hero.dead:

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    pygame.mixer.music.play(loops=-1)
                    menuLoop(('Game','Options', 'Exit'))

        button('Start new', 50,300,100,25,(0,200,0),(0,255,0))
        button('Menu',250,300,100,25,(200,0,0),(255,0,0))             
        #pygame.draw.rect(window, (0,255,0), (50,300,50,50))
        window.blit(font, rect)
        pygame.display.update()

def button(msg,x,y,w,h,ac,ic):
    """
    Function helps other func creat buttons.
    """
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(window, ic, (x, y, w, h))
        if click[0] == 1:
            if msg == 'Start new':
                pygame.key.set_repeat(1,1)
                asteroid.x = 420
                asteroid.y = random.randrange(380)
                asteroid.speed = 5
                rocket.x = 0
                rocket.y = -40
                rocket.Ipl = 0
                rocket.push = False
                hero.dead = False
                hero.y = 150
                hero.hearts = 2
                pygame.mixer.music.play(loops=-1)
            if msg == 'Menu':
                pygame.mixer.music.play(loops=-1)
                asteroid.x = 420
                asteroid.y = random.randrange(380)
                asteroid.speed = 5
                rocket.x = 0
                rocket.y = -40
                rocket.push = False
                hero.dead = False
                hero.y = 150
                hero.hearts = 2
                rocket.Ipl = 0
                menuLoop(('Game','Options', 'Exit'))
            if msg == 'Continue':
                pygame.key.set_repeat(1,1)
                pygame.mixer.music.unpause()
                hero.dead = False
    else:
        pygame.draw.rect(window, ac, (x, y, w, h))

    text = pygame.font.Font('fonts\\JazzBall.ttf', 20)
    font = text.render(msg, 1, (0,0,0))
    rect = font.get_rect()
    rect.center = (x + (w/2), y + (h/2))
    window.blit(font,rect)

def Options():

    global music_vol
    global sound_vol

    check_sound = pygame.mixer.Sound('sounds\\bang.ogg')
    sounds[check_sound] = check_sound
    X = 255
    
    death = False
    while not death:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    death = True

      
        screen.fill(black)
        fill_screen.fill(black)

        "title of menu"

        head = pygame.font.Font('fonts\\Regular1.ttf',30)
        fonthead = head.render('SETTINGS', 1, (255,X,255))
        recthead = fonthead.get_rect()
        recthead.center = (200, 25)
        screen.blit(fonthead,recthead)

        click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()

        "Setting music volume"

    ##    test = test.menusPoints(gameDisplay, click, mouse, music_vol, "SET MUS VOL", 38, (255,255,255),140, 60,300, 50, 25, 25)
    ##    if test:
    ##        music_vol = test
        
        vol = pygame.font.Font('fonts\\a_LCDNova.ttf',38)
        fontvol = vol.render('SET MUS VOL %.1f'%music_vol, 1, (255,255,255))
        rectvol = fontvol.get_rect()
        rectvol.center = (140, 90)
        screen.blit(fontvol,rectvol)
        
        pygame.draw.rect(screen, red, (300, 80, 25, 25))
        if 300 < mouse[0] < 325 and 110 < mouse[1] < 135:
            pygame.draw.rect(screen, (200,0,0) , (300, 80, 25, 25))
            if click[0] == 1:
                if round(music_vol, 1) > .0:
                    music_vol -= .1
                    pygame.mixer.music.set_volume(music_vol)
        pygame.draw.rect(screen, green, (325, 80, 25, 25))
        if 325 < mouse[0] < 350 and 110 < mouse[1] < 135:
            pygame.draw.rect(screen, (0,200,0), (325, 80, 25, 25))
            if click[0] == 1:
                if round(music_vol, 1) < 1.:
                    music_vol += .1
                    pygame.mixer.music.set_volume(music_vol)
        pygame.draw.line(screen, black, (305,92),(320,92), 4)
        pygame.draw.line(screen, black, (330,92),(345,92), 4)
        pygame.draw.line(screen, black, (337,85),(337,100), 4)

        "Setting sounds volume"

        vols = pygame.font.Font('fonts\\a_LCDNova.ttf',38)
        fontvols = vols.render('SET SND VOL %.1f'%sound_vol, 1, (255,255,255))
        rectvols = fontvols.get_rect()
        rectvols.center = (140, 147)
        screen.blit(fontvols,rectvols)

        pygame.draw.rect(screen, red, (300, 135, 25, 25))
        if 300 < mouse[0] < 325 and 165 < mouse[1] < 190:
            pygame.draw.rect(screen, (200,0,0) , (300, 135, 25, 25))
            if click[0] == 1:
                if round(sound_vol, 1) > 0.:
                    sound_vol -= .1
                    set_vol_sounds()
        pygame.draw.rect(screen, green, (325, 135, 25, 25))
        if 325 < mouse[0] < 350 and 165 < mouse[1] < 190:
            pygame.draw.rect(screen, (0,200,0), (325, 135, 25, 25))
            if click[0] == 1:
                if round(sound_vol, 1) < 1.:
                    sound_vol += .1
                    set_vol_sounds()
        pygame.draw.line(screen, black, (305,147),(320,147), 4)
        pygame.draw.line(screen, black, (330,147),(345,147), 4)
        pygame.draw.line(screen, black, (337,140),(337,155), 4)



        "check for sounds"
        
        pygame.draw.rect(screen, red, (150, 180, 100, 50))
        if 150 < mouse[0] < 250 and 210 < mouse[1] < 260:
            if click[0] == 1:
                pygame.mixer.Sound.play(sounds[check_sound])

        check = pygame.font.Font('fonts\\a_LCDNova.ttf',20)
        fontcheck = check.render('CHEK SND', 1, white)
        rectcheck = fontcheck.get_rect()
        rectcheck.center = (200, 205)
        screen.blit(fontcheck,rectcheck)

        "Reset current record"

        pygame.draw.rect(screen, red, (150, 310, 100, 50))
        if 150 < mouse[0] < 250 and 340 < mouse[1] < 390:
            if click[0] == 1:
                rectozero()

        file = open('files\\Record.pkl', 'rb')
        reck = pygame.font.Font('fonts\\a_LCDNova.ttf',38)
        fontreck = reck.render('NOW YOU RECORD %d'%pickle.load(file), 1, white)
        rectreck = fontreck.get_rect()
        rectreck.center = (200, 280)
        screen.blit(fontreck,rectreck)
        file.close()

        res = pygame.font.Font('fonts\\a_LCDNova.ttf',20)
        fontres = res.render('RESET', 1, white)
        rectres = fontres.get_rect()
        rectres.center = (200, 335)
        screen.blit(fontres,rectres)

        back = pygame.font.Font('fonts\\neo-latina-demo-FFP.ttf',18)
        fontback = back.render('PRESS <ESCAPE> FOR BACK TO MENU', 1, white)
        rectback = fontback.get_rect()
        rectback.center = (200, 390)
        screen.blit(fontback,rectback)

        window.blit(fill_screen, (0,0))
        window.blit(screen, (0,30))
        pygame.time.delay(30)
        pygame.display.flip()
        

def welcomeLoop():
    
    """Welcome"""
    
    X = 226
    while X:

        screen.fill(black)
        fill_screen.fill(black)
        
        text1 = pygame.font.Font('fonts\\Millionaire.ttf',54)
        font1 = text1.render('WELCOME', 1, (207,X,20))
        rect1 = font1.get_rect()
        rect1.center = (200,150)
        screen.blit(font1,rect1)

        text2 = pygame.font.Font('fonts\\neo-latina-demo-FFP.ttf',28)
        font2 = text2.render('let\'s feed dick to the chick', 1, (207,X,20))
        rect2 = font2.get_rect()
        rect2.center = (200,200)
        screen.blit(font2,rect2)

        X -= 2
        
        window.blit(fill_screen, (0,0))
        window.blit(screen, (0,30))
        pygame.time.delay(60)
        pygame.display.flip()
        
        #time.sleep(3)
        
        #if True: break


def menuLoop(menuSet=('first',)):
    
    pygame.mouse.set_visible(True)
    pygame.key.set_repeat(0,0)
    set_joice = 0
    
    menu = True
    while menu:
        
        screen.fill((100,50,200))
        fill_screen.fill((100,50,200))

        mouseXY = pygame.mouse.get_pos()
        
        for i in menuSet:
            if  (120 < mouseXY[0] < 120 + 155 and
            180 + 50*menuSet.index(i) - 25 < mouseXY[1] < 180 + 50*menuSet.index(i) + 25):
                 set_joice = menuSet.index(i)

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                #dumbPkl(pygame.mixer.music.get_pos()) # сохранить позицию музыки
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    #dumbPkl(pygame.mixer.music.get_pos())
                    pygame.quit()
                    quit()
                elif event.key == pygame.K_UP:
                    if set_joice > 0:
                        set_joice -= 1
                elif event.key == pygame.K_DOWN:
                    if set_joice < len(menuSet) - 1:
                        set_joice += 1
                elif event.key == pygame.K_RETURN:
                    if set_joice == 0:
                        pygame.key.set_repeat(1,1)
                        menu = False
                    if set_joice == 1:
                        Options()
                    if set_joice == 2:
                        #dumbPkl(pygame.mixer.music.get_pos())
                        pygame.quit()
                        quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if set_joice == 0:
                        pygame.key.set_repeat(1,1)
                        menu = False
                    if set_joice == 1:
                        Options()
                    if set_joice == 2:
                        #dumbPkl(pygame.mixer.music.get_pos())
                        pygame.quit()
                        quit()
        
        for obj in menuSet:
            text = pygame.font.Font('fonts\\Millionaire.ttf',54)
        
            if set_joice == menuSet.index(obj):
                font = text.render(obj, 1, (207,0,20))
                rect = font.get_rect()
                rect.center = (200,150+50*menuSet.index(obj))
                screen.blit(font,rect)
            else:
                font = text.render(obj, 1, (207,227,20))
                rect = font.get_rect()
                rect.center = (200,150+50*menuSet.index(obj))
                screen.blit(font,rect)
            
        window.blit(fill_screen, (0,0))
        window.blit(screen, (0,30))
        pygame.time.delay(30)
        pygame.display.flip()

def set_vol_sounds():
    for sound in sounds.values():
        sound.set_volume(sound_vol)

def rectozero():
    file = open('files\\Record.pkl', 'wb')
    pickle.dump(0.0, file)
    file.close()

def IntersectObj(x1, x2, y1, y2, dx, dy):
    #if x1 > x2 - 50 and x1 < x2 + 50 and y1 > y2 - 41 and y1 < y2 + 41:
    if x2 - dx < x1 < x2 + dx and y2 - dy < y1 < y2 + dy:
        return 1
    else:
        return 0

#creating game objects
asteroid = Sprite(500, 250, 'images//asteroid.png')
asteroid.speed = 5

hero = Sprite(0,180,'images//Cracer.png')
hero.hearts = 2
hero.dead = False
hero.score = 0

randZet = 'images\\whores\\' + random.choice(os.listdir('images\\whores\\'))
zet = Sprite(359,359,randZet)
zet.move_up = True
zet.step = 5

rocket = Sprite(0,-40, 'images//cock.png')
rocket.push = False
rocket.Ipl = 0

heart = Sprite(450, random.randrange(380), 'images//heart(1).png')
heart.speed = 5
heart.screen = False

randFon = 'images\\background\\' + random.choice(os.listdir('images\\background\\'))
fon = Sprite(0,0,randFon)

music_vol = .4
sound_vol = 1.
### downloading position music which stop in a past game session
##try:
##    f = open('files//dumbPkl.pkl', 'rb') # download value from file
##    musPos = pickle.load(f)
##    f.close()
####    if musPos > (60*60 + 30):
####        musPos = 0 # to zero if music ends
##except:
##    musPos = 0 # for first start
rand = random.choice(os.listdir('music\\'))
pygame.mixer.music.load('music\\' + rand) 
pygame.mixer.music.play(loops=-1) 
# pygame.mixer.music.queue('music\\SophAspin.ogg') 
pygame.mixer.music.set_volume(music_vol)

# creating text obj for game loop
# pygame.font.init() innitialaze module font if do not - pygame.init()
text_speed = pygame.font.Font('fonts\\Regular1.ttf', 16)
text_mark = pygame.font.Font('fonts\\Regular1.ttf', 16)
text_heart = pygame.font.Font('fonts\\Regular1.ttf', 16)

welcomeLoop()

whoresintro = SoudsWhores(brittany='sounds\\brittanysays.ogg',
                    karina='sounds\\karinatyan.ogg',
                    olyasha='sounds\\olyasha.ogg',
                    diana='sounds\\diana2.ogg',
                    nastya='sounds\\nastya2.ogg',
                    pink='sounds\\pink.ogg')

whoreSay = SoudsWhores(brittany='sounds\\brittanyshitsay.ogg',
                    karina='sounds\\karinasucksdicks.ogg',
                    olyasha='sounds\\olyashawhores.ogg',
                    diana='sounds\\diana2.ogg',
                    nastya='sounds\\nastya.ogg',
                    pink='sounds\\pink.ogg')

#sounds.update(whoresintro.sounds)
sounds.update(whoreSay.sounds)

menuLoop(('Game','Options', 'Exit')) # start menu
whoresintro.play(randZet)
pygame.key.set_repeat(1,1) # activate repeating press on button
pygame.mouse.set_visible(False)# invis for cursor
done = True
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            #dumbPkl(pygame.mixer.music.get_pos())
            done = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_DOWN:
                if hero.y < 350: hero.y += 5
            elif e.key == pygame.K_UP:
                if hero.y > 0: hero.y -=5
            elif e.key == pygame.K_SPACE:
                if not rocket.push:
                    rocket.y = hero.y + 15
                    rocket.push = True
                    pygame.mixer.Sound.play(shot_sound)
            elif e.key == pygame.K_p:
                paused()
            elif e.key == pygame.K_ESCAPE:
                menuLoop(('Game','Options', 'Exit'))
                #pygame.key.set_repeat(1,1)
                pygame.mouse.set_visible(False)
        '''            
        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                if not rocket.push:
                    rocket.y = hero.y + 15
                    rocket.push = True
        if e.type == pygame.MOUSEMOTION:
            print(pygame.mouse.get_pos())
        '''
        
    if zet.move_up: # рычаг движения цели
        zet.y -= zet.step
        if zet.y < 0:
            zet.move_up = False
    else:
        zet.y += zet.step
        if zet.y > 350:
            zet.move_up = True 

    if rocket.push: # 
        rocket.x += 5
        if rocket.x > 400:
            rocket.push = False
            rocket.x = 0
            rocket.y = -40

    if IntersectObj(zet.x, rocket.x, zet.y, rocket.y, 45, 44): # checking hit
        rocket.push = False
        rocket.x = 0
        rocket.y = -40
        hero.score += (100 + 100*(rocket.Ipl/10))
##      zet.step += 1 # speedering zet, when rocket push up into zet
        if random.choice([True, False, False, False, False, False, False, False, False]):
            whoreSay.play(randZet)
        #print('PUSHHHH')
        if rocket.Ipl < 10:
            rocket.Ipl += 1
            asteroid.speed += .5
        

    asteroid.x -= asteroid.speed
    if asteroid.x < 0 - 20:
        asteroid.x = 420
        asteroid.y = random.randrange(380)

    if not heart.screen:
        if random.randrange(1000) == 42:
            heart.screen = random.choice([True, False, False])

    if heart.screen:
        heart.x -= heart.speed
        if heart.x < 0 - 20:
            heart.x = 420
            heart.y = random.randrange(380)
            heart.screen = False
    
    screen.fill((50,50,50))
    fill_screen.fill((50,50,50))
    fon.render()

    fon.x -= 0.5
    if fon.x < -1200:
        fon.x = 0

    '''
    if IntersectObj(zet.x, rocket.x, zet.y, rocket.y, 45, 44):
        fill_screen.blit(text_mark.render('Попадания: %s'%rocket.Ipl, 1, (255,0,0)), (140,5))
    else:
        fill_screen.blit(text_mark.render('Попадания: %s'%rocket.Ipl, 1, (100,40,190)), (140,5))
    '''
    fill_screen.blit(text_speed.render('SCORE: %06d'%hero.score, 1, (100,176,49)), (5,5))
    fill_screen.blit(text_mark.render('BONUS: %s'%(rocket.Ipl*10), 1, (100,40,190)), (160,5))
    fill_screen.blit(text_heart.render('LIVES: %s'%hero.hearts, 1, (190,100,40)), (285,5))
    
    if IntersectObj(hero.x, heart.x, hero.y, heart.y, 50, 41):
        hero.hearts += 1
        heart.x = 450
        heart.y = random.randrange(380)
        heart.screen = False
    
    if IntersectObj(hero.x, asteroid.x, hero.y, asteroid.y, 40, 31):
        hero.hearts -= 1
        if rocket.Ipl == 10:
            rocket.Ipl = 0
            asteroid.speed = 5

        if hero.hearts < 0:
            full_score = hero.score
            hero.score = 0
            deathFunc(full_score)
            pygame.mouse.set_visible(False)
            continue
        text_crashed = pygame.font.Font('fonts\\Millionaire.ttf', 30)
        font = text_crashed.render('You Crashed!', True, (255,0,0))
        rect = font.get_rect()
        rect.center = (200,200)
        window.blit(font, rect)
        pygame.display.update()
        time.sleep(2)
        hero.y = 150
        asteroid.x = 420
        asteroid.y = random.randrange(380)
        #continue

    heart.render()
    asteroid.render()
    zet.render()
    hero.render()
    rocket.render()
    window.blit(fill_screen, (0,0))
    window.blit(screen, (0,30))
    pygame.display.flip()
    pygame.time.delay(15)
  
pygame.quit()
quit()
