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

def remove_stop_word(word_list, stop_word_list):
    # ストップワードの単語を除去
    new_word_list = [word for word in word_list if word not in stop_word_list]
    
    return new_word_list

def main():
    # 読み込み
    df = read_txt('../data_file/interim/task1-2_result.txt', False)
    df_stop = read_txt('../data_file/raw/stop_words_list(UTF-8).txt', True)
    
    # 前処理
    word_list = [word.replace(' ', '') for word in df['word'].values.flatten()]
    df['word'] = word_list
    stop_word_list = df_stop['stop_word'].values.flatten()

    # 除去
    new_word_list = remove_stop_word(word_list, stop_word_list)

    # 出力
    for word in df.values:
        [print('{:<15}\t {}'.format(word[0], word[1])) for new_word in new_word_list if word[0] == new_word] # brokenheartedlyが15文字で最大    

if __name__ == "__main__":
    main()