class OpenReplicaCoord():
    def __init__(self, **kwargs):
        self.nodes = {}

    def addnodetosubdomain(self, subdomain, node, **kwargs):
        if subdomain in self.nodes:
            self.nodes[subdomain].add(node)
        else:
            self.nodes[subdomain] = set()
            self.nodes[subdomain].add(node)

    def delsubdomain(self, subdomain, **kwargs):
        exists = subdomain in self.nodes
        if exists:
            del self.nodes[subdomain]
        return exists
        
    def delnodefromsubdomain(self, subdomain, node, **kwargs):
        exists = subdomain in self.nodes
        if exists:
            self.nodes[subdomain].remove(node)
        return exists

    def getnodes(self, subdomain, **kwargs):
        return self.nodes[subdomain]

    def getsubdomains(self, **kwargs):
        return self.nodes.keys()

    def _reinstantiatefromstr(self, state, **kwargs):
        self.nodes = {}
        for subdomain in state.split('-'):
            if subdomain != '':
                subdomainitems = subdomain.split('\n')
                self.nodes[subdomainitems[0]] = set(subdomainitems[1:])

    def __str__(self, **kwargs):
        rstr = ''	
        for domain,nodes in self.nodes.iteritems():
            rstr += domain + '\n' + '\n'.join(nodes) + "-"
        return rstr
