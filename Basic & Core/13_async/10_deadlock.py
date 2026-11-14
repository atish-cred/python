import threading

lock_a = threading.Lock()
lock_b = threading.Lock()


# First function locking thread a and b
# Second function locking thread b and a
# From above both method it is calling dead lock. both are locking each other


def task1():
    with lock_a:
        print("Task 1 acquired lock a")
        with lock_b:
            print("Task 1 acquired lock b")


def task2():
    with lock_b:
            print("Task 2 acquired lock b")
            with lock_a:
                print("Task 2 acquired lock a")

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()

# t1.join()
# t2.join()