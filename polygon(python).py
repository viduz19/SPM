class Polygon:
    __length=None
    __breadth=None
    
    def set_length(self,length):
        self.__length=length

    def get_length(self):
        return self.__length
    
    def set_breadth(self,breadth):
        self.__breadth=breadth
        
    def get_breadth(self):
        return self.__breadth
        
class Rectangle(Polygon):
    def area(self):
        return (self.get_length()*self.get_breadth())
    
class Square(Polygon):
    def area(self):
        return (self.get_length()*self.get_length())

rec_length= float(input("rec_length="))
rec_breadth=float(input("rec_breadth="))
squ_length=float(input("squ_length="))

rec=Rectangle()
rec.set_length(rec_length)
rec.set_breadth(rec_breadth)
print(rec.area())

squ=Square()
squ.set_length(squ_length)
print(squ.area())


