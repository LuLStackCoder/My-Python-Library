def selection_sort(iterable, fn=lambda x,y: x<y, inplace=True):
    '''
        Selection sort function
        Parameters:
        iterable (object): Iterable object
        fn (function): Comparsion function
        inplace (bool): Sort inplace or make copy
        Returns:
        object: Return sorted iterable object
    '''
    def sort(iterable, fn):
        length = len(iterable)
        for i in range(length):
            for j in range(i+1, length):
                if fn(iterable[j], iterable[i]):
                    iterable[i], iterable[j] = iterable[j], iterable[i]
        return iterable

    if inplace == False:
        iterable = iterable.copy()
    return sort(iterable, fn)
