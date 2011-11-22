#automatically generated by the proxygenerator
from clientproxyonerun import *

class OpenReplicaCoordProxy():
    def __init__(self, bootstrap):
        self.proxy = ClientProxy(bootstrap)
        self.number = 1

    def __str__(self):
        self.number += 1
        self.proxy.invoke_command(self.number, "__str__")

    def addnodetosubdomain(self, subdomain, node):
        self.number += 1
        self.proxy.invoke_command(self.number, "addnodetosubdomain", subdomain, node)

    def addsubdomain(self, subdomain):
        self.number += 1
        self.proxy.invoke_command(self.number, "addsubdomain", subdomain)

    def delnodefromsubdomain(self, subdomain, node):
        self.number += 1
        self.proxy.invoke_command(self.number, "delnodefromsubdomain", subdomain, node)

    def delsubdomain(self, subdomain):
        self.number += 1
        self.proxy.invoke_command(self.number, "delsubdomain", subdomain)

    def getnodes(self, subdomain):
        self.number += 1
        self.proxy.invoke_command(self.number, "getnodes", subdomain)

    def getsubdomains(self):
        self.number += 1
        self.proxy.invoke_command(self.number, "getsubdomains")

