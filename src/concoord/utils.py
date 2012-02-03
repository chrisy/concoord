'''
@author: Deniz Altinbuken, Emin Gun Sirer
@note: Utility functions for the runtime. Includes a timer module for collecting measurements.
@date: February 3, 2011
@copyright: See COPYING.txt
'''
import socket
import os, sys
import time
import string
import threading
from enums import *

def findOwnIP():
    """Retrieves the hostname of the caller"""
    return socket.gethostbyname(socket.gethostname())

class ConsoleLogger():
    def __init__(self, name):
        self.prefix = name
        self.logfile = open("concoord_log_"+name, 'w')

    def write(self, cls, str):
        print "%s [%s] %s: %s\n" % (time.asctime(time.localtime(time.time())), self.prefix + '_' + threading.current_thread().name, cls, str)
        self.logfile.write("%s [%s] %s: %s\n" % ((time.asctime(time.localtime(time.time())), self.prefix, cls, str)))
        self.logfile.flush()

    def close(self):
        self.logfile.close()

class NetworkLogger():
    def __init__(self, name, lognode):
        self.prefix = name
        logaddr,logport = lognode.split(':')
        try:
            self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
            self.socket.setsockopt(socket.IPPROTO_TCP,socket.TCP_NODELAY,1)
            self.socket.connect((logaddr,int(logport)))
        except socket.error, e:
            return

    def write(self, cls, str):
        try:
            print "%s [%s] %s: %s\n" % (time.asctime(time.localtime(time.time())), self.prefix + '_' + threading.current_thread().name, cls, str)
            self.socket.send("[%s] %s: %s\n" % (self.prefix + '_' + threading.current_thread().name, cls, str))
        except:
            return

    def close(self):
        self.socket.close()
        
timers = {}
def starttimer(timerkey, timerno):
    global timers
    index = "%s-%s" % (str(timerkey),str(timerno))
    if not timers.has_key(index):
        timers[index] = [time.time(), 0]

def endtimer(timerkey, timerno):
    global timers
    index = "%s-%s" % (str(timerkey),str(timerno))
    try:
        if timers[index][1] == 0:
            timers[index][1] = time.time()
    except:
        print "Can't stop timer %s %s." % (str(timerkey),str(timerno))
    
def dumptimers(numreplicas, numacceptors, ownertype, outputdict):
    global timers
    if ownertype == NODE_REPLICA:
        filename = "output/replica/%s-%s" % (str(numreplicas), str(numacceptors))
    elif ownertype == NODE_ACCEPTOR:
        filename = "output/acceptor/%s-%s" % (str(numreplicas), str(numacceptors))
    try:
        outputfile = open(outputdict+filename, "w")
    except:
        outputfile = open("./"+filename, "w")
    for index,numbers in timers.iteritems():
        timerkey, timerno = index.rsplit("-")
        if not numbers[1]-numbers[0] < 0:
            outputfile.write("%s:\t%s\t%s\t%s\n"  % (str(timerno), str(numreplicas), str(numacceptors), str(numbers[1]-numbers[0])))
    outputfile.close()

def starttiming(fn):
    """Decorator used to start timing. Keeps track of the count for the first and second calls."""
    def new(*args, **kw):
        obj = args[0]
        if obj.firststarttime == 0:
            obj.firststarttime = time.time()
        elif obj.secondstarttime == 0:
            obj.secondstarttime = time.time()
        return fn(*args, **kw)
    return new

def endtiming(fn):
    """Decorator used to end timing. Keeps track of the count for the first and second calls."""
    NITER = 10000
    def new(*args, **kw):
        ret = fn(*args, **kw)
        obj = args[0]
        if obj.firststoptime == 0:
            obj.firststoptime = time.time()
        elif obj.secondstoptime == 0:
            obj.secondstoptime = time.time()
        elif obj.count == NITER:
            now = time.time()
            total = now - obj.secondstarttime
            perrequest = total/NITER
            filename = "output/%s-%s" % (str(len(obj.groups[NODE_REPLICA])+1),str(len(obj.groups[NODE_ACCEPTOR])))
            outputfile = open("./"+filename, "a")
            # numreplicas #numacceptors #perrequest #total
            outputfile.write("%s\t%s\t%s\t%s\n" % (str(len(obj.groups[NODE_REPLICA])+1), str(len(obj.groups[NODE_ACCEPTOR])), str(perrequest), str(total)))
            outputfile.close()
            obj.count += 1
            sys.stdout.flush()
            profile_off()
            profilerdict = get_profile_stats()
            for key, value in sorted(profilerdict.iteritems(), key=lambda (k,v): (v[2],k)):
                print "%s: %s" % (key, value)
            time.sleep(10)
            sys.stdout.flush()
            os._exit(0)
        else:
            obj.count += 1
        return ret
    return new