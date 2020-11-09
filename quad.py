class quadrilateral:
    #Code
    def _init_(self,name):
        self.name=name

    def parent(self):
         for base in self.__class__.__bases__:
             print(base.__name__)

class kite(quadrilateral):
    #Code
    def _init_(self,name):
        super()._init_(name)
    def parent(self):
        for base in self.__class__.__bases__:
            print(base.__name__)

class trapezoid(quadrilateral):
    #Code
    def _init_(self,name):
        super()._init_(name)
    def parent(self):
        for base in self.__class__.__bases__:
            print(base.__name__)

class parallelogram(trapezoid):
    #Code
    def _init_(self,name):
        super()._init_(name)
    def parent(self):
        for base in self.__class__.__bases__:
            print(base.__name__)

class isosceles(trapezoid):
    #Code
    def _init_(self,name):
        super()._init_(name)
    def parent(self):
        for base in self.__class__.__bases__:
            print(base.__name__)

class rectangle(parallelogram,isosceles):
    #Code
    def _init_(self,name):
        super()._init_(name)
    def parent(self):
        for base in self.__class__.__bases__:
            print(base.__name__)

class rhombus(kite,parallelogram):
    #Code
    def _init_(self,name):
        super()._init_(name)
    def parent(self):
        for base in self.__class__.__bases__:
            print(base.__name__)

class square(rhombus,rectangle):
    #Code
    def _init_(self,name):
        super()._init_(name)
    def parent(self):
        for base in self.__class__.__bases__:
            print(base.__name__)

print("\nquadrilateral\nparents:")
Quad_foo = quadrilateral()
Quad_foo.parent()

print("\nkite\nparents:")
kite_foo = kite()
kite_foo.parent()

print("\ntrapezoid\nparents:")
trapezoid_foo = trapezoid()
trapezoid_foo.parent()

print("\nparallelogram\nparents:")
parallelogram_foo = parallelogram()
parallelogram_foo.parent()

print("\nisosceles\nparents:")
isosceles_foo = isosceles()
isosceles_foo.parent()

print("\nrectangle\nparents:")
rectangle_foo = rectangle()
rectangle_foo.parent()

print("\nrhombus\nparents:")
rhombus_foo = rhombus()
rhombus_foo.parent()

print("\nsquare\nparents:")
square_foo = square()
square_foo.parent()
