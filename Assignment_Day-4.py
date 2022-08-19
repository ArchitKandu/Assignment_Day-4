import numpy as np
arr_3D = np.array([[[0,1],[2,3]],[[4,5],[6,7]]])
for x in np.nditer(arr_3D):
    print(x)