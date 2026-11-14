from multiprocessing import Process
import time

def brew_chai(name):
    print(f"Start of {name} chai brewing")
    time.sleep(3) # 3 seconds
    print(f"End of {name} chai brewing")

# print(__name__)
#  __main__ method is used for entry point of your process, threads know its own but process needs this

if __name__ == "__main__":
    # Comprehension
    # chai_makers = [<Process name='Process-1' parent=20244 initial>, <Process name='Process-2' parent=20244 initial>, <Process name='Process-3' parent=20244 initial>]
    chai_makers = [
        Process(target=brew_chai, args={f"Chai maker # {i+1}", })
        for i in range(3)
    ]

    # Start all process
    for p in chai_makers:
        p.start()

    # Wait for all to complete
    for p in chai_makers:
        p.join()

    print("All chai served!")

