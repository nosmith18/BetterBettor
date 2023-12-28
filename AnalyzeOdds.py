import csv
import os, glob,sys

# First let's read in our csv data
def getData():

    path = '/american-football/'
    print(os.getcwd())
    for filename in glob.glob(os.path.join(path, '*.csv')):
        print(filename)
        with open(os.path.join(os.getcwd(), filename), 'r') as f:
            reader = csv.reader(f)
            try:
                for row in reader:
                    print(row)
            except csv.Error as e:
                sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))
    return 0

getData()