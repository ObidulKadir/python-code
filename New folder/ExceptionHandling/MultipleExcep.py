
# Multiple Exceptions

try:
    disk_file = open("filename")

except (FileNotFoundError,PermissionError):
    print("Can't open thaa file.")


try:
    disk_file = open('filename')

except FileNotFoundError:
    print("File doesnot found.")

except PermissionError:
    print("permission denied to open the file  ")