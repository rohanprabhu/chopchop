from ..endpoints.Endpoints import Endpoints
from .HandlerStore import HandlerStore

from wsgiref.simple_server import make_server

'''
Keeping the function so that I can chuckle to myself
every now and then. Check the non-commented clean_endpoints 

def clean_endpoints(endpoint_parts):
    count = len(endpoint_parts)
    i = 0
   
    while True:
        if i >= count:
            break
           
        if endpoint_parts[i].isspace() or endpoint_parts[i] is "":
            count = count - 1
            del endpoint_parts[i]
        else:
            endpoint_parts[i] = endpoint_parts[i].strip()
            i = i + 1
'''
            
def clean_endpoints(endpoint_parts):
    return [ele.strip() for ele in endpoint_parts if not ele.isspace() or ele is ""]

def chopchop_app(environ, start_response):
    path_info = environ["PATH_INFO"]
    path = path_info.split('/')
    path = clean_endpoints(path)
    
    response_body = "ChopChop is running"
    
    print path
    
    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain'),
                  ('Content-Length', str(len(response_body)))]
                  
    start_response(status, response_headers)
       
    return [response_body]

class ChopChop:
    endpoint_store = Endpoints()
    httpd = None
    handler_store = HandlerStore()
    
    global chopchop_app
    
    def __init__(self):
        self.httpd = make_server('localhost', 3737, chopchop_app)
        
    def start(self):
        while True:
            self.httpd.handle_request()
        
chopchop = ChopChop()
