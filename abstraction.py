from abc import ABC,abstractmethod 

class abs(ABC):
    def print(self, y):
        self.y =  y
        print("passed value is " , self.y)
        
    @abstractmethod
    def work(self):
        print("this is called as abstraction method of python .")


class test(abs):
    def work(self):
        print("this is known as sub class method .")


test_object=test()
test_obeject.print(7)
test_object.work()