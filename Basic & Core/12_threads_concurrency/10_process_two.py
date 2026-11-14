from multiprocessing import Process
import time

def cpu_heavy():
    print(f"Crunching some numbers...")
    total = 0
    for i in range(10**7):
        total += i
    print(f"Done")


if __name__ == '__main__':
    start = time.time()

    processess = [Process(target=cpu_heavy) for _ in range(2)]

    [p.start() for p in processess]
    [p.join() for p in processess ]

    end = time.time()
    print(f"Time taken: {end-start:.2f} seconds")
