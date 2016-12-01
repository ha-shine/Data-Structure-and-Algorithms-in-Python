def sort(alist):
    sortSplit(alist, 0, len(alist)-1)

def sortSplit(alist, first, last):
    if first<last:
        splitpoint = partition(alist, first, last)

        sortSplit(alist, first, splitpoint-1)
        sortSplit(alist, splitpoint+1, last)

def partition(alist, first, last):
    pivot = alist[first]

    leftmark = first+1
    rightmark = last

    while leftmark < rightmark:
        while leftmark <= rightmark and alist[leftmark] <= pivot:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivot and rightmark >= leftmark:
            rightmark = rightmark - 1
        
        if rightmark > leftmark:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]

    alist[first], alist[rightmark] = alist[rightmark], alist[first]
    return rightmark

def main():
    alist = [54,26,93,17,77,31,44,55,20]
    sort(alist)
    print(alist)

if __name__=="__main__":
    main()