class quadrilateral:
    #Code
    def _init_(self,name):
        self.name=name

class kite(quadrilateral):
    #Code
    def _init_(self,name):
        super()._init_(name)

class trapezoid(quadrilateral):
    #Code
    def _init_(self,name):
        super()._init_(name)

class parallelogram(trapezoid):
    #Code
    def _init_(self,name):
        super()._init_(name)

class isosceles(trapezoid):
    #Code
    def _init_(self,name):
        super()._init_(name)

class rectangle(parallelogram,isosceles):
    #Code
    def _init_(self,name):
        super()._init_(name)

class rhombus(kite,parallelogram):
    #Code
    def _init_(self,name):
        super()._init_(name)

class square(rhombus,rectangle):
    #Code
    def _init_(self,name):
        super()._init_(name)
        