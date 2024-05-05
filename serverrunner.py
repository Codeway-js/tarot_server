import server
from tarot_class import *
import json
import le_jeu

AJoueur:list[Joueur] = []

if input("terminale == ").lower()!="oui":
    def get_J()-> list[Joueur]:
        return server.client_queue[4].get(timeout=120)
    AJoueur = get_J()
else :

    j1 = Joueur(None,None,queue.Queue(),"1",True)
    j2 = Joueur(None, None,queue.Queue(),"2",True)
    j3 = Joueur(None,None,queue.Queue(),"3",True)
    j4 = Joueur(None,None,queue.Queue(),"5",True)
    AJoueur = [j1,j2,j3,j4]


lj = le_jeu.Jeu(AJoueur)

lj.Jeu()



