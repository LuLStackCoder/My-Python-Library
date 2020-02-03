def heap_sort(iterable, fn=lambda x,y: x<y, inplace=True):
    '''
        Heap sort function
        Parameters:
        iterable (object): Iterable object
        fn (function): Comparsion function
        inplace (bool): Sort inplace or make copy
        Returns:
        object: Return sorted iterable object
    '''
    def sink(iterable, i, curr_len):
        while i < curr_len:
            large = i
            childl = 2 * i + 1
            childr = childl + 1
            if childl < curr_len and fn(iterable[large], iterable[childl]):
                large = childl
            if childr < curr_len and fn(iterable[large], iterable[childr]):
                large = childr
            if large == i:
                return
            iterable[i], iterable[large] = iterable[large], iterable[i]
            i = large

    def heapify(iterable):
        for i in range(len(iterable)//2, -1, -1):
            sink(iterable, i, len(iterable))
        return iterable

    def sort(iterable, low, high):
        heapify(iterable)
        for i in range(len(iterable)-1, -1, -1):
            iterable[i], iterable[0] = iterable[0], iterable[i]
            sink(iterable, 0, i)
        return iterable
    
    if inplace == False:
        iterable = iterable.copy()

    return sort(iterable, 0, len(iterable)-1)
