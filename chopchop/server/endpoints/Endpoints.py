import sys

class EndpointNode(dict):
    load = None
    previous_node = None
    label = ''
    
    def __init__(self, label='', load=None, previous_node=None):
        self.load = load
        self.previous_node = previous_node
        self.label = label
        
class Endpoints:
    # Create the root node for all endpoints
    root_endpoint = EndpointNode()
    
    def add_endpoint(self, endpoint_parts, load=None):
        current_endpoint = self.root_endpoint
        
        for endpoint_part in endpoint_parts:
            if endpoint_part not in current_endpoint:
                current_endpoint[endpoint_part] = EndpointNode(endpoint_part, load, current_endpoint)
                current_endpoint = current_endpoint[endpoint_part]
            else:
                current_endpoint = current_endpoint[endpoint_part]
                
        current_endpoint.load = load
    
    def get_endpoint_node(self, endpoint_parts):
        hit = True
        current_endpoint = self.root_endpoint
        
        for endpoint_part in endpoint_parts:
            if endpoint_part not in current_endpoint:
                hit = False
                break
            else:
                current_endpoint = current_endpoint[endpoint_part]
        
        if hit is True:
            return current_endpoint
        else:
            raise KeyError("Provided endpoint was not found")
        
    def get_load_for_endpoint(self, endpoint_parts):
        try:
            endpoint_node = self.get_endpoint_node(endpoint_parts)
        except KeyError:
            raise KeyError("Provided endpoint was not found")
        
        try:
            return endpoint_node.load
        except:
            raise TypeError("Invalid endpoint node")
        
    def remove_endpoint(self, endpoint_parts):
        try:
            endpoint_node = self.get_endpoint_node(endpoint_parts)
        except KeyError:
            raise KeyError("Provided endpoint was not found")
        
        current_endpoint = endpoint_node
        ret_load = endpoint_node.load
        
        while current_endpoint is not self.root_endpoint:
            current_endpoint = current_endpoint.previous_node
            
            if len(current_endpoint) is 1:
                del current_endpoint[current_endpoint.keys()[0]]
                break
                
        return ret_load
        
    def move_endpoint(self, old_endpoint, new_endpoint, load=None, strict=False):
        put_load = load
        
        try:
            put_load = self.remove_endpoint(old_endpoint)
        except KeyError:
            if strict is False:
                ''' Essentially ignore any errors'''
                put_load = load
            else:
                raise KeyError("The endpoint to be moved was not present")
        
        self.add_endpoint(new_endpoint, put_load)
                
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
endpoint.add_endpoint(["you", "hello", "here", "there"], 11)
print "---------------------"
endpoint.remove_endpoint(["you", "hello", "here", "something"])

print endpoint.get_load_for_endpoint(["hello", "world"])
print endpoint.get_load_for_endpoint(["lol", "me"])
print endpoint.get_load_for_endpoint(["hello", "you"])
print endpoint.get_load_for_endpoint(["you", "hello"])
print endpoint.get_load_for_endpoint(["hello", "something"])
print endpoint.get_load_for_endpoint(["something", "world"])
print endpoint.get_load_for_endpoint(["o", "really"])


endpoint.add_endpoint(["hello", "world", "here"], 99)
endpoint.add_endpoint(["hello", "world", "there"], 99)
endpoint.add_endpoint(["hello", "something", "somewhere"], 199)

endpoint.move_endpoint(["hello", "something", "somewhere"], ["wicked", "sick"])
print endpoint.get_load_for_endpoint(["wicked", "sick"])

'''
