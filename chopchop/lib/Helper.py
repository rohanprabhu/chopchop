from FunctionInfo import FunctionInfo
from ..exceptions.NoParentClassException import NoParentClassException
from ..lib.Constants import constants

import types


class Helper:
    @staticmethod
    def is_func(func):
        _valid_func_types = [types.FunctionType, types.LambdaType, types.UnboundMethodType, types.MethodType]
        return type(func) in _valid_func_types

    @staticmethod
    def get_function_info(func):
        className = ''
        funcName = func.__name__
        
        if type(func) == types.MethodType:
            _class = func.im_class

            if _class is not None:
                className = _class.__name__
            else:
                raise NoParentClassException(funcName)
        elif type(func) == types.FunctionType:
            className = constants.get_root_class_name()

        return FunctionInfo(funcName, className)
