import csv
f = open("new.csv",'a',newline='')
wo = csv.writer(f)
data =[["a","b","c","d"],[12,22,13,33],[20,23,30,99],[18,17,19,10],[78,56,89,55]]
wo.writerows(data)
f.close()

'''
f = open('new.csv','r')
re = csv.reader(f)
li  =list(re)
for row in li:
    print(row)
'''
