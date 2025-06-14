### simple matrix operations
import numpy as np

def h():
    return np.array([[0.3, 0.6 ], [0.1, 2],[0.9, 3.7],[0,1]])

def w():
    return np.array([[0.3], [0.9]])

def w2():
    return np.array([0.75,0.15,0.22,0.33])

def chapter_zero():    
    h_val = h()
    w_val = w()
    w2_val = w2()
    result = np.matmul(h_val, w_val)
    result2 = np.matmul(w2_val,result)
    return(result2)

print(chapter_zero())