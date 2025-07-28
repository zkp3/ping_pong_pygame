import pygame

class scaler:
    @staticmethod
    def scaleSize(origSize, newSize, origObjSize):
        scaleFactor = min(
            newSize[0]/origSize[0],
            newSize[1]/origSize[1]
        )
        return [round(origObjSize[0]*scaleFactor),round(origObjSize[1]*scaleFactor)]

    @staticmethod
    def imgTransf(path, newSize):
        img = pygame.image.load(path).convert_alpha()
        img = pygame.transform.scale(img, (newSize[0], newSize[1]))
        return img
