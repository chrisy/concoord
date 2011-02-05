'''
@author: denizalti
@note: The Client connects to a Leader and makes requests.
@date: February 1, 2011
'''
import socket

from optparse import OptionParser
from threading import Thread, Lock, Condition
from node import Node
from enums import *
from utils import findOwnIP
from communicationutils import scoutReply,commanderReply
from connection import ConnectionPool, Connection
from group import Group
from peer import Peer
from message import ClientMessage,Message,PaxosMessage,HandshakeMessage,PValue,PValueSet

parser = OptionParser(usage="usage: %prog -b bootstrap")
parser.add_option("-b", "--boot", action="store", dest="bootstrap", help="address:port:type triple for the bootstrap peer")
(options, args) = parser.parse_args()

class Client():
    def __init__(self, bootstrap):
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        bootaddr,bootport = bootstrap.split(":")
        self.socket.connect((bootaddr,int(bootport)))
        myaddr = findOwnIP()
        myport = self.socket.getsockname()[1]
        self.me = Peer(myaddr,myport,NODE_CLIENT)
        self.id = self.me.id()
        self.conn = Connection(self.socket)
        self.alive = True
        
    def clientloop(self):
        while self.alive:
            try:
                input = raw_input("client-shell> ")
                if len(input) == 0:
                    continue
                else:
                    cm = ClientMessage(MSG_CLIENTREQUEST, self.me, input)
                    self.conn.send(cm)
                    reply = self.conn.receive()
                    print reply
            except ( KeyboardInterrupt,EOFError ):
                os._exit(0)
        return
        
theClient = Client(options.bootstrap)
theClient.clientloop()

  


    
