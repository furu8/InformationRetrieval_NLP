import pandas as pd
import numpy as np
import re
from sklearn.feature_extraction.text import CountVectorizer

def print_preprocessing_debug(doc_list):
    # print('# https') # https
    # print(doc_list[261134])
    # print(re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", doc_list[261134]))
    # print(doc_list[270337])
    # print(re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", doc_list[270334]), end='')
    # print(re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", doc_list[270335]), end='')
    # print(re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", doc_list[270336]), end='')
    # print(re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", doc_list[270337]), end='')
    # print(re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", doc_list[270338]), end='')
    # print(re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", doc_list[270339]), end='')
    # print(re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", doc_list[270340]), end='')
    # print(re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", doc_list[270341]), end='')

    # print('#半角記号') #半角記号
    # print(doc_list[6977])
    # print(re.sub(r'[~`!@#$%^&*()\-━+={}|.,<>/?:;"[\]\'\\]', "", doc_list[6977]))
    print(doc_list[267193])
    print(re.sub(r'[~`!@#$%^&*()\-━+={}|.,<>/?:;"[\]\'\\]', "", doc_list[267191]), end='')
    print(re.sub(r'[~`!@#$%^&*()\-━+={}|.,<>/?:;"[\]\'\\]', "", doc_list[267192]), end='')
    print(re.sub(r'[~`!@#$%^&*()\-━+={}|.,<>/?:;"[\]\'\\]', "", doc_list[267193]), end='')
    print(re.sub(r'[~`!@#$%^&*()\-━+={}|.,<>/?:;"[\]\'\\]', "", doc_list[267194]), end='')
    print(re.sub(r'[~`!@#$%^&*()\-━+={}|.,<>/?:;"[\]\'\\]', "", doc_list[267195]), end='')
    print(re.sub(r'[~`!@#$%^&*()\-━+={}|.,<>/?:;"[\]\'\\]', "", doc_list[267196]), end='')
    print(re.sub(r'[~`!@#$%^&*()\-━+={}|.,<>/?:;"[\]\'\\]', "", doc_list[267197]), end='')
    print(re.sub(r'[~`!@#$%^&*()\-━+={}|.,<>/?:;"[\]\'\\]', "", doc_list[267198]), end='')
    print(re.sub(r'[~`!@#$%^&*()\-━+={}|.,<>/?:;"[\]\'\\]', "", doc_list[267199]), end='')

    # print('# 全角記号') # 全角記号
    # print(doc_list[18309])
    # print(re.sub(r'[︰”「」@]', "", doc_list[18309]))

    # print("# [’]を[']に置換") # [’]を[']に置換
    # print(doc_list[15])
    # print(re.sub(r'[‘’]', "'", doc_list[15]))

    # print('# 大文字小文字変換') # 大文字小文字変換
    # print(doc_list[2])
    # print(doc_list[2].lower())

    # print('# \\n削除') # \\n削除
    # print(doc_list[2])
    # print(re.sub(r'[\n]', "", doc_list[2]))

def read_doc_txt(path):
    with open(path, 'r') as f:
        doc_list = f.readlines()
        # 記事のタイトルだけ抽出（index番号が文書番号となる）
        title_list = [doc_list[i] for i in range(1, len(doc_list)) if doc_list[i-2] == '\n' and doc_list[i-1] == '\n' and doc_list[i+1] == '\n']
        # 記事だけ抽出
        doc_list = [doc_list[i] for i in range(1, len(doc_list)) if doc_list[i-1] != '\n' or doc_list[i+1] != '\n']
    
    return title_list, doc_list

def read_stop_words(path):
    df = pd.read_csv(path, sep='\n')
    df = df.rename(columns={'#http://www.textfixer.com/resources/common-english-words.txt': 'stop_word'})
    return df

def remove_url(doc):
    return re.sub(r'https?://[\w/:%#\$&\?\(\)~\.\,=\+\-…]+', "", doc)

def remove_newline(doc):
    return re.sub(r'[\n]', "", doc)

def replace_apostrophe(doc):
    # 置換すればpeople’sがpeople'sとして扱えるが、'mental enslavement'などが残る
    return re.sub(r'[‘’]', "'", doc)

def remove_en(doc):
    return re.sub(r'[~`!@#$%^&*()\-━+={}|.,<>/?:;"[\]\'\\]', "", doc)

def remove_em(doc):
    return re.sub(r'[︰”「」@]', "", doc)

def remove_symbol_word(doc):
    """
    不要な記号を除去
    """
    # \\n削除
    new_doc = remove_newline(doc)

    # https
    new_doc = remove_url(new_doc)

    # [‘]と[’]を[']に置換
    # new_doc = replace_apostrophe(new_doc)
    
    # 半角記号
    new_doc = remove_en(new_doc)

    # 全角記号
    new_doc = remove_em(new_doc)

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

def generate_df(article_dict):
    """
    単語文書行列を作成
    """
    # ストップワード
    df_stop = read_stop_words('../data_file/raw/stop_words_list(UTF-8).txt')
    stop_words = list(df_stop.values.flatten())
    
    # 単語の出現回数をカウント
    doc_list = np.array(list(article_dict.values()))
    cv = CountVectorizer(stop_words=stop_words)
    cv.fit(doc_list)
    freq_word_list = cv.transform(doc_list)

    # データフレーム形式で先頭5行まで表示
    print(pd.DataFrame(freq_word_list.toarray(), columns=cv.get_feature_names()))

def make_article_dict(title_list, article_list):
    article_dict = {title: article for title, article in zip(title_list, article_list)}
    return article_dict

def concat_article_line(article, doc):
    word_list = doc.split(' ')
    article_one_line = ' '.join(word_list) # 単語リストを空白切りに
    article += article_one_line + ' ' # 連結
    return article
    
def generate_article_dict(title_list, doc_list):
    """
    一行ずつの記事の内容と記事ごとに連結
    連結した記事を辞書型で紐付けて返却
    """
    blank_count = 0       # 空文字をカウントする
    article_list = []     # 記事ごとのリスト
    article = ''          # 記事を連結する一時変数
    isblank = False
    
    # 記事連結処理
    for i, doc in enumerate(doc_list):
        if doc == doc_list[-1]: # 記事の最後に到達したときの例外処理
            article = concat_article_line(article, doc)
            article_list.append(article)
        elif doc == '': # 空文字のときカウント
            blank_count += 1
            if doc_list[i+1] == '':
                isblank = True
            else:
                isblank = False
            # 空文字が3に達したとき、articleが一つの記事になっている
            if blank_count >= 3 and not isblank:
                blank_count = 0
                article_list.append(article)
                # print(article)
                article = '' # 初期化
        else: # 記事の内容の一文を連結
            blank_count = 0
            article = concat_article_line(article, doc)

    # 辞書型にして返却
    return make_article_dict(title_list, article_list)

def main():
    # テキストから記事のタイトルと内容を取得
    title_list, doc_list = read_doc_txt('../data_file/raw/doc_set.txt')

    # 前処理
    # print_preprocessing_debug(doc_list) # 前処理確認デバッグ
    new_doc_list = preprocessing_doc(doc_list) # 記事の内容の前処理
    new_title_list = [remove_newline(title) for title in title_list] # 記事のタイトルの前処理(改行文字除去)
    
    # 記事辞書の作成
    article_dict = generate_article_dict(new_title_list, new_doc_list)
    # print('\nanegpur')
    # print(article_dict['Balvantray Mehta Vidya Bhawan Anguridevi Shersingh'])
    # print(article_dict['Stanley Hall, Clayfield'])
    
    # generate_df(article_dict)

    

if __name__ == "__main__":
    main()