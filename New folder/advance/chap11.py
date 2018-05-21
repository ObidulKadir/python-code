
with open('F:/DIU/phython wp/program/article.txt') as fobj:
    for num ,line in enumerate(fobj):
        print(num + 1,line.upper())
