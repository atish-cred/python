import threading 
import time

def prepare_chai(type_, wait_time):
    print(f"{type_} chai: brewing...")
    time.sleep(wait_time)
    print(f"{type_} chai: Ready.")


# in args (arguments) passed tuples, you can pass tuple and increase the tuple as many you want
t1 = threading.Thread(target=prepare_chai, args=("masala", 2))
t2 = threading.Thread(target=prepare_chai, args=("ginger", 3))

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()

# https://httpbin.org/image/jpeg

