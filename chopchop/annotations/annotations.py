from ..lib.Helper import Helper
from ..lib.FunctionInfo import FunctionInfo

something = None

class cc:
    

    @staticmethod
    def expose_function(func):
        
        return func
        
    @staticmethod
    def expose_class(clazz):
        print clazz.__dict__.keys()
        return clazz        
