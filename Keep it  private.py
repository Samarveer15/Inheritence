class myclass:

    __privateVar = 27
    
    def __privMeth(self):
        print("I'm inside the class myclass")


    def hello(self):
        print("Private Variable values:",myclass.__privateVar)


foo = myclass()
foo.hello()
foo.__privMeth()