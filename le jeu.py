import tarot_class
from random import*


j1=tarot_class.Joueur("abdoul",[],False)
j2=tarot_class.Joueur("amhed",[],False)
j3=tarot_class.Joueur("coucou",[],False)
j4=tarot_class.Joueur("cpamwa",[],False)

dct = [
    j1,
    j2,
    j3,
    j4
]
c=["ca","co","pi","tr","at"]    
def distribution():
    """CREATION DU TAS AVEC TOUTES LES CARTES"""
    
    tas=[]
    for h in range(4):
        for l in range(1,15):
            tas.append(tarot_class.Carte(l,c[h]))
    for m in range(22):
        tas.append(tarot_class.Carte(m,c[4]))
    #res=tarot_class.Tas(tas).toList()
    #print(res)

    """DISTRIBUTION DE TOUS LES JOUEURS ET LE CHIEN"""
    for i in range (6): #y'a 6 tours de cartes
        for k in range(4): #y'a 4 joueurs je change de joueur à chaque fois
            jactt=dct[k]
            for j in range (3): #html faire animation distribution de cartes
                cartenum=randint(0,len(tas)-1)
                jactt.append(tas[cartenum])
                tas.remove(tas[cartenum])
            #res2=tarot_class.Tas(jactt.carte).toList()  
    chien=tas
    return chien
    #chien=tarot_class.Tas(tas).toList()
    #print(j1.carte)
    #print(j2.carte)
    #print(j3.carte)
    #print(j4.carte)
    #print(chien)
distribution()
r=[]
for el in j1.cartes:
    r.append(str(el))
print(r,j1.cartes)
async def prisoupaspris():
    joueurquiontpris=[]
    joueurquiprends=""
    for k in range(4):
        c="j"+str(k+1)
        jact=await choix(c)
        tuprendsoupas=input("Voulez-vous prendre ?")
        if tuprendsoupas=="Oui":
            jact.pris=True
            joueurquiontpris.append(c)
            print("ok")
        elif tuprendsoupas=="Non":
            print("c ciao on s'en fou de toi")
    if len(joueurquiontpris)>1:
        print("eh bah faut faire je sais plus quoi")
    else:
        jact=joueurquiontpris[0]
     #jact.carte.append(chien) #ça je dois le mettre dans le truc global ou dans la distribution peut etre jsp
#distribution()
# prisoupaspris()