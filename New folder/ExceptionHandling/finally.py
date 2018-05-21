
def division ( x , y ):
    try:
        result = x / y

    except Exception as e:
        print("Error Happend.",e)

    else:
        print("div result is = "+ str(result))

    finally:
        print("whateever happen its run the first")

division(10,0)