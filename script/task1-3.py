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

def remove_stop_word(df, df_stop):
    # 前処理
    word_list = [word.replace(' ', '') for word in df['word'].values.flatten()]
    stop_word_list = df_stop['stop_word'].values.flatten()
    
    # ストップワードの単語を除去
    new_word_list = [word for word in word_list if word not in stop_word_list]
    
    return new_word_list

def main():
    # 読み込み
    df = read_txt('../data_file/interim/task1-2_result.txt', False)
    df_stop = read_txt('../data_file/raw/stop_words_list(UTF-8).txt', True)
    
    # 除去
    new_word_list = remove_stop_word(df, df_stop)

    # 出力

    
if __name__ == "__main__":
    main()