# Binary Search : https://en.wikipedia.org/wiki/Binary_search_algorithm
def binarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binarySearch(alist[:midpoint], item)
            else:
                return binarySearch(alist[midpoint+1:], item)

def main():
    testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
    print(binarySearch(testlist, 3))
    print(binarySearch(testlist, 13))

if __name__=="__main__":
    main()