# define class Complex
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    def getRealPart(self):
        return self.r

    def getImagePart(self):
        return self.i

# 类XC继承至Complex
class XC(Complex):
    def showRealAndImage(self):
        print self.r
        print self.i

xc = XC(3.0, -1.0)
xc.showRealAndImage()