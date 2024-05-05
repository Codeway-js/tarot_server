from tarot_class import *
import json


# distribution()
def send_distrib(AJoueur):
    for j in range(len(AJoueur)):
        otherplay = ['left','top','right']
        dj= {}
        for i in range(4):
            if(i!=j):
                dj[AJoueur[i].nom] = otherplay[0]
                otherplay.pop(0)
            else:
                dj[AJoueur[j].nom] = "bottom"
        print(dj)
        dct = {
            'op':2,
            "data":{
                'carte': AJoueur[j].toList(),
                "joueur":dj
            }
        }
        AJoueur[j].sendmsg(json.dumps(dct))

# send_distrib()

def actu_enchere(AJoueur,jou:Joueur,lvl):
    for j in AJoueur:
        dct = {
            "op":3,
            "data":{
                'joueur':jou.nom,
                "lvl":lvl
            }
        }
        j.sendmsg(json.dumps(dct))
# actu_enchere(AJoueur[0],5)

def fin_enchere(AJoueur,jou:Joueur,chien):
    for j in AJoueur:
        dct = {
            'op':4,
            "data":{
                "joueur":jou.nom,
                "chien" : chien.toList()
            }
        }
        j.sendmsg(json.dumps(dct))

def actu_tour(AJoueur,jou:Joueur,carte):
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

def fin_tour(AJoueur,gagnant:bool):
    for j in AJoueur:
        dct = {
            "op":6,
            "data":{
                "prenneur":gagnant,
            }
        }
        j.sendmsg(json.dumps(dct))


def fin_jeu(AJoueur,gagnant:bool,pts):
    for j in AJoueur:
        dct = {
            "op":7,
            "data":{
                "prenneur":gagnant,
                "pts":pts
            }
        }
        j.sendmsg(json.dumps(dct))


def playertoplay(jou:Joueur,carte):
    jou.sendmsg(json.dumps({'op':8,"data":{"carte":carte}}))
    
def toplay(A):
    for j in A:
        j.sendmsg(json.dumps({"op":9}))

def cartejouablechien(jou:Joueur,l:list):
    jou.sendmsg(json.dumps({"op":11,"data":{"carte":l}}))