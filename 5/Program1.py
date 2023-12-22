def multiply(*args):
    result = 1
    for num in args:
        result = result * num
    return result

result = multiply(3,4,2)
print(result)
