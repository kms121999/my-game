import pygame, sys, random, time
from pygame.locals import *
# I need to set up a control of difficulty during game play. I also need to set up a record.
pygame.init()
mainClock = pygame.time.Clock()
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
LIME = (0, 255, 0)
RED = (255, 0, 0)
FONTXL = pygame.font.SysFont(None, 50)
FONTL = pygame.font.SysFont(None, 40)
FONTM = pygame.font.SysFont(None, 35)
FONTS = pygame.font.SysFont(None, 25)
FONTXS = pygame.font.SysFont(None, 15)
#640, 480
WINDOWWIDTH = 800
WINDOWHEIGHT = 700
#blocks
BACKBOX = pygame.Rect(20, WINDOWHEIGHT - 55, 35, 35)
back = pygame.image.load(r'data\core\images\other\pback.png')
BACKIM = pygame.transform.scale(back, (35, 35))
#window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), pygame.FULLSCREEN)
window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Raid!!!')#####################
icon = pygame.image.load(r'data\core\images\other\gameimage.png')
pygame.display.set_icon(icon)
pygame.mixer.init()#This probably doesn't need to be here
pygame.mixer.music.load(r'data\core\music\FreedomDance.wav')
pygame.mixer.music.queue(r'data\core\music\LoopyMusic.wav')
musicCurrent = 1
pygame.mixer.music.play(3, 0.0)
MPLAY = True
MPASS = True
screenful = False
def startUp():
    redim = pygame.image.load(r'data\core\images\units\predmen.png').convert()
    blueim = pygame.image.load(r'data\core\images\units\pbluemen.png').convert()
    blueim = pygame.transform.flip(blueim, True, False)
    blockb = pygame.Rect(WINDOWWIDTH / 2 + 15, WINDOWHEIGHT / 2 - 40, 45, 70)
    blockr = pygame.Rect(WINDOWWIDTH / 2 - 60, WINDOWHEIGHT / 2 - 40, 45, 70)
    window.fill(LIME)
    loop = True
    text = FONTXL.render('Raid!!!', True, BLACK)
    text2 = FONTS.render('Click to Continue', True, BLACK)
    textp2 = text2.get_rect()
    textp2.centerx = window.get_rect().centerx = 320
    textp2.centery = window.get_rect().centery = 440
    textp = text.get_rect()
    textp.centerx = window.get_rect().centerx = 320
    textp.top = window.get_rect().top = 60
    window.blit(text, textp)
    window.blit(text2, textp2)
    window.blit(blueim, blockb)
    window.blit(redim, blockr)
    pygame.display.update()
    finisheds = 0
    while loop:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONUP:
                loop = False
def mainMenue():
    window.fill(LIME)
    t = FONTL.render('To Be Named', True, BLACK)
    t1 = FONTM.render('PLAY', True, BLACK)
    t2 = FONTM.render('SETTINGS', True, BLACK)
    t3 = FONTM.render('HOT_KEYS', True, BLACK)
    t4 = FONTM.render('QUIT', True, BLACK)
    tp = t.get_rect()
    tp.centerx = window.get_rect().centerx
    tp.centery = window.get_rect().centery = 30
    tp1 = t1.get_rect()
    tp1.left = window.get_rect().left = 35
    tp1.top = window.get_rect().top = 60
    tp2 = t2.get_rect()
    tp2.left = window.get_rect().left = 35
    tp2.top = window.get_rect().top = 105
    tp3 = t3.get_rect()
    tp3.left = window.get_rect().left = 35
    tp3.top = window.get_rect().top = 150
    tp4 = t4.get_rect()
    tp4.left = window.get_rect().left = 35
    tp4.top = window.get_rect().top = 195
    window.blit(t, tp)
    window.blit(t1, tp1)
    window.blit(t2, tp2)
    window.blit(t3, tp3)
    window.blit(t4, tp4)
    pygame.display.update()
    test123 = pygame.mixer.music.get_busy()
    if test123 == 0:
        MPLAY = False
    else:
        MPLAY = True
    loop = True
    while loop:
        if MPLAY:
            test123 = pygame.mixer.music.get_busy()
            if test123 == 0:
                pygame.mixer.music.play(3, 0.0)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == ord('m'):
                    if MPLAY:
                        pygame.mixer.music.stop()
                        MPLAY = False
                    else:
                        pygame.mixer.music.play(3, 0.0)
                        MPLAY = True
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONUP:
                #mainMenue() and loop = False, were hooked up on 1, 2, and 3; but I see no need.
                if tp1.collidepoint(event.pos[0],event.pos[1]):
                    Play()
                if tp2.collidepoint(event.pos[0],event.pos[1]):
                    settingsScreen()
                if tp3.collidepoint(event.pos[0],event.pos[1]):
                    hotKeys()
                if tp4.collidepoint(event.pos[0],event.pos[1]):
                    pygame.quit()
                    sys.exit()
