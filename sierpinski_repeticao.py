import numpy as np
import matplotlib.pyplot as plt
 
N = int(input('Informe o número de recursões: '))
 
 
L1 = np.array([0, 0])
L2 = np.array([2, 0])
L3 = np.array([1, np.sqrt(3)])
pontoInicial = np.array([0, 0])
 
def mid_point(p1, p2):
  mid = (p1 + p2) / 2
  return mid
 
 
for i in range(N):
  rn = np.random.randint(1, 4)
  if (rn == 1):
    pontoMedio = mid_point(pontoInicial, L1)
  if (rn == 2):
    pontoMedio = mid_point(pontoInicial, L2)
  if (rn == 3):
    pontoMedio = mid_point(pontoInicial, L3)
 
  pontoInicial = pontoMedio
 
  plt.plot(pontoInicial[0], pontoInicial[1], '.')