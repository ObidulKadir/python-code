
# Exception HandlinG

def division(x, y):

    try:
        result = x / y

    except ZeroDivisionError: #its only for one part of error
        print("its not possible to divide Zero.")
        return None


    except Exception as e:   #its for all error handling but its need to refer to show error.
        print("Error Occured.",e)
        return None


    return result





print(division(0,10))
print(division(4, '2'))
print(division(5 ,0))
print(division(4,4.7))