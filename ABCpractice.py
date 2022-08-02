import random
from abc import ABC,abstractmethod

class lis0(ABC):
    def __init__(self,size):
        self.size=size
        self.LIST=[]

    @abstractmethod
    def setter(self,size):
        pass
    @abstractmethod
    def maker(self):
        pass


class lis1(lis0):
    def __init__(self,size):
        lis0.__init__(self,size)
    def maker(self):
        if self.size.isdigit():
            pass
        else:
            print(f"ERROR '{self.size}' is not digit!")
            exit()
        i = 0
        x = 0
        while i != int(self.size):
            x = random.randint(0, 20)
            self.LIST.append(x)
            i += 1
    def setter(self,size):
        self.LIST.clear()
       # self.size = size
        if size.isdigit():
            self.size=size
        else:
            print(f"ERROR '{size}' is not digit!")
            exit()

class lis2(lis0):
    def __init__(self,size):
        lis0.__init__(self,size)
    def maker(self):
        if self.size.isdigit():
            pass
        else:
            print(f"ERROR '{self.size}' is not digit!")
            exit()
        i = 0
        x = 0
        while i != int(self.size):
            x = random.randint(0, 20)
            self.LIST.append(x)
            i += 1
    def setter(self,size):
        self.LIST.clear()
        #self.size = size
        if size.isdigit():
            self.size=size
        else:
            print(f"ERROR '{size}' is not digit!")
            exit()
class lis3():
    def __init__(self,lis01,lis02):
        self.LIST=[]
        self.lis01=lis01
        self.lis02=lis02
    def maker(self):
        for i in self.lis01:
            if i in self.lis02:
                self.LIST.append(i)


def main():
    x= input("Введите размер первого списка: ")
    ist1=lis1(x)
    
    ist1.maker()
    x = input("Введите размер второго списка: ")
    ist2 = lis2(x)
    
    ist2.maker()
    list11=ist1.LIST
    list22=ist2.LIST
    ist12=lis3(list11,list22)
    ist12.maker()
    list12=ist12.LIST
    print("",list11 ,"\n",list22,"\n",list12)
    x = input("Введите размер первого списка: ")
    ist1.setter(x)
    
    ist1.maker()
    x = input("Введите размер второго списка: ")
    ist2.setter(x)
    
    ist2.maker()
    list11 = ist1.LIST
    list22 = ist2.LIST
    ist12 = lis3(list11, list22)
    ist12.maker()
    list12 = ist12.LIST
    print("", list11, "\n", list22, "\n", list12)

if __name__=='__main__':
    main()