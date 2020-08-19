import pandas as pd
import numpy as np

def read_df(path):
    with open(path, 'r') as f:
        doc_list = f.readlines()

    return doc_list

def input_keyword():
    search_word = input('your search input: ') # 入力はスペース区切り
    keyword_list = [word for word in search_word.split(' ')]
    return keyword_list

def get_doc_number(tfidf_df):
    keyword_list = input_keyword() # 入力してキーワードを抽出

    doc_num_dict = {}
    for keyword in keyword_list:
        doc_num_list = [] # 文書番号リスト
        df = tfidf_df
        try:
            for i in range(10):
                print(i, end=' ')
                doc_num = df[keyword].idxmax()
                df = df.drop(doc_num)
                doc_num_list.append(doc_num)
            doc_num_dict[keyword] = doc_num_list
        except:
            print('キーワード: {} は文書の中にありませんでした'.format(keyword))
            continue

    return doc_num_dict

def main():
    doc_list = read_df('/Users/furuhama/Desktop/task2-1_tfidf_result.txt')
    print(doc_list[0])
    
    # doc_num_dict = get_doc_number(tfidf_df)
    # print(doc_num_dict)

if __name__ == "__main__":
    main()