# import modules
import quandl
from datetime import datetime
import matplotlib.pyplot as plt
  
# initialize parameters
start = datetime(2000, 1, 1)
end = datetime(2022, 12, 31)
  
# get the data
df = quandl.get('WIKI/ORCL', start_date = start,
                end_date = end, 
                authtoken = 'shybQ5WyDXe5cycEQUs4')
  
print(df.head())

df.to_csv("orclQuanDlData.csv")
# display
plt.figure(figsize=(20,10))
plt.title('Opening Prices from {} to {}'.format(start, end))
plt.plot(df['Open'])
plt.show()  