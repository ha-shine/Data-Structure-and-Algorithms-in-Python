def solve(coinValueList, change, minCoins, coinsUsed):
    for cents in range(change+1):
        coinCount = cents
        newCoin = 1
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
                coinCount = minCoins[cents-j]+1
                newCoin = j
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin
    return minCoins[change]

def printCoins(coinsUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinsUsed[coin]
        print(thisCoin, end=" ")
        coin = coin - thisCoin

def main():
    amnt = 63
    clist = [1, 5, 10, 21, 25]
    coinsUsed = [0]*(amnt+1)
    coinCount = [0]*(amnt+1)

    print("Making change for %d requires" % amnt)
    print("%d coins" % solve(clist, amnt, coinCount, coinsUsed))
    print("They are:")
    printCoins(coinsUsed, amnt)

if __name__ == "__main__":
    main()