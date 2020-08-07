import pandas as pd
import numpy as np

def read_txt(path):
    df = pd.read_csv(path, sep='\n', names=('word',))
    return df

def calc_word_count(df):
    # カウント
    df_count = df['word'].value_counts() 
    df_count = df_count.reset_index(drop=False)
    df_count = df_count.rename(columns={'index': 'word', 'word':'count'}) # カラム名変更

    return df_count

def main():
    # 読み込み
    df = read_txt('../data_file/interim/task1-1_result.txt')

    # カウント数出力
    
    print(df_count)
    

    # for c in df_count.values:
    #     print(c)

if __name__ == "__main__":
    main()