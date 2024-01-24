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