def Play():
    ablock = pygame.Rect(15, 40, 50, 50)
    ablockim = pygame.image.load(r'data\core\images\other\parrow.png')
    menblue = []
    menred = []
    redim = pygame.image.load(r'data\core\images\units\predmen.png').convert()
    blueim = pygame.image.load(r'data\core\images\units\pbluemen.png').convert()
    blueim = pygame.transform.flip(blueim, True, False)
    loop = True
    down = False
    up = False
    men = False
    #1600
    money = 3000
    health = 10
    hard1 = 5 #5 lower the harder
    hard1s = hard1
    hard2 = 8 #8 higher the harder
    hard2s = hard2
    price = 70
    price1 = 100
    price2 = 140
    healthc = 100
    healthtext = healthc
    create = False
    ypost = 0
    ypostt = 0
    redim.set_colorkey(LIME, pygame.RLEACCEL)
    blueim.set_colorkey(LIME, pygame.RLEACCEL)
    ablockim.set_colorkey(LIME, pygame.RLEACCEL)
    test123 = pygame.mixer.music.get_busy()
    if test123 == 0:
        MPLAY = False
    else:
        MPLAY = True
    musicCurrent = 1
    menc = False
    while loop:
        if MPLAY:
            musicOn = pygame.mixer.music.get_busy()
            MPASS = True
            if musicOn == 0:
                musicCurrent += 1
                if musicCurrent > 2:
                    musicCurrent = 1
                if musicCurrent == 1:
                    pygame.mixer.music.load(r'data\core\music\FreedomDance.wav')
                if musicCurrent == 2:
                    pygame.mixer.music.load(r'data\core\music\LoopyMusic.wav')
                if musicCurrent == 2:
                    pygame.mixer.music.play(8, 0.0)
                else:
                    pygame.mixer.music.play(4, 0.0)
        class red:
            def __init__(self):
                self.x = 5
                self.y = ablock.top
                self.l = 3
                self.d = 1
        class red1:
            def __init__(self):
                self.x = 5
                self.y = ablock.top
                self.l = 9
                self.d = 1
        class red2:
            def __init__(self):
                self.x = 5
                self.y = ablock.top
                self.l = 3
                self.d = 3
        class blue:#computer
            def __init__(self):
                self.l = 3
                self.x = (WINDOWWIDTH - 50)
                pickb = random.randint(1,100)
                if pickb*hard1 > 100 and menred != []:
                    for r in menred:
                        self.y = r.y
                else:
                    pickb = random.randint(0, 5)
                    self.y = 40+(pickb*75)
                    
            '''def __init__(self):
                self.x = (WINDOWWIDTH - 50)
                self.ypos = random.randint(1, 6)
                self.l = 3
                if self.ypos == 1:
                    self.y = 40
                if self.ypos == 2:
                    self.y = 115
                if self.ypos == 3:
                    self.y = 190
                if self.ypos == 4:
                    self.y = 265
                if self.ypos == 5:
                    self.y = 340
                if self.ypos == 6:
                    self.y = 415
                if ypost != 0:
                    self.y = ypost
                if ypostt == 'yes':
                    self.ypos = random.randint(1, 6)
                    if self.ypos == 1:
                        self.y = 40
                    if self.ypos == 2:
                        self.y = 115
                    if self.ypos == 3:
                        self.y = 190
                    if self.ypos == 4:
                        self.y = 265
                    if self.ypos == 5:
                        self.y = 340
                    if self.ypos == 6:
                        self.y = 415'''
        ypostt = 0
        ypost = 0
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_DOWN or event.key == ord('s'):
                    down = True
                if event.key == K_UP or event.key == ord('w'):
                    up = True
                if event.key == K_SPACE:
                    men = True
                if event.key == K_1:
                    if money >= price1:
                        menred.append(red1())
                        money -= price1
                if event.key == K_2:
                    if money >= price2:
                        menred.append(red2())
                        money -= price2
                if event.key == ord('l'):
                    loop = False
                    mainMenue()
                if event.key == ord('p'):
                    paused()
                if event.key == ord('m'):
                    if MPLAY:
                        pygame.mixer.music.stop()
                        MPLAY = False
                    else:
                        if musicCurrent == 1:
                            pygame.mixer.music.play(3, 0.0)
                        else:
                            pygame.mixer.music.play(8, 0.0)
                        MPLAY = True
                if event.key == K_0:
                    men = True
                    menc = True
                if event.key == K_9:
                    money += 1000000
                if event.key == ord('n'):
                    pygame.mixer.music.stop()
                    MPASS = False
            if event.type == KEYUP:
                if event.key == K_0:
                    menc = False
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                #button 3
                if event.button == 1 or event.button == 3:
                    if event.pos[1] > 30 and event.pos[1] < 112:
                        ablock.top = 40
                    if event.pos[1] > 113 and event.pos[1] < 187:
                        ablock.top = 115
                    if event.pos[1] > 188 and event.pos[1] < 262:
                        ablock.top = 190
                    if event.pos[1] > 263 and event.pos[1] < 337:
                        ablock.top = 265
                    if event.pos[1] > 338 and event.pos[1] < 412:
                        ablock.top = 340
                    if event.pos[1] > 413 and event.pos[1] < WINDOWHEIGHT:
                        ablock.top = 415
                if event.button == 1:
                    men = True
        window.fill(LIME)
        for r in menred:
            # 3 ################################
            r.x += 3
            if r.x > WINDOWWIDTH:
                menred.remove(r)
                healthc -= 1
        #75
        if down and ablock.bottom != 465:
            ablock.top += 75
            down = False
        else:
            down = False
        if up and ablock.top != 40:
            ablock.top -= 75
            up = False
        else:
            up = False
        if men == True and money >= price:
            menred.append(red())
            if not menc:
                men = False
            money -= price
        for b in menblue:
            # 3 ###################################
            b.x -= 3
            if (b.x + 45) < 0:
                menblue.remove(b)
                health -= 1
        ###Harder
        if (len(menred)-len(menblue)) > 5:
            hardc = (len(menred)-len(menblue))/5
            hardc = int(hardc*1)/1
            hardcl = len(str(hardc))-2
            hardc = str(hardc)[0:hardcl]
            hardc = int(hardc)
            hard2 = hard2s + hardc*2
        else:
            hard2 = hard2s
        ly1 = False
        ly2 = False
        ly3 = False
        ly4 = False
        ly5 = False
        ly6 = False
        lyc = 0
        for r in menred:
            if r.y == 40 and not ly1:
                ly1 = True
                lyc += 1
            if r.y == 115 and not ly2:
                ly2 = True
                lyc += 1
            if r.y == 190 and not ly3:
                ly3 = True
                lyc += 1
            if r.y == 265 and not ly4:
                ly4 = True
                lyc += 1
            if r.y == 340 and not ly5:
                ly5 = True
                lyc += 1
            if r.y == 415 and not ly6:
                ly6 = True
                lyc += 1
        if lyc < 3:
            hard1 = hard1s-2
        else:
            hard1 = hard1s
        '''if healthc < 50:
            hard2 += 2
        if healthc < 25:
            hard1 -= 1'''#hard as progress
        ###Harder
        bm = random.randint(1, 100)
        if bm < hard2:#computer
            #for r in menred:   'I don't know why this was here'
            create = True
        for b in menblue:
            for r in menred:
                if b.y != r.y:
                    ypost = r.y
        if create:
            menblue.append(blue())
            create = False
        create = False
        if bm < 40:
            if bm > 70:
                ypostt = yes
        if menblue != [] and menred != []:
            for b in menblue:
                for r in menred:
                    if r.y == b.y:
                        if (r.x + 45) > b.x:
                            b.x += 60
                            b.l = b.l - r.d
                            r.x -= 60
                            r.l -= 1
        #dead
        for b in menblue:
            if b.l <= 0:
                menblue.remove(b)
                #80 ############################
                money += 80
        for r in menred:
            if r.l == 0:
                menred.remove(r)
        for r in range(len(menred)):
            for r in menred:
                redb = pygame.Rect(r.x, r.y, 45, 70)
                window.blit(redim, redb)
        for b in range(len(menblue)):
            for b in menblue:
                blueb = pygame.Rect(b.x, b.y, 45, 70)
                window.blit(blueim, blueb)
        mh = pygame.Rect(30, 25, health * 10, 10)
        ch = pygame.Rect(WINDOWWIDTH - 130 + (healthtext - healthc), 25, healthc, 10)
        pygame.draw.rect(window, RED, mh)
        pygame.draw.rect(window, RED, ch)
        moneyt = str(money)
        text = FONTS.render(moneyt, True, BLACK)
        vhealth = '  ' + str(health)
        vchealth = str(healthc) + '  '
        texth = FONTS.render(vhealth, True, BLACK)
        textph = texth.get_rect()
        textph.centerx = window.get_rect().centerx = mh.centerx
        textph.top = window.get_rect().top = 8
        textch = FONTS.render(vchealth, True, BLACK)
        textpch = textch.get_rect()
        textpch.centerx = window.get_rect().centerx = ch.centerx
        textpch.top = window.get_rect().top = 8
        textp = text.get_rect()
        textp.midtop = window.get_rect().midtop
        textp.top = window.get_rect().top = 8
        window.blit(text, textp)
        window.blit(ablockim, ablock)
        window.blit(texth, textph)
        window.blit(textch, textpch)
        pygame.display.update()
        if health < 1:
            gameOver()
        if healthc < 1:
            youWin()
        #70
        mainClock.tick(50)
