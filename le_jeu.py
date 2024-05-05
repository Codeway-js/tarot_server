import tarot_class as tc
from random import *
import time

import message as ms

# j1 = tc.Joueur("1")
# j2 = tc.Joueur("2")
# j3 = tc.Joueur("3")
# j4 = tc.Joueur("5")

c = ["ca", "co", "pi", "tr", "at"]

class Jeu :
    def __init__(self,dct:list[tc.Joueur]) -> None:
        self.dct=dct

    def distribution(self):
        """CREATION DU TAS AVEC TOUTES LES CARTES"""

        tas = []
        for coul in range(4):
            for num in range(1, 15):
                tas.append(tc.Carte(num, c[coul]))
        for atnum in range(22):
            tas.append(tc.Carte(atnum, c[4]))


        """DISTRIBUTION DE TOUS LES JOUEURS ET LE CHIEN"""
        for tour in range(6):  # y'a 6 tours de cartes
            for joueur in range(4):  # y'a 4 joueurs je change de joueur à chaque fois
                jactt = self.dct[joueur]
                for j in range(3): 
                    cartenum = randint(0, len(tas)-1)
                    jactt.append(tas[cartenum])
                    tas.remove(tas[cartenum])
        chien = tas
        return chien
        

    def enchère(self):
        joueurquiontpris = []
        niveau = 0
        scoreafaire = 56
        v2=[]
        for k in range(4):
            jact = self.dct[k]
            print(str(jact))
            # tuprendsoupas = input(jact.nom+" Voulez-vous prendre ? ")
            # if tuprendsoupas=="non":
            #     res =-1
            # else:
            #     res=0
                
            res =jact.waitmsg(2)
            
            if res!=-1:
                joueurquiontpris.append(jact)
                ms.actu_enchere(self.dct,jact,res)
        while len(joueurquiontpris) > 1:
            v2 = [i for i in joueurquiontpris]
            niveau += 1
            for i in range(len(joueurquiontpris)):
                jact = v2[i]
                # tuprendsoupas = input(jact.nom+" Voulez-vous prendre ? ")
                # if tuprendsoupas=="non":
                #     res =-1
                # else:
                #     res=0
                    
                res =jact.waitmsg(2)
                
                if res==-1:
                    joueurquiontpris.remove(jact)
        
        if len(joueurquiontpris) == 0:
            preneur = randint(0, len(v2)-1)
            jact = v2[preneur]
            jact.pris = True
            scoreafaire+=5*(niveau-1)
        
        else:
            scoreafaire+=5*niveau
            jact = joueurquiontpris[0]
            jact.pris = True
        return [scoreafaire, jact]

    def objectifp(self,prenneur,ancscore):
            nbbouts=0
            for carte in prenneur.cartes:
                if str(carte)=="Aat" or str(carte)=="Vat" or str(carte)=="Bat":
                    nbbouts+=1
            if nbbouts==1:
                ancscore-=5
            elif nbbouts==2:
                ancscore-=15
            elif  nbbouts==3:
                ancscore-=20
            return ancscore


    def get_val(self,carte):
        return ord(carte[0])-65
    # carte base = [class, valeur]
    def cartejouable(self,carte:tc.Carte, maxvalatout, coul):
        if str(carte) == "Aat":
            return 0
        if coul != "at":
            if carte.types == coul:
                return 4
            elif carte.types == "at":
                if carte.numero > maxvalatout:
                    return 3
                return 2
            return 1
        else:
            if carte.types == "at":
                if carte.numero > maxvalatout:
                    return 3
                return 2
            return 1

    def cartejouablepremiertour(self,carte,cartesjeu):
        for cartejeu in cartesjeu :
            if cartejeu == carte and str(cartejeu)!="Aat":
                return True
        return False


    def cartepuiss(self,jeu:tc.Tas,puiss)->tc.Tas:
        t=tc.Tas([])
        maximum = puiss[0]
        for j in puiss: #test des cartes jouables
            if j>maximum:
                maximum=j
        print(maximum)
        for i in range(len(jeu.cartes)):
            if puiss[i]==maximum or puiss[i]==0:
                t.append(jeu.cartes[i])
        return t

    def tour(self,starter:tc.Joueur):
        onjoue=True
        premcarte=tc.convertstrcarte("Aat")
        cj=tc.convertstrcarte("Aat")
        tas=[]
        maxvalatout = 0
        jcarte =""
        couleur_jouée = ""
        numstart=0
        for j in range (4): #détermine le numéro du joueur qui commence
            if starter==self.dct[j]:
                numstart=j
        
        # tas est une liste qui contient en première position le numéro du plus fort atout et en 2 eme element la carte jouer
        # on les a mit ensemble car il sont appeler pratiquement au mm moment
        # aussi tas va retenir routes les carte posez dans le jeu
        ms.playertoplay(starter,starter.toList())
        while onjoue : #joueur 1 puis s'il peut jouer ça continue
            print(starter)
            
            # j1carte=trycarte(starter.nom+" Quel carte voulez-vous déposer ? ")
            # j1carte = str(starter.cartes[0])
            # premcarte=tc.convertstrcarte(j1carte)
            
            c = starter.waitmsg(4)
            print(c)
            premcarte = tc.convertstrcarte(c)
            couleur_jouée = premcarte.types
            tas.append(premcarte)
            if self.cartejouablepremiertour(premcarte,starter.cartes):
                starter.remove(premcarte)
                onjoue=False
            else:
                print("Cette carte n'est pas jouable, veuillez en sélectionner une jouable.")

        if premcarte.types=="at":
            maxvalatout=premcarte.numero
        win = [premcarte.numero,couleur_jouée]
        winnerpov=starter
        ms.actu_tour(self.dct,starter,premcarte)
        for i in range (1,4): 
            jact=self.dct[(i+numstart)%4]
            puiss=[self.cartejouable(carte,maxvalatout,couleur_jouée) for carte in jact.cartes]
            jouable=self.cartepuiss(jact,puiss)
            # jouable ici une list[str] pour faciliter les transfert avec le serv pour une future update.
            peutjouer=True
            ms.playertoplay(jact,jouable.toList())
            while peutjouer : #action concrète des autres joueurs
                print(jouable)
                
                # jcarte=trycarte(jact.nom+" Quel carte voulez-vous déposer ? ")
                # jcarte = str(jouable.cartes[0])
                jcarte = jact.waitmsg(4)
                print(jcarte)
                cj=tc.convertstrcarte(jcarte)
                # if jcarte in str(jouable) :
                    #détermine si la carte posé par dessus est supérieur aux autre. Ainsi on détermine le gagnant par celui qui à poser en dernier la plus forte carte
                win2=self.gagnantuntour(win,cj)
                if win2!=win:
                    winnerpov=jact
                win=win2
                peutjouer=False
                # else:
                #     print("Cette carte n'est pas jouable, veuillez en sélectionner une jouable.")
            tas.append(cj)
            jact.removeCartestr(jcarte)
            ms.actu_tour(self.dct,jact,cj)
            if cj.numero>maxvalatout and cj.types=="at":
                maxvalatout=cj.numero
        score=self.points(tas)
        return [score, winnerpov]
            
    def gagnantuntour(self,carteav,cartenew): 
        valancienne=self.cartejouable(tc.Carte(carteav[0],carteav[1]),0,"at") 
        valnew=self.cartejouable(cartenew,0,"at")
        if valancienne>valnew:
            return carteav
        elif valnew>valancienne:
            return [cartenew.numero,cartenew.types] 
        elif cartenew.numero>carteav[0]:
            return [cartenew.numero,cartenew.types] 
        else:
            return carteav

    def points(self,ttecartes : list[tc.Carte]):
        score=0
        for carte in ttecartes:
            if carte.types!="at":
                if carte.numero==11:
                    score+=1.5
                elif carte.numero==12:
                    score+=2.5
                elif carte.numero==13:
                    score+=3.5
                elif carte.numero==14:
                    score+=4.5
                else:
                    score+=0.5
            else:
                if carte.numero==0 or carte.numero==1 or carte.numero==21:
                    score+=4.5
                else:
                    score+=0.5
        return score


    def lepotichien(self,chien,joueur:tc.Joueur):
        carteenlever=[]
        cartejouable=[]
        carteaenlever = tc.convertstrcarte("Aat")
        for j in chien:
            joueur.append(j)
        for carte in joueur.cartes:
            if carte.types!="at" and carte.numero!=14:
                cartejouable.append(str(carte))
        ms.cartejouablechien(joueur,cartejouable)
        # pour switch entre test et web
        res:list = joueur.waitmsg(3) # type: ignore
        carteenlever = list(map(lambda x: tc.convertstrcarte(x),res))
        for el in carteenlever:
            joueur.remove(el)
        
        return carteenlever

    def Jeu (self):
        scoresolo=0
        chien=self.distribution()
        ms.send_distrib(self.dct)
        solo=self.enchère()
        objectif=int(solo[0])
        firstkiller=solo[1]
        prenneur=solo[1]
        ms.fin_enchere(self.dct,prenneur,tc.Tas(chien))
        tasdetruc=self.lepotichien(chien,prenneur)
        scoresolo+=self.points(tasdetruc)
        for i in range(4):
            print(len(self.dct[i].cartes))
            
        ms.toplay(self.dct)
        for _ in range (18):
            res=self.tour(prenneur) #res c'est une liste qui reçoit le score et le joueur qui a gagné
            if res[1]==solo[1]:
                ms.fin_tour(self.dct,True)
                scoresolo+=res[0]
            else:
                ms.fin_tour(self.dct,False)
            prenneur=res[1]
        objectif=self.objectifp(firstkiller,objectif)

        if scoresolo>=objectif:
            ms.fin_jeu(self.dct,True,round(scoresolo))
            print("Le gagnant est le prenneur ! Avec",scoresolo,"sur",objectif,"points.")
        else:
            ms.fin_jeu(self.dct,False,round(scoresolo))
            print("Le prenneur a perdu ! Il a fait",scoresolo,"points sur",objectif,"points. Félicitation aux autres !")

# jc = Jeu()
# jc.Jeu()