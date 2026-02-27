import os
import pandas as pd
import matplotlib.pyplot as plt

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

def plot_selected(df, columns, start_idx, end_idx):
    plot_data(df.loc[start_idx:end_idx, columns])

def plot_data(df, title="Stock Prices"):
    ax = df.plot(title=title)
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    plt.show()

def normalize_data(df):
    return df/df.iloc[0,:]

def test_run():
    start_date = '2010-01-01'
    end_date = '2010-12-31'
    dates = pd.date_range(start_date, end_date)
    symbols = ['GOOG', 'IBM', 'GLD']

    df = get_stock_data(symbols, dates)
    
    #plot_selected(df, ['SPY', 'IBM'], start_date, end_date)
    plot_data(normalize_data(df))

if __name__ == "__main__":
    test_run()