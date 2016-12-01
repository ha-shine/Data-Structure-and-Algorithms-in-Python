def sort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        sort(lefthalf)
        sort(righthalf)

        l = 0
        r = 0
        c = 0
        while l < len(lefthalf) and r < len(righthalf):
            if lefthalf[l] < righthalf[r]:
                alist[c] = lefthalf[l]
                l = l + 1
            else:
                alist[c] = righthalf[r]
                r = r + 1
            c = c + 1

        while l < len(lefthalf):
            alist[c] = lefthalf[l]
            l = l + 1
            c = c + 1

        while r < len(righthalf):
            alist[c] = righthalf[r]
            r = r + 1
            c = c + 1

def main():
    alist = [54,26,93,17,77,31,44,55,20]
    sort(alist)
    print(alist)

if __name__=="__main__":
    main()