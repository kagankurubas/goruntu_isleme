import numpy as np

dizi1 = np.array([[1, 2], [3, 4]])
dizi2 = np.array([[4, 5], [6, 7]])

yeni_dizi = np.dstack((dizi1, dizi2))

print(yeni_dizi)
