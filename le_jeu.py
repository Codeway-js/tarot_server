import tarot_class
from random import*


j1 = tarot_class.Joueur("abdoul", [], False)
j2 = tarot_class.Joueur("amhed", [], False)
j3 = tarot_class.Joueur("coucou", [], False)
j4 = tarot_class.Joueur("cpamwa", [], False)

dct = [
    j1,
    j2,
    j3,
    j4
]
c = ["ca", "co", "pi", "tr", "at"]


def distribution():
    """CREATION DU TAS AVEC TOUTES LES CARTES"""

    tas = []
    for coul in range(4):
        for num in range(1, 15):
            tas.append(tarot_class.Carte(num, c[coul]))
    for atnum in range(22):
        tas.append(tarot_class.Carte(atnum, c[4]))
    # res=tarot_class.Tas(tas).toList()
    # print(res)

    """DISTRIBUTION DE TOUS LES JOUEURS ET LE CHIEN"""
    for tour in range(6):  # y'a 6 tours de cartes
        for joueur in range(4):  # y'a 4 joueurs je change de joueur à chaque fois
            jactt = dct[joueur]
            for j in range(3):  # html faire animation distribution de cartes
                cartenum = randint(0, len(tas)-1)
                jactt.append(tas[cartenum])
                tas.remove(tas[cartenum])
            # res2=tarot_class.Tas(jactt.carte).toList()
    chien = tas
    return chien
    
    # chien=tarot_class.Tas(tas).toList()
    # print(j1.cartes)
    # print(j2.carte)

    # print(chien)


def enchère():
    joueurquiontpris = []
    niveau = 0
    for k in range(4):
        jact = dct[k]
        tuprendsoupas = input("Voulez-vous prendre ? ")
        if tuprendsoupas == "Oui":
            joueurquiontpris.append(jact)
    while len(joueurquiontpris) > 1:
        v2 = [i for i in joueurquiontpris]
        niveau += 1
        for i in range(len(joueurquiontpris)):
            jact = v2[i]
            tuprendsoupas = input(
                "Voulez-vous prendre mais avec "+str(5*niveau)+" points de plus à réaliser ? ")
            if tuprendsoupas == "Non":
                joueurquiontpris.remove(jact)
    if len(joueurquiontpris) == 0:
        preneur = randint(0, len(v2)-1)
        jact = v2[preneur]
        jact.pris = True
    else:
        jact = joueurquiontpris[0]
        jact.pris = True

     # jact.carte.append(chien) #ça je dois le mettre dans le truc global ou dans la distribution peut etre jsp
distribution()
print(j3.toList())
print(j4.toList())
# enchère()

def cartejouable(carte, cartebase):
    if carte == "Aat":
        return 0
    if cartebase[1] != "at":
        if carte[1:] == cartebase[1]:
            return 4
        elif carte[1:] == "at":
            if ord(carte[0])-65 > cartebase[0]:
                return 3
            return 2
        return 1
    else:
        if carte[1:] == "at":
            if ord(carte[0])-65 > cartebase[0]:
                return 3
            return 2
        return 1

def cartejouablepremiertour(carte,cartesjeu):
    for cartejeu in cartesjeu :
        if str(cartejeu) == carte:
            return True
    return False

def tour(starter):
    onjoue=True

    for j in range (3): #détermine le numéro du joueur qui commence
        if starter==dct[j]:
            numstart=j

    while onjoue : #joueur 1 puis s'il peut jouer ça continue
        j1carte=input("Quel carte voulez-vous déposer ? ")
        tas=[0,j1carte[1:]]
        verif=cartejouablepremiertour(j1carte,starter.cartes)

        if verif==True:
            if j1carte[1:]=="at":
                tas[0]=ord(j1carte[0])-65
                print(tas[0])

            for i in range (1,4): #test de la puissance
                jact=dct[(i+numstart)%4]
                puiss=[cartejouable(str(jact.cartes[i]),tas) for i in range (len(jact.cartes))]
                maximum=puiss[0]

                for j in puiss: #test des cartes jouables
                    if j>maximum:
                        maximum=j
                jouable=[str(jact.cartes[i]) for i in range (len(jact.cartes)) if puiss[i]==maximum or puiss[i]==0]
                print(jouable)

                peutjouer=True
                while peutjouer : #action concrète des autres joueurs
                    print(jact.toList())
                    jcarte=input("Quel carte voulez-vous déposer ? ")
                    if jcarte in jouable :
                        cj=tarot_class.convertstrcarte(jcarte)
                        tas.append(cj)
                        jact.removeCartestr(jcarte)
                        print(jact.toList())
                        if cj.numero>tas[0]:
                            tas[0]=cj.numero
                        print(tas)
                        peutjouer=False
                    else:
                        print("Cette carte n'est pas jouable, veuillez en sélectionner une jouable.")
            onjoue=False
        else:
            print("Cette carte n'est pas jouable, veuillez en sélectionner une jouable.")
        # Faut faire le gagnant : jpeux me servir de la puissance (je pense car ça peut me faire gagner du temps, dans le sens, je prends la première carte, 
        # dans tous ce qui peut être mieux = de toutes les cartes, si dans les cartes suivantes y'a ça qu'est joué alors c bon) 
        # OU dans le sens ou je regarde une par une les cartes pour savoir si c de l'atout ou de la couleur. 
        # Si ce de l'atout le winner sera celui avec le plus grand. Si c'est de la couleur et que y'a pas d'atout dedans, alors il faut que le gagnant soit le plus haut 
        # chiffre de la couleur correspondant à la première couleur jouée.

tour(j3)

    