def changet():
    global screenful
    screenful = False
    window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)

def changef():
    global screenful
    screenful = True
    window = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), pygame.FULLSCREEN)
def settingsScreen():
    t1 = FONTS.render('Turn on Fullscreen', True, BLACK)
    t2 = FONTS.render('Turn off Fullscreen', True, BLACK)
    tp1 = t1.get_rect()
    tp2 = t2.get_rect()
    tp1.top = window.get_rect().top = 30
    tp1.left = window.get_rect().left = 50
    tp2.top = window.get_rect().top = 30
    tp2.left = window.get_rect().left = 50
    loop = True
    while loop:
        window.fill(LIME)
        if screenful:
            window.blit(t2,tp2)
        else:
            window.blit(t1, tp1)
        window.blit(BACKIM, BACKBOX)
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == ord('s'):
                    loop = False
                    mainMenue()
            if event.type == MOUSEBUTTONUP:
                if BACKBOX.collidepoint(event.pos[0], event.pos[1]):
                    loop = False
                    mainMenue()
                if screenful:
                    if tp2.collidepoint(event.pos[0], event.pos[1]):
                        changet()
                else:
                    if tp1.collidepoint(event.pos[0], event.pos[1]):
                        changef()
        pygame.display.update()
        
            
def paused():
    loop = True
    ptext = FONTXL.render('PAUSED', True, BLACK)
    pp = ptext.get_rect()
    pp.center = window.get_rect().center
    window.blit(ptext, pp)
    ptext1 = FONTXS.render('press any key to unpause', True, BLACK)
    pp1 = ptext1.get_rect()
    pp1.top = window.get_rect().top = (WINDOWHEIGHT / 2 + 25)
    pp1.centerx = window.get_rect().centerx
    window.blit(ptext1, pp1)
    pygame.display.update()
    while loop:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                loop = False
