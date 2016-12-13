import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

web_stats = {'Day':[1,2,3,4,5,6],
             'Visitors':[43,34,65,56,29,76],
             'Bounce Rate':[65,67,78,65,45,52]}

df=pd.DataFrame(web_stats)
##print(df.Visitors)
##df['Visitors'].plot()
df['Day'].plot()
##df.plot()
plt.show()
##df.set_index('Visitors', inplace=True)
##print(df[['Day','Visitors','Bounce Rate']])
##not able use index when print used like this
##print(df)
