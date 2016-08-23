___author___ = "Sajad Azami"
'''
Bosch Production Line Performance,
Kaggle.com,
BoschDataAnalyzer
8/23/16,
Sajad Azami
'''

import pandas as pd


def create_submission(data: dict):
    pd.DataFrame.from_dict(data, orient='index').to_csv('write_test.csv', header=False)
    with open('write_test.csv', 'r') as original:
        data_temp = original.read()
    with open('write_test.csv', 'w') as modified:
        modified.write("Id,Response\n" + data_temp)

# Test(Use Like This):
# test_dict = {1: 0, 2: 0, 3: 0, 4: 1, 5: 1, 6: 0, 7: 1, 8: 0}
# create_submission(test_dict)
