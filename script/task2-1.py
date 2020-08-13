import pandas as pd
import numpy as np

def read_txt(path):
    with open(path, 'r') as f:
        doc_dict = f.readlines()
        # 記事のタイトルだけ抽出（index番号が文書番号となる）
        title_list = [doc_dict[i] for i in range(1, len(doc_dict)-1) if doc_dict[i-1] == '\n' and doc_dict[i+1] == '\n']
        # 記事だけ抽出
        doc_list = [doc_dict[i] for i in range(1, len(doc_dict)-1) if doc_dict[i-1] != '\n' or doc_dict[i+1] != '\n']
        
        

        for i, doc in enumerate(title_list):
            if i == 150:
                break
            print(doc, end='')

def main():
    read_txt('../data_file/raw/doc_set.txt')

if __name__ == "__main__":
    main()