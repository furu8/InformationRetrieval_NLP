import pandas as pd
import numpy as np
import re

def print_preprocessing_debug(doc_list):
    print('# https') # https
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
        title_list = [doc_dict[i] for i in range(1, len(doc_dict)-1) if doc_dict[i-2] == '\n' and doc_dict[i-1] == '\n' and doc_dict[i+1] == '\n']
        # 記事だけ抽出
        doc_list = [doc_dict[i] for i in range(1, len(doc_dict)-1) if doc_dict[i-1] != '\n' or doc_dict[i+1] != '\n']
    
    return title_list, doc_list

def remove_symbol_word(doc):
    # https
    # new_doc = re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", doc)

    # \\n削除
    new_doc = re.sub(r'[\n]', "", doc)

    # [‘]と[’]を[']に置換
    # new_doc = (re.sub(r'[‘’]', "'", new_doc) # 置換すればpeople’sがpeople'sとして扱えるが、'mental enslavement'などが残る
    
    # 半角記号
    new_doc = re.sub(r'[~`!@#$%^&*()\-━+={}|.,<>/?:;"[\]\'\\]', "", new_doc)
    
    # 全角記号
    new_doc = re.sub(r'[︰”「」@]', "", new_doc)

    return new_doc

def preprocessing_doc(doc_list):
    """
    前処理をほどこす
    """
    # 小文字変換
    doc_lower_list = [doc.lower() for doc in doc_list]
    
    # 記号除去
    doc_sym_list = [remove_symbol_word(doc) for doc in doc_lower_list]

    # \xa0を除去
    new_doc_list = [doc.replace('\xa0', ' ') for doc in doc_sym_list]

    return new_doc_list

def make_word_index(doc_list):
    """
    全記事の内容から、単語を抽出し、重複と空白は削除
    """
    word_index_list = [] # 索引語
    for i, doc in enumerate(doc_list):
        word_list = doc.split(' ') # 空白文字で単語に分割
        for word in word_list:
            word_index_list.append(word) 
            
    word_index_list = list(set(word_index_list)) # 重複削除
    word_index_list = [word for word in word_index_list if word != ''] # 空白だけの単語を削除

    return word_index_list

def generate_df(new_doc_list):
    """
    単語文書行列を作成
    """
    # インデックス
    word_index_list = make_word_index(new_doc_list)
    

def main():
    # テキストから記事のタイトルと内容を取得
    title_list, doc_list = read_txt('../data_file/raw/doc_set.txt')

    # 前処理
    # print_preprocessing_debug(doc_list) # 前処理確認デバッグ
    # doc_list = [doc for doc in doc_list if doc != '\n'] # 改行文字しかない要素を除外
    new_doc_list = preprocessing_doc(doc_list)
    # word_index_list = make_word_index(new_doc_list)
    print(len(new_doc_list))
    blank_count_list = []
    article_list = []
    article = ''
    for i, doc in enumerate(new_doc_list):
        if doc == '':
            blank_count_list.append(i)
            if len(blank_count_list) >= 3:
                blank_count_list.clear()
                article_list.append(article)
                article = ''
        else:
            blank_count_list.clear()
            word_list = doc.split(' ')
            article_one_line = ' '.join(word_list)
            article += article_one_line + ' '
    print(len(article_list))
    print(len(title_list))
    
    # for t, a in zip(title_list[9000:9400], article_list[9000:9400]):
    #     print(t, a)
    # print(article_list[-1])
    # for i in range(2):
    #     print(article_list[i])

    
    
    


if __name__ == "__main__":
    main()