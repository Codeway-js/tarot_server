import asyncio
import time 
async def simple_print(msg):
    time.sleep(3)
    print(msg)
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(simple_print('Hello'))

for _ in range(10):
    print("yo")

def cdir(m):
    nb1=0
    streak1=True
    for el in m:
        if el == 1:
            if streak1==False:
                return -1
            nb1+=1
        else:
            streak1=False
    return nb1 