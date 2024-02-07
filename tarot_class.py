from random import*
import server
import asyncio
import queue
class Carte:
    def __init__(self,numero,types):
        self.numero=numero
        self.types=types
    def __str__(self):
        return str(chr(self.numero+65)+self.types)
    def __eq__(self, o: object) -> bool:
        if isinstance(o,Carte):
            return self.numero == o.numero and self.types == o.types
        return False

def convertstrcarte(s):
    l1=s[0]
    num=ord(l1)-65
    return Carte(num,s[1:])

class Tas:
    def __init__(self, cartes= []):
        self.cartes=cartes
        
    def toList(self):
        """From liste de cartes to affichage"""
        a=""
        for i in self.cartes:
            a+=str(i)+" "
        return a
    
    def addCartestr(self, carte):
        return self.cartes.append(convertstrcarte(carte))
    
    def removeCartestr(self, carte):
        for el in self.cartes :
            if carte==str(el) :
                return self.cartes.remove(el)

    def filtre(self,f):
        T = Tas()
        for i in range(len(self.cartes)):
            el = self.cartes[i] 
            if f(el,i):
                T.append(el)
        return T

    def append(self, v):
        self.cartes.append(v)
    
    def __str__(self):
        s = "["
        for el in self.cartes:
            s+=str(el)+", "
        return s+"]"



class Joueur (Tas):
    def __init__(self, ws,queue:queue.Queue,nom):
        Tas.__init__(self,[])
        self.pris=False
        self.ws = ws
        self.queue = queue
        self.nom = nom
    
    def sendmsg(self,msg):
        asyncio.run(server.send_msg(self.ws,msg))

    def waitmsg(self):
        while self.queue.qsize()>0:
            self.queue.get()
        return self.queue.get()

    





c1=Carte(1,"ca")
#print(c1)
c2=Tas([c1])
#print(c2.toList())
c2.addCartestr("Cca")
#print(c2.toList())
c2.removeCartestr("Bca")
#print(c2.toList())
