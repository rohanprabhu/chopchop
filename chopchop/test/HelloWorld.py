from ..annotations.annotations import cc

@cc.expose_class
class HelloWorld:
    string = "Hello World"

    def __init__(self):
        self.string = "Hello World"

    @cc.expose_function
    def showHelloWorld(self):
        return self.string

print "POST", type(HelloWorld.showHelloWorld)