import pandas

# Creating one chunk of 1000 row from each data set and write it to file to work on
chunk_size = 10 ** 3
print('Starting')
for data in pandas.read_csv('../data_sets/train/train_date.csv', iterator=True, chunksize=chunk_size):
    data.to_csv('../data_sets/samples/date_sample.csv')
    break
for data in pandas.read_csv('../data_sets/train/train_categorical.csv', iterator=True, chunksize=chunk_size):
    data.to_csv('../data_sets/samples/categorical_sample.csv')
    break
for data in pandas.read_csv('../data_sets/train/train_numeric.csv', iterator=True, chunksize=chunk_size):
    data.to_csv('../data_sets/samples/numeric_sample.csv')
    break
