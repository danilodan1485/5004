class Puzzle():
    def __init__(self,column=3,row=3):
        import random
        values = []
        for i in range(column*row):
            values.append(i+1)
        self.tela = {}
        self.cols = column
        self.rows = row
        empty = False
        for c in range(column):
            self.tela[c] = {}
            for r in range(row):
                value = random.choice(values)
                values.remove(value)
                self.tela[c][r] = str(value).replace(str(column*row),'E')
                if self.tela[c][r] == 'E':
                    self.emptyPos = (c,r)
                    print('Achou')
                    print(self.emptyPos)
    
    def getScreen(self):
        return self.tela

    def moveUp(self):
        if self.emptyPos[0] == self.rows-1:
            print("Can't do that")
        else:
            posX = self.emptyPos[1]
            posY = self.emptyPos[0]+1
            value = self.tela[posY][posX]
            self.tela[posY][posX] = 'E'
            self.emptyPos = (posY,posX)
            print(self.emptyPos)
            self.tela[posY-1][posX] = value
            
    def moveDown(self):
        if self.emptyPos[0] == 0:
            print("Can't do that")
        else:
            posX = self.emptyPos[1]
            posY = self.emptyPos[0]-1
            value = self.tela[posY][posX]
            self.tela[posY][posX] = 'E'
            self.emptyPos = (posY,posX)
            print(self.emptyPos)
            self.tela[posY+1][posX] = value

    def moveLeft(self):
        if self.emptyPos[1] == self.cols-1:
            print("Can't do that")
        else:
            posX = self.emptyPos[1]+1
            posY = self.emptyPos[0]
            value = self.tela[posY][posX]
            self.tela[posY][posX] = 'E'
            self.emptyPos = (posY,posX)
            print(self.emptyPos)
            self.tela[posY][posX-1] = value

    def moveRight(self):
        if self.emptyPos[1] == 0:
            print("Can't do that")
        else:
            posX = self.emptyPos[1]-1
            posY = self.emptyPos[0]
            value = self.tela[posY][posX]
            self.tela[posY][posX] = 'E'
            self.emptyPos = (posY,posX)
            print(self.emptyPos)
            self.tela[posY][posX+1] = value
