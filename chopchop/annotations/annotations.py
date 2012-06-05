from ..lib.Helper import Helper
from ..lib.FunctionInfo import FunctionInfo


class cc:

    @staticmethod
    def expose_function(func):
        info = Helper.get_function_info(func)
        print info.name
        print info.className
