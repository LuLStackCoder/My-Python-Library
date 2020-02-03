def merge_sort(iterable, fn=lambda x,y: x<y, inplace=True):
    '''
        Merge sort function
        Parameters:
        iterable (object): Iterable object
        fn (function): Comparsion function
        inplace (bool): Sort inplace or make copy
        Returns:
        object: Return sorted iterable object
    '''
    def merge(left, right, fn):
        i, j, k = 0, 0, 0
        merged = [0] * (len(left) + len(right))
        while i < len(left) and j < len(right):
            if fn(left[i], right[j]):
                merged[k] = left[i]
                i += 1
            else:
                merged[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            merged[k] = left[i]
            k += 1
            i += 1
        while j < len(right):
            merged[k] = right[j]
            k += 1
            j += 1
        return merged

    def sort(iterable):
        length = len(iterable)
        if len(iterable) <= 1:
            return iterable
        left = iterable[:length//2]
        right = iterable[length//2:]
        return merge(sort(left), sort(right), fn)

    if inplace == False:
        iterable = iterable.copy()
    return sort(iterable)
