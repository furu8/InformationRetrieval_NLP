import pandas as pd
import numpy as np
import re

def print_preprocessing_debug(doc_list):
    print('# httpsデバッグ') # httpsデバッグ
    print(doc_list[45989], end='')
    print(re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", doc_list[45989]))
    print('#半角記号,数字,英字') #半角記号,数字,英字
    print(doc_list[6])
    print(re.sub(r'[~`!@#$%^&*()-+={}|.,<>/?:;"[\]\'\\]', "", doc_list[6]))
    print('# 半角記号,数字,英字') # 半角記号,数字,英字
    print(doc_list[6])
    print(re.sub(r'[-]', "", doc_list[6]))
    # text=re.sub(r'[︰；’”「」-＠]', "", text)#全角記号

def read_txt(path):
    with open(path, 'r') as f:
        doc_dict = f.readlines()
        # 記事のタイトルだけ抽出（index番号が文書番号となる）
        title_list = [doc_dict[i] for i in range(1, len(doc_dict)-1) if doc_dict[i-1] == '\n' and doc_dict[i+1] == '\n']
        # 記事だけ抽出
        doc_list = [doc_dict[i] for i in range(1, len(doc_dict)-1) if doc_dict[i-1] != '\n' or doc_dict[i+1] != '\n']
    
    return title_list, doc_list

def main():
    # テキストから記事のタイトルと内容を取得
    titile_list, doc_list = read_txt('../data_file/raw/doc_set.txt')

    # 前処理debug
    print_preprocessing_debug(doc_list) 

    # 前処理
    # doc_list = [doc for doc in doc_list if doc != '\n'] # 改行文字しかない要素を除外
    
    


if __name__ == "__main__":
    main()