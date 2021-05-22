import pandas_datareader as pdr
import matplotlib as mpl
from Colors import *


class Chart:
    @classmethod
    def create_chart(cls, cryptos, start, end, columns=['Close'], log_scale=False):
        for i in range(len(cryptos)):
            cryptos[i] += "-USD"
        try:
            df = pdr.get_data_yahoo(cryptos, start, end)[columns]
            mpl.rcParams['grid.color'] = COLOR_ORANGE
            mpl.rcParams['axes.facecolor'] = COLOR_VERY_LIGHT_GREY
            mpl.rcParams['axes.edgecolor'] = COLOR_ORANGE
            mpl.rcParams['text.color'] = COLOR_WHITE
            mpl.rcParams['figure.facecolor'] = COLOR_VERY_LIGHT_GREY
            mpl.rcParams['figure.figsize'] = (10, 6)
            mpl.rcParams['axes.labelcolor'] = COLOR_WHITE
            mpl.rcParams['xtick.color'] = COLOR_WHITE
            mpl.rcParams['ytick.color'] = COLOR_WHITE
            mpl.rcParams['legend.framealpha'] = 0.6
            mpl.rcParams['legend.edgecolor'] = COLOR_ORANGE
            mpl.rcParams['lines.linewidth'] = 2
            fig = df.plot(grid=True, legend=True, logy=log_scale, ylabel="USD").get_figure()
            fig.savefig('images/chart.png')
        except ValueError:
            pass
