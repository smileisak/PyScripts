#!/usr/bin/env python

import threading
import time

class Affiche(threading.Thread):
    def __init__(self, nom = ''):
        threading.Thread.__init__(self)
        self.nom = nom
        self.Terminated = False
    def run(self):
        i = 0
        while not self.Terminated:
            print self.nom, i
            i += 1
            time.sleep(2.0)
        print "le thread "+self.nom +" s'est termine proprement"
    def stop(self):
        self.Terminated = True  


class Affiche2(threading.Thread):
    def __init__(self, nom = ''):
        threading.Thread.__init__(self)
        self.nom = nom
        self._stopevent = threading.Event( )
    def run(self):
        i = 0
        while not self._stopevent.isSet():
            print self.nom, i
            i += 1
            self._stopevent.wait(2.0)
        print "le thread "+self.nom +" s'est termine proprement"
    def stop(self):
        self._stopevent.set( )
        
a = Affiche('Thread A')
b = Affiche('Thread B')
c = Affiche2('Thread C')

a.start()
b.start()
c.start()
time.sleep(6.5)
a._Thread__stop()
b.stop()
c.stop()