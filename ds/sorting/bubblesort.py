def sort(alist):
    for num in range(len(alist)):
        for i in range(num, 0, -1):
            if alist[i-1] > alist[i]:
                alist[i-1], alist[i] = alist[i], alist[i-1]

def main():
    alist = [54,26,93,17,77,31,44,55,20]
    sort(alist)
    print(alist)

if __name__=="__main__":
    main()