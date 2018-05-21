
def div ( x, y ):
    return x / y

try:
    div_result = div(9,0)

except :
    print("Zero division is not possible.")

else:
    print("Division Result:" + str(div_result))
