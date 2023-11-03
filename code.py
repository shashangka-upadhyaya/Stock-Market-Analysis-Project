#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install yfinance')


# In[3]:


# Import yfinance package
import yfinance as yf

# Set the start and end date
start_date = '2023-10-1'
end_date = '2023-10-13'

# Set the ticker

ticker = 'SPY'

# Get the data
data = yf.download(ticker, start_date, end_date)

# Print 5 rows
data.tail()


# In[4]:


# Import packages
import yfinance as yf
import pandas as pd

# Set the start and end date
#start_date = '1990-01-01'
# end_date = '2021-07-12'

# Set the start and end date
start_date = '2023-10-15'
end_date = '2023-11-2'

# Define the ticker list
tickers_list = ['AAPL', 'IBM', 'MSFT', 'WMT']

# Create placeholder for data
data = pd.DataFrame(columns=tickers_list)

# Fetch the data
for ticker in tickers_list:
    data[ticker] = yf.download(ticker, 
                               start_date,
                               end_date)['Adj Close']
    
# Print first 25 rows of the data
data.head(25)


# In[9]:


# Import yfinance package
import yfinance as yf

# Set the start and end date
start_date = '2023-10-15'
end_date = '2023-11-3'

# Set the ticker
ticker = 'MSFT'

# Get the data
data = yf.download(ticker, start_date, end_date)

# Print 5 rows
data.tail()


# In[11]:


#To visualize the adjusted close price data, we can use the matplotlib library and plot method as shown below.

# Import matplotlib for plotting
import matplotlib.pyplot as plt

# Plot adjusted close price data
data['Adj Close'].plot()
plt.show()


# In[ ]:




