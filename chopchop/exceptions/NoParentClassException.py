class NoParentClassException(Exception):

    def __init__(self):
        Exception.__init__(self)

    def __init__(self, func_name):
        self.func_name = func_name

    def get_func_name(self):
        return self.func_name

    def set_func_name(self):
        return self.func_name

    def __str__():
        return "No class found for function: `" + self.func_name + "`"
