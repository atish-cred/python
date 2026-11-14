from multiprocessing import Process, Queue, Value
import time

def prepare_chai(queue):
    queue.put("Masala chai is ready.")

# value will be key value pair
# It will get lock automatically
counter = Value('1', 0)


if __name__ == '__main__':
    queue = Queue()

    p = Process(target=prepare_chai, args=(queue,))

    p.start()
    p.join()

    print(queue.get())