import queue
import json
import tarot_class
from websocket_server import WebsocketServer
USER = []
conter = []
nombrejoueur = 4

client_queue = []
for i in range(5):
    client_queue.append(queue.Queue())
cq = client_queue


def new_player(c,s):       
    global USER
    USER.append(c)
    
    
def msg(c,s,m):
    global conter
    index = USER.index(c)
    try:
        dct = json.loads(m)
        print(dct)
        if dct["op"] == 1:
            print('gkflgk')
            if len(conter) < nombrejoueur:
                print('yoyooy')
                conter.append(tarot_class.Joueur(c,s,cq[USER.index(c)],dct["data"]["nom"],False))
                print(conter)
                if len(conter) == nombrejoueur:
                    print("fjdindfsh")
                    cq[4].put(conter) 
        elif dct["op"] == 2:
            cq[index].put(dct["data"]["lvl"])
        elif dct["op"] == 3:
            print("yo")
            cq[index].put(dct["data"]["carte"])
        elif dct["op"] == 4:
            cq[index].put(dct["data"]["carte"])
    except:
        print('fail to transformto json')



server = WebsocketServer(port=800)
server.set_fn_new_client(new_player)
server.set_fn_message_received(msg)
server.run_forever(True)


