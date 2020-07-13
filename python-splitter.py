import pandas as pd

filename = '' #put the file name here.

smallFileSize = 10 ** 6 * 2

i = 0

for chunk in pd.read_csv(filename + '.csv', smallFileSize = smallFileSize):
    chunk.to_csv(path_or_buff = f'{filename}{i}.csv', index = False)
    i += 1