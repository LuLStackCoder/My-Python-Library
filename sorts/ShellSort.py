def shell_sort(iterable, fn=lambda x,y: x<y, inplace=True):
    '''
        Shell sort function
        Parameters:
        iterable (object): Iterable object
        fn (function): Comparsion function
        inplace (bool): Sort inplace or make copy
        Returns:
        object: Return sorted iterable object
    '''
    def sort(iterable, fn):
        h = 1
        length = len(iterable)
        while h < length // 3:
            h = 3 * h + 1
        while h > 0:
            for i in range(h, length):
                j = i
                while j > 0 and fn(iterable[j], iterable[j-h]):
                    iterable[j], iterable[j-h] = iterable[j-h], iterable[j]
                    j -= h
            h = (h - 1) // 3
        return iterable

    if inplace == False:
        iterable = iterable.copy()
    return sort(iterable, fn)
