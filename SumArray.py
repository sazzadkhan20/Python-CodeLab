# import numpy as np
# a1 = np.array([[1,2,3],[4,5,6]])
# a2 = np.array([[7,8,9],[10,11,23]])
# print(a1+a2)


# import numpy as np
# a1 = np.array([[1,2,3],[4,5,6]])
# print(a1.cumsum())

# import numpy as np
# a1 = np.array([[1,2,3],[4,5,6]])
# print(a1.cumsum())

import numpy as np
a1 = np.array([[1,2,3,4],[5,6,7,8]])

a1[0][0] = 100
a2 = np.transpose(a1)
print(a2)
a1.shape = 2,-1
print(a1)