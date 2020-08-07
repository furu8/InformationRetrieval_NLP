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

def pre_replace_word(doc_list, symbol_list):
    """
    文書のsymbol_listの記号と空白文字を\nに置き換え
    """
    doc_str_list = str(doc_list)
    doc_sym_list = [doc_str_list.replace(sym, '\n') for sym in symbol_list]
    print(doc_sym_list)


def preprocessing_word(df):
    """
    前処理をほどこす
    """
    doc_list = df.values # 二次元リスト
    print([pre_lower_word(doc) for doc in doc_list])
    # doc_lower_list = [pre_lower_word(doc) for doc in doc_list]
    # print(np.array(doc_lower_list).shape)
    # print(doc_lower_list)
    symbol_list = ['(', ')', '"', '-', ' ']
    # doc_sym_list = [pre_replace_word(doc, symbol_list) for doc in doc_lower_list]



def main():
    df = read_txt('../data_file/raw/doc.txt')
    preprocessing_word(df)

if __name__ == "__main__":
    main()