#  File: LinearEquation.py
#  Description: HW11: Linear Equations
#  Student's Name: Austin Keith Faulkner
#  Student's UT EID: akf354
#  Course Name: CS 303E 
#  Unique Number: 50075
#
#  Date Created: October 23, 2019
#  Date Last Modified: October 29, 2019 (4:56 pm)

############################################################################


class LinearEquation():

    def __init__(self, m, b):                                                   
        self.__m = m
        self.__b = b

    def showEq(self):                                                          
        if self.__m > 0 and self.__b > 0:
            return str(self.__m) + "x + " + str(self.__b)
        elif self.__m > 0 and self.__b == 0:
            return str(self.__m) + "x" 
        elif self.__m > 0 and self.__b < 0:
            return str(self.__m) + "x - " + str(abs(self.__b))
        elif self.__m < 0 and self.__b < 0:
            return "- " + str(abs(self.__m)) + "x - " + str(abs(self.__b))
        elif self.__m < 0 and self.__b == 0:
            return "- " + str(abs(self.__m)) 
        elif self.__m < 0 and self.__b > 0:
            return "- " + str(abs(self.__m)) + "x + " + str(self.__b)
        elif self.__m == 0: 
            return str(self.__b)
        elif self.__b == 0:
            return str(self.__m) + "x" 
        elif self.__m == 0 and self.__b == 0:
            return 0
        
    def evaluate(self, x):
        return self.__m * x + self.__b      

    def compose(self, linearEquation):
        return LinearEquation(self.__m * linearEquation.__m, self.__m * linearEquation.__b + self.__b)  

    def add(self, linearEquation):                                                                      
        return LinearEquation(self.__m + linearEquation.__m, self.__b + linearEquation.__b)

    def sub(self, linearEquation):
        return LinearEquation(self.__m - linearEquation.__m, self.__b - linearEquation.__b)
        

def main():

   f = LinearEquation(5,3)
   print("f(x) =",f.showEq())
   print("f(3) =",f.evaluate(3),"\n")
         
   g = LinearEquation(-2,-6)
   print("g(x) =",g.showEq())
   print("g(-2) =",g.evaluate(-2),"\n")

   h = f.add(g)
   print("h(x) = f(x) + g(x) =",h.showEq())
   print("h(-4) =",h.evaluate(-4),"\n")

   j = f.sub(g)
   print("j(x) = f(x) - g(x) =",j.showEq())
   print("j(-4) =",j.evaluate(-4),"\n")

   k = f.compose(g)
   print("f(g(x)) =",k.showEq(),"\n")

   m = g.compose(f)
   print("g(f(x)) =",m.showEq(),"\n")

   g = LinearEquation(5,-3)
   print("g(x) =",g.showEq())
   print("g(-2) =",g.evaluate(-2),"\n")

   h = f.add(g)
   print("h(x) = f(x) + g(x) =",h.showEq())
   print("h(-4) =",h.evaluate(-4),"\n")

   j = f.sub(g)
   print("j(x) = f(x) - g(x) =",j.showEq())
   print("j(-4) =",j.evaluate(-4),"\n")

main()
