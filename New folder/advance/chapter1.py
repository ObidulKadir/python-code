


 #   with open('F:/DIU/phython wp/program/article.txt') as obj:
   #     contents = obj.read()
  #      print(contents)

 ##except Exception as e:
   # print("file error",e)'''
try:
     obj = open('F:/DIU/phython wp/program/article.txt')


except Exception as e:
    print("File Error,", e)
else:
    content = obj.read()
    print(content)

finally:
    obj.close()

