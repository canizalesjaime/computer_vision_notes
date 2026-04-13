import numpy as np
from scipy.signal import convolve2d

# f = [1,2,3,4]
# g = [1,2]
#print(np.convolve(f,g))

i= [[0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,1,1,1,1,0,0],
    [0,0,1,1,1,1,0,0],
    [0,0,1,1,1,1,0,0],
    [0,0,1,1,1,1,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0]]

s_x= [[-1,0,1],
      [-2,0,2],
      [-1,0,1]]

s_y= [[-1,-2,-1],
      [0,0,0],
      [1,2,1]]

I_x=convolve2d(i, s_x, mode="same")
I_y=convolve2d(i, s_y, mode="same")
print(I_x)
print()
print(I_y)
print()

out = np.round(np.sqrt((I_x*I_x)+(I_y*I_y)),decimals=2)
print(out)