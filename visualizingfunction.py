'''
panda & iPython workshop
https://www.youtube.com/watch?v=F6kmIpWWEdU

installing pandas etc and basics of pandas using pip
https://www.youtube.com/watch?v=Iqjy9UqKKuo&list=PLQVvvaa0QuDc-3szzjeP6N6b0aDrrKyL-



to do:
visualiseer:
- gemiddelde
- mediaan
- best case
- Na hoeveel runs verbetert hij niet meer?

Optioneel:
- Greedy visualiseren (losse grafiek) (ALS we hem al gaan gebruiken)

Pittig maar nodig:
- 8 Combinaties visualiseren:
* 2 beginsituaties (random, greedy (greedy kan op nóg meer manieren. Greedy nu: cargo is density gesorteerd, je begint bij pakketje met hoogste density 
	en stopt hem in de hoogste density qua capaciteit) )

Vraag voor morgen:
- Wat plotten we gemiddelde/mediaan/best case van elke combinatie??

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