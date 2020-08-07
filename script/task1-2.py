import pandas as pd
import numpy as np

def read_txt(path):
    df = pd.read_csv(path, sep='\n', names=('word',))
    return df

def main():
    # 読み込み
    df = read_txt('../data_file/interim/task1-1_result.txt')

    print(df)

if __name__ == "__main__":
    main()