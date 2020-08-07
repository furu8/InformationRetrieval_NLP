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

    # カウント数計算
    df_count = calc_word_count(df)
    
    # カウント数出力
    [print('{:<15}\t {}'.format(cnt[0], cnt[1])) for cnt in df_count.values] # brokenheartedlyが15文字で最大

if __name__ == "__main__":
    main()