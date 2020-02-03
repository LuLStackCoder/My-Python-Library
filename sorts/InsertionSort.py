def insertion_sort(iterable, fn=lambda x,y: x<y, inplace=True):
    '''
        Insertion sort function
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
            for j in range(i, 0, -1):
                if fn(iterable[j], iterable[j-1]):
                    iterable[j], iterable[j-1] = iterable[j-1], iterable[j]
                else:
                    break
        return iterable

    if inplace == False:
        iterable = iterable.copy()
    return sort(iterable, fn)


