from ..annotations.annotations import cc


class HelloWorld:
    string = "Hello World"

    def __init__(self):
        self.string = "Hello World"

    @cc.expose_function
    def showHelloWorld(self):
        return self.string
