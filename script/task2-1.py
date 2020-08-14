import pandas as pd
import numpy as np
import re

def print_preprocessing_debug(doc_list):
    print('# httpsデバッグ') # https
    print(doc_list[45989])
    print(re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", doc_list[45989]))

    print('#半角記号') #半角記号
    print(doc_list[6977])
    print(re.sub(r'[~`!@#$%^&*()\-━+={}|.,<>/?:;"[\]\'\\]', "", doc_list[6977]))

    print('# 全角記号') # 全角記号
    print(doc_list[18309])
    print(re.sub(r'[︰”「」@]', "", doc_list[18309]))

    print("# [’]を[']に置換") # [’]を[']に置換
    print(doc_list[15])
    print(re.sub(r'[‘’]', "'", doc_list[15]))

    print('# 大文字小文字変換') # 大文字小文字変換
    print(doc_list[2])
    print(doc_list[2].lower())

    print('# \\n削除') # \\n削除
    print(doc_list[2])
    print(re.sub(r'[\n]', "", doc_list[2]))

def read_txt(path):
    with open(path, 'r') as f:
        doc_dict = f.readlines()
        # 記事のタイトルだけ抽出（index番号が文書番号となる）
        title_list = [doc_dict[i] for i in range(1, len(doc_dict)-1) if doc_dict[i-1] == '\n' and doc_dict[i+1] == '\n']
        # 記事だけ抽出
        doc_list = [doc_dict[i] for i in range(1, len(doc_dict)-1) if doc_dict[i-1] != '\n' or doc_dict[i+1] != '\n']
    
    return title_list, doc_list

def remove_symbol_word(doc):
    # https
    new_doc = re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", doc)

    # \\n削除
    new_doc = re.sub(r'[\n]', "", new_doc)

    # # [‘]と[’]を[']に置換
    # new_doc = (re.sub(r'[‘’]', "'", new_doc) # 置換すればpeople’sがpeople'sとして扱えるが、'mental enslavement'などが残る
    
    # 半角記号
    new_doc = re.sub(r'[~`!@#$%^&*()\-━+={}|.,<>/?:;"[\]\'\\]', "", new_doc)
    
    # 全角記号
    new_doc = re.sub(r'[︰”「」@]', "", new_doc)

    return new_doc

def preprocessing_word(doc_list):
    """
    前処理をほどこす
    """
    # 小文字変換
    doc_lower_list = [doc.lower() for doc in doc_list]
    
    # 記号除去
    doc_sym_list = [remove_symbol_word(doc) for doc in doc_lower_list]

    return doc_sym_list

def main():
    # テキストから記事のタイトルと内容を取得
    titile_list, doc_list = read_txt('../data_file/raw/doc_set.txt')

    # 前処理
    # print_preprocessing_debug(doc_list) # 前処理確認デバッグ
    doc_list = [doc for doc in doc_list if doc != '\n'] # 改行文字しかない要素を除外
    new_doc_list = preprocessing_word(doc_list)
        

if __name__ == "__main__":
    main()