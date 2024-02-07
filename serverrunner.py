import server 
import queue
import threading
import json
from tarot_class import *
client_queue = []
for i in range(5):
    client_queue.append(queue.Queue())

#  create the serv thread

Tws = threading.Thread(target=server.ws, args=(client_queue,))
Tws.start()

def get_J()-> list[Joueur]:
    return client_queue[4].get()
AJoueur = get_J()
print(AJoueur)

def send_distrib():
    for j in AJoueur:
        dct = {
            'op':2,
            "data":{
                'carte': str(j)
            }
        }
        j.sendmsg(json.dumps(dct))


def actu_enchere(jou:Joueur,lvl:int):
    for j in AJoueur:
        dct = {
            "op":3,
            "data":{
                'joueur':jou.nom,
                "lvl":lvl
            }
        }
        j.sendmsg(json.dumps(dct))
actu_enchere(AJoueur[0],5)

def fin_enchere(jou:Joueur,chien:Tas):
    for j in AJoueur:
        dct = {
            'op':4,
            "data":{
                "joueur":jou.nom,
                "chien" : str(chien)
            }
        }
        j.sendmsg(json.dumps(dct))

def actu_tour(jou:Joueur,carte:Carte):
    for j in AJoueur:
        if j.nom!=jou.nom:
            dct = {
                "op":5,
                "data":{
                    "joueur":jou.nom,
                    "carte":str(carte)
                }
            }
            j.sendmsg(json.dumps(dct))

def fin_tour(gagnant:Joueur,carte:Carte):
    for j in AJoueur:
        dct = {
            "op":6,
            "data":{
                "joueur":gagnant.nom,
                "carte":str(carte)
            }
        }
        j.sendmsg(json.dumps(dct))


def fin_jeu(gagnant:Joueur,pts:int):
    for j in AJoueur:
        dct = {
            "op":7,
            "data":{
                "joueur":gagnant.nom,
                "pts":pts
            }
        }
        j.sendmsg(json.dumps(dct))

Tws.join()