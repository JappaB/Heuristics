'''
panda & iPython workshop
https://www.youtube.com/watch?v=F6kmIpWWEdU

installing pandas etc and basics of pandas using pip
https://www.youtube.com/watch?v=Iqjy9UqKKuo&list=PLQVvvaa0QuDc-3szzjeP6N6b0aDrrKyL-



to do totale project:
visualiseer:
- gemiddelde
- mediaan
- best case
- Na hoeveel runs verbetert hij niet meer?
- Welke cargolist
- Wat we optimaliseren

Optioneel:
- Greedy visualiseren (losse grafiek) (ALS we hem al gaan gebruiken)

Pittig maar nodig:
- 8 Combinaties visualiseren:
* 2 beginsituaties (random, greedy (greedy kan op nóg meer manieren. Greedy nu: cargo is density gesorteerd, je begint bij pakketje met hoogste density 
	en stopt hem in de hoogste density qua capaciteit) )
* HC op twee manieren of SA op twee manieren

Vraag voor morgen:
- Wat plotten we gemiddelde/mediaan/best case van elke combinatie??


headers: Gebruik header blocks (bijv eerste 10 is informatie)=> geef door an pandas en dan snapt 'ie dat.

heuristiek d en e: 

'''

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

columns = ["datetime", "miliseconds", "name", "iterations", "swaps","kgs","m3","cargoonground"]
df = pd.read_csv("HillClimberData.csv", names = columns, header="infer")

print df.head(10)
print df.tail(10)
print df

df['m3'].plot()
plt.show()