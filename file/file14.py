with open('file1.py') as f, open('file10.py') as d:
    for i,j in zip(f,d):
        print(i+j)