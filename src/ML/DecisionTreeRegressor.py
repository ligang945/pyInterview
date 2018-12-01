from itertools import product
from numpy import *
import numpy as np
import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.tree import DecisionTreeRegressor

x = np.linspace(1,10,10)
X = mat(x).T

y = [5.56,5.70,5.91,6.40,6.80,7.05,8.90,8.70,9.00,9.05]
Y = mat(y).T

# 训练模型，限制树的最大深度4
clf = DecisionTreeRegressor(max_depth=5)
#拟合模型
clf.fit(X, Y)

p = np.linspace(1,10,1000)
q=[]
for m in p:
    q.append(clf.predict(m))

plt.plot(x, y, 'or')
plt.plot(p, q)

plt.show()