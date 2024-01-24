import time
import queue
import asyncio
import websockets
import threading
ALLUSER = set()

USER = []
shared = queue.Queue()
c = threading.Condition()
shared_bool = threading.Event()

def ws(queue):
    async def echo(websocket):
        global USER,ALLUSER
        if not  websocket in ALLUSER:
            USER.append(websocket)
        async for message in websocket:
            websockets.broadcast(USER,""+message)
                
            if message =="yo":
                queue.put(message)
                
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
    print("testck",queue.get(),ALLUSER,USER)
    asyncio.run(send_msg(USER[0],'yoo'))

async def send_msg(Ws,msg):
    await Ws.send(msg)

t1 = threading.Thread(target=ws,args=(shared,))
t2 = threading.Thread(target=cl,args=(shared,))
t1.start()
t2.start()
print("yo")

t1.join()
t2.join()
### OMGGGGGG CA MARCHE CKDSFKJ?LDSKFLDSKFLMKDLFKDMLKFMLSKFLKDSLMFKGKJLfk