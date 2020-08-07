import pandas as pd
import numpy as np

def read_txt(path):
    df = pd.read_csv(path, sep='\n')
    df = df.rename(columns={'#http://disney.wikia.com/wiki/Frozen': 'doc'})
    return df

def pre_lower_word(doc_list):
    """
    文書をすべて小文字に変換
    """
    # 小文字変換
    doc_lower_str_list = str(doc_list[0]).lower() # listは0番目しかない
    # 比較
    # print(doc_list)
    # print(doc_lower_str_list)

    return doc_lower_str_list

def pre_replace_word(doc, symbol_list):
    """
    文書のsymbol_listの記号の除去とと空白文字を\nに置換
    """
    # symbolを除去
    for sym in symbol_list:
        doc = doc.replace(sym, '')
    
    # 空白を改行文字に
    new_doc = doc.replace(' ', '\n')

    return new_doc

def preprocessing_word(df):
    """
    前処理をほどこす
    """
    # 小文字変換
    doc_list = df.values # 二次元リスト
    doc_lower_list = [pre_lower_word(doc) for doc in doc_list] # 一次元リスト
    
    # 記号除去、空白置換
    symbol_list = ['(', ')', '"', '-', ',', '.']
    doc_sym_list = [pre_replace_word(doc, symbol_list) for doc in doc_lower_list]

    return doc_sym_list

def main():
    # 読み込み
    df = read_txt('../data_file/raw/doc.txt')

    # 前処理
    word_doc_list = preprocessing_word(df)

    # 出力
    [print(word) for word in word_doc_list]

if __name__ == "__main__":
    main()