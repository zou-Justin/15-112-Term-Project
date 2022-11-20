class Player():

    def __init__(self,x,y):
        self.x = x
        self.y = y

    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

    def moveLeft(self):
        self.x -= 10
    
    def moveRight(self):
        self.x += 10
    
    def moveUp(self):
        self.y -= 10

    def moveDown(self):
        self.y += 10