def quick_sort(iterable, fn=lambda x,y: x<y, inplace=True):
    '''
        Quick sort function
        Parameters:
        iterable (object): Iterable object
        fn (function): Comparsion function
        inplace (bool): Sort inplace or make copy
        Returns:
        object: Return sorted iterable object
    '''
    def partition(iterable, low, high, fn):
        pivot = iterable[(low + high) // 2]
        i = low - 1
        j = high + 1
        while True:
            i += 1
            while fn(iterable[i], pivot):
                i += 1
            j -= 1
            while iterable[j] >= pivot:
                j -= 1
            if i >= j:
                return j
            iterable[i], iterable[j] = iterable[j], iterable[i]

    def sort(iterable, low, high):
        if low < high:
            j = partition(iterable, low, high, fn)
            sort(iterable, low, j)
            sort(iterable, j+1, high)
        return iterable

    if inplace == False:
        iterable = iterable.copy()
    return sort(iterable, 0, len(iterable)-1)
