class Person:
    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name
    
    def greet(self):
        print("hello, this is %s" % self.name)

foo = Person()
foo.setName("Andy")

foo.greet()