
import threading
import time
def affiche(nb, nom = ''):
    i=0
    while True:
     	print nom, i
     	time.sleep(2)


a = threading.Thread(None, affiche, None, (10,), {'nom':'thread a'})
b = threading.Thread(None, affiche, None, (10,), {'nom':'thread b'})
a.start()
b.start()