import sys
from distutils.core import setup

concoordversion = '0.9.0'

classifiers = [ 'Development Status :: 3 - Alpha'
              , 'Intended Audience :: Developers'
              , 'Intended Audience :: System Administrators'
              , 'License :: OSI Approved :: BSD License'
              , 'Operating System :: Windows'
              , 'Programming Language :: Python'
              ]

ldesc = "ConCoord is a novel coordination service that provides replication an\
d synchronization support for large-scale distributed systems. ConCoord employ\
s an object-oriented approach, in which the system actively creates and mainta\
ins live replicas for user-provided objects. Through ConCoord, the clients are\
able to access these replicated objects transparently as if they are local obj\
ects.  The ConCoord approach proposes using these replicated objects to implem\
ent coordination constructs in large-scale distributed systems, in effect esta\
blishing a transparent way of providing a coordination service."

setup(name='concoord',
      version=concoordversion,
      author='Deniz Altinbuken, Emin Gun Sirer',
      author_email='deniz@systems.cs.cornell.edu, egs@systems.cs.cornell.edu',
      packages=['concoord', 'concoord.object', 'concoord.proxy', 'concoord.threadingobject', 'concoord.openreplica'],
      scripts=['scripts/concoord'],
      license='3-Clause BSD',
      url='http://openreplica.org/',
      description='Coordination service for distributed systems.',
      long_description=ldesc,
      classifiers=classifiers,
      )
