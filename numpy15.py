import numpy as np
a=[1,2,3,4,5,6,7]
a=np.array(a)
c=a[1:6].copy() #copy function creates a copy and changes value only in that not in main variable
c[:]=0
print(a)