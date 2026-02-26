import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg') 

def get_max_close(symbol):
    df = pd.read_csv("data/{}.csv".format(symbol))
    return df['Close'].max()

def get_mean_volume(symbol):
    df = pd.read_csv("data/{}.csv".format(symbol))
    return df['Volume'].mean()

def test_run():
    #df = pd.read_csv("data/AAPL.csv")
    #print(df[10:21])

    # for symbol in ['AAPL', 'IBM']:
    #     print("Max close")
    #     print(symbol, get_max_close(symbol))

    # for symbol in ['AAPL', 'IBM']:
    #     print("Mean Volume")
    #     print(symbol, get_mean_volume(symbol))

    # df = pd.read_csv("data/AAPL.csv")
    # print(df['Adj Close'])
    # df["Adj Close"].plot()
    # plt.show()

    # df = pd.read_csv("data/IBM.csv")
    # print(df['High'])
    # df["High"].plot()
    # plt.show()

    df = pd.read_csv("data/AAPL.csv")
    print(df[['Close','Adj Close']])
    df[['Close','Adj Close']].plot()
    plt.show()

if __name__ == "__main__":
    test_run()