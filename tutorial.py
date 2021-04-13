import numpy as np
import matplotlib
import matplotlib.pyplot as pl
import pandas as pa

data = {'x': [1,2,3], 'y': [2,4,6]}
t = pa.DataFrame(data)

m = t['y'].mean()

print(m)
