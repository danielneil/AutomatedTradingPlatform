# Plugins Documentation

This is the plugins documentation.
The plugins are mostly python scripts that enable the platform to monitor and alert on just about anything of interest.

# Contents
* [check_rsi](#check_rsi)
* [check_strategy](#check_strategy)
* [check_price](#check_price)
* [check_website](#check_website)
* [check_sma](#check_sma)
* [check_vix](#check_vix)
* [check_trend](#check_trend)
* [check_short_interest](#check_short_interest)
## <a name="check_rsi"/>check_rsi

**Usage:** check_rsi.py [-h] [-t TICKER] [-p PERIODS] [-max MAX] [-min MIN]
                    [-r [RAW]]

This plugin computes the relative strength index (RSI) for a stock.

**Optional Arguments**:
  -h, --help            show this help message and exit
  -t TICKER, --ticker TICKER
                        ticker code of the stock
  -p PERIODS, --periods PERIODS
                        Number of trading periods for which to compute
                        against.
  -max MAX, --max MAX   Warn if the RSI is greater than this threshold.
  -min MIN, --min MIN   Warn if the RSI is less than this threshold.
  -r [RAW], --raw [RAW]
                        Just print the price minus pretty output.
## <a name="check_template"/>check_template

**Usage:** check_template.py [-h] [-t TICKER]

This is a template for a python check for the trading platform, make it as
descriptive as possible as it will be used to generate documentation

**Optional Arguments**:
  -h, --help            show this help message and exit
  -t TICKER, --ticker TICKER
                        ticker code of the stock
## <a name="check_strategy"/>check_strategy

**Usage:** check_strategy.py [-h] [-t TICKER] [-s STRATEGY]

This runs the platform strategy. For a simple strategy, see the template
strategy for an example

**Optional Arguments**:
  -h, --help            show this help message and exit
  -t TICKER, --ticker TICKER
                        Ticker code of the stock in question
  -s STRATEGY, --strategy STRATEGY
                        The file name of the custom strategy
## <a name="check_price"/>check_price

**Usage:** check_price.py [-h] [-t TICKER] [-r [RAW]]

Get the latest price of a stock.

**Optional Arguments**:
  -h, --help            show this help message and exit
  -t TICKER, --ticker TICKER
                        Ticker code of the stock
  -r [RAW], --raw [RAW]
                        Just print the price minus pretty output and return
                        OK(0)
## <a name="check_website"/>check_website

**Usage:** check_website.py [-h] [-t TICKER] [-u URL]

This plugin monitors a website for changes. E.g. the Investor Information
section of a publicly listed company, or a page displaying news for a specific
derivative.

**Optional Arguments**:
  -h, --help            show this help message and exit
  -t TICKER, --ticker TICKER
                        ticker code of the stock
  -u URL, --url URL     URL of the website of interest
## <a name="check_sma"/>check_sma

**Usage:** check_sma.py [-h] [-t TICKER] [-p PERIODS] [-r [RAW]] [-max MAX]
                    [-min MIN]

Computes a simple moving average of a ticker against a specific number of
trading periods.

**Optional Arguments**:
  -h, --help            show this help message and exit
  -t TICKER, --ticker TICKER
                        Ticker code of the stock.
  -p PERIODS, --periods PERIODS
                        Number of trading periods for which to compute
                        against.
  -r [RAW], --raw [RAW]
                        Just print the price minus pretty output.
  -max MAX, --max MAX   Warn if the result is greater than this threshold.
  -min MIN, --min MIN   Warn if the result is less than this threshold.
## <a name="check_vix"/>check_vix

**Usage:** check_vix.py [-h]

Get the VIX (Volatility Index).

**Optional Arguments**:
  -h, --help  show this help message and exit
## <a name="check_trend"/>check_trend

**Usage:** check_trend.py [-h] [-t TICKER] [-1st FIRSTMA] [-2nd SECONDMA]
                      [-3rd THIRDMA]

This analyses the trend of a stock based upon multiple moving averages. It
takes three numbers/moving averages and determines if the stock is in an
uptrend, and also returns a range calculation to determine the 'distance'
between the moving averages

**Optional Arguments**:
  -h, --help            show this help message and exit
  -t TICKER, --ticker TICKER
                        Ticker code of the stock
  -1st FIRSTMA, --firstMA FIRSTMA
                        First moving average (the shorter, e.g. 10 days)
  -2nd SECONDMA, --secondMA SECONDMA
                        Second moving average (the longer, e.g. 50 days)
  -3rd THIRDMA, --thirdMA THIRDMA
                        Third moving average (the longest. e.g. 100 days)
## <a name="check_short_interest"/>check_short_interest

**Usage:** check_short_interest.py [-h] [-t TICKER]

Alarms on the short interest of a specific ASX ticker.

**Optional Arguments**:
  -h, --help            show this help message and exit
  -t TICKER, --ticker TICKER
                        Ticker code of the stock


This is automatically generated, do not edit this file, instead amend the help text in the plugin's source code.