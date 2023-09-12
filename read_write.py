f=open("/Users/samarthmengji/Desktop/test.txt",'r')

for line in f:
    tokens= line.split(' ')
    print(line,'Wordcount: ',str(len(tokens)))

f.close()