import sys, os, pygame, importlib, random
from src import scaler, drawText
import conf
drawText=drawText.drawText
scaler=scaler.scaler()

mainDir=os.path.dirname(__file__)
themeConf=importlib.import_module('themes.' + conf.theme + '.themeConf')
themePath=os.path.dirname(os.path.abspath(themeConf.__file__))
pygame.init()
clock=pygame.time.Clock()
pygame.display.set_caption('ping_pong')
displayInfo=pygame.display.Info()

scrnSize=[800,600]
origSurface=pygame.Surface((800,600))
if conf.fullscreen:scrnSize=[displayInfo.current_w,displayInfo.current_h]
screen=pygame.display.set_mode((scrnSize),pygame.FULLSCREEN)

music=pygame.mixer.music.load(themePath+themeConf.pathes['music'])
pygame.mixer_music.play(-1)
sfx={
    'success':pygame.mixer.Sound(themePath+themeConf.pathes['successSfx']),
    'nSuccess':pygame.mixer.Sound(themePath+themeConf.pathes['nSuccessSfx'])
}
pygame.mixer.music.set_volume(0.2)
sfx['success'].set_volume(1)
sfx['nSuccess'].set_volume(1)

players={
    0:{
        'pos':[0,0],
        'score': 0,
        'speed':conf.dfSpeed,
        'size':[32,64]
    },
    1:{
        'pos':[768,0],
        'score':0,
        'speed':conf.dfSpeed,
        'size':[32,64]
    }
}
ball={
    'pos':[384,284],
    'speed':[conf.dfSpeed,conf.dfSpeed],
    'size':[32,32]
}
textsConf={
    'start':{
        'fontPath':themePath+themeConf.pathes['font'],
        'pos':[400,300],
        'size':100,
        'color':themeConf.fontColor,
        'text':'Press Enter',
        'center':1
    },
    'help':{
        'fontPath':themePath+themeConf.pathes['font'],
        'pos':[400,500],
        'size':23,
        'color':themeConf.fontColor,
        'text':'To set up, open the conf.py file in the game directory',
        'center':1
    },
    'score':{
        'fontPath':themePath+themeConf.pathes['font'],
        'pos':[400,25],
        'size':50,
        'color':themeConf.fontColor,
        'text':'0|0',
        'center':1
    }
}
imgs={
    'menuBg':scaler.imgTransf(themePath+themeConf.pathes['menuBg'],[800,600]),
    'gameBg':scaler.imgTransf(themePath+themeConf.pathes['gameBg'],[800,600]),
    'rect':scaler.imgTransf(themePath+themeConf.pathes['rectImg'],[32,64]),
    'ball':scaler.imgTransf(themePath+themeConf.pathes['ballImg'],[32,32])
}
snowflakes=[]
for _ in range(conf.snowflakes['maxNum']):
    snowflakes.append({
        'pos':[random.randint(0,800),random.randint(0,600)],
        'size':random.randint(1,conf.snowflakes['maxSize']) if conf.snowflakes['maxSize']>0 else 0,
        'speed':random.randint(1,conf.snowflakes['maxSpeed']) if conf.snowflakes['maxSpeed']>0 else 0
    })

def handleEvents(run):
    pressedKeys = {}
    for event in pygame.event.get():
        if event.type==pygame.QUIT:run=0
        elif event.type==pygame.KEYDOWN and event.key not in pressedKeys:
            pressedKeys[event.key]=1
        elif event.type==pygame.KEYUP and event.key in pressedKeys:
            pressedKeys[event.key]=0
    return run, pressedKeys
run='menu'
while run:
    run,pressedKeys=handleEvents(run)
    oneKeyD=pressedKeys.get

    keys=pygame.key.get_pressed()
    if run=='menu':
        origSurface.blit(imgs['menuBg'],(0,0))
        drawText(textsConf['start'],origSurface)
        drawText(textsConf['help'],origSurface)
        for snowflake in snowflakes:
            pos=snowflake['pos']
            size=snowflake['size']
            speed=snowflake['speed']
            pos[1]+=speed
            if pos[1]>600:pos[1]=0
            pygame.draw.rect(origSurface,themeConf.fontColor,(pos[0],pos[1],size,size))
        if oneKeyD(pygame.K_ESCAPE):run=0
        if keys[pygame.K_RETURN]:run='game'
    elif run=='game':
        origSurface.blit(imgs['gameBg'],(0,0))
        drawText(textsConf['score'],origSurface)
        origSurface.blit(imgs['rect'],players[0]['pos'])
        origSurface.blit(imgs['rect'],players[1]['pos'])
        origSurface.blit(imgs['ball'],ball['pos'])
        for snowflake in snowflakes:
            pos=snowflake['pos']
            size=snowflake['size']
            speed=snowflake['speed']
            pos[1]+=speed
            if pos[1]>600:pos[1]=0
            pygame.draw.rect(origSurface,themeConf.fontColor,(pos[0],pos[1],size,size))

        ball['pos'][0] += ball['speed'][0]
        ball['pos'][1] += ball['speed'][1]
        if ball['pos'][0] <= 0 and ball['speed'][0] < 0:
            ball['pos'][0]+=players[0]['size'][0]+1
            ball['speed'][0] = -ball['speed'][0]
            players[1]['score']+=1
            players[0]['speed']*=conf.accelerat
            sfx['nSuccess'].play()
        if ball['pos'][0] >= 800 - ball['size'][0] and ball['speed'][0] > 0:
            ball['pos'][0]-=players[1]['size'][0]+1
            ball['speed'][0] = -ball['speed'][0]
            players[0]['score']+=1
            players[1]['speed']*=conf.accelerat
            sfx['nSuccess'].play()
        if ((ball['pos'][1] <= 0 and ball['speed'][1] < 0) or
            (ball['pos'][1] >= 600 - ball['size'][1] and ball['speed'][1] > 0)):
            ball['speed'][1] = -ball['speed'][1]


        if keys[pygame.K_w]:
            if players[0]['pos'][1]-players[0]['speed']>=0:
                players[0]['pos'][1]-=players[0]['speed']
            elif players[0]['pos'][1]>0:players[0]['pos'][1]=0
        if keys[pygame.K_s]:
            if players[0]['pos'][1]+players[0]['speed']<=600-players[0]['size'][1]:
                players[0]['pos'][1]+=players[0]['speed']
            elif players[0]['pos'][1]<600-players[0]['size'][1]:
                players[0]['pos'][1]=600-players[0]['size'][1]
        if keys[pygame.K_UP]:
            if players[1]['pos'][1]-players[1]['speed']>=0:
                players[1]['pos'][1]-=players[1]['speed']
            elif players[1]['pos'][1]>0:players[1]['pos'][1]=0
        if keys[pygame.K_DOWN]:
            if players[1]['pos'][1]+players[1]['speed']<=600-players[1]['size'][1]:
                players[1]['pos'][1]+=players[1]['speed']
            elif players[1]['pos'][1]<600-players[1]['size'][1]:
                players[1]['pos'][1]=600-players[1]['size'][1]
        playersRect=[
            pygame.Rect(players[0]['pos'][0],players[0]['pos'][1],players[0]['size'][0],players[0]['size'][1]),
            pygame.Rect(players[1]['pos'][0],players[1]['pos'][1],players[1]['size'][0],players[1]['size'][1])
        ]
        ballRect = pygame.Rect(ball['pos'][0],ball['pos'][1],ball['size'][0],ball['size'][1])
        if playersRect[0].colliderect(ballRect):
            ball['pos'][0]+=players[0]['size'][0]+1
            players[0]['score']+=1
            players[1]['speed']*=conf.accelerat
            ball['speed'][0]*=conf.accelerat
            ball['speed'][1]*=conf.accelerat
            if ball['speed'][0]<0:ball['speed'][0]=-ball['speed'][0]
            sfx['success'].play()
        if playersRect[1].colliderect(ballRect):
            ball['pos'][0]-=players[1]['size'][0]+1
            players[1]['score']+=1
            players[0]['speed']*=conf.accelerat
            ball['speed'][0]*=conf.accelerat
            ball['speed'][1]*=conf.accelerat
            if ball['speed'][0]>0:ball['speed'][0]=-ball['speed'][0]
            sfx['success'].play()
        textsConf['score']['text']=str(players[0]['score'])+'|'+str(players[1]['score'])

        if oneKeyD(pygame.K_ESCAPE):
            oneKeyD=handleEvents(run)[1].get
            ball['pos']=[384,384]
            ball['speed']=[conf.dfSpeed,conf.dfSpeed]
            players[1]['speed']=players[0]['speed']=conf.dfSpeed
            players[1]['score']=players[0]['score']=0
            players[1]['pos'][1]=players[0]['pos'][1]=0
            run='menu'

    scaledSurfaceSize=scaler.scaleSize([800,600],scrnSize,[800,600])
    scaledSurfacePos=[(scrnSize[0]-scaledSurfaceSize[0])//2, (scrnSize[1]-scaledSurfaceSize[1])//2]

    scaledSurface=pygame.transform.scale(origSurface,(scaledSurfaceSize[0],scaledSurfaceSize[1]))
    screen.blit(scaledSurface,(scaledSurfacePos[0],scaledSurfacePos[1]))
    clock.tick(60)
    pygame.display.flip()
pygame.quit()
sys.exit()
