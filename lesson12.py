import asyncio

# Multiprocessing/threading

# import multiprocessing
# import threading
# def test(t, num):
#     print(t, ':', num)
#
#
#
#
# if __name__== '__main__':
#     processes = []
#     for i in range(5):
#         processes.append(multiprocessing.Process(target=test, args=('Process: ', i,)))
#
#     for pr in processes:
#         pr.start()
#
#
#     threads = []
#     for i in range(5):
#         threads.append(threading.Thread(target=test, args=('Thread: ', i,)))
#
#     for th in threads:
#         th.run()
#

# Generator
#
# def lazy_range(up_to):
#     index = 0
#     while index < up_to:
#         jump = yield index
#         if not jump:
#             jump = 1
#         index += jump
#
#
# if __name__ == '__main__':
#     gen = lazy_range(5)
#     print(next(gen))
#     print(gen.send(3))
#     print(gen.send(1))


async def countdown(number, n):
    while n > 0:
        print('%s minus %s' % (n, number))
        # await asyncio.sleep(1)
        await asyncio.sleep(0)
        n -= number


loop = asyncio.get_event_loop()
tasks = [
    asyncio.ensure_future(countdown(1, 15)),
    asyncio.ensure_future(countdown(2, 4))
]
loop.run_until_complete(asyncio.wait(tasks))