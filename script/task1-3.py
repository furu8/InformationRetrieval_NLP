import pandas as pd
import numpy as np

def read_txt(path):
    df = pd.read_csv(path, sep='\t', names=('word', 'count'))
    return df

def main():
    # 読み込み
    df = read_txt('../data_file/interim/task1-2_result.txt')
    print(df)
    
if __name__ == "__main__":
    main()