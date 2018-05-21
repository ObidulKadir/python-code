
## Temporary file

from tempfile import  TemporaryFile

with TemporaryFile('w+') as obj:
    obj.write("Life is cool")

    obj.seek(5)
    data = obj.read()
    print(data)