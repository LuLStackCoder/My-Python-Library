def bubble_sort(iterable, fn=lambda x,y: x<y, inplace=True):
    '''
        Bubble sort function
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
            swapped = False
            for j in range(length-i-1):
                if fn(iterable[j+1], iterable[j]):
                    iterable[j], iterable[j+1] = iterable[j+1], iterable[j]
                    swapped = True
            if swapped == False:
                break
        return iterable

    if inplace == False:
        iterable = iterable.copy()
    return sort(iterable, fn)
