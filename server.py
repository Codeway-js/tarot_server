import time
import queue
import asyncio
import websockets
import threading
import _thread
import json
import tarot_class
USER = []
# shared = [queue.Queue() for _ in range(5)]
c = threading.Condition()
shared_bool = threading.Event()

conter = []
nombrejoueur = 1
def ws(queue):
    
    async def echo(websocket):
        global USER,conter
        if not websocket in USER:
            USER.append(websocket)
        async for message in websocket:
            index = USER.index(websocket)
            print(message,index)
            if message =="yo":
                queue[index].put(message)
            try:
                dct = json.loads(message)
                print(dct)
                if dct["op"] == 1:
                    print('gkflgk')
                    if len(conter) < nombrejoueur:
                        print('yoyooy')
                        conter.append(tarot_class.Joueur(websocket,queue[USER.index(websocket)],dct["data"]["nom"]))
                        print(conter)
                        if len(conter) == nombrejoueur:
                            queue[4].put(conter) 
                elif dct["op"] == 2:
                    queue[index].put(dct["data"]["niveau"])
                elif dct["op"] == 3:
                    queue[index].put(dct["data"]["chien"])
            except:
                print('fail to transformto json')

            
                
    async def main():
        async with websockets.serve(echo, "localhost", 800):
            while True:
                await asyncio.Future()
         
    asyncio.run(main())


def cl(queue):
    
    global val
    
    print("Main thread waiting 10s")
    time.sleep(10)
    print("finish waiting")
    print("testck",queue[0].get(),USER)
    asyncio.run(send_msg(USER[0],'yoo'))

async def send_msg(Ws,msg):
    await Ws.send(msg)

# t1 = threading.Thread(target=ws,args=(shared,))
# # t2 = threading.Thread(target=cl,args=(shared,))
# t1.start()
# # t2.start()
# print("yo")

# t1.join()
# # t2.join()
### OMGGGGGG CA MARCHE CKDSFKJ?LDSKFLDSKFLMKDLFKDMLKFMLSKFLKDSLMFKGKJLfk