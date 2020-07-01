# ============================================================================
# Import intraday OHLCV data using alphavantage
# =============================================================================


# importing libraries
from alpha_vantage.timeseries import TimeSeries
import pandas as pd


all_tickers = ["AAPL","MSFT","CSCO","AMZN"]
key_path = "D:\\Udemy\\Quantitative Investing Using Python\\2_Getting Data\\AlphaVantage\\key.txt"

ts = TimeSeries(key=open(key_path,'r').read(), output_format='pandas')
data = ts.get_intraday(symbol='MSFT',interval='1min', outputsize='full')[0]
data.columns = ["open","high","low","close","volume"]

# extracting stock data (historical close price) for the stocks identified
close_prices = pd.DataFrame()
cp_tickers = all_tickers
attempt = 0
drop = []
while len(cp_tickers) != 0 and attempt <=5:
    print("-----------------")
    print("attempt number ",attempt)
    print("-----------------")
    cp_tickers = [j for j in cp_tickers if j not in drop]
    for i in range(len(cp_tickers)):
        try:
            ts = TimeSeries(key=open(key_path,'r').read(), output_format='pandas')
            data = ts.get_intraday(symbol=cp_tickers[i],interval='1min', outputsize='full')[0]
            data.columns = ["open","high","low","close","volume"]
            close_prices[cp_tickers[i]] = data["close"]
            drop.append(cp_tickers[i])       
        except:
            print(cp_tickers[i]," :failed to fetch data...retrying")
            continue
    attempt+=1