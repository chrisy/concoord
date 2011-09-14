"""
@author: denizalti
@note: Peer
@date: February 1, 2011
"""
from enums import *
from utils import *

class Peer():
    """Peer instance of a Node"""
    def __init__(self, peeraddr, peerport, peertype=-1):
        """Initialize Peer

        Peer State
        - type: type of Peer (NODE_LEADER | NODE_ACCEPTOR | NODE_REPLICA | NODE_CLIENT)
        - port: port of Peer
        - addr: hostname of Peer
        """
        self.type = peertype
        self.port = peerport
        self.addr = peeraddr

    def getid(self):
        """Returns the id (addr:port) of the Peer"""
        return "%s:%d" % (self.addr, self.port)
    
    def __hash__(self):
        """Returns the hashed id"""
        return self.getid().__hash__()

    def __eq__(self, otherpeer):
        """Equality function for two Peers.
        Returns True if given Peer is equal to Peer, False otherwise.
        """
        if otherpeer == None:
            return False
        else:
            return self.addr == otherpeer.addr and self.port == otherpeer.port 

    # Added for testing
    def __lt__(self, otherpeer):
        if otherpeer == None:
            return False
        else:
            # XXX
            if otherpeer.addr == "128.84.96.226" or otherpeer.addr == "128.84.227.65":
                return False
            else:
                return self.port < otherpeer.port

    def __gt__(self, otherpeer):
        if otherpeer == None:
            return False
        else:
            # XXX
            if otherpeer.addr == "128.84.96.226"or otherpeer.addr == "128.84.227.65":
                return True
            else:
                return self.port > otherpeer.port

    def __ne__(self, otherpeer):
        """Non-equality function for two Peers.
        Returns True if given Peer is not equal to Peer, False otherwise.
        """
        if otherpeer == None:
            return False
        else:
            return self.addr != otherpeer.addr or self.port != otherpeer.port
        
    def __str__(self):
        """Return Peer information"""
        return '%s PEER(%s:%d)' % (node_names[self.type] if self.type != -1 else "UNKNOWN", self.addr, self.port)
