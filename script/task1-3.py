import pandas as pd
import numpy as np

def read_txt(path, isstopword):
    # stopwordかどうか
    if isstopword:
        df = pd.read_csv(path, sep='\n')
        df = df.rename(columns={'#http://www.textfixer.com/resources/common-english-words.txt': 'stop_word'})
    else:
        df = pd.read_csv(path, sep='\t', names=('word', 'count'))
    return df

def main():
    # 読み込み
    df = read_txt('../data_file/interim/task1-2_result.txt', False)
    df_stop = read_txt('../data_file/raw/stop_words_list(UTF-8).txt', True)
    print(df_stop)
    
if __name__ == "__main__":
    main()