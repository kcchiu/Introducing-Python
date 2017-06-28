import multiprocessing
import os
import time
import random
from time import sleep

def do_this(seconds):
    from datetime import datetime
    sleep(seconds)
    print(seconds, datetime.utcnow())
    
if __name__ == "__main__":
    for n in range(3):
        seconds = random.random()
        p = multiprocessing.Process(target=do_this,
                                   args=(seconds,))
        p.start()