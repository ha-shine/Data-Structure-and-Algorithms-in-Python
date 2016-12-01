def sort(alist):
    for num in range(len(alist)-1, 0, -1):
        maxpos = 0
        for i in range(1, num+1):
            if alist[maxpos] < alist[i]:
                maxpos = i
        alist[maxpos], alist[num] = alist[num], alist[maxpos]

def main():
    alist = [54,26,93,17,77,31,44,55,20]
    sort(alist)
    print(alist)

if __name__ == "__main__":
    main()