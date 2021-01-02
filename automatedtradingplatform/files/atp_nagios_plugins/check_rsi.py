#!/usr/bin/python

import pandas as pd
import numpy as np
import datetime

import sys

def computeRSI (data, time_window):
    diff = data.diff(1).dropna()        # diff in one field(one day)

    #this preservers dimensions off diff values
    up_chg = 0 * diff
    down_chg = 0 * diff
    
    # up change is equal to the positive difference, otherwise equal to zero
    up_chg[diff > 0] = diff[ diff>0 ]
    
    # down change is equal to negative deifference, otherwise equal to zero
    down_chg[diff < 0] = diff[ diff < 0 ]
    
    # check pandas documentation for ewm
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.ewm.html
    # values are related to exponential decay
    # we set com=time_window-1 so we get decay alpha=1/time_window
    up_chg_avg   = up_chg.ewm(com=time_window-1 , min_periods=time_window).mean()
    down_chg_avg = down_chg.ewm(com=time_window-1 , min_periods=time_window).mean()
    
    rs = abs(up_chg_avg/down_chg_avg)
    rsi = 100 - 100/(1+rs)
    return rsi

if __name__ == "__main__":

    ticker = sys.argv[1]
    rsiPeriod = sys.argv[2]
    minAlert = int(sys.argv[3])
    maxAlert = int(sys.argv[4])

    data = pd.read_csv('/atp/ticker-data/'+ticker+'.AX.txt')

    data['RSI'] = computeRSI(data['Adj Close'], int(rsiPeriod))
    
    df = data['RSI']
    
    rsiValue =  np.round(df.iloc[-1],2)
    rsiValueStr = str(rsiValue)
    
    if rsiValue > maxAlert:
        print("CRITICAL - RSI("+rsiValueStr+") is above " + str(maxAlert))
        sys.exit(2)
    elif rsiValue < minAlert:
        print("CRITICAL - RSI("+rsiValueStr+") is below " + str(minAlert))
        sys.exit(2)
    else:
        print("OK - RSI("+rsiValueStr+")")
        sys.exit(0)
