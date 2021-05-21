def linearSearch(array, x):
    n = len(array)
    # Going through array sequencially
    for i in range(0, n):
        nombre = array[i].split("|")[1]
        if (x in nombre):
            return i
    return -1

