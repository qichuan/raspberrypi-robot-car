#This class is created for mock up purpose only
class FGPIO:
    #Constant
    BOARD = 1
    OUT = 2
    IN = 3
    
    def setmode(self, mode):
        print mode
        
    def setwarnings(self, warnings):
        print warnings
        
    def setup(self, pin, mode):
        print pin + mode
        