import csv
import pprint
import os

test = "hello world"
print(test)

fpath = os.path.dirname(__file__)

with open(fpath + '/out_testdata/testdata1.csv','w', newline="") as f :
    w = csv.writer(f)
    w.writerow([1,'test user', 'aaa'])
    w.writerow([2,'山田太郎'   , 'bbb'])