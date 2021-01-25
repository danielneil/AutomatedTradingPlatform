# Shark - An Automated Trading Platform

Shark is an open source automated trading platform derived from tools that monitor IT infrastructure.

It enables the use of programmable strategies to identify and execute upon trading opportunities.

The example strategy is simple moving averages crossover with the chosen financial market being the Australian Stock Exchange (Top 20). 

Though it focuses on the ASX, it could easily be adjusted to suit any financial market, along with an adapted strategy, too.  

See the [plugins](https://github.com/danielneil/AutomatedTradingPlatform/blob/main/doc/README.PLUGINS.md) for a list of capabilities.

See the example [strategy](https://github.com/danielneil/AutomatedTradingPlatform/blob/main/automatedtradingplatform/files/strategies/moving_averages.py).

# Setup Instructions

1. Install ansible on your local machine.

2. Prepare a vanilla Debian server.

3. Add its IP address to the ./hosts files under [atp-server]

4. Change the http credentials in ./site.yml to your liking.

5. Run: ./build.sh

6. Navigate to https://atp-server/nagios using the aforementioned credentials.

# Screen Shot

![alt text](https://github.com/danielneil/AutomatedTradingPlatform/blob/main/screenshots/screenshot.JPG?raw=true)

# Warning

1. Don't install this on an internet-facing server.

2. [Read the disclaimer](https://github.com/danielneil/AutomatedTradingPlatform/blob/main/DISCLAIMER).

