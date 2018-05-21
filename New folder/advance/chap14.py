
# Write a binary data to a file

with open('F:/DIU/phython wp/program/binary', 'wb') as obj:
    obj.write(b'Life is good')


    #read a binary data file

with open ('F:/DIU/phython wp/program/binary' ,'rb') as obj:
    binary_data = obj.read()
    decoded_data = binary_data.decode('utf-8')
    print( decoded_data )