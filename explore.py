import pandas as pd

sample_sub = pd.read_csv('spaceship-titanic/sample_submission.csv')
train_df = pd.read_csv('spaceship-titanic/train.csv')
test_df = pd.read_csv('spaceship-titanic/test.csv')

print(sample_sub.columns.values)
print(train_df.columns.values)
print(test_df.columns.values)

print(train_df.shape)
print(test_df.shape)
