class  Bank:
    def __init__(self,name,age,money,key):
        self._name=name
        self._age=age
        self.__money=money
        self.__key=key

    def set_name(self,name):...

    def get_name(self):...

class MyBank(Bank) :
    def __init__(self,argument1,argument2):
        @property
        def argument1(self):
            return self._argument1
        @argument1.setter
        def argument1(self,value):
            self._argument1=value
            @property
            def argument2(self):
                return self._argument2
            @argument2.setter
            def  argument2(self,value):
                self._argument2= value

class MyNewBank (MyBank):
    def __init__(self,argument1,argument2, argument3, argument4):
        super(). __init__(argument1, argument2)
        self.argument3= argument3
        self._argument4= argument4
        @property
        def argument3(self):
            return self._argument3git
        @argument3.setter
        def argument3(self, value):

            self._argument3= value
        @property
        def argument4(self):
            return self._argument4
        @argument4.setter
        def argument4(self, value):
            self._argument4= value
