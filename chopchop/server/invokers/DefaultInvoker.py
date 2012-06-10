from Invoker import Invoker
from ...lib.Helper import Helper

class DefaultInvoker(Invoker):
    def get_identifier(self):
        return "default"
        
    def set_preparator(self, prep_func):
        super(DefaultInvoker, self).set_preperator(prep_func)
        
    def set_janitor(self, janitor_func):
        super(DefaultInvoker, self).set_janitor(janitor_fun)
        
    def invoke(self, func):
        if Helper.is_func(func):
            return func()
        else:
            raise TypeError("Cannot invoke function. Provided value is not a function")


Invoker.register(DefaultInvoker)

'''
def hello():
    print 'Hello World'
    
class Something:
    def hello(self):
        print 'Hello World [class]'
    
    @staticmethod
    def st_hello():
        print 'Hello World [static]'
        
defInvoke = DefaultInvoker()
defInvoke.invoke(hello)
defInvoke.invoke(Something.st_hello)

smInstance = Something()
defInvoke.invoke(smInstance.hello)
'''
