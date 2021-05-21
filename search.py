def linearSearch(array, n, x):

    # Going through array sequencially
    for i in range(0, n):
        nombre = array[i].split("|")[1]
        if (x in nombre):
            return i
    return -1


array = ['l1|n1|3', 'l2|n2|1', 'l3|n3|3', 'nada|nada muy importante|1']
x = 'nada'
result = linearSearch(array, len(array), x)
if(result == -1):
    print("Element not found")
else:
    print("Element found at index: ", array[result])