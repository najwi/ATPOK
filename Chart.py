import pandas_datareader as pdr
import datetime
import matplotlib


class Chart:
    @classmethod
    def create_chart(cls, cryptos, start, end):
        for i in range(len(cryptos)):
            cryptos[i] += "-USD"
        try:
            df = pdr.get_data_yahoo(cryptos, start, end)['Close']
            df.plot().get_figure().savefig('images/chart.png')
        except ValueError:
            pass
