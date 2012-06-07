import abc
import types

class Invoker(object):
    __metaclass__ = abc.ABCMeta
    
    @staticmethod
    def is_func(func):
        _valid_func_types = [types.FunctionType, types.LambdaType, types.UnboundMethodType, types.MethodType]
        return type(func) in _valid_func_types
        
    @staticmethod
    def func_requires_parent(func):
        _valid_func_types = [types.UnboundMethodType, types.MethodType]
        return type(func) in _valid_func_types
    
    @abc.abstractmethod
    def invoke(self, func):
        """
        Invoke a function and return immediately. This function
        may or may not return what the function actually returned.
        If a function call fails, it is expected to throw an exception
        and not a status code
        """
        return
        
    @abc.abstractmethod
    def set_preparator(self, prep_func):
        self.prep_func = prep_func
        
    @abc.abstractmethod
    def set_janitor(self, janitor_func):
        self.janitor_func = janitor_func
        
    @abc.abstractmethod
    def get_identifier(self):
        """
        Should return an identifier which can be used to identify a
        invoker. Should never return 'default' by any other invoker
        other than the DefaultInvoker
        """
        return
'''
def something():
    return
    
class Something:
    def hello(self):
        return
        
    @staticmethod
    def stm():
        return
        
print Invoker.is_func(something)
print Invoker.is_func(Something.stm)
print Invoker.is_func(Something().hello)
print Invoker.is_func(lambda x: x)
print "---------------------------"
print Invoker.func_requires_parent(Something.stm)
print Invoker.func_requires_parent(Something().hello)
'''
