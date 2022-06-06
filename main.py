import pandas as pd
import time
import os
# You should not modify this part.
def config():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--consumption", default="./data/consumption.csv", help="input the consumption data path")
    parser.add_argument("--generation", default="./data/generation.csv", help="input the generation data path")
    parser.add_argument("--bidresult", default="./data/bidresult.csv", help="input the bids result path")
    parser.add_argument("--output", default="output.csv", help="output the bids path")

    return parser.parse_args()


def output(path, data):
    import pandas as pd

    df = pd.DataFrame(data, columns=["time", "action", "target_price", "target_volume"])
    df.to_csv(path, index=False)

    return

def transpose(date,plus_time):
    pre_d = time.strptime(date,'%Y-%m-%d %X')
    pre_d = time.mktime(pre_d)
    next_d = pre_d + plus_time
    next_d = time.localtime(next_d)
    next_d = time.strftime("%Y-%m-%d %X",next_d)
    return next_d

if __name__ == "__main__":
    args = config()
    
    data_dir = ''
    cons_name = 'consumption.csv'
    gene_name = 'generation.csv'
    bid_name = 'bidresult.csv'

    cons_df = pd.read_csv(args.consumption)
    gene_df = pd.read_csv(args.generation)
    bid_df = pd.read_csv(args.bidresult)
    
    data = []
    data_last_date = cons_df['time'].tolist()[-24]
    tomorrow_date = transpose(data_last_date,86400)
    for i in range(24):
        if(i>=9 and i<=16):
            data.append([tomorrow_date, "buy", 2.3, 1])
            data.append([tomorrow_date, "buy", 2.1, 0.5])
        if(i>=0 and i<=9):
            data.append([tomorrow_date, "sell", 2.666, 5])
            data.append([tomorrow_date, "sell", 2.588, 5])
        tomorrow_date = transpose(tomorrow_date,3600)
    output(args.output, data)
