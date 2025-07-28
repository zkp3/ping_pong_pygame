import pygame
def drawText(textConf,surface):
    font=pygame.font.Font(textConf['fontPath'],textConf['size'])
    textSurface=font.render(textConf['text'],1,textConf['color'])
    if textConf['center']:pos=textSurface.get_rect(center=textConf['pos'])
    else:pos=textConf['pos'].copy()
    return surface.blit(textSurface,pos)
