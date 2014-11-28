#This class is created for mock up purpose only
class FGPIO:
    #Constant
    BOARD = 1
    OUT = 2
    IN = 3
    
    def setmode(self, mode):
        print "set mode " , mode
        
    def setwarnings(self, warnings):
        print "setwarnings " ,warnings
        
    def setup(self, pin, mode):
        print "setup pin", pin , " mode ", mode
        