

import time

t1 = time.time()

list_ = [i**2 for i in range(10000000)] # 10 million for list

print('List take ',time.time() - t1,' seconds') # list take 400mb in this time

t2 = time.time()

Generator  = (i**2 for i in range(10000000))  # 10 million for generator

print('Generator take ',time.time() - t2,' seconds') # Generator take almost none
