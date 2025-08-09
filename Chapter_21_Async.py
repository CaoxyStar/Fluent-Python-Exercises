import time
import asyncio

async def asyncio_hello_world():
    now = time.time()
    await asyncio.sleep(1)
    print('Hello world! (%.2f seconds)' % (time.time() - now))
    await asyncio.sleep(1)
    print('Hello again! (%.2f seconds)' % (time.time() - now))

async def main():
    await asyncio.gather(
        asyncio_hello_world(),
        asyncio_hello_world(),
        asyncio_hello_world(),
    )

now = time.time()
asyncio.run(main())
print('Async Total time: %.2f seconds' % (time.time() - now))

def normal_hello_world():
    now = time.time()
    time.sleep(1)
    print('Hello world! (%.2f seconds)' % (time.time() - now))
    time.sleep(1)
    print('Hello again! (%.2f seconds)' % (time.time() - now))

now = time.time()
normal_hello_world()
normal_hello_world()
normal_hello_world()
print('Normal Total time: %.2f seconds' % (time.time() - now))