import pandas as pd
import matplotlib.pyplot as plt
import os

def symbol_to_path(symbol, base_dir='data'):
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def get_stock_data(symbols, dates):
    df = pd.DataFrame(index=dates)
    # Add SPY for reference, if absent
    if 'SPY' not in symbols:
        symbols.insert(0,'SPY')

    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol)
                        ,index_col="Date"
                        ,parse_dates=True
                        ,usecols=['Date','Adj Close']
                        ,na_values=['nan'])
        df_temp = df_temp.rename(columns={'Adj Close':symbol})
        df = df.join(df_temp)
        if symbol == 'SPY':
            df = df.dropna(subset=['SPY'])

    return df

def plot_data(df, title="Stock Prices", xlabel="Date", ylabel='Price'):
    ax = df.plot(title=title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.show()

def get_rolling_mean(values, window):
    return values.rolling(window=window).mean()

def get_rolling_std(values, window):
    return values.rolling(window=window).std()

def get_bollinger_bands(rm, rstd):
    upper_band = rm + 2*rstd
    lower_band = rm - 2*rstd
    return upper_band, lower_band

def compute_daily_returns(df):
    daily_returns = (df/df.shift(1))-1
    daily_returns.iloc[0,:]=0
    return daily_returns

def test_run():
    dates = pd.date_range('2012-07-01', '2012-07-31')
    # symbols = ['SPY', 'XOM', 'GOOG', 'GLD']
    # df = get_stock_data(symbols, dates)

    # print(df.mean())
    # print(df.std())

    # plot_data(df)

    symbols = ['SPY','XOM']
    df = get_stock_data(symbols, dates)
    # ax = df['SPY'].plot(title='SPY Rolling Mean', label='SPY')
    # rm_SPY = df['SPY'].rolling(window=20).mean()
    # rm_SPY.plot(label='Rolling Mean', ax=ax)
    # ax.set_xlabel("Date")
    # ax.set_ylabel("Price")
    # ax.legend(loc='upper left')
    # plt.show()

    # rm_SPY = get_rolling_mean(df['SPY'], 20)
    # rstd_SPY = get_rolling_std(df['SPY'], 20)
    # upper_band, lower_band = get_bollinger_bands(rm_SPY, rstd_SPY)
    # ax = df['SPY'].plot(title="Bollinger Bands", label='SPY')
    # rm_SPY.plot(label='Rolling Mean', ax=ax)
    # upper_band.plot(label='Upper Band', ax=ax)
    # lower_band.plot(label='Lower Band', ax=ax)
    # ax.set_xlabel('Date')
    # ax.set_ylabel('Price')
    # ax.legend(loc='upper left')
    # plt.show()

    daily_returns = compute_daily_returns(df)
    plot_data(daily_returns, title="Daily Return", ylabel="Daily Returns")

if __name__ == '__main__':
    test_run()