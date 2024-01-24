from random import*

class Carte:
    def __init__(self,numero,types):
        self.numero=numero
        self.types=types
    def __str__(self):
        return str(chr(self.numero+65)+self.types)

def convertstrcarte(s):
    l1=s[0]
    num=ord(l1)-65
    return Carte(num,s[1:])

class Tas:
    def __init__(self, cartes):
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


    def append(self, v):
        self.cartes.append(v)
    
class Joueur (Tas):
    def __init__(self, nom, carte, pris):
        self.nom=nom
        Tas.__init__(self, carte)
        self.pris=pris
    
c1=Carte(1,"ca")
#print(c1)
c2=Tas([c1])
#print(c2.toList())
c2.addCartestr("Cca")
#print(c2.toList())
c2.removeCartestr("Bca")
#print(c2.toList())
