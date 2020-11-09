class quadrilateral:
    #Code
    def _init_(self,name,side):
        self.name=name
        self.side=side

class kite(quadrilateral):
    #Code
    def _init_(self,name,side):
        super()._init_(name,side)

class trapezoid(quadrilateral):
    #Code
    def _init_(self,name,side):
        super()._init_(name,side)

class parallelogram(trapezoid):
    #Code
    def _init_(self,name,side):
        super()._init_(name,side)

class isosceles(trapezoid):
    #Code
    def _init_(self,name,side):
        super()._init_(name,side)

class rectangle(parallelogram,isosceles):
    #Code
    def _init_(self,name,side):
        super()._init_(name,side)

class rhombus(kite,parallelogram):
    #Code
    def _init_(self,name,side):
        super()._init_(name,side)

class square(rhombus,rectangle):
    #Code
    def _init_(self,name,side):
        super()._init_(name,side)
        