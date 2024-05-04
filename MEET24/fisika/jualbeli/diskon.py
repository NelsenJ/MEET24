def beli(x):
    def diskon(y):
        return y*(100 - x)/ 100
    return diskon