import pandas as pd

def read_txt(path):
    df = pd.read_csv(path, sep='\n')
    df = df.rename(columns={'#http://disney.wikia.com/wiki/Frozen': 'doc'})
    return df

def pre_lower_word(doc_list):
    doc_str_list = str(doc_list)
    return doc_str_list.lower()

def preprocessing_word(df):
    doc_list = df.values
    lower_list = [pre_lower_word(doc) for doc in doc_list]
    print(lower_list)

def main():
    df = read_txt('../data_file/raw/doc.txt')
    preprocessing_word(df)

if __name__ == "__main__":
    main()