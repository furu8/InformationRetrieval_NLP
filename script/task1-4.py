import pandas as pd
import numpy as np

def read_txt(path):
    df = pd.read_csv(path, sep='\t', names=('word', 'count'))
    return df

def merge_df(df_word, df_new_word):
    # 結合のための前処理
    df_word = df_word.set_index('word') # wordをindexに
    df_new_word = df_new_word.set_index('word')  # wordをindexに
    df_word['count'] = df_word['count'].astype(float) # count型変換
    df_new_word = df_new_word.rename(columns={'count': 'new_count'}) # countの名前変更

    # 結合
    new_df = pd.concat([df_word, df_new_word], axis=1, join='outer', sort=False)
    new_df = new_df.reset_index(drop=False) # wordをcolumnに
    new_df = new_df.rename(columns={'index':'word', 'count':'        count'}) # indexの名前変更とカラム一調整

    return new_df

def main():
    # 読み込み
    df_word = read_txt('../data_file/interim/task1-2_result.txt')
    df_new_word = read_txt('../data_file/interim/task1-3_result.txt')

    # 結合
    new_df = merge_df(df_word, df_new_word)

    # 出力
    print(new_df)

    # 保存
    new_df.to_csv('../data_file/interim/task1-4_result.txt', sep='\t')


if __name__ == "__main__":
    main()