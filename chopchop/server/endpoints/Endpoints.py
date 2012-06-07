import sys

class EndpointNode(dict):
    load = None
    previous_node = None
    
    def __init__(self, load=None, previous_node=None):
        self.load = load
        self.previous_node = previous_node
        
class Endpoints:
    # Create the root node for all endpoints
    root_endpoint = EndpointNode()
    
    def add_endpoint(self, endpoint_parts, load=None):
        current_endpoint = self.root_endpoint
        
        for endpoint_part in endpoint_parts:
            if endpoint_part not in current_endpoint:
                current_endpoint[endpoint_part] = EndpointNode()
                current_endpoint = current_endpoint[endpoint_part]
            else:
                current_endpoint = current_endpoint[endpoint_part]
                
        current_endpoint.load = load
        
    def get_load_for_endpoint(self, endpoint_parts):
        hit = True
        current_endpoint = self.root_endpoint
        
        for endpoint_part in endpoint_parts:
            if endpoint_part not in current_endpoint:
                hit = False
                break
            else:
                current_endpoint = current_endpoint[endpoint_part]
        
        if hit is True:
            return current_endpoint.load
        
        return None
                
    def visualize(self, endpoint_node=None, level=0):
        if endpoint_node is None:
            endpoint_node = self.root_endpoint
        
        for i in range(0, level):
            sys.stdout.write('    ')
            
        for endpoint_part in endpoint_node:
            print endpoint_part
            self.visualize(endpoint_node[endpoint_part], level+1)

endpoint = Endpoints()

'''
SimpleTests: Yes, I know I should use some damn test framework.

endpoint.add_endpoint(["hello", "world"], 100)
print "---------------------"
endpoint.add_endpoint(["lol", "me"], 99)
print "---------------------"
endpoint.add_endpoint(["hello", "you"], 98)
print "---------------------"
endpoint.add_endpoint(["you", "hello"], 11)
print "---------------------"

print endpoint.get_load_for_endpoint(["hello", "world"])
print endpoint.get_load_for_endpoint(["lol", "me"])
print endpoint.get_load_for_endpoint(["hello", "you"])
print endpoint.get_load_for_endpoint(["you", "hello"])
print endpoint.get_load_for_endpoint(["hello", "something"])
print endpoint.get_load_for_endpoint(["something", "world"])
print endpoint.get_load_for_endpoint(["o", "really"])
'''
