import pandas as pd

def read_txt(path):
    df = pd.read_csv(path, sep='\n')
    df = df.rename(columns={'#http://disney.wikia.com/wiki/Frozen': 'doc'})
    return df

def main():
    df = read_txt('../data_file/raw/doc.txt')


if __name__ == "__main__":
    main()