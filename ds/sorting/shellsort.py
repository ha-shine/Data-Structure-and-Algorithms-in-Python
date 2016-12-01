def sort(alist):
    gap = len(alist) // 2
    
    while gap > 0:
        for start in range(gap):
            gapSort(alist, start, gap)
        gap = gap // 2

def gapSort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):
        current = alist[i]
        pos = i
        while pos >= gap and alist[pos-gap]>current:
            alist[pos] = alist[pos-gap]
            pos = pos - gap

        alist[pos] = current

def main():
    alist = [54,26,93,17,77,31,44,55,20]
    sort(alist)
    print(alist)

if __name__=="__main__":
    main()