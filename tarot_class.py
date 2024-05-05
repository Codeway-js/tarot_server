import queue
from random import*
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
        a=[]
        for el in self.cartes:
            a.append(str(el))
        return a
    
    def addCartestr(self, carte):
        return self.cartes.append(convertstrcarte(carte))
    
    def removeCartestr(self, carte):
        for el in self.cartes :
            if carte==str(el) :
                return self.cartes.remove(el)
        print("yp nn effectif")

    def filtre(self,f):
        T = Tas()
        for i in range(len(self.cartes)):
            el = self.cartes[i] 
            if f(el,i):
                T.append(el)
        return T

    def append(self, v):
        self.cartes.append(v)

    def remove(self,v):
        self.cartes.remove(v)
    
    def __str__(self):
        s = "["
        for el in self.cartes:
            s+=str(el)+", "
        s=s[:-1]
        return s+"]"

def trycarte(s):
    print(s)
    c= input("donne carte ")
    try:
        t = convertstrcarte(c)
        if not t.types in c:
            raise IndexError()
        return c
    except:
        print("ptiote error tkt")
        return trycarte(s)

def cartejouablepremiertour(carte,cartesjeu):
    for cartejeu in cartesjeu :
        if str(cartejeu) == carte:
            return True
    return False
class Joueur (Tas):
    def __init__ (self,ws,s,q:queue.Queue,nom,terminal:bool):
        Tas.__init__(self,[])
        self.pris=False
        self.ws = ws
        self.queue = q
        self.server = s
        self.nom = nom
        self.terminal =terminal
    
    def sendmsg(self,msg):
        if not self.terminal:
            self.server.send_message(self.ws,msg)

    def waitmsg(self,op,l=[]):
        if not self.terminal:
            while self.queue.qsize()>0:
                self.queue.get()
            
            return waitq(self.queue)
        else:
            if op ==2:
                tuprendsoupas = input(self.nom+" Voulez-vous prendre ? ")
                if tuprendsoupas=="non":
                    res =-1
                else:
                    res=0
                return res
            elif op ==3:
                r=[]
                while len(r)!=6:
                    jouable=True
                    while jouable :
                        print(str(self))
                        print(r)
                        cartestr=trycarte("Quel carte voulez-vous retirer ?")
                        carteaenlever=convertstrcarte(cartestr) #PAS DATOUT NI ROI
                        # carteaenlever = self.cartes[randint(0,len(self.cartes)-1)]
                        # cartestr = str(carteaenlever)
                        if cartejouablepremiertour(cartestr,self.cartes)==True:
                            if carteaenlever.numero==14 or carteaenlever.types=="at":
                                print("Vous ne pouvez pas déposer de roi ni d'atout")
                            else:
                                r.append(cartestr)
                                jouable=False
                        else:
                            print("pas dans le jeu")
                return r
            elif op==4:
                return l[0]
                # return trycarte(self.nom+" Quel carte voulez-vous déposer ? ")
                        

    
def waitq(q:queue.Queue):
    try:
        return q.get(timeout=1)
    except queue.Empty:
        return waitq(q)

class fakePlayer(Tas):
    def __init__ (self,nom):
        Tas.__init__(self,[])
        self.pris=False
        self.nom = nom
    
    def sendmsg(self,msg):
        return msg
    def waitmsg(self):
        return


c1=Carte(1,"ca")
#print(c1)
c2=Tas([c1])
#print(c2.toList())
c2.addCartestr("Cca")
#print(c2.toList())
c2.removeCartestr("Bca")
#print(c2.toList())
