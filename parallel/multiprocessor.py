import os
import multiprocessing
import time

from math import sqrt

from joblib import Parallel, delayed

print(os.cpu_count())
print(multiprocessing.cpu_count())

def my_fun(i):
    time.sleep(1)
    print('done')
    return sqrt(i**2)

n = 10

Parallel(n_jobs=-1)(delayed(my_fun)(i) for i in range(n))