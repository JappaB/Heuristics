'''
panda & iPython workshop
https://www.youtube.com/watch?v=F6kmIpWWEdU

installing pandas etc and basics of pandas using pip
https://www.youtube.com/watch?v=Iqjy9UqKKuo&list=PLQVvvaa0QuDc-3szzjeP6N6b0aDrrKyL-
'''

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

columns = ["datetime", "miliseconds", "name", "iterations", "swaps","kgs","m3","cargoonground"]
df = pd.read_csv("HillClimberData.csv", names = columns)

print df.head(10)
print df.tail(10)
print df

df['m3'].plot()
plt.show()