def hotKeys():
    window.fill(LIME)
    t = FONTS.render('"'"M"'" turns the music on and off, "'"N"'" changes the music.', True, BLACK)
    t1 = FONTS.render('(The "'"N"'" does not work in this window.)  "'"ESCAPE"'" Closes the program', True, BLACK)
    tp = t.get_rect()
    tp.top = window.get_rect().top = 30
    tp.centerx = window.get_rect().centerx
    tp1 = t1.get_rect()
    tp1.top = window.get_rect().top = 70
    tp1.centerx = window.get_rect().centerx
    window.blit(BACKIM, BACKBOX)
    window.blit(t, tp)
    window.blit(t1, tp1)
    pygame.display.update()
    test123 = pygame.mixer.music.get_busy()
    if test123 == 0:
        MPLAY = False
    else:
        MPLAY = True
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == KEYDOWN:
                if event.key == ord('m'):
                    if MPLAY:
                        pygame.mixer.music.stop()
                        MPLAY = False
                    else:
                        pygame.mixer.music.play(8, 0.0)
                        MPLAY = True
            if event.type == MOUSEBUTTONUP:
                if BACKBOX.collidepoint(event.pos[0], event.pos[1]):
                    loop = False
                    mainMenue()
def gameOver():
    blueim = pygame.image.load(r'data\core\images\units\pbluemen.png')
    blueim = pygame.transform.flip(blueim, True, False)
    window.fill(LIME)
    text = FONTXL.render('GAME OVER!!!', True, BLUE)
    textp = text.get_rect()
    textp.center = window.get_rect().center
    b = pygame.Rect((WINDOWWIDTH / 2 - 22.5), (WINDOWHEIGHT / 2 + 20), 45, 70)
    window.blit(text, textp)
    window.blit(blueim, b)
    pygame.display.update()
    time.sleep(1)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                mainMenue()
            if event.type == MOUSEBUTTONDOWN:
                mainMenue()
def youWin():
    redim = pygame.image.load(r'data\core\images\units\predmen.png')
    window.fill(LIME)
    text = FONTXL.render('YOU WIN!!!', True, RED)
    textp = text.get_rect()
    textp.center = window.get_rect().center
    b = pygame.Rect((WINDOWWIDTH / 2 - 22.5), (WINDOWHEIGHT / 2 + 20), 45, 70)
    window.blit(text, textp)
    window.blit(redim, b)
    pygame.display.update()
    time.sleep(1)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                mainMenue()
            if event.type == MOUSEBUTTONDOWN:
                mainMenue()
startUp()
mainMenue()
