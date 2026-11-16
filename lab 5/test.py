from abc import ABC, abstractmethod


class F(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    

    def prt(self):
        return f'name: {self.name}'        

class A(F):
    def __init__(self, name):
        super().__init__(name)

f = F('dima')

print(f.prt())
print(A('max').prt())