from ...lib.Helper import Helper

import types

class HandlerStore:
    handlers = {}
    
    def add_handler(self, load_type, handler, overwrite=False):
        if is_func(handler) is False:
            raise ValueError("Handler is expected to be a function")
            
        if type(load_type) is not types.TypeType:
            raise ValueError("Load type must be a type")
            
        if load_type in handlers:
            if overwrite is True:
                raise ValueError("A handler is already associated with the given load type")
        
        handlers[load_type] = handler
        
    def get_handler(self, load_type):
        return handlers[load_type]
    