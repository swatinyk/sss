import  os
from datetime import *
stats= os.stat("abcddd.txt")
print('size',stats.st_size)
print(datetime.fromtimestamp(stats.st_ctime